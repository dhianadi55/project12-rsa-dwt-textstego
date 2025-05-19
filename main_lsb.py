# main.py
import os
from src.crypto.keygen import generate_rsa_keys
from src.crypto.encrypt import rsa_encrypt
from src.crypto.decrypt import rsa_decrypt
from src.stego.embed import embed_dwt
from src.stego.extract import extract_dwt
from src.stego_audio.embed_lsb_audio import embed_lsb_audio
from src.stego_audio.extract_lsb_audio import extract_lsb_audio

def is_audio(file_path):
    return file_path.lower().endswith('.wav')

if __name__ == "__main__":
    # 1. Generate RSA Keys
    os.makedirs('keys', exist_ok=True)
    priv_path, pub_path = generate_rsa_keys(2048, 'keys/private.pem', 'keys/public.pem')
    print(f"Keys generated: {priv_path}, {pub_path}")

    # 2. Encrypt message
    message = b"Ini pesan rahasia dengan cover image atau audio"
    ciphertext = rsa_encrypt(message, pub_path)
    print("Ciphertext length:", len(ciphertext))

    # 3. Choose cover file (image or audio)
    cover_path = 'data/cover/cover1.jpg'  # ganti ke .wav untuk audio
    cover_path = 'data/cover/cover1.wav'  # ganti ke .wav untuk audio
    stego_path = 'data/stego/stego1' + ('.wav' if is_audio(cover_path) else '.png')

    # 4. Embed ciphertext
    if is_audio(cover_path):
        embed_lsb_audio(cover_path, ciphertext, stego_path)
        print("Stego audio saved to:", stego_path)
    else:
        embed_dwt(cover_path, ciphertext, stego_path)
        print("Stego image saved to:", stego_path)

    # 5. Extract & decrypt
    if is_audio(cover_path):
        extracted = extract_lsb_audio(stego_path, len(ciphertext))
    else:
        extracted = extract_dwt(stego_path, len(ciphertext))

    # Debug: bandingkan ciphertext asli dan hasil ekstraksi
    print("Ciphertext asli     :", ciphertext.hex())
    print("Ciphertext ekstraksi:", extracted.hex())
    print("Sama?", ciphertext == extracted)

    recovered = rsa_decrypt(extracted, priv_path)
    print("Recovered message:", recovered.decode())
