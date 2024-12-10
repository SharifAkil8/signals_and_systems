import numpy as np
import matplotlib.pyplot as plt
from utils import calculate_fourier_coefficients, approximate_fourier_series

# Define the square wave function
def square_wave(x):
    return 1 * (x % (2 * np.pi) < np.pi) - 1 * (x % (2 * np.pi) >= np.pi)

# Discretized x values
x = np.linspace(-3*np.pi, 3*np.pi, 1000)

# Calculate Fourier coefficients and approximate the function
harmonics = [1, 3, 5, 7]
approximations = []

for L in harmonics:
    coefficients = calculate_fourier_coefficients(square_wave, L)
    approximation = approximate_fourier_series(coefficients, x)
    approximations.append(approximation)

# Plotting using subplots
plt.figure(figsize=(10, 12))

for i, (L, approximation) in enumerate(zip(harmonics, approximations), start=1):
    plt.subplot(len(harmonics), 1, i)
    plt.plot(x, square_wave(x), label="Original", color='black', linestyle='dotted')
    plt.plot(x, approximation, label=f"L={L}")
    plt.title(f"Fourier Series Approximation (L={L} Harmonics)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

plt.show()