import numpy as np
from scipy.io import wavfile
from scipy.fftpack import dct

def extract_dct_audio(wav_in_path, data_len: int, block_size=1024, bits_per_block=4) -> bytes:
    """
    Ekstrak data biner dari koefisien DCT audio.
    """
    rate, signal = wavfile.read(wav_in_path)
    if signal.ndim > 1:
        signal = signal[:, 0]
    signal = signal.astype(np.float64)

    total_bits = data_len * 8
    n_blocks = int(np.ceil(total_bits / bits_per_block))

    bits = []
    idx = 0
    for i in range(n_blocks):
        start = i * block_size
        end = start + block_size
        if end > len(signal):
            break
        block = signal[start:end]
        dct_block = dct(block, norm='ortho')
        for b in range(bits_per_block):
            if idx < total_bits:
                coef_idx = 10 + b
                bit = int(dct_block[coef_idx]) & 1
                bits.append(bit)
                idx += 1
        if idx >= total_bits:
            break

    bits = np.array(bits, dtype=np.uint8)
    data = np.packbits(bits)
    return data.tobytes()[:data_len]