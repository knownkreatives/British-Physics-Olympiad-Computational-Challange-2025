import matplotlib.pyplot as plt
import numpy as np

"""
The angle of a ray incident to the suface of a transparent material, will change in speed depending on the optical density of the refracting medium
"""
def equation(
    x: float,
    y: float,
    length: float,
    refractiveIndex: float,
    speedOfRay: float = 3e8):
    timeOfFlight: float = ((x**2 + y**2)**0.5) / (speedOfRay / refractiveIndex)
    timeOfFlight += (((length - x)**2 + y**2)**0.5) / (speedOfRay / refractiveIndex)
    
    return timeOfFlight

def test(
    start = 0,
    middle = 1,
    end = 2,
    count = 50,
    fig: plt.Figure = None, ax: plt.Axes = None):
    x = np.linspace(start, end, count)
    
    if fig is None and ax is None:
        fig, ax = plt.subplots()

    ax.set_title("Flight time of light")
    ax.plot(x, equation(x, middle, end, 1))
    ax.autoscale()
    ax.set_xlabel("x (m)")
    ax.set_xlim(start, end)
    ax.set_ylabel("Time of flight (s)")
    
    return fig, ax

if __name__ == "__main__":
    fig, ax = test()
    plt.show()