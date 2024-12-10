import numpy as np
import matplotlib.pyplot as plt
from utils import generate_sine_wave, calculate_discrete_fourier_transform

f = 10  # For example purposes
duration = 1  # 1 second
sample_rate_1 = 5*f
sample_rate_2 = (3/2)*f

# 1. Generate the two sinusoid signals
_, signal1 = generate_sine_wave(f, 1, duration, sample_rate=sample_rate_1)
_, signal2 = generate_sine_wave(f, 1, duration, sample_rate=sample_rate_2)

# 2. Compute the DFT of the first signal with exact number of samples
N1 = len(signal1)
dft_signal1_exact = calculate_discrete_fourier_transform(signal1, N1)
dft_signal1_numpy = np.fft.fft(signal1)

# 3. Compute the DFT of the first signal with five times the number of samples
N2 = 5 * len(signal1)
dft_signal1_padded = calculate_discrete_fourier_transform(signal1, N2)
dft_signal1_padded_numpy = np.fft.fft(signal1, N2)

# 4. Compute the DFT of the second signal with the same number as previous item
dft_signal2 = calculate_discrete_fourier_transform(signal2, N2)
dft_signal2_numpy = np.fft.fft(signal2, N2)

# Plotting
plt.figure(figsize=(10, 8))  # Adjust the size as needed

# DFT Signal 1 Exact
plt.subplot(3, 1, 1)
freqs1 = np.fft.fftfreq(N1, 1/sample_rate_1)
plt.plot(np.fft.fftshift(freqs1), np.abs(np.fft.fftshift(dft_signal1_exact)), 'b-', label='utils.py')
plt.plot(np.fft.fftshift(freqs1), np.abs(np.fft.fftshift(dft_signal1_numpy)), 'r--', label='numpy (ground truth)')
plt.title('DFT of Signal 1 (Exact samples)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.legend()

# DFT Signal 1 Padded
plt.subplot(3, 1, 2)
freqs2 = np.fft.fftfreq(N2, 1/sample_rate_1)
plt.plot(np.fft.fftshift(freqs2), np.abs(np.fft.fftshift(dft_signal1_padded)), 'b-', label='utils.py')
plt.plot(np.fft.fftshift(freqs2), np.abs(np.fft.fftshift(dft_signal1_padded_numpy)), 'r--', label='numpy (ground truth)')
plt.title('DFT of Signal 1 (Padded)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.legend()

# DFT Signal 2
plt.subplot(3, 1, 3)
freqs3 = np.fft.fftfreq(N2, 1/sample_rate_2)
plt.plot(np.fft.fftshift(freqs3), np.abs(np.fft.fftshift(dft_signal2)), 'b-', label='utils.py')
plt.plot(np.fft.fftshift(freqs3), np.abs(np.fft.fftshift(dft_signal2_numpy)), 'r--', label='numpy (ground truth)')
plt.title('DFT of Signal 2')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.legend()

plt.tight_layout()
plt.show()

'''What is the DFT and its Purpose?
The DFT is an algorithm that transforms a finite sequence of equally-spaced 
samples of a function (often a time-domain signal) into a sequence of coefficients 
of a finite combination of complex sinusoids, ordered by their frequencies.
It is used to analyze the frequency content of digital signals and systems.'''

'''Transforming a Discrete Time-Domain Signal into the Discrete Frequency Domain:
The DFT takes a discrete time-domain signal, which is typically a sequence of 
real or complex numbers representing the signal amplitude at successive time 
intervals, and converts it into a discrete frequency domain representation. 
This frequency domain representation is a sequence of complex numbers that 
represent the amplitude and phase of sinusoids that, when combined, would 
produce the original time-domain signal. This transformation is crucial 
for analyzing the frequency components of the signal, which can reveal important 
characteristics invisible in the time domain.'''

'''DFT formula: X[k] = Sum from n=0 to N-1 of x[n] * exp((-j * 2 * pi  * k * n)/ N)
Here, X[k] is the k-th element of the frequency-domain representation, 
and the exponential term represents a complex sinusoid. The index k runs 
from 0 to N-1, where N is the number of samples in the time-domain signal.'''

'''Limitations or Challenges with DFT

Computational Complexity: The primary challenge with the DFT, particularly 
for large datasets, is its computational complexity. The standard DFT computation 
has a complexity of O(N^2), which becomes prohibitive for large N.
Spectral Leakage: When the DFT is applied to a signal that contains frequencies 
not exactly matching the DFT sampling grid, spectral leakage occurs, which can 
distort the frequency spectrum.
Resolution: The frequency resolution of the DFT is limited by the length of the 
time-domain signal. Short data sequences can lead to poor frequency resolution.
Windowing Effects: Applying a window to the time-domain signal before performing 
the DFT can reduce some issues like spectral leakage, but it introduces its own 
distortions.'''

'''Fast Fourier Transform (FFT):
The FFT is an algorithm to compute the DFT efficiently. It significantly reduces 
the computational complexity from O(N^2) to O(N log N). There are various FFT 
algorithms, with the most common one being the Cooley-Tukey algorithm. The FFT 
produces the same result as the DFT but is much faster for large datasets.'''

'''Reduction in Computational Complexity by FFT:
The FFT achieves its efficiency by exploiting the symmetry and periodicity 
properties of the DFT. It divides the DFT computation into smaller DFTs, 
recursively, and combines their results to produce the final output. This 
method of divide-and-conquer reduces the number of computations required, 
leading to a dramatic decrease in the time required to compute the DFT, 
especially for signals with a large number of samples.'''