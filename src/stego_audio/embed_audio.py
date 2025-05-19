from scipy.io import wavfile
import numpy as np
import pywt
import os

def embed_dwt_audio(wav_in_path, data: bytes, wav_out_path, level=1):
    rate, signal = wavfile.read(wav_in_path)
    if signal.ndim > 1:
        signal = signal[:, 0]
    signal = signal.astype(np.float64)

    coeffs = pywt.wavedec(signal, 'haar', level=level)
    flat = np.concatenate([c.flatten() for c in coeffs[1:]])
    bits = np.unpackbits(np.frombuffer(data, dtype=np.uint8))

    if len(bits) > len(flat):
        raise ValueError("Payload too large for this audio")

    flat[:len(bits)] = (flat[:len(bits)].astype(np.int32) & ~1) | bits

    idx = 0
    new_coeffs = [coeffs[0]]
    for c in coeffs[1:]:
        size = c.size
        new_c = flat[idx:idx + size].reshape(c.shape)
        new_coeffs.append(new_c)
        idx += size

    stego_signal = pywt.waverec(new_coeffs, 'haar')
    stego_signal = np.clip(stego_signal, -32768, 32767).astype(np.int16)

    os.makedirs(os.path.dirname(wav_out_path), exist_ok=True)
    wavfile.write(wav_out_path, rate, stego_signal)