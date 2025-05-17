from Crypto.PublicKey import RSA

def generate_rsa_keys(bits: int = 2048, priv_path: str = 'keys/private.pem', pub_path: str = 'keys/public.pem'):
    """
    Generate RSA key pair and save to PEM files.
    """
    key = RSA.generate(bits)
    with open(priv_path, 'wb') as priv_file:
        priv_file.write(key.export_key('PEM'))
    with open(pub_path, 'wb') as pub_file:
        pub_file.write(key.publickey().export_key('PEM'))
    return priv_path, pub_path