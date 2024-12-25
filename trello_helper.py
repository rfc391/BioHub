
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
BASE_URL = "https://api.trello.com/1"

def create_board(name):
    url = f"{BASE_URL}/boards/"
    params = {
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN,
        "name": name,
    }
    response = requests.post(url, params=params)
    return response.json()

def create_list(board_id, name):
    url = f"{BASE_URL}/boards/{board_id}/lists"
    params = {
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN,
        "name": name,
    }
    response = requests.post(url, params=params)
    return response.json()

def setup_project_management():
    # Create a Trello board
    board = create_board("BioHub Project Management")
    print("Board created:", board["url"])

    # Add lists to the board
    board_id = board["id"]
    create_list(board_id, "To Do")
    create_list(board_id, "In Progress")
    create_list(board_id, "Done")
    print("Lists created successfully.")

if __name__ == "__main__":
    setup_project_management()
