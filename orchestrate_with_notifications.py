import subprocess
import docker
from trello import TrelloClient
import requests
import time
import schedule
import logging
import yagmail
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Secure Configuration - Load from environment variables
TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
TRELLO_API_TOKEN = os.getenv('TRELLO_API_TOKEN')
TRELLO_BOARD_ID = os.getenv('TRELLO_BOARD_ID')
CLOUDFLARE_API_TOKEN = os.getenv('CLOUDFLARE_API_TOKEN')
CLOUDFLARE_ZONE_ID = os.getenv('CLOUDFLARE_ZONE_ID')
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
EMAIL_RECIPIENT = os.getenv('EMAIL_RECIPIENT')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

# Validate required environment variables
required_vars = [
    'TRELLO_API_KEY', 'TRELLO_API_TOKEN', 'TRELLO_BOARD_ID',
    'CLOUDFLARE_API_TOKEN', 'CLOUDFLARE_ZONE_ID',
    'EMAIL_USER', 'EMAIL_PASS', 'EMAIL_RECIPIENT',
    'WEBHOOK_URL'
]

missing_vars = [var for var in required_vars if not os.getenv(var)]
if missing_vars:
    raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")

# Initialize Cloudflare headers with secure token
CLOUDFLARE_HEADERS = {
    "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
    "Content-Type": "application/json",
}

# Initialize Trello client with secure credentials
trello_client = TrelloClient(api_key=TRELLO_API_KEY, api_secret=TRELLO_API_TOKEN)
board = trello_client.get_board(TRELLO_BOARD_ID)
task_list = board.open_lists()[0]  # Use the first open list

# Initialize Docker client
docker_client = docker.from_env()

def send_email_alert(subject, body):
    """Send email alerts with secure credentials"""
    try:
        yag = yagmail.SMTP(EMAIL_USER, EMAIL_PASS)
        yag.send(EMAIL_RECIPIENT, subject, body)
        logging.info(f"Email alert sent: {subject}")
    except Exception as e:
        logging.error(f"Failed to send email alert: {e}")

def send_webhook_notification(message):
    """Send webhook notifications with error handling"""
    try:
        payload = {"text": message}
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 200:
            logging.info("Webhook notification sent.")
        else:
            logging.error(f"Failed to send webhook notification: {response.text}")
    except Exception as e:
        logging.error(f"Error sending webhook notification: {e}")

def list_dns_records():
    """List DNS records with secure API calls"""
    logging.info("Listing DNS records...")
    url = f"https://api.cloudflare.com/client/v4/zones/{CLOUDFLARE_ZONE_ID}/dns_records"
    try:
        response = requests.get(url, headers=CLOUDFLARE_HEADERS)
        if response.status_code == 200 and response.json().get("success"):
            records = response.json()["result"]
            for record in records:
                logging.info(f"{record['type']} {record['name']} -> {record['content']} (ID: {record['id']})")
        else:
            logging.error(f"Failed to list DNS records: {response.text}")
    except Exception as e:
        logging.error(f"Error listing DNS records: {e}")
        send_email_alert("DNS Record Error", str(e))

def add_dns_record(record_type, name, content, ttl=3600):
    """Add DNS records with secure API calls and validation"""
    logging.info(f"Adding DNS record: {name} -> {content}")
    url = f"https://api.cloudflare.com/client/v4/zones/{CLOUDFLARE_ZONE_ID}/dns_records"

    try:
        data = {"type": record_type, "name": name, "content": content, "ttl": ttl}
        response = requests.post(url, headers=CLOUDFLARE_HEADERS, json=data)
        if response.status_code == 200 and response.json().get("success"):
            logging.info(f"DNS record added: {name} -> {content}")
            send_webhook_notification(f"DNS record added: {name} -> {content}")
        else:
            error_msg = f"Failed to add DNS record: {response.text}"
            logging.error(error_msg)
            send_email_alert("DNS Record Error", error_msg)
    except Exception as e:
        error_msg = f"Error adding DNS record: {str(e)}"
        logging.error(error_msg)
        send_email_alert("DNS Record Error", error_msg)

def monitor_docker_events():
    """Monitor Docker events with error handling"""
    logging.info("Starting Docker event monitor...")
    try:
        for event in docker_client.events(decode=True):
            try:
                status = event.get("status")
                container_id = event.get("id")
                container_name = event.get("Actor", {}).get("Attributes", {}).get("name")

                if status in ["start", "stop", "die"]:
                    task_name = f"Container {container_name} - {status}"
                    task_desc = f"Container ID: {container_id}\nStatus: {status}"
                    task_list.add_card(task_name, task_desc)
                    logging.info(f"Created Trello card for container event: {task_name}")
                    send_webhook_notification(f"Docker event: {task_name}")
            except Exception as e:
                logging.error(f"Error processing Docker event: {e}")
    except Exception as e:
        error_msg = f"Docker event monitor error: {str(e)}"
        logging.error(error_msg)
        send_email_alert("Docker Monitor Error", error_msg)

def scheduled_dns_check():
    """Scheduled DNS check with error handling"""
    logging.info("Running scheduled DNS check...")
    try:
        list_dns_records()
    except Exception as e:
        error_msg = f"Scheduled DNS check error: {str(e)}"
        logging.error(error_msg)
        send_email_alert("DNS Check Error", error_msg)

def main():
    """Main function with comprehensive error handling"""
    logging.info("Starting automation...")

    try:
        # Verify environment variables are loaded
        if not all([TRELLO_API_KEY, TRELLO_API_TOKEN, CLOUDFLARE_API_TOKEN]):
            raise EnvironmentError("Missing critical environment variables")

        # Step 1: Build and start Docker containers
        logging.info("Building and starting Docker containers...")
        subprocess.run(["docker-compose", "build"], check=True)
        subprocess.run(["docker-compose", "up", "-d"], check=True)

        # Step 2: Add DNS records to Cloudflare
        logging.info("Configuring Cloudflare DNS...")
        add_dns_record("A", "example.yourdomain.com", "192.0.2.1")

        # Step 3: Set up scheduled tasks
        logging.info("Setting up scheduled tasks...")
        schedule.every(10).minutes.do(scheduled_dns_check)

        # Step 4: Monitor Docker events and update Trello
        logging.info("Monitoring Docker events...")
        try:
            while True:
                schedule.run_pending()  # Run scheduled tasks
                monitor_docker_events()
        except KeyboardInterrupt:
            logging.info("Automation stopped by user.")
        except Exception as e:
            error_msg = f"Error in main event loop: {str(e)}"
            logging.error(error_msg)
            send_email_alert("Critical Error", error_msg)
            raise

    except Exception as e:
        error_msg = f"Critical error in main function: {str(e)}"
        logging.error(error_msg)
        send_email_alert("Critical Error", error_msg)
        raise

if __name__ == "__main__":
    main()