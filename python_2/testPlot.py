import numpy as np
import matplotlib.pyplot as plt
from utils import generate_sine_wave, generate_square_wave, generate_triangle_wave, convolve_1d

# Parameters
frequency = 5
amplitude = 1
duration = 1
sample_rate = 1000  # Reduced sample rate for clarity

# Generate signals
t, sine_wave = generate_sine_wave(frequency, amplitude, duration, sample_rate)
_, square_wave = generate_square_wave(frequency, amplitude, duration, sample_rate)
_, triangle_wave = generate_triangle_wave(frequency, amplitude, duration, sample_rate)

# Convolve signals
square_square = convolve_1d(square_wave, square_wave)
triangle_square = convolve_1d(triangle_wave, square_wave)

# Time axes for convolved signals
t_conv = np.linspace(0, 2*duration, len(square_square), endpoint=False)
t_conv2 = np.linspace(0, 2*duration, len(triangle_square), endpoint=False)

# Plot convolved signals
plt.figure(figsize=(6, 4))
plt.plot(t_conv, square_square)
plt.title('Square Wave Convolved with Square Wave')
plt.tight_layout()
plt.show()

# Plot the second convolved signal in a new window
plt.figure(figsize=(6, 4))
plt.plot(t_conv2, triangle_square)
plt.title('Triangle Wave Convolved with Square Wave')
plt.tight_layout()
plt.show()