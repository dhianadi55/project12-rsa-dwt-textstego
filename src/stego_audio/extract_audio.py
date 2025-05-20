import numpy as np
import pywt
from scipy.io import wavfile

def extract_dwt_audio(wav_in_path, data_len: int, level=1) -> bytes:
    """
    Ekstrak data biner dari koefisien DWT audio.
    """
    # Baca file WAV
    rate, signal = wavfile.read(wav_in_path)
    if signal.ndim > 1:
        signal = signal[:, 0]
    signal = signal.astype(np.float64)

    # Dekomposisi DWT
    coeffs = pywt.wavedec(signal, 'haar', level=level)
    flat = np.concatenate([c.flatten() for c in coeffs[1:]])

    # Ambil bit dari LSB koefisien
    total_bits = data_len * 8
    bits = flat[:total_bits].astype(np.int32) & 1
    data = np.packbits(bits)
    return data.tobytes()[:data_len]  # pastikan panjang sesuai