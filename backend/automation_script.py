
import os
import subprocess
import psutil
import requests
from datetime import datetime

def update_dependencies():
    try:
        print("Updating dependencies...")
        subprocess.run(["npm", "install"], check=True)
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        print("Dependencies updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error updating dependencies: {e}")

def run_tests():
    try:
        print("Running tests...")
        subprocess.run(["npm", "test"], check=True)
        subprocess.run(["pytest", "--cov=."], check=True)
        print("All tests passed.")
    except subprocess.CalledProcessError as e:
        print(f"Error during testing: {e}")

def check_system_health():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    
    print(f"\nSystem Health Check:")
    print(f"CPU Usage: {cpu_percent}%")
    print(f"Memory Usage: {memory_percent}%")
    print(f"Disk Usage: {disk_usage}%")
    
    # Alert if resources are running high
    if any([cpu_percent > 80, memory_percent > 80, disk_usage > 80]):
        print("WARNING: System resources running high!")

def run_security_scan():
    try:
        print("Running security scan...")
        subprocess.run(["npm", "audit"], check=True)
        print("Security scan completed.")
    except subprocess.CalledProcessError as e:
        print(f"Security scan found issues: {e}")

if __name__ == "__main__":
    print(f"Starting automation script at {datetime.now()}")
    update_dependencies()
    run_tests()
    check_system_health()
    run_security_scan()
    print(f"Automation completed at {datetime.now()}")
