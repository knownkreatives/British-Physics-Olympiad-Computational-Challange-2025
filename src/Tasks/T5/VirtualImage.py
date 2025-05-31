from Utilities.ImageControls import *
from Utilities.ManageLines import *
from Utilities.Transformations import *

import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

def plot_image(
    imageScale = 0.5,
    imageShift = [20, 10],
    imageRot = 0,
    fig: plt.Figure = None, ax: plt.Axes = None):
    
    if fig is None and ax is None:
        fig, ax = plt.subplots()

    image = GeometricImage(upload_local_image())

    try:
        image.scale = create_2d_scaling_matrix(imageScale, imageScale)
        image.pos = create_2d_translation_matrix(*imageShift)
        image.rot = create_2d_rotation_matrix(np.radians(imageRot))
        image.plot()
        ax.set_title('Image Translated on Plot')
        
        ax.set_xlim(-image.sacale[0] * 2, -image.sacale[0] * 2)
        ax.set_ylim(-image.scale[1] * 2, -image.sacale[1] * 2)
    except Exception as e:
        print(f"Error displaying image: {e}")

    return fig, ax, image

def plot_relfection_line(
    line: list[tuple[float, float], tuple[float, float]] = [(10, 0), (-10, 0)],
    normal_point: tuple[float, float] = (0, 10),
    fig: plt.Figure = None, ax: plt.Axes = None):

    gradient = get_gradient(*line)
    p_gradient = get_perpendicular_gradient(gradient)
    intersection_point = get_line_intersection(find_midpoint(*line), gradient, normal_point, p_gradient)

    normal_line = [normal_point, intersection_point]

    if fig is None and ax is None:
        fig, ax = plt.subplots()

    ax.plot(*line[0], marker='o', color="#000000", label="Mirror Point 1")
    ax.plot(*line[1], marker='o', color="#000000", label="Mirror Point 2")
    ax.plot(*normal_point, marker='x', color="#000000", label="Reflect Point")
    ax.plot(*intersection_point, marker='x'  , color="#000000", label="Intersection Point")

    plt.axline(*line, linestyle='-', linewidth=1.5, color="#000000", label="Mirror")
    plt.axline(*normal_line, linestyle='--', linewidth=1.5, color="#000000", label="Normal Line")

    return fig, ax, normal_line

# if __name__ == "__main__":
#     fig , ax1 = plt.subplots()
#     ax2 = ax1.twinx()
    
#     _, _, img = plot_image(fig=fig, ax=ax1)

#     point1 = (10, 0)
#     point2 = (-10, 0)
#     point3 = (0, 10)
#     reflectPoint = (10, 10)
#     test(point1, point2, point3, 30, fig=fig, ax=ax2)

#     def sync_ylim(event_ax):
#         ax2.set_ylim(ax1.get_ylim())
#     ax1.callbacks.connect("ylim_changed", sync_ylim)
#     ax2.yaxis.set_visible(False)

#     ax1.set_xlabel("X-axis")
#     ax1.set_ylabel("Y-axis")

#     plt.show()