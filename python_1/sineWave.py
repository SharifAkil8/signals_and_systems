#%%

import numpy as np

#%%

def generate_sine_wave(frequency, amplitude, duration, sampling_rate=44100):
    """
    Generates a sine wave signal.

    Parameters:
    - frequency (float): Frequency of the sine wave in Hertz.
    - amplitude (float): Amplitude of the sine wave.
    - duration (float): Duration of the sine wave in seconds.
    - sampling_rate (int, optional): The rate at which values are sampled. Default is 44100 (CD quality).

    Returns:
    - t (numpy.ndarray): Time array.
    - y (numpy.ndarray): Generated sine wave signal.
    """
    # Calculate the time array
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    
    # Calculate the sine wave signal
    y = amplitude * np.sin(2 * np.pi * frequency * t)
    
    return t, y

# Example usage:
# t, sine_wave = generate_sine_wave(440, 1, 1)
# This will generate a 440Hz sine wave of amplitude 1 for a duration of 1 second.
# %%