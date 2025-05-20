import numpy as np
from scipy.io import wavfile
import os

def embed_echo_audio(wav_in_path, data: bytes, wav_out_path, delay_0=100, delay_1=200, alpha=0.6):
    """
    Sisipkan data biner ke audio menggunakan Echo Hiding.
    delay_0, delay_1: delay (samples) untuk bit 0 dan 1.
    alpha: echo amplitude (0 < alpha < 1).
    """
    rate, signal = wavfile.read(wav_in_path)
    if signal.ndim > 1:
        signal = signal[:, 0]
    signal = signal.astype(np.float64)

    bits = np.unpackbits(np.frombuffer(data, dtype=np.uint8))
    n = len(bits)
    min_len = (n+1) * max(delay_0, delay_1)
    if len(signal) < min_len:
        raise ValueError("Audio terlalu pendek untuk payload ini.")

    stego = np.copy(signal)
    for i, bit in enumerate(bits):
        d = delay_1 if bit else delay_0
        idx = i * d
        if idx + d < len(stego):
            stego[idx + d] += alpha * signal[idx]
    stego = np.clip(stego, -32768, 32767).astype(np.int16)
    os.makedirs(os.path.dirname(wav_out_path), exist_ok=True)
    wavfile.write(wav_out_path, rate, stego)