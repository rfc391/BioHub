
import subprocess
import sys
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_tests():
    """Run all tests using pytest with detailed logging"""
    try:
        logger.info("Starting test suite execution...")
        
        # Run unit tests
        logger.info("Running unit tests...")
        subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"], check=True)
        
        # Run performance tests
        logger.info("Running performance tests...")
        subprocess.run([sys.executable, "-m", "pytest", "tests/test_performance.py", "-v"], check=True)
        
        # Run integration tests
        logger.info("Running integration tests...")
        subprocess.run([sys.executable, "-m", "pytest", "tests/test_integration.py", "-v"], check=True)
        
        logger.info("All tests completed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Tests failed with error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)

def run_linting():
    """Run code quality checks"""
    try:
        logger.info("Running code quality checks...")
        subprocess.run(["flake8", "src/", "tests/"], check=True)
        subprocess.run(["black", "src/", "tests/", "--check"], check=True)
        logger.info("Code quality checks passed.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Code quality checks failed: {e}")
        sys.exit(1)

def main():
    logger.info("Starting automation workflow...")
    run_linting()
    run_tests()
    logger.info("Automation completed successfully.")

if __name__ == "__main__":
    main()
