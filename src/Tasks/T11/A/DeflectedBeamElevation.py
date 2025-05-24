from Utilities import VisibleColors
from Tasks.T1.B.EmpiricalFormula import equation

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
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


count = 50
frequencies = np.linspace(405e12, 790e12, count)
wavelengths = (3e8 / frequencies) * 1e9
angles_of_incidence = np.linspace(0, 90, count)
refractive_indices = equation(frequencies)

primary_elevations = [get_elevation_angle_primary(n, a) for n, a in zip(refractive_indices, angles_of_incidence)]
secondary_elevations = [get_elevation_angle_secondary(n, a) for n, a in zip(refractive_indices, angles_of_incidence)]

primary_minimum_angle = np.min([find_angle_of_incidence_primary(n) for n in refractive_indices])
primary_minimum_elevation = np.min(primary_elevations)
secondary_maximum_angle = np.max([find_angle_of_incidence_secondary(n) for n in refractive_indices])
secondary_maximum_elevation = np.max(secondary_elevations)

primary_points = np.array([angles_of_incidence, primary_elevations]).T.reshape(-1, 1, 2)
secondary_points = np.array([angles_of_incidence, secondary_elevations]).T.reshape(-1, 1, 2)
primary_segments = np.concatenate([primary_points[:-1], primary_points[1:]], axis=1)
secondary_segments = np.concatenate([secondary_points[:-1], secondary_points[1:]], axis=1)

colors = [VisibleColors.wavelength_to_rgb(wl) for wl in wavelengths]
hexColors = [VisibleColors.rgb_to_hex(*c) for c in colors]
segmentColors = hexColors[:-1]  # One less than number of points

# Create the LineCollection
primary_curve = LineCollection(primary_segments, colors=segmentColors, linewidth=2)
secondary_curve = LineCollection(secondary_segments, colors=segmentColors, linewidth=2)

fig, ax = plt.subplots()

ax.set_title('Deflected Beam Elevation Angles')
ax.add_collection(primary_curve)
ax.add_collection(secondary_curve)
ax.axline((primary_minimum_angle, primary_minimum_elevation), slope=0, label='Primary Minimum Angle')
ax.axline((secondary_maximum_angle, secondary_maximum_elevation), slope=0, label='Secondary Maximum Angle')
ax.set_xlim([0, 90])
ax.set_ylim([0, 180])
ax.set_xlabel('Angle of Incidence (degrees)')
ax.set_ylabel('Elevation (degrees)')
ax.grid(True)
plt.show()