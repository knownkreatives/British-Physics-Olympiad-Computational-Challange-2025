from Utilities import VisibleColors
from Tasks.T01.B.EmpiricalFormula import equation

import matplotlib.pyplot as plt
import numpy as np

def get_elevation_angle_primary(refractve_index: float, angle_of_incidence: float) -> float:
    # pi - 6 arcsin(sin(θ) / n) + 2θ
    return np.degrees(np.pi - 6 * np.arcsin(np.sin(np.radians(angle_of_incidence)) / refractve_index) + 2 * np.radians(angle_of_incidence))

def get_elevation_angle_secondary(refractive_index: float, angle_of_incidence: float) -> float:
    # 4 arcsin(sin(θ) / n) - 2θ
    return np.degrees(4 * np.arcsin(np.sin(np.radians(angle_of_incidence)) / refractive_index) - 2 * np.radians(angle_of_incidence))

def find_angle_of_incidence_primary(refractive_index: float) -> float:
    # arcsin(sqrt((9 - n^2) / 8))
    return np.degrees(np.arcsin(np.sqrt((9 - refractive_index**2) / 8)))

def find_angle_of_incidence_secondary(refractive_index: float) -> float:
    # arcsin(sqrt((4 - n^2) / 3))
    return np.degrees(np.arcsin(np.sqrt((4 - refractive_index**2) / 3)))

def plot_primary_curve(frequency: float, angles_of_incidence: np.array,
    fig: plt.Figure = None, ax: plt.Axes = None) -> tuple[plt.Figure, plt.Axes]:
    
    # Calculate refractive index once
    n = equation(frequency)
    wavelength = VisibleColors.frequency_to_wavelength(frequency)
    color = VisibleColors.rgb_to_hex(*VisibleColors.wavelength_to_rgb(wavelength))
    
    # Calculate elevations
    elevations = [get_elevation_angle_primary(n, a) for a in angles_of_incidence]
    
    if fig is None and ax is None:
        fig, ax = plt.subplots()
    
    # Plot the main curve
    ax.plot(angles_of_incidence, elevations, 
           color=color, 
           linewidth=2,
           label=f'Primary {wavelength:.0f} nm')
    
    # Find and plot minimum
    min_angle = find_angle_of_incidence_primary(n)
    min_elevation = get_elevation_angle_primary(n, min_angle)

    ax.axline((min_angle, min_elevation), slope=0, color=color,
             label=f'Primary Minimum Angle of Incidence ({wavelength:.0f} nm)')

    return fig, ax

def plot_secondary_curve(frequency: float, angles_of_incidence: np.array,
    fig: plt.Figure = None, ax: plt.Axes = None) -> tuple[plt.Figure, plt.Axes]:
    
    # Calculate refractive index once
    n = equation(frequency)
    wavelength = VisibleColors.frequency_to_wavelength(frequency)
    color = VisibleColors.rgb_to_hex(*VisibleColors.wavelength_to_rgb(wavelength))
    
    # Calculate elevations
    elevations = [get_elevation_angle_secondary(n, a) for a in angles_of_incidence]
    
    if fig is None and ax is None:
        fig, ax = plt.subplots()
    
    # Plot the secondary curve
    ax.plot(angles_of_incidence, elevations, 
           color=color, 
           linewidth=2,
           label=f'Secondary {wavelength:.0f} nm')
    
    # Find and plot maximum
    max_angle = find_angle_of_incidence_secondary(n)
    max_elevation = get_elevation_angle_secondary(n, max_angle)

    ax.axline((max_angle, max_elevation), slope=0, color=color,
             label=f'Secondary maximum Angle of Incidence ({wavelength:.0f} nm)')

    return fig, ax

def plot_rainbow_curves(bands: int = 7,
    start: float = 405e12,
    end: float = 790e12,
    count: int = 50,
    fig: plt.Figure = None, ax: plt.Axes = None) -> tuple[plt.Figure, plt.Axes]:
    """
    Plot primary and secondary curves for a range of frequencies across the visible spectrum.
    """
    angles_of_incidence = np.linspace(0, 90, count)
    
    if fig is None and ax is None:
        fig, ax = plt.subplots()

    for i in range(bands):
        frequency = np.mean(np.linspace(start + (end - start) * i / bands, start + (end - start) * (i + 1) / bands, 2))
        plot_primary_curve(frequency, angles_of_incidence, fig, ax)
        plot_secondary_curve(frequency, angles_of_incidence, fig, ax)

    return fig, ax

def test(count = 50,
    start = 405e12,
    end = 790e12,
    bands = 7,
    fig: plt.Figure = None, ax: plt.Axes = None):
    ax.set_title("Elevation Angles of deflected beams in a rainbow")

    plot_rainbow_curves(bands, start, end, count, fig, ax)

    ax.set_xlabel("Angle of Incidence (degrees)")
    ax.set_ylabel("Deflected Beam Elevation Angle (degrees)")

    ax.set_xlim([0, 90])
    ax.set_ylim([0, 180])
    ax.grid(True)
    plt.show()

if __name__ == "__main__":
    fig, ax = plt.subplots()
    
    test()
    
    plt.show()
    