
import hashlib
import hmac
from cryptography.fernet import Fernet

class SecurityModule:
    def __init__(self, key_file="security_key.key"):
        self.key_file = key_file
        self.secret_key = self.load_or_generate_key()
        self.cipher = Fernet(self.secret_key)

    def load_or_generate_key(self):
        """Load the encryption key from a file or generate a new one."""
        try:
            with open(self.key_file, "rb") as key_file:
                return key_file.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as key_file:
                key_file.write(key)
            return key

    def hash_data(self, data: str) -> str:
        """Hash data using SHA-256."""
        return hashlib.sha256(data.encode()).hexdigest()

    def hmac_signature(self, data: str, key: str) -> str:
        """Generate HMAC signature."""
        return hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()

    def encrypt_data(self, data: str) -> str:
        """Encrypt data using symmetric encryption."""
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt encrypted data."""
        return self.cipher.decrypt(encrypted_data.encode()).decode()

# Test the SecurityModule
if __name__ == "__main__":
    sec = SecurityModule()
    message = "Secure Message"
    hashed = sec.hash_data(message)
    signature = sec.hmac_signature(message, "secret_key")
    encrypted = sec.encrypt_data(message)
    decrypted = sec.decrypt_data(encrypted)

    print("Original:", message)
    print("Hashed:", hashed)
    print("HMAC Signature:", signature)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
