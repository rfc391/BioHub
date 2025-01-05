
import pytest
import sys
import os

# Add the backend and src directories to the Python path dynamically
backend_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../backend")
src_path = os.path.join(backend_path, "src")
if backend_path not in sys.path:
    sys.path.append(backend_path)
if src_path not in sys.path:
    sys.path.append(src_path)

from cyber_analysis import analyze_data

def test_analyze_data():
    # Mock input data
    data = {"key": "value"}
    # Call the function and validate it doesn't raise exceptions
    try:
        analyze_data(data)
    except Exception as e:
        pytest.fail(f"analyze_data raised an exception: {e}")
