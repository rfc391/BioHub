
# 📴 BioHub Airgap Setup

BioHub can be fully deployed in environments with no internet access.

## Steps:

1. Pre-download packages:
   ```
   pip download -r biohub_core/requirements.txt -d offline-packages
   ```

2. Install using local cache:
   ```
   pip install --no-index --find-links=offline-packages -r biohub_core/requirements.txt
   ```

3. Run in `.airgap` mode to block all external connections.

## Additional Notes:
- All model files, binaries, and assets are bundled.
- Logging is local only and persistent in /logs.
