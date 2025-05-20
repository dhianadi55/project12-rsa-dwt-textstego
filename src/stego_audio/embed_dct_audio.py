import numpy as np
from scipy.io import wavfile
from scipy.fftpack import dct, idct
import os

def embed_dct_audio(wav_in_path, data: bytes, wav_out_path, block_size=1024, bits_per_block=4):
    """
    Sisipkan data biner ke dalam koefisien DCT audio (bukan LSB PCM).
    """
    # Baca file WAV
    rate, signal = wavfile.read(wav_in_path)
    if signal.ndim > 1:
        signal = signal[:, 0]
    signal = signal.astype(np.float64)

    # Ubah data ke bit array
    bits = np.unpackbits(np.frombuffer(data, dtype=np.uint8))
    total_bits = len(bits)
    n_blocks = int(np.ceil(total_bits / bits_per_block))

    if n_blocks * block_size > len(signal):
        raise ValueError("Payload terlalu besar untuk audio ini")

    stego_signal = np.copy(signal)
    idx = 0
    for i in range(n_blocks):
        start = i * block_size
        end = start + block_size
        if end > len(signal):
            break
        block = stego_signal[start:end]
        dct_block = dct(block, norm='ortho')
        for b in range(bits_per_block):
            if idx < total_bits:
                coef_idx = 10 + b  # gunakan koefisien 10,11,12,13
                coef = int(dct_block[coef_idx])
                coef = (coef & ~1) | int(bits[idx])  # pastikan bits[idx] bertipe int
                dct_block[coef_idx] = coef
                idx += 1
        stego_signal[start:end] = idct(dct_block, norm='ortho')
        if idx >= total_bits:
            break

    stego_signal = np.clip(stego_signal, -32768, 32767).astype(np.int16)
    os.makedirs(os.path.dirname(wav_out_path), exist_ok=True)
    wavfile.write(wav_out_path, rate, stego_signal)