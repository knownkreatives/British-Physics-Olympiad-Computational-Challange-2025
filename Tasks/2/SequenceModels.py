import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error

### Done with AI

# Original data
x = np.arange(len([65.5, 40, 31, 27, 25, 23.1, 21.5, 20.5]))
y = np.array([65.5, 40, 31, 27, 25, 23.1, 21.5, 20.5])
x_shifted = x + 1  # avoid log(0), div by 0, etc.

# Model definitions
def log_model(x, a, b, c):
    return a * np.log(x + b) + c

def exp_model(x, a, b, c):
    return a * np.exp(-b * x) + c

def power_model(x, a, b, c):
    return a * np.power(x + b, -1) + c

def inverse_model(x, a, b, c):
    return a / (x + b) + c

# Fit all models
models = {
    "Logarithmic": log_model,
    "Exponential": exp_model,
    "Power Law": power_model,
    "Inverse": inverse_model
}

params = {}
mse_scores = {}
x_fit = np.linspace(1, len(x), 100)

# Fit and calculate MSE
for name, model in models.items():
    popt, _ = curve_fit(model, x_shifted, y, maxfev=10000)
    y_pred = model(x_shifted, *popt)
    mse = mean_squared_error(y, y_pred)
    mse_scores[name] = mse
    params[name] = popt

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(x_shifted, y, 'o', label='Original Data', color='black')

for name, model in models.items():
    y_fit = model(x_fit, *params[name])
    plt.plot(x_fit, y_fit, label=f'{name} Fit (MSE: {mse_scores[name]:.3f})')

plt.title('Model Fits to the Sequence')
plt.xlabel('Index (shifted)')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Print MSEs and parameters
print("Mean Squared Errors and Parameters:\n")
for name in models:
    print(f"{name}: MSE = {mse_scores[name]:.4f}, Parameters = {params[name]}")
