from Utilities import VisibleColors
from Tasks.T11.A.DeflectedBeamElevation import get_elevation_angle_primary, get_elevation_angle_secondary, find_angle_of_incidence_primary, find_angle_of_incidence_secondary
from Tasks.T1.B.EmpiricalFormula import equation

import matplotlib.pyplot as plt
import numpy as np

def plot_primary_curve(start: float, end: float, count: float,
    fig: plt.Figure = None, ax: plt.Axes = None) -> tuple[plt.Figure, plt.Axes]:
    frequencies = np.linspace(start, end, count)
    wavelengths = VisibleColors.frequency_to_wavelength(frequencies)
    colors = [VisibleColors.rgb_to_hex(*VisibleColors.wavelength_to_rgb(wl)) for wl in wavelengths]

    angles_of_elevation = []

    for i in range(count):
        # Process each frequency/refractive index individually
        n = equation(frequencies[i])
        
        # Get angle of incidence for this specific refractive index
        angle_of_incidence = find_angle_of_incidence_primary(n)
        
        # Get elevation angle for this specific case
        elevation_angle = get_elevation_angle_primary(n, angle_of_incidence)
        angles_of_elevation.append(elevation_angle)

    points = np.array([frequencies, angles_of_elevation])

    if fig is None and ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(points[0], points[1], c=colors)
    
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Elevation Angle (degrees)')

    return fig, ax

def plot_secondary_curve(start: float, end: float, count: float,
    fig: plt.Figure = None, ax: plt.Axes = None) -> tuple[plt.Figure, plt.Axes]:
    frequencies = np.linspace(start, end, count)
    wavelengths = VisibleColors.frequency_to_wavelength(frequencies)
    colors = [VisibleColors.rgb_to_hex(*VisibleColors.wavelength_to_rgb(wl)) for wl in wavelengths]

    angles_of_elevation = []

    for i in range(count):
        # Process each frequency/refractive index individually
        n = equation(frequencies[i])
        
        # Get angle of incidence for this specific refractive index
        angle_of_incidence = find_angle_of_incidence_secondary(n)
        
        # Get elevation angle for this specific case
        elevation_angle = get_elevation_angle_secondary(n, angle_of_incidence)
        angles_of_elevation.append(elevation_angle)

    points = np.array([frequencies, angles_of_elevation])

    if fig is None and ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(points[0], points[1], c=colors)
    
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Elevation Angle (degrees)')

    return fig, ax

def test(count: int = 50,
    start: float = 405e12,
    end: float = 790e12,
    fig: plt.Figure = None, ax: plt.Axes = None) -> tuple[plt.Figure, plt.Axes]:
    """
    Test function to plot primary and secondary curves for a range of frequencies across the visible spectrum.
    """
    if fig is None and ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    plot_primary_curve(start, end, count, fig, ax)
    plot_secondary_curve(start, end, count, fig, ax)

    ax.set_title("Elevation Angles of Primary and Secondary Rainbows")
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Elevation Angle (degrees)")
    ax.grid()
    ax.legend(['Primary Rainbow', 'Secondary Rainbow'])

    return fig, ax

if __name__ == "__main__":
    fig, ax = test()
    plt.show()