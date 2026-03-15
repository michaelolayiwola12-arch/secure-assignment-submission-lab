import hashlib
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

# STEP 1: Load public key

with open("student_public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# STEP 2: Recalculate assignment hash

with open("assignment.txt", "rb") as f:
    data = f.read()

new_hash = hashlib.sha256(data).hexdigest()

print("Calculated hash:", new_hash)

# STEP 3: Load signature

with open("signature.sig", "rb") as f:
    signature = f.read()

# STEP 4: Verify signature

try:
    public_key.verify(
        signature,
        new_hash.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("Assignment VERIFIED")
    print("Student submission is authentic")

except:
    print("Verification FAILED")
