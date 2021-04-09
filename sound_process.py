import librosa
import numpy as np
from constants import *

# constants
hop_length = 512
n_fft = 8192

time_series, sample_rate = librosa.load(filename)

# Short-time Fourier transform - frequencies over time
stft = np.abs(librosa.stft(time_series, hop_length=hop_length, n_fft=n_fft))

# transpose frequency to dB
spectrogram = librosa.amplitude_to_db(stft, ref=np.max)

# generate an array of frequencies
frequencies = librosa.core.fft_frequencies(n_fft=n_fft)

# generate an array of time periods
spectrogram_time_count = spectrogram.shape[1]
times = librosa.core.frames_to_time(np.arange(spectrogram_time_count), sr=sample_rate, hop_length=hop_length,
                                    n_fft=n_fft)


def get_index_ratio(arr):
    return len(arr) / arr[len(arr) - 1]


# ratios
time_index_ratio = get_index_ratio(times)
frequencies_index_ratio = get_index_ratio(frequencies)


def get_decibel(target_time, freq):
    return spectrogram[int(freq * frequencies_index_ratio)][int(target_time * time_index_ratio)]
