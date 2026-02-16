from Utilities import VisibleColors
from Tasks.T11.A.DeflectedBeamElevation import get_elevation_angle_primary, get_elevation_angle_secondary
from Tasks.T01.B.EmpiricalFormula import equation

import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

def calculate_arc(distance: float, solar_angle: float, elevation_angle: float):
    if solar_angle == 0:
        return 0, distance, 0, 0 # No elevation or arc if solar angle is zero
    max_solar_ray_length = np.abs(distance / np.cos(np.radians(elevation_angle - solar_angle)))
    rainbow_height = max_solar_ray_length * np.sin(np.radians(elevation_angle - solar_angle))
    radius = np.abs(np.sin(np.radians(elevation_angle)) * np.cos(np.radians(solar_angle)) * max_solar_ray_length)

    # Calculate the height of the rainbow above the ground

    # rainbow_height = height + anti_solar_depth
    # anti_solar_depth = ray_length * sin(elevation) * cos(solar_angle) - ray_length * sin(elevation - solar_angle) - height
    # rainbow_height = ray_length * sin(elevation - solar_angle)
    # height = rainbow_height - anti_solar_depth
    # height = ray_length(sin(elevation - solar_angle) - (sin(elevation) * cos(solar_angle) - sin(elevation - solar_angle) - height)
    #        = ray_length(2sin(elevation - solar_angle) - sin(elevation) * cos(solar_angle)) + height)
    # height - ray_length * height = ray_length(2sin(elevation - solar_angle) - sin(elevation) * cos(solar_angle))
    # height = ray_length(2sin(elevation - solar_angle) - sin(elevation) * cos(solar_angle)) / (1 - ray_length)
    # Avoid division by zero and ensure the formula is mathematically valid
    if max_solar_ray_length != 1:
        height = -(2 * rainbow_height - radius) / (1 - max_solar_ray_length)
    else:
        height = 0  # or set to np.nan if you want to indicate undefined

    anti_solar_depth = radius - rainbow_height - height

    return radius, rainbow_height, height, anti_solar_depth

def plot_arc(distance: float, solar_angle: float, angle_of_elevation: float, freqency: float,
    fig: plt.Figure=None, ax: plt.Axes=None):
    wavelength = VisibleColors.frequency_to_wavelength(freqency)
    color = VisibleColors.rgb_to_hex(*VisibleColors.wavelength_to_rgb(wavelength))
    radius, rh, _, _ = calculate_arc(distance, solar_angle, angle_of_elevation)

    if fig is None or ax is None:
        fig, ax = plt.subplots()
    
    if radius > 0:
        theta1 = min(angle_of_elevation, 180 - angle_of_elevation)
        theta2 = max(angle_of_elevation, 180 - angle_of_elevation)
        # Ensure theta1 < theta2 for Arc
        if theta1 > theta2:
            theta1, theta2 = theta2, theta1
        arc = Arc((0, 0), 2 * radius, 2 * radius, angle=0, theta1=theta1, theta2=theta2, color=color, lw=2)
        ax.add_patch(arc)
    else:
        ax.text(0.5, 0.5, "No rainbow (radius=0)", ha='center', va='center', transform=ax.transAxes)
    return fig, ax, radius


def plot_rainbow(start: float, end: float, solar_angle: float, distance: float, bands: int,
                 fig: plt.Figure=None, ax: plt.Axes=None):

    if fig is None or ax is None:
        fig, ax = plt.subplots()
    
    max_radius: float = 0
    for i in range(bands):
        frequency = np.mean(np.linspace(start + (end - start) * i / bands, start + (end - start) * (i + 1) / bands, 2))
        primary_angle_of_elevation = get_elevation_angle_primary(equation(frequency), solar_angle)
        _, _, r = plot_arc(distance, solar_angle, primary_angle_of_elevation, frequency, fig, ax)

        secondary_angle_of_elevation = get_elevation_angle_secondary(equation(frequency), solar_angle)
        plot_arc(distance, solar_angle, secondary_angle_of_elevation, frequency, fig, ax)
        
        if r > max_radius:
            max_radius = r
    
    # Set limits based on the maximum radius
    ax.set_xlim(-max_radius * 1.1, max_radius * 1.1)
    ax.set_ylim(0, max_radius * 1.1)
    
    return fig, ax

# Create arcs for primary and secondary rainbow
fig, ax = plt.subplots()

plot_rainbow(450e12, 790e12, 5, 1, 7, fig, ax)

ax.set_aspect('equal', adjustable='box')
ax.set_title("Rainbow Formation: Primary and Secondary Arcs")
ax.grid()
plt.show()