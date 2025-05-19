from scipy.io import wavfile
import numpy as np
import os

def embed_lsb_audio(wav_in_path, data: bytes, wav_out_path):
    rate, signal = wavfile.read(wav_in_path)
    if signal.ndim > 1:
        signal = signal[:, 0]
    signal = signal.copy()
    flat = signal.flatten()
    bits = np.unpackbits(np.frombuffer(data, dtype=np.uint8))
    if len(bits) > len(flat):
        raise ValueError("Payload too large for this audio")
    flat[:len(bits)] = (flat[:len(bits)] & ~1) | bits
    stego_signal = flat.reshape(signal.shape)
    os.makedirs(os.path.dirname(wav_out_path), exist_ok=True)
    wavfile.write(wav_out_path, rate, stego_signal.astype(signal.dtype))