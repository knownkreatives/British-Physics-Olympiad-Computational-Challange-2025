from Utilities import VisibleColors
from Simulations import LawOfRefraction
from Tasks.T11.A.DeflectedBeamElevation import get_elevation_angle_primary, get_elevation_angle_secondary, find_angle_of_incidence_primary, find_angle_of_incidence_secondary
from Tasks.T1.B.EmpiricalFormula import equation

import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

height = 0.5
distance = 10

view_angle = np.degrees(np.arctan(height / distance))
solar_angle = 20

def calculate_arc(height: float, distance: float, solar_angle: float, angle_of_incidence: float, view_angle: float, frequency: float) -> tuple[float, float, float]:
    refraction_angle = LawOfRefraction.calculate_angle_of_refraction(angle_of_incidence, LawOfRefraction.REFRACTIVE_INDICIES['air'], equation(frequency))
    
    ray_length = distance / np.cos(np.radians(solar_angle))
    radius = ray_length * np.sin(np.radians(refraction_angle)) * np.cos(np.radians(view_angle))
    
    rainbow_height = ray_length * np.sin(np.radians(refraction_angle - solar_angle))
    anti_solar_depth = radius - rainbow_height - height
    
    beta = np.abs(np.degrees(np.arctan(anti_solar_depth / distance)))
    
    return radius, rainbow_height, anti_solar_depth, beta

def plot_arc(radius: float, height: float, anti_depth: float, beta: float, frequency: float,
    fig: plt.Figure = None, ax: plt.Axes = None):

    if fig is None and ax is None:
        fig, ax = plt.subplots()

    color = VisibleColors.rgb_to_hex(*VisibleColors.wavelength_to_rgb(VisibleColors.frequency_to_wavelength(frequency)))
    arc = Arc((0, height - anti_depth), 2 * radius, 2 * radius, angle=0, theta1=beta, theta2=180 - beta, color=color, lw=2)
    plt.gca().add_patch(arc)

def plot_rainbow(start: float, end: float, height: float, distance: float, solar_angle: float, view_angle: float, bands: int = 10,
    fig: plt.Figure = None, ax: plt.Axes = None):
    
    if fig is None and ax is None:
        fig, ax = plt.subplots()
    
    for i in range(bands):
        frequency = np.mean(np.linspace(start + (end - start) * i / bands, start + (end - start) * (i + 1) / bands, 2))

        radius, _, anti_depth, beta = calculate_arc(height, distance, solar_angle, find_angle_of_incidence_primary(equation(frequency)), view_angle, frequency)
        plot_arc(radius, height, anti_depth, beta, frequency, fig, ax)

        radius_secondary, _, anti_depth_secondary, beta_secondary = calculate_arc(height, distance, solar_angle, find_angle_of_incidence_secondary(equation(frequency)), view_angle, frequency)
        plot_arc(radius_secondary, height, anti_depth_secondary, beta_secondary, frequency, fig, ax)
    
    r, h, _, _ = calculate_arc(height, distance, solar_angle, find_angle_of_incidence_primary(equation(f)), view_angle, end)
    ax.set_ylim(-h * 1.5, h * 1.5)
    ax.set_xlim(-r * 1.5, r * 1.5)

plot_rainbow(405e12, 790e12, height, distance, solar_angle, view_angle)

plt.gca().set_aspect('equal', adjustable='box')

plt.title("Rainbow Formation: Primary and Secondary Arcs")

plt.grid()
plt.show()