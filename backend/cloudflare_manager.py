
import os
import requests

# Cloudflare API settings
API_URL = "https://api.cloudflare.com/client/v4/zones"
API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
ZONE_ID = os.getenv("CLOUDFLARE_ZONE_ID")

# Headers for Cloudflare API requests
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Function to add or update a DNS record
def manage_dns_record(record_name, record_type, content):
    url = f"{API_URL}/{ZONE_ID}/dns_records"
    data = {
        "type": record_type,
        "name": record_name,
        "content": content,
        "ttl": 1,
        "proxied": True
    }
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 200:
        print("DNS record managed successfully.")
    else:
        print("Error managing DNS record:", response.json())

# Example usage
if __name__ == "__main__":
    manage_dns_record("example.com", "A", "123.123.123.123")
