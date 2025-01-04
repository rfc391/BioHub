import zipfile
import os
import shutil
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_and_integrate():
    """
    Extract FES-main.zip and integrate its contents into the project
    """
    zip_path = os.path.join("attached_assets", "Archive.zip")
    extract_path = os.path.join("attached_assets", "temp")

    try:
        # Ensure zip file exists
        if not os.path.exists(zip_path):
            raise FileNotFoundError(f"ZIP file not found at {zip_path}")

        # Create temp directory if it doesn't exist
        os.makedirs(extract_path, exist_ok=True)
        logger.info(f"Created temporary directory at {extract_path}")

        # Extract zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
            logger.info("Successfully extracted ZIP contents")

        # Get the root directory of extracted contents
        extracted_root = os.path.join(extract_path, "FES-main")
        if not os.path.exists(extracted_root):
            raise FileNotFoundError(f"Expected directory not found at {extracted_root}")

        # Copy relevant files to their destinations
        files_copied = 0
        for root, dirs, files in os.walk(extracted_root):
            for file in files:
                src_path = os.path.join(root, file)
                # Get relative path from extracted root
                rel_path = os.path.relpath(src_path, extracted_root)
                # Create destination path
                dest_path = os.path.join(os.getcwd(), rel_path)

                # Create destination directory if it doesn't exist
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                # Copy file if it's not already in our codebase
                if not os.path.exists(dest_path):
                    shutil.copy2(src_path, dest_path)
                    files_copied += 1
                    logger.info(f"Copied: {rel_path}")

        logger.info(f"Successfully integrated {files_copied} files")

    except Exception as e:
        logger.error(f"Error during extraction: {str(e)}")
        raise
    finally:
        # Clean up temp directory
        if os.path.exists(extract_path):
            shutil.rmtree(extract_path)
            logger.info("Cleaned up temporary directory")

if __name__ == "__main__":
    try:
        extract_and_integrate()
        logger.info("Integration completed successfully")
    except Exception as e:
        logger.error(f"Integration failed: {str(e)}")
        exit(1)
