import numpy as np
import pywt
from PIL import Image

def embed_dwt(image_path: str, data: bytes, output_path: str, level: int = 1):
    """
    Embed binary data into an image using DWT.
    """
    img = Image.open(image_path).convert('L')
    arr = np.array(img, dtype=float)

    # Decompose
    coeffs = pywt.wavedec2(arr, 'haar', level=level)
    cA, details = coeffs[0], coeffs[1:]

    # Flatten detail coefficients
    flat = np.concatenate([cH.flatten() for (cH, cV, cD) in details] + 
                           [cV.flatten() for (cH, cV, cD) in details] + 
                           [cD.flatten() for (cH, cV, cD) in details])
    flat_int = flat.astype(np.int32)

    # Convert data to bits
    bits = np.unpackbits(np.frombuffer(data, dtype=np.uint8))
    if bits.size > flat_int.size:
        raise ValueError('Payload too large')

    # Embed bits in LSB
    flat_int[:bits.size] = (flat_int[:bits.size] & ~1) | bits

    # Reconstruct details
    new_details = []
    idx = 0
    for cH, cV, cD in details:
        size = cH.size
        new_cH = flat_int[idx:idx+size].reshape(cH.shape); idx += size
        size = cV.size
        new_cV = flat_int[idx:idx+size].reshape(cV.shape); idx += size
        size = cD.size
        new_cD = flat_int[idx:idx+size].reshape(cD.shape); idx += size
        new_details.append((new_cH, new_cV, new_cD))

    # Inverse DWT
    new_coeffs = [cA] + new_details
    stego_arr = pywt.waverec2(new_coeffs, 'haar')
    stego_img = Image.fromarray(np.clip(stego_arr, 0, 255).astype(np.uint8))
    stego_img.save(output_path)
    return output_path
