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