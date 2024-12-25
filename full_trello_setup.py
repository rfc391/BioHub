
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Trello API credentials
TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
BASE_URL = "https://api.trello.com/1"

# Function to get board details
def get_board(board_id):
    url = f"{BASE_URL}/boards/{board_id}"
    params = {
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN,
    }
    response = requests.get(url, params=params)
    return response.json()

# Function to create a list on a board
def create_list(board_id, name):
    url = f"{BASE_URL}/boards/{board_id}/lists"
    params = {
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN,
        "name": name,
    }
    response = requests.post(url, params=params)
    return response.json()

# Function to create a card in a list
def create_card(list_id, name, description=""):
    url = f"{BASE_URL}/cards"
    params = {
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN,
        "idList": list_id,
        "name": name,
        "desc": description,
    }
    response = requests.post(url, params=params)
    return response.json()

# Full setup: Board details, lists, and cards
def setup_full_project(board_id):
    # Get board details
    board_details = get_board(board_id)
    print("Board Details:", board_details)

    # Add lists
    to_do_list = create_list(board_id, "To Do")
    in_progress_list = create_list(board_id, "In Progress")
    done_list = create_list(board_id, "Done")
    print("Lists Created:", to_do_list, in_progress_list, done_list)

    # Add example cards
    create_card(to_do_list["id"], "Set up Docker", "Build and test Docker environment for the project.")
    create_card(to_do_list["id"], "Write Documentation", "Create initial project documentation.")

    print("Project setup completed!")

if __name__ == "__main__":
    # Replace with your actual board ID
    board_id = "ITLfDr4L"
    setup_full_project(board_id)
