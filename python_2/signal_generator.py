# signal_generator.py

import numpy as np
import matplotlib.pyplot as plt
from utils import generate_sine_wave, generate_square_wave, generate_triangle_wave

# Parameters
frequency = 5
amplitude = 1
duration = 1

# Generate signals
t_sine, sine_wave = generate_sine_wave(frequency, amplitude, duration)
t_square, square_wave = generate_square_wave(frequency, amplitude, duration)
t_triangle, triangle_wave = generate_triangle_wave(frequency, amplitude, duration)

# Plot signals
plt.figure(figsize=(12,8))
plt.subplot(3,1,1)
plt.title('Sine Wave')
plt.plot(t_sine, sine_wave)

plt.subplot(3,1,2)
plt.title('Square Wave')
plt.plot(t_square, square_wave)

plt.subplot(3,1,3)
plt.title('Triangle Wave')
plt.plot(t_triangle, triangle_wave)

plt.tight_layout()
plt.show()