
import unittest
from BioHub.backend.biohub import app

class TestBioHub(unittest.TestCase):
    def test_app_exists(self):
        self.assertIsNotNone(app)

if __name__ == "__main__":
    unittest.main()
    