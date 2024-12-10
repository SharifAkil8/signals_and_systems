# utils.py

import numpy as np

def generate_sine_wave(frequency, amplitude, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate*duration), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, signal

def generate_square_wave(frequency, amplitude, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate*duration), endpoint=False)
    signal = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))
    return t, signal

def generate_triangle_wave(frequency, amplitude, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate*duration), endpoint=False)
    period = 1.0 / frequency
    signal = 2 * (t/period - np.floor(1/2 + t/period))  # Triangle wave from -1 to 1
    signal = amplitude * (np.abs(signal) * 2 - 1)  # Convert to amplitude
    return t, signal

def convolve_1d(signal1, signal2):
    m, n = len(signal1), len(signal2)
    result = np.zeros(m + n - 1)

    for i in range(m):
        for j in range(n):
            result[i+j] += signal1[i] * signal2[j]

    return result

def calculate_fourier_coefficients(f, N):
    coefficients = []

    x = np.linspace(-np.pi, np.pi, 1000)  # Discretize the interval [-pi, pi]
    dx = x[1] - x[0]

    for n in range(N+1):
        a_n = (1/np.pi) * np.sum(f(x) * np.cos(n*x)) * dx
        b_n = (1/np.pi) * np.sum(f(x) * np.sin(n*x)) * dx
        coefficients.append((a_n, b_n))

    return coefficients

def approximate_fourier_series(coefficients, x):
    approximation = np.zeros_like(x)
    for n, (a_n, b_n) in enumerate(coefficients):
        approximation += a_n * np.cos(n*x) + b_n * np.sin(n*x)
    return approximation

def calculate_discrete_fourier_transform(signal, N):
    # Pad zeros if N is larger than the signal length
    if N > len(signal):
        signal = np.pad(signal, (0, N - len(signal)), 'constant')

    result = np.zeros(N, dtype=complex)

    for k in range(N):
        for n in range(N):
            result[k] += signal[n] * np.exp(-1j * (2 * np.pi / N) * k * n)
    
    return result