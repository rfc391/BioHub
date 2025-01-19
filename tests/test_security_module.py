
import unittest
from backend_organized.core.security_module import SecurityModule

class TestSecurityModule(unittest.TestCase):
    def setUp(self):
        self.security = SecurityModule()
        self.test_data = "Test Message"
        self.secret_key = "TestKey123"
    
    def test_hash_data(self):
        hashed = self.security.hash_data(self.test_data)
        self.assertEqual(len(hashed), 64, "Hash length should be 64 characters for SHA-256")

    def test_hmac_signature(self):
        signature = self.security.hmac_signature(self.test_data, self.secret_key)
        self.assertTrue(isinstance(signature, str), "HMAC signature should be a string")

    def test_encrypt_and_decrypt(self):
        encrypted = self.security.encrypt_data(self.test_data)
        decrypted = self.security.decrypt_data(encrypted)
        self.assertEqual(decrypted, self.test_data, "Decrypted data should match the original message")

if __name__ == "__main__":
    unittest.main()
