from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import matplotlib.pyplot as plt
import numpy as np

"""
"""
def equation(
    distanceToSource: float,
    distanceToScreen: float):
    focalDistanceInverse: float

    focalDistanceInverse = (1 / distanceToSource) + (1 / distanceToScreen)

    focalDistance: float = 1 / focalDistanceInverse
    return focalDistance

def generate_spreadsheet(
    sheetName: str,
    fileName: str,
    distancesToSource: list[float],
    distancesToScreen: list[float]):
    wb = Workbook()
    
    ws = wb.active
    ws.title = sheetName
    
    header = ['u (cm)', 'v (cm)', '1 / u', '1 / v', 'f (cm)']
    ws.append(header)
    
    for row in range(0, len(distancesToSource)):
        for col in range(1, 6):
            cell = get_column_letter(col) + str(row + 2)
            match(col):
                case 1:
                    ws[cell] = distancesToSource[row]
                case 2:
                    ws[cell] = distancesToScreen[row]
                case 3:
                    ws[cell] = 1 / distancesToSource[row]
                case 4:
                    ws[cell] = 1 / distancesToScreen[row]
                case 5:
                    ws[cell] = equation(distancesToScreen[row], distancesToSource[row])
    
    wb.save(fileName+".xlsx")

def test():
    u = [20, 25, 30, 35, 40, 45, 50, 55]
    v = [65.5, 40, 31, 27, 25, 23.1, 21.5, 20.5]
    generate_spreadsheet("Test", "File", u, v)

    uInverse = np.array([1 / val for val in u])
    vInverse = np.array([1 / val for val in v])
    
    coefficients = np.polyfit(uInverse, vInverse, 1)
    lineOfBestFit = np.poly1d(coefficients)

    y_fit = lineOfBestFit(uInverse)

    meanAbsoluteError = np.mean(np.abs(y_fit - vInverse))
    meanSquaredError = np.mean((y_fit - vInverse)**2)
    rootMeanSquaredError = np.sqrt(meanSquaredError)
    print(f"Mean Absolute Error: {meanAbsoluteError}",
          f"Mean Squared Error: {meanSquaredError}",
          f"Root Mean Squared Error:: {rootMeanSquaredError}", sep="\n")

    fig, ax = plt.subplots()

    ax.set_title("Assessing the veracity of the thin lens equation")
    ax.scatter(uInverse, vInverse, color="#D5615F", marker="x")
    ax.plot(uInverse, y_fit, color="#41A3D0")
    ax.set_xlabel("1 / u")
    ax.set_xlabel("1 / y")
    plt.show()

test()
