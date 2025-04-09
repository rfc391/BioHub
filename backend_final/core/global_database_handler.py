
import requests

class GlobalDatabaseHandler:
    def __init__(self):
        self.base_urls = {
            "FAOSTAT": "https://www.fao.org/faostat/api/v1/data",
            "AGRIS": "https://agris.fao.org/agris-search/api/v1/records",
            "NCBI": "https://api.ncbi.nlm.nih.gov/datasets/v1/",
            "GBIF": "https://api.gbif.org/v1/",
            "GSAP": "https://gsapdata.org/api/v1/"
        }

    def fetch_data(self, database_name, endpoint="", params=None):
        if database_name not in self.base_urls:
            raise ValueError(f"Unknown database: {database_name}")
        url = f"{self.base_urls[database_name]}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

# Example usage
if __name__ == "__main__":
    handler = GlobalDatabaseHandler()
    # Example: Fetch data from FAOSTAT
    try:
        faostat_data = handler.fetch_data("FAOSTAT", "production", {"area": "world"})
        print("FAOSTAT Data Sample:", faostat_data)
    except Exception as e:
        print("Error:", e)
