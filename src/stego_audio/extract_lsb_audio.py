import numpy as np
from scipy.io import wavfile

def extract_lsb_audio(wav_in_path, data_len: int) -> bytes:
    rate, signal = wavfile.read(wav_in_path)
    if signal.ndim > 1:
        signal = signal[:, 0]
    flat = signal.flatten()
    total_bits = data_len * 8
    bits = flat[:total_bits] & 1
    data = np.packbits(bits)
    return data.tobytes()