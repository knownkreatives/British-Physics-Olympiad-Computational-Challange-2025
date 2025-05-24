from Utilities import VisibleColors

import matplotlib.pyplot as plt
import numpy as np

# Define number of bands
bands = 7

# Define the range of the X-axis (e.g. visible light spectrum or angle range)
x_min, x_max = 380, 750  # could also be an angle range like 130–138 degrees
x_vals = np.linspace(x_min, x_max, 500)

# Generate dummy data for plotting
elevation_primary = np.sin((x_vals - x_min) / (x_max - x_min) * np.pi) * 10 + 40

# Compute band edges
band_edges = np.linspace(x_min, x_max, bands + 1)

# Plot
fig, ax = plt.subplots()

# Add vertical bands (no color, just vertical lines or labels)
for i in range(bands):
    start = band_edges[i]
    end = band_edges[i + 1]
    ax.axvspan(start, end, color=VisibleColors.rgb_to_hex(*VisibleColors.wavelength_to_rgb((start + end) / 2)), alpha=0.1)
    ax.text((start + end) / 2, ax.get_ylim()[1] - 1, f'Band {i+1}',
            ha='center', va='top', fontsize=9, color='black')

# Plot example data
ax.plot(x_vals, elevation_primary, label='Primary Rainbow', color='black')

# Finalize plot
ax.set_xlabel('Wavelength (nm)')  # or 'Deflection Angle (degrees)'
ax.set_ylabel('Elevation Angle (degrees)')
ax.set_title(f'Rainbow Elevation with {bands} Bands')
ax.legend()
plt.grid(True)
plt.tight_layout()

x_min, x_max = 380, 750
x_vals = np.linspace(x_min, x_max, 1000)
y_vals = np.sin((x_vals - x_min) / (x_max - x_min) * np.pi) * 10 + 40  # Example data

# Band edges
band_edges = np.linspace(x_min, x_max, bands + 1)

# Colors or styles for each band (optional)
colors = plt.cm.viridis(np.linspace(0, 1, bands))  # or use fixed list: ['red', 'green', ...]

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

for i in range(bands):
    start = band_edges[i]
    end = band_edges[i + 1]

    # Mask for current band
    mask = (x_vals >= start) & (x_vals <= end)

    # Plot segment
    ax.plot(x_vals[mask], y_vals[mask], label=f'Band {i + 1}', color=colors[i])

# Labels and legend
ax.set_xlabel('Wavelength (nm)')
ax.set_ylabel('Elevation Angle (degrees)')
ax.set_title(f'Rainbow Elevation with {bands} Bands (Segmented)')
ax.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
