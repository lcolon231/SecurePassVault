# SecurePassVault

A simple, local. encrypted password manager built in Python. SecurePassVault lets you generate, store, and retrieve credentials securely - all from the command line.

---

## Features
- Encrypts credentials with AES (Fernet)
- Stores data locally in vaul.json.enc
- Protects data with a master encryption key
- Built-in secure password generator
- Lightweight and beginner-friendly CLI

---

## How IT Works

- On first run, a secret encryption key is generated and stored in 'secret.key'
- Credentials are stored in memory, encrypted using Fernet, and saved to 'vault.json.enc'
- You can:
  - Add new login credentials
  - View saved credentials
  - Generate random secure passwords

---

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/lcolon231/SecurePassVault.git
cd SecurePassVault