from Utilities import VisibleColors
from Simulations import LawOfRefraction
from Tasks.T11.A.DeflectedBeamElevation import find_angle_of_incidence_primary, find_angle_of_incidence_secondary
from Tasks.T1.B.EmpiricalFormula import equation

import matplotlib.pyplot as plt
import numpy as np

def plot_primary_curve(start: float, end: float, count: float, refractive_index: float = 1.0003, 
    fig: plt.Figure = None, ax: plt.Axes = None) -> tuple[plt.Figure, plt.Axes]:
    frequencies = np.linspace(start, end, count)
    wavelengths = VisibleColors.frequency_to_wavelength(frequencies)
    colors = [VisibleColors.rgb_to_hex(*VisibleColors.wavelength_to_rgb(wl)) for wl in wavelengths]
    
    angles_of_refraction = []

    for i in range(count):
        # Process each frequency/refractive index individually
        n = equation(frequencies[i])
        
        # Get angle of incidence for this specific refractive index
        angle_of_incidence = find_angle_of_incidence_primary(n)
        
        # Get elevation angle for this specific case
        refaction_angle = LawOfRefraction.calculate_angle_of_refraction(angle_of_incidence, refractive_index, n)
        angles_of_refraction.append(refaction_angle)

    points = np.array([frequencies, angles_of_refraction])

    if fig is None and ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(points[0], points[1], c=colors)
    ax.plot(points[0], points[1], color='red', linewidth=2, label='Primary')

    return fig, ax

def plot_secondary_curve(start: float, end: float, count: float, refractive_index: float = 1.0003,
    fig: plt.Figure = None, ax: plt.Axes = None) -> tuple[plt.Figure, plt.Axes]:
    frequencies = np.linspace(start, end, count)
    wavelengths = VisibleColors.frequency_to_wavelength(frequencies)
    colors = [VisibleColors.rgb_to_hex(*VisibleColors.wavelength_to_rgb(wl)) for wl in wavelengths]
    
    angles_of_refraction = []

    for i in range(count):
        # Process each frequency/refractive index individually
        n = equation(frequencies[i])
        
        # Get angle of incidence for this specific refractive index
        angle_of_incidence = find_angle_of_incidence_secondary(n)
        
        # Get elevation angle for this specific case
        refaction_angle = LawOfRefraction.calculate_angle_of_refraction(angle_of_incidence, refractive_index, n)
        angles_of_refraction.append(refaction_angle)

    points = np.array([frequencies, angles_of_refraction])

    if fig is None and ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(points[0], points[1], c=colors)
    ax.plot(points[0], points[1], color='blue', linewidth=2, label='Secondary')

    return fig, ax

def plot_critical_angle(start: float, end: float, count: float, refractive_index: float = 1.0003,
    fig: plt.Figure = None, ax: plt.Axes = None) -> tuple[plt.Figure, plt.Axes]:
    frequencies = np.linspace(start, end, count)

    angles_of_refraction = []

    for i in range(count):
        n = equation(frequencies[i])
        critical_angle = LawOfRefraction.calculate_critical_angle(n, refractive_index)

        angles_of_refraction.append(critical_angle)
    
    points = np.array([frequencies, angles_of_refraction])

    if fig is None and ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(points[0], points[1], color='black', linewidth=2, label='Critical Angle')

    ax.legend()

    return fig, ax

def test(count: int = 50, start: float = 405e12, end: float = 790e12,
    refractive_index: float = 1.0003,
    fig: plt.Figure = None, ax: plt.Axes = None) -> tuple[plt.Figure, plt.Axes]:

    if fig is None and ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    ax.set_title("Elevation Angles of Deflected Beams in a Rainbow")

    plot_primary_curve(start, end, count, refractive_index, fig, ax)
    plot_secondary_curve(start, end, count, refractive_index, fig, ax)
    plot_critical_angle(start, end, count, refractive_index, fig, ax)
    
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Refraction Angle (degrees)')

    ax.set_xlim(start, end)
    ax.set_ylim(38, 50)

    return fig, ax

if __name__ == "__main__":
    fig, ax = test()
    plt.show()