
import unittest
import requests

BASE_URL = "http://localhost:8081"

class TestEndToEnd(unittest.TestCase):
    def test_security_hashing(self):
        endpoint = f"{BASE_URL}/api/security/hash"
        payload = {"data": "Test Message"}
        response = requests.post(endpoint, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("hashed_data", response.json())

    def test_security_encryption(self):
        endpoint = f"{BASE_URL}/api/security/encrypt"
        payload = {"data": "Test Message"}
        response = requests.post(endpoint, json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("encrypted_data", response.json())

    def test_security_decryption(self):
        encrypt_endpoint = f"{BASE_URL}/api/security/encrypt"
        decrypt_endpoint = f"{BASE_URL}/api/security/decrypt"
        payload = {"data": "Test Message"}
        encrypt_response = requests.post(encrypt_endpoint, json=payload)
        encrypted_data = encrypt_response.json().get("encrypted_data")

        decrypt_payload = {"encrypted_data": encrypted_data}
        decrypt_response = requests.post(decrypt_endpoint, json=decrypt_payload)
        self.assertEqual(decrypt_response.status_code, 200)
        self.assertEqual(decrypt_response.json().get("decrypted_data"), "Test Message")

    def test_global_database_fetch(self):
        endpoint = f"{BASE_URL}/api/global-data/FAOSTAT"
        params = {"endpoint": "production", "area": "world"}
        response = requests.get(endpoint, params=params)
        self.assertEqual(response.status_code, 200)
        self.assertIn("data", response.json())

if __name__ == "__main__":
    unittest.main()
