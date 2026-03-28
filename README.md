# Secure Assignment Submission Lab

This project demonstrates practical implementation of cryptographic security controls in real-world scenarios.

This project is a simple cybersecurity lab that demonstrates the four major information security principles:

- Confidentiality
- Integrity
- Authenticity
- Non-Repudiation

The lab simulates a scenario where a student securely submits an assignment to a lecturer using cryptographic techniques.

---

# Background

In many academic environments, assignments are submitted via email or file upload systems. However, these methods do not guarantee:

- the identity of the student submitting the work
- that the file has not been modified
- proof that the student actually submitted the file

This lab demonstrates how cryptographic techniques can solve these problems.

---

# Security Principles Demonstrated

## Confidentiality
Sensitive information should not be accessible to unauthorized users.

## Integrity
The system ensures that the submitted file has not been altered.

This is achieved using **SHA256 hashing**.

## Authenticity
The lecturer can verify that the assignment was submitted by the legitimate student.

This is achieved using **public key cryptography**.

## Non-Repudiation
The student cannot deny submitting the assignment because the submission contains a **digital signature** created using the student's private key.

---

# How the System Works

1. The student submits an assignment.
2. The system generates a SHA256 hash of the assignment file.
3. The student signs the hash using their private key.
4. The lecturer verifies the signature using the student's public key.

---

# Project Structure

secure-assignment-submission-lab
│
├── assignment.txt
├── student_submit.py
├── lecturer_verify.py
└── README.md


---

# Installation

Install Python and the required library.
apt install python3-cryptography


---

# Running the Lab

### Step 1 — Student Submission
python student_submit.py

This script:

- generates RSA keys
- creates a SHA256 hash of the assignment
- signs the hash using the student's private key

---

### Step 2 — Lecturer Verification
python lecturer_verify.py

This script:

- recalculates the assignment hash
- verifies the digital signature
- confirms authenticity of the submission

---

# Testing Integrity Protection

Modify the assignment file:
nano assignment.txt

Change any content.

Run verification again:
python lecturer_verify.py

The system will output:
Verification FAILED

This proves the system detects file tampering.

---

# Technologies Used

- Python
- SHA256 hashing
- RSA digital signatures
- Cryptography library

---

# Learning Objectives

This lab demonstrates practical applications of:

- Public Key Infrastructure (PKI)
- Digital Signatures
- Data Integrity Protection
- Identity Verification

---

# Author

Michael Olayiwola  
Cybersecurity Analyst | ISC2 CC Certified
