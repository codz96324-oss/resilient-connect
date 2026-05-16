from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

def encrypt_message(message: str):
    return fernet.encrypt(message.encode())

def decrypt_message(token: bytes):
    return fernet.decrypt(token).decode()
