import numpy as np

def get_gradient(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    try:
        gradient = (point2[1] - point1[1]) / (point2[0] - point1[0])
    except ZeroDivisionError:
        gradient = float('inf')
    
    return gradient

def get_perpendicular_gradient(gradient: float):
    if gradient == 0:
        return float('inf')  # vertical line
    elif gradient == float('inf'):
        return 0  # horizontal line
    else:
        return -1 / gradient

def get_line_intersection(p1, m1, p2, m2):
    x1, y1 = p1
    x2, y2 = p2

    # Handle vertical lines (infinite slope)
    if np.isinf(m1):
        x = x1
        y = m2 * (x - x2) + y2
    elif np.isinf(m2):
        x = x2
        y = m1 * (x - x1) + y1
    else:
        # Solve for intersection: m1*(x - x1) + y1 = m2*(x - x2) + y2
        x = ((m1 * x1 - y1) - (m2 * x2 - y2)) / (m1 - m2)
        y = m1 * (x - x1) + y1
    return (x, y)

def find_midpoint(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def find_midpoint_2(xx: tuple[float, float], yy: tuple[float, float]) -> tuple[float, float]:
    return ((xx[0] + xx[1]) / 2, (yy[0] + yy[1]) / 2)

def find_distance(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    return np.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def find_distance_2(xx: tuple[float, float], yy: tuple[float, float]) -> float:
    return np.sqrt((xx[1] - xx[0]) ** 2 + (yy[1] - yy[0]) ** 2)

def find_reflected_point(point: tuple[float, float], intersectPoint: tuple[float, float]):
    reflectPoint = 2 * np.array(intersectPoint) - np.array(point)
    return reflectPoint

def reflect_points(points: list[tuple[float, float]], reflection_line: list[tuple[float, float], tuple[float, float]]):
    gradient = get_gradient(*reflection_line)
    perpendicular_gradient = get_perpendicular_gradient(gradient)
    intersection_point = get_line_intersection(reflection_line[0], gradient, reflection_line[1], perpendicular_gradient)

    reflected_points = np.empty(shape=(len(points), 2))
    
    for i in len(points):
        reflected_points[i] = find_reflected_point(points[i], intersection_point)

    return reflected_points

def reflect_line(line: list[tuple[float, float], tuple[float, float]], reflection_line: list[tuple[float, float], tuple[float, float]]):
    reflected_start = find_reflected_point(line[0], get_line_intersection(line[0], get_gradient(*reflection_line), reflection_line[0], get_perpendicular_gradient(get_gradient(*reflection_line))))
    reflected_end = find_reflected_point(line[1], get_line_intersection(line[1], get_gradient(*reflection_line), reflection_line[0], get_perpendicular_gradient(get_gradient(*reflection_line))))
    reflected_line = [tuple(reflected_start), tuple(reflected_end)]
    return reflected_line