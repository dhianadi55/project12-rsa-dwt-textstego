import numpy as np
import pywt
from PIL import Image

def extract_dwt(stego_path: str, data_len: int, level: int = 1) -> bytes:
    """
    Extract binary data from a stego-image using DWT.
    """
    img = Image.open(stego_path).convert('L')
    arr = np.array(img, dtype=float)

    coeffs = pywt.wavedec2(arr, 'haar', level=level)
    _, details = coeffs[0], coeffs[1:]

    # Flatten detail coefficients
    flat = np.concatenate([cH.flatten() for (cH, cV, cD) in details] + 
                           [cV.flatten() for (cH, cV, cD) in details] + 
                           [cD.flatten() for (cH, cV, cD) in details])
    flat_int = flat.astype(np.int32)

    # Extract bits
    total_bits = data_len * 8
    bits = flat_int[:total_bits] & 1
    data = np.packbits(bits)
    return data.tobytes()