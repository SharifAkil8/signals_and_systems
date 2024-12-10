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
sine_square = convolve_1d(sine_wave, square_wave)

# Time axes for convolved signals
t_conv = np.linspace(0, 2*duration, len(square_square), endpoint=False)
t_conv2 = np.linspace(0, 2*duration, len(triangle_square), endpoint=False)
t_conv3 = np.linspace(0, 2*duration, len(sine_square), endpoint=False)

# Create a figure to contain the subplots
plt.figure(figsize=(10, 9))

# First subplot for square_square
plt.subplot(3, 1, 1)  # 3 rows, 1 column, 1st plot
plt.plot(t_conv, square_square)
plt.title('Square Wave Convolved with Square Wave')

# Second subplot for triangle_square
plt.subplot(3, 1, 2)  # 3 rows, 1 column, 2nd plot
plt.plot(t_conv2, triangle_square)
plt.title('Triangle Wave Convolved with Square Wave')

# Third subplot for sine_square
plt.subplot(3, 1, 3)  # 3 rows, 1 column, 3rd plot
plt.plot(t_conv3, sine_square)
plt.title('Sine Wave Convolved with Square Wave')

plt.tight_layout()
plt.show()