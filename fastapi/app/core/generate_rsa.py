from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend)
private_key_pem = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption())
public_key_pem = private_key.public_key().public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

with open("private_key.pem", "wb") as pf:
    pf.write(private_key_pem)

with open("public_key.pem", "wb") as ppf:
    ppf.write(public_key_pem)

print("RSA keys generated in current directory.")
