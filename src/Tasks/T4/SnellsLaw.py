from Tasks.T3.FermatsPrinciple import equation as fermatsPrinciple

import matplotlib.pyplot as plt
import numpy as np

"""
The angle of a ray incident to the suface of a transparent material, will change in speed depending on the optical density of the refracting medium
"""
def equation(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    refractiveIndex: float,
    speedOfRay: float = 3e8):
    timeOfFlight: float = ((x1**2 + y1**2)**0.5) / (speedOfRay / refractiveIndex)
    timeOfFlight += (((x2 - x1)**2 + (y2 - y1)**2)**0.5) / (speedOfRay / refractiveIndex)
    
    return timeOfFlight

def test():
    start = 0
    middle = 1
    end = 2
    count = 50
    x = np.linspace(start, end, count)

    fig, ax = plt.subplots()
    ax.set_title("Flight time of light")
    ax.plot(x, fermatsPrinciple(x, middle, end, 1))
    ax.plot(x, equation(x, middle, 2 * x, end, 1))
    ax.autoscale()
    ax.set_xlabel("x (m)")
    ax.set_xlim(start, end)
    ax.set_ylabel("Time of flight (s)")

    return fig, ax

if __name__ == "__main__":
    fig, ax = test()
    plt.show()