import sys
import numpy as np
import pandas as pd

# Check if the user provided a file path
if len(sys.argv) < 2:
    print("Usage: python3 script.py <path_to_csv>")
    sys.exit(1)

# Load the CSV file
file_path = sys.argv[1]
data = pd.read_csv(file_path, skiprows=6, header=None, names=["T", "V"], low_memory=False)  # Skip the header lines until the data starts

# Extract time (T) and signal (v(OSC))
time = data['T'].values
signal = data['V'].values

# Calculate the amplitude midpoint
amplitude_midpoint = (np.max(signal) + np.min(signal)) / 2

# Find rising edge crossings of the midpoint
rising_edges = np.where((signal[:-1] < amplitude_midpoint) & (signal[1:] >= amplitude_midpoint))[0]

# Interpolate crossing times for better accuracy
interpolated_crossings = []
for idx in rising_edges:
    t1, t2 = time[idx], time[idx + 1]
    v1, v2 = signal[idx], signal[idx + 1]
    interpolated_time = t1 + (amplitude_midpoint - v1) * (t2 - t1) / (v2 - v1)
    interpolated_crossings.append(interpolated_time)

interpolated_crossings = np.array(interpolated_crossings)
periods = np.diff(interpolated_crossings)
crystal_frequency = 1 / np.mean(periods)

# Convert crystal frequency to MHz
crystal_frequency_mhz = crystal_frequency / 1e6

print(f"Frequency: {crystal_frequency_mhz:.6f} MHz")

