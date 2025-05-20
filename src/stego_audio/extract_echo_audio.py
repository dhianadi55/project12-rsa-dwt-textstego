import numpy as np
from scipy.io import wavfile

def extract_echo_audio(wav_in_path, data_len: int, delay_0=100, delay_1=200, alpha=0.6) -> bytes:
    """
    Ekstrak data biner dari audio yang disisipi dengan Echo Hiding menggunakan autocorrelation.
    """
    rate, signal = wavfile.read(wav_in_path)
    if signal.ndim > 1:
        signal = signal[:, 0]
    signal = signal.astype(np.float64)

    n_bits = data_len * 8
    bits = []
    win_size = max(delay_0, delay_1) * 2
    for i in range(n_bits):
        # Ambil window untuk bit ke-i
        start = i * max(delay_0, delay_1)
        end = start + win_size
        if end > len(signal):
            bits.append(0)
            continue
        window = signal[start:end]
        window = window - np.mean(window)  # normalisasi DC offset
        # Normalisasi energi window
        norm = np.linalg.norm(window)
        if norm > 0:
            window = window / norm
        # Hitung autocorrelation untuk dua delay
        ac0 = np.correlate(window[:-delay_0], window[delay_0:])[0]
        ac1 = np.correlate(window[:-delay_1], window[delay_1:])[0]
        bits.append(1 if ac1 > ac0 else 0)
    data = np.packbits(bits)
    return data.tobytes()[:data_len]