import json
import getpass
import os
from cryptography.fernet import Fernet
from password_generator import generate_password
from crypto_utils import load_key, save_key, encrypt_data, decrypt_data

VAULT_FILE = "vault.json.enc"
KEY_FILE = "secret.key"


def load_vault():
    if not os.path.exists(VAULT_FILE):
        return {}
    key = load_key(KEY_FILE)
    with open(VAULT_FILE, "rb") as file:
        encrypted = file.read()
    decrypted = decrypt_data(encrypted, key)
    return json.loads(decrypted)


def save_vault(vault_data):
    key = load_key(KEY_FILE)
    encrypted = encrypt_data(json.dumps(vault_data), key)
    with open( VAULT_FILE, "wb") as file:
        file.write(encrypted)


def main():
    if not os.path.exists(KEY_FILE):
        print("[*] First-time setup: generating encryption key.....")
        save_key(KEY_FILE)
    vault = load_vault()

    while True:
        print("\n--- SecurePassVault ---")
        print("1. Add new credential")
        print("2. View credential")
        print("3. Search by Site")
        print("4. Generate a secure password")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            site = input("Site Name: ")
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            vault[site] = {"username" : username, "password" : password}
            save_vault(vault)
            print("[*] Credential saved.")
        elif choice == "2":
            for site, creds in vault.items():
                print(f"\n{site}")
                print(f"   Username: {creds['username']}")
                print(f"   Password: {creds['password']}")
        elif choice == "3":
            search = input("Enter site name: ").lower()
            found = False
            for site, creds in vault.items():
                if search in site.lower():
                    print(f"\n [+] Found entry for '{site}':")
                    print(f"   Username: {creds['username']}")
                    print(f"   Paswword: {creds['password']}")
                    found = True
            if not found:
                print("[-] No matching site found.")
        elif choice == '4':
            print("Generated Password", generate_password())

        elif choice == '5':
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()