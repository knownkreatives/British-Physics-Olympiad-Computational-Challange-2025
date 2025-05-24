from Utilities.ImageControls import upload_local_image, convert_image_to_array
from Utilities.ManageLines import *

import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

def get_reflected_point(point: tuple[float, float], intersectPoint: tuple[float, float]):
    reflectPoint = 2 * np.array(intersectPoint) - np.array(point)
    return reflectPoint

def image_test(
        imageScale = 0.5,
        imageShift = [20, 10],
        fig: plt.Figure = None, ax: plt.Axes = None):
    
    if fig is None and ax is None:
        fig, ax = plt.subplots()

    image = upload_local_image()

    try:
        newSize = (int(image.width * imageScale), int(image.height * imageScale))
        resizedImage = image.resize(newSize)

        ax.imshow(resizedImage, extent=(imageShift[0], imageShift[0] + convert_image_to_array(resizedImage).shape[1], imageShift[1], imageShift[1] + convert_image_to_array(resizedImage).shape[0]))
        
        ax.set_title('Image Translated on Plot')
        
        ax.set_xlim(-convert_image_to_array(resizedImage).shape[1] * 2, convert_image_to_array(resizedImage).shape[1] * 2)
        ax.set_ylim(-convert_image_to_array(resizedImage).shape[0] * 2, convert_image_to_array(resizedImage).shape[0] * 2)
    except Exception as e:
        print(f"Error displaying image: {e}")

    return fig, ax

def test(
        point1: tuple[float, float] = (10, 0),
        point2: tuple[float, float] = (-10, 0),
        reflectPoint: tuple[float, float] = (0, 10),
        angleOfIncidence: float = 45,
        fig: plt.Figure = None, ax: plt.Axes = None):
    gradient = get_gradient(point1, point2)
    intersectionPoint = get_line_intersection(find_midpoint(point1, point2), gradient, reflectPoint, get_perpendicular_gradient(gradient))
    angledGradient = np.tan(np.radians(angleOfIncidence))

    arcRadius = 100
    arc = Arc(intersectionPoint, arcRadius, arcRadius, angle=0, theta1=0, theta2=angleOfIncidence, color='000000')
    xTxt, yTxt = intersectionPoint[0] + arcRadius*0.06, intersectionPoint[1] + arcRadius*0.02  
    
    if fig is None and ax is None:
        fig, ax = plt.subplots()

    ax.plot(*point1, marker='o', color="#000000", label="Mirror Point 1")
    ax.plot(*point2, marker='o', color="#000000", label="Mirror Point 2")
    ax.plot(*reflectPoint, marker='x', color="#000000", label="Reflect Point")
    ax.plot(*intersectionPoint, marker='x', markersize=20, color="#FF0000", label="Intersection Point")
    ax.add_patch(arc)
    ax.text(xTxt, yTxt, f"{angleOfIncidence:.1f}°", fontsize=12)

    mirrorLine = plt.axline(point1, point2, linestyle='-', linewidth=1.5, color="#000000", label="Mirror")
    normalLine = plt.axline(reflectPoint, intersectionPoint, linestyle='--', linewidth=1.5, color="#000000", label="Normal Line")
    rayLine1 = plt.axline(intersectionPoint, slope=angledGradient, linestyle='-', color="#ff0000", label="Incident Ray")

    return fig, ax

if __name__ == "__main__":
    fig , ax1 = plt.subplots()
    ax2 = ax1.twinx()
    
    image_test(fig=fig, ax=ax1)

    point1 = (10, 0)
    point2 = (-10, 0)
    point3 = (0, 10)
    reflectPoint = (10, 10)
    test(point1, point2, point3, 30, fig=fig, ax=ax2)
    
    reflectedPoint = get_reflected_point(reflectPoint, get_line_intersection(point1, get_gradient(point1, point2), reflectPoint, get_perpendicular_gradient(get_gradient(point1, point2))))

    ax2.plot(*reflectPoint, marker='*', color="#0000FF", label="Reflected Point")
    ax2.plot(*reflectedPoint, marker='*', color="#0000FF", label="Reflected Point")

    def sync_ylim(event_ax):
        ax2.set_ylim(ax1.get_ylim())
    ax1.callbacks.connect("ylim_changed", sync_ylim)
    ax2.yaxis.set_visible(False)

    ax1.set_xlabel("X-axis")
    ax1.set_ylabel("Y-axis")

    plt.show()