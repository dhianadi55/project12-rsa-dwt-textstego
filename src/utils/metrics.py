import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim

def compute_psnr(original, stego):
    return psnr(original, stego)

def compute_ssim(original, stego):
    return ssim(original, stego)
