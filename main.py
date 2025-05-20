import os
from src.crypto.keygen import generate_rsa_keys
from src.crypto.encrypt import rsa_encrypt
from src.crypto.decrypt import rsa_decrypt
from src.stego_audio.embed_dct_audio import embed_dct_audio
from src.stego_audio.extract_dct_audio import extract_dct_audio

def is_audio(file_path):
    return file_path.lower().endswith('.wav')

if __name__ == "__main__":
    # 1. Generate RSA Keys
    os.makedirs('keys', exist_ok=True)
    priv_path, pub_path = generate_rsa_keys(2048, 'keys/private.pem', 'keys/public.pem')
    print(f"Keys generated: {priv_path}, {pub_path}")

    # 2. Encrypt message
    message = b"Test"
    ciphertext = rsa_encrypt(message, pub_path)
    print("Ciphertext length:", len(ciphertext))

    # 3. Choose cover file (audio)
    cover_path = 'data/cover/cover1.wav'
    stego_path = 'data/stego/stego1.wav'

    # 4. Embed ciphertext
    embed_dct_audio(cover_path, ciphertext, stego_path, block_size=1024, bits_per_block=4)
    print("Stego audio saved to:", stego_path)

    # 5. Extract & decrypt
    extracted = extract_dct_audio(stego_path, len(ciphertext), block_size=1024, bits_per_block=4)
    # Debug: bandingkan ciphertext asli dan hasil ekstraksi
    print("Ciphertext asli     :", ciphertext.hex())
    print("Ciphertext ekstraksi:", extracted.hex())
    print("Sama?", ciphertext == extracted)
    for i, (a, b) in enumerate(zip(ciphertext, extracted)):
        if a != b:
            print(f"Byte ke-{i}: asli={a:02x}, ekstrak={b:02x}")
            break

    recovered = rsa_decrypt(extracted, priv_path)
    print("Recovered message:", recovered.decode())