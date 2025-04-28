import os
import sys

sys.path.append(os.path.abspath("../../../Utitlties"))
import VisibleColors

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

"""
The Empirical formula for water areound the ranges of 405 - 790 THz shows how the different wavelengths of light are refracted by
"""
def equation(frequency: float):
    a: float = (frequency / 1e15)**2
    b: float = (1.732 - 0.261 * a)**(-0.5)
    refractiveIndex: float = (b + 1)**0.5
    return refractiveIndex

def test():
    start = 405e12
    end = 790e12
    count = 50
    frequency = np.linspace(start, end, count)
    wavelength = (3e8 / frequency) * 1e9
    refractiveIndex = equation(frequency)

    points = np.array([frequency, refractiveIndex]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    # Map each segment to a color
    colors = [VisibleColors.wavelength_to_rgb(wl) for wl in wavelength]
    hexColors = [VisibleColors.rgb_to_hex(*c) for c in colors]
    segmentColors = hexColors[:-1]  # One less than number of points

    # Create the LineCollection
    lc = LineCollection(segments, colors=segmentColors, linewidth=2)

    fig, ax = plt.subplots()

    ax.set_title("Model of the refractive index of water")
    ax.add_collection(lc)
    ax.autoscale()
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Refractive Index')
    return fig, ax
