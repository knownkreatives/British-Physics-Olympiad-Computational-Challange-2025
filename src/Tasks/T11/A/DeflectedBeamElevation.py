from Utilities import VisibleColors
from Tasks.T1.B.EmpiricalFormula import equation

import matplotlib.pyplot as plt
import numpy as np


def get_elevation_angle_primary(refractve_index: float, angle_of_incidence: float) -> float:
    # pi - 6 arcsin(sin(θ) / n) + 2θ
    return np.pi - 6 * np.arcsin(np.sin(np.radians(angle_of_incidence)) / refractve_index) + 2 * np.radians(angle_of_incidence)

def get_elevation_angle_secondary(refractive_index: float, angle_of_incidence: float) -> float:
    # 4 arcsin(sin(θ) / n) - 2θ
    return 4 * np.arcsin(np.sin(np.radians(angle_of_incidence)) / refractive_index) - 2 * np.radians(angle_of_incidence)

def find_angle_of_incidence_primary(refractive_index: float) -> float:
    # arcsin(sqrt((9 - n^2) / 8))
    return np.degrees(np.arcsin(np.sqrt((9 - refractive_index**2) / 8)))

def find_angle_of_incidence_secondary(refractive_index: float) -> float:
    # arcsin(sqrt((4 - n^2) / 3))
    return np.degrees(np.arcsin(np.sqrt((4 - refractive_index**2) / 3)))


