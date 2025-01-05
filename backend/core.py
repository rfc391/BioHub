
"""Core functionality for Fluctuation-Enhanced Sensing (FES)."""

import logging
from typing import Dict, Optional
import requests

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_message(message: str, level: str = 'info') -> None:
    """Log a message at the specified level.
    
    Args:
        message: The message to log
        level: Logging level (debug, info, warning, error, critical)
    """
    log_levels = {
        'debug': logging.debug,
        'info': logging.info,
        'warning': logging.warning,
        'error': logging.error,
        'critical': logging.critical
    }
    log_func = log_levels.get(level, logging.info)
    log_func(message)

class FESCore:
    """Core functionality for FES operations."""

    def __init__(self) -> None:
        """Initialize FESCore."""
        self.api_data: Dict = {}

    def fetch_rods_data(self, api_url: str, params: Optional[Dict] = None) -> Dict:
        """Fetch RODS-compatible data from APIs.
        
        Args:
            api_url: The API endpoint URL
            params: Optional query parameters
            
        Returns:
            Dict containing the API response data
            
        Raises:
            Exception: If the API request fails
        """
        try:
            response = requests.get(api_url, params=params or {})
            response.raise_for_status()
            self.api_data = response.json()
            return self.api_data
        except requests.exceptions.RequestException as error:
            raise Exception(f"Error fetching RODS data: {str(error)}")

    def alert_biothreat(self, threat_level: int, location: str) -> None:
        """Alert authorities about a biothreat.
        
        Args:
            threat_level: Integer indicating threat severity (0-10)
            location: String describing the threat location
            
        Raises:
            ValueError: If threat_level is not an integer
        """
        if not isinstance(threat_level, int):
            raise ValueError("Threat level must be an integer")
            
        message = (f"CRITICAL: High biothreat at {location}!" if threat_level > 7 
                  else f"WARNING: Biothreat at {location}")
        level = 'critical' if threat_level > 7 else 'warning'
        log_message(message, level)
