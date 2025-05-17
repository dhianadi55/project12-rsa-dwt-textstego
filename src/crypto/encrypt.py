from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def rsa_encrypt(message: bytes, pub_path: str = 'keys/public.pem') -> bytes:
    """
    Encrypt message using RSA public key.
    """
    key_data = open(pub_path, 'rb').read()
    rsa_key = RSA.import_key(key_data)
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.encrypt(message)