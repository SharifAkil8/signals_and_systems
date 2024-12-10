# Import necessary libraries
#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Function to generate a sine wave
def generate_sine_wave(frequency, amplitude, duration, sampling_rate=44100):
    # Create an array of time values, spaced according to the sampling rate
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    # Generate the sine wave values for the time array
    y = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, y

# Function to generate a square wave
def generate_square_wave(frequency, amplitude, duration, sampling_rate=44100):
    # Create an array of time values, spaced according to the sampling rate
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    # Generate the square wave values using the sign of the sine wave
    y = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))
    return t, y

# Function to generate a triangle wave
def generate_triangle_wave(frequency, amplitude, duration, sampling_rate=44100):
    # Create an array of time values, spaced according to the sampling rate
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    # Generate the triangle wave values using the sawtooth function with width set to 0.5
    y = amplitude * signal.sawtooth(2 * np.pi * frequency * t, width=0.5)
    return t, y

# Main function to demonstrate signal generation and plotting
def main():
    # Set common parameters for all waveforms
    frequency = 1/(2*np.pi)
    amplitude = 1
    duration = 4/frequency

    # Generate the waveforms using the functions defined above
    t1, sine_wave = generate_sine_wave(frequency, amplitude, duration)
    t2, square_wave = generate_square_wave(frequency, amplitude, duration)
    t3, triangle_wave = generate_triangle_wave(frequency, amplitude, duration)

    # Begin plotting
    plt.figure(figsize=(12, 8))

    # Plot the sine wave
    plt.subplot(3, 1, 1)
    plt.title("Sine Wave")
    plt.plot(t1, sine_wave)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.xlim((0,duration))

    # Plot the square wave
    plt.subplot(3, 1, 2)
    plt.title("Square Wave")
    plt.plot(t2, square_wave)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.xlim((0,duration))

    # Plot the triangle wave
    plt.subplot(3, 1, 3)
    plt.title("Triangle Wave")
    plt.plot(t3, triangle_wave)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.xlim((0,duration))

    # Adjust the layout and display the plot
    plt.tight_layout()
    plt.show()

main()
# %%
