# main.py
from src.crypto.keygen import generate_rsa_keys
from src.crypto.encrypt import rsa_encrypt
from src.crypto.decrypt import rsa_decrypt
from src.stego.embed import embed_dwt
from src.stego.extract import extract_dwt

if __name__ == "__main__":
    # 1. Generate RSA Keys
    priv_path, pub_path = generate_rsa_keys(2048, 'keys/private.pem', 'keys/public.pem')
    print(f"Keys generated: {priv_path}, {pub_path}")

    # 2. Encrypt message
    message = b"Ini pesan rahasia"
    ciphertext = rsa_encrypt(message, pub_path)
    print("Ciphertext length:", len(ciphertext))

    # 3. Embed ke cover image
    stego_path = embed_dwt('data/cover/cover1.jpg', ciphertext, 'data/stego/stego1.png')
    print("Stego image saved to:", stego_path)

    # 4. Extract & decrypt
    extracted = extract_dwt(stego_path, len(ciphertext))
    recovered = rsa_decrypt(extracted, priv_path)
    print("Recovered message:", recovered.decode())
