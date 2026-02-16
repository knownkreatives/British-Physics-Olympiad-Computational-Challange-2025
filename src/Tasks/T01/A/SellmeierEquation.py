from Utilities import VisibleColors

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np


"""
The Sellmeier equation is used to determine the dispersion of light in the medium.
It describes relation between the refactive index and the wavelength for a particular transparent object.
"""
def equation(
    wavelength: float,
    coefficents_B: list[float],
    coefficents_C: list[float]):
    
    refractiveIndex: float = 0.0

    sigma_i: float = 0.0
    for Bi, Ci in zip(coefficents_B, coefficents_C):
        sigma_i += (Bi * wavelength**2) / (wavelength**2 - Ci)

    refractiveIndex = pow(1 + sigma_i, 0.5)
    
    return refractiveIndex

def test(
    start = 0.3,
    end = 0.9,
    count = 50,
    B_coefficents = [1.03961212, 0.231792344, 1.01146945],
    C_coefficents = [0.00600069867, 0.0200179144, 103.560653],
    fig: plt.Figure = None, ax: plt.Axes = None):

    wavelength = np.linspace(start, end, count)
    refractiveIndex = equation(wavelength, B_coefficents, C_coefficents)

    points = np.array([wavelength, refractiveIndex]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    lc = LineCollection(segments, colors=VisibleColors.get_color_gradient(wavelength), linewidth=2)
    
    if fig is None and ax is None:
        fig, ax = plt.subplots()

    ax.set_title("Model of the refractive index of crown glass")
    ax.add_collection(lc)
    ax.autoscale()
    ax.set_xlabel("Wavelength (microns)")
    ax.set_ylabel("Refractive Index")
    return fig, ax

if __name__ == "__main__":
    fig, ax = test()
    plt.show()
