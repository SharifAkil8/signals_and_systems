import numpy as np

def generate_triangle_wave(frequency, amplitude, duration, sampling_rate=44100):
    """
    Generates a triangle wave signal.

    Parameters:
    - frequency (float): Frequency of the triangle wave in Hertz.
    - amplitude (float): Amplitude of the triangle wave.
    - duration (float): Duration of the triangle wave in seconds.
    - sampling_rate (int, optional): The rate at which values are sampled. Default is 44100 (CD quality).

    Returns:
    - t (numpy.ndarray): Time array.
    - y (numpy.ndarray): Generated triangle wave signal.
    """
    # Calculate the time array
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    
    # Calculate the triangle wave signal using numpy's sawtooth function
    # The width parameter set to 0.5 will give a triangle wave
    y = amplitude * np.sawtooth(2 * np.pi * frequency * t, width=0.5)
    
    return t, y

# Example usage:
# t, triangle_wave = generate_triangle_wave(440, 1, 1)
# This will generate a 440Hz triangle wave of amplitude 1 for a duration of 1 second.