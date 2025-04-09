#!/bin/bash
set -e

echo "[+] BioHub Universal Installer"
echo "-----------------------------------"

# Ensure system is updated
echo "[*] Updating system..."
sudo apt update && sudo apt upgrade -y

# Check Python3 and Pip
echo "[*] Checking Python and pip..."
sudo apt install -y python3 python3-pip python3-venv

# Create and activate virtual environment
echo "[*] Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "[*] Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install essential tools
echo "[*] Installing additional system tools..."
sudo apt install -y curl git jq

# Set permissions
chmod +x ./ai_automation.sh || true

# Final message
echo "[✓] BioHub installed successfully."
echo "Run with: source venv/bin/activate && python3 main.py"

# Secure server hardening additions
echo "Configuring firewall..."
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp
ufw allow from ::1 to any port 5000 proto tcp
ufw enable
