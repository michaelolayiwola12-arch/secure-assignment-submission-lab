import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# STEP 1: Generate student RSA keys

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

# Save private key
with open("student_private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Save public key
with open("student_public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("Keys generated")


# STEP 2: Generate file hash (Integrity)

with open("assignment.txt", "rb") as f:
    data = f.read()

file_hash = hashlib.sha256(data).hexdigest()

print("File hash:", file_hash)


# STEP 3: Sign the hash (Authenticity + Non-repudiation)

signature = private_key.sign(
    file_hash.encode(),
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Save signature
with open("signature.sig", "wb") as f:
    f.write(signature)

print("Assignment signed successfully")
