
class MockGlobalDatabaseHandler:
    def fetch_data(self, database_name, endpoint="", params=None):
        if database_name == "FAOSTAT":
            return {
                "data": [
                    {"country": "World", "year": 2020, "value": 123456},
                    {"country": "World", "year": 2021, "value": 234567},
                ],
                "metadata": {
                    "source": "Mock FAOSTAT",
                    "description": "Simulated response for testing purposes",
                },
            }
        else:
            raise ValueError(f"Mock data not available for {database_name}")
