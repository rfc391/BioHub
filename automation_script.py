
import os
import subprocess

def update_dependencies():
    try:
        print("Updating dependencies...")
        result = subprocess.run(["pip", "install", "--upgrade", "-r", "requirements.txt"], capture_output=True, text=True)
        if result.returncode == 0:
            print("Dependencies updated successfully.")
        else:
            print("Error updating dependencies:", result.stderr)
    except Exception as e:
        print(f"Error during dependency update: {e}")

def run_tests():
    try:
        print("Running tests...")
        result = subprocess.run(["pytest", "--cov=."], capture_output=True, text=True)
        if result.returncode == 0:
            print("All tests passed.")
        else:
            print("Some tests failed:", result.stderr)
    except Exception as e:
        print(f"Error during testing: {e}")

if __name__ == "__main__":
    update_dependencies()
    run_tests()
