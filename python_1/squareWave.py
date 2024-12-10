import numpy as np

def generate_square_wave(frequency, amplitude, duration, sampling_rate=44100):
    """
    Generates a square wave signal.

    Parameters:
    - frequency (float): Frequency of the square wave in Hertz.
    - amplitude (float): Amplitude of the square wave.
    - duration (float): Duration of the square wave in seconds.
    - sampling_rate (int, optional): The rate at which values are sampled. Default is 44100 (CD quality).

    Returns:
    - t (numpy.ndarray): Time array.
    - y (numpy.ndarray): Generated square wave signal.
    """
    # Calculate the time array
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    
    # Calculate the square wave signal using numpy's sign function and sin wave
    y = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))
    
    return t, y

# Example usage:
# t, square_wave = generate_square_wave(440, 1, 1)
# This will generate a 440Hz square wave of amplitude 1 for a duration of 1 second.