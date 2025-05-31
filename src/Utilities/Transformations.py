import numpy as np

def create_2d_rotation_matrix(angle_radians):
    """Create 2D rotation matrix"""
    cos_a = np.cos(angle_radians)
    sin_a = np.sin(angle_radians)
    return np.array([
        [cos_a, -sin_a],
        [sin_a,  cos_a]
    ])

def create_2d_scaling_matrix(sx, sy):
    """Create 2D scaling matrix"""
    return np.array([
        [sx, 0],
        [0, sy]
    ])

def create_2d_translation_matrix(tx, ty):
    """Create 2D translation matrix (homogeneous coordinates)"""
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def create_2d_shear_matrix(shx, shy):
    """Create 2D shear matrix"""
    return np.array([
        [1, shx],
        [shy, 1]
    ])