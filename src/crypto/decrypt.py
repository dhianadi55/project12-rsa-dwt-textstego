from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def rsa_decrypt(ciphertext: bytes, priv_path: str = 'keys/private.pem') -> bytes:
    """
    Decrypt ciphertext using RSA private key.
    """
    key_data = open(priv_path, 'rb').read()
    rsa_key = RSA.import_key(key_data)
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.decrypt(ciphertext)