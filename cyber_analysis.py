import numpy as np
from scipy import signal
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from sklearn.ensemble import IsolationForest
import pywt
import logging
from src.utils.security_validator import SecurityValidator

@dataclass
class CyberThreatIndicator:
    threat_type: str
    confidence: float
    timestamp: float
    characteristics: Dict[str, float]
    recommendation: str

class CyberWarfareAnalyzer:
    """Advanced signal analysis for cyber warfare detection and countermeasures"""

    def __init__(self, sampling_rate: float = 1000.0):
        self.sampling_rate = sampling_rate
        self.security_validator = SecurityValidator()
        self.attack_patterns = {
            'frequency_hopping': self._detect_frequency_hopping,
            'signal_injection': self._detect_signal_injection,
            'jamming': self._detect_jamming,
            'replay_attack': self._detect_replay_attack
        }
        logging.info("CyberWarfareAnalyzer initialized with sampling rate: %f", sampling_rate)

    def analyze_threats(self, signal_data: np.ndarray, 
                       time: np.ndarray) -> List[CyberThreatIndicator]:
        """
        Perform comprehensive cyber threat analysis with security validation
        """
        try:
            # Validate input signal data
            is_valid, error_msg = self.security_validator.validate_signal(signal_data, time)
            if not is_valid:
                logging.error("Signal validation failed: %s", error_msg)
                return []

            threats = []
            # Analyze each potential attack pattern
            for attack_type, detector in self.attack_patterns.items():
                try:
                    detected_threats = detector(signal_data, time)
                    threats.extend(detected_threats)
                except Exception as e:
                    logging.error("Error in %s detection: %s", attack_type, str(e))
                    continue

            return sorted(threats, key=lambda x: x.confidence, reverse=True)

        except Exception as e:
            logging.error("Critical error in threat analysis: %s", str(e))
            return []

    def _detect_frequency_hopping(self, data: np.ndarray, time: np.ndarray) -> List[CyberThreatIndicator]:
        """Detect frequency hopping patterns indicating potential communication hijacking"""
        threats = []
        window_size = min(256, len(data))

        try:
            # Compute spectrogram with overlapping windows for better detection
            f, t, Sxx = signal.spectrogram(data, fs=self.sampling_rate, 
                                         nperseg=window_size,
                                         noverlap=window_size//2)

            # Get the dominant frequencies at each time point
            peak_freqs = []
            for i in range(Sxx.shape[1]):
                # Get top 3 frequencies to improve detection
                top_indices = np.argsort(Sxx[:, i])[-3:]
                peak_freqs.append(np.mean(f[top_indices]))

            peak_freqs = np.array(peak_freqs)
            freq_changes = np.abs(np.diff(peak_freqs))

            # Calculate baseline variation using a more sensitive approach
            baseline_var = np.percentile(freq_changes, 75)
            threshold = max(baseline_var * 0.5, 0.05)  # More sensitive threshold
            rapid_changes = np.where(freq_changes > threshold)[0]

            if len(rapid_changes) > 0:
                for i in range(len(rapid_changes)):
                    change_magnitude = freq_changes[rapid_changes[i]]
                    confidence = min(0.95, change_magnitude / baseline_var)

                    metadata = {
                        'frequency_change': float(freq_changes[rapid_changes[i]]),
                        'duration': float(window_size / self.sampling_rate)
                    }
                    # Sanitize metadata before creating threat indicator
                    safe_metadata = self.security_validator.sanitize_metadata(metadata)

                    threats.append(CyberThreatIndicator(
                        threat_type="Frequency Hopping",
                        confidence=confidence,
                        timestamp=float(t[rapid_changes[i]]),
                        characteristics=safe_metadata,
                        recommendation="Monitor frequency spectrum for unauthorized transmissions"
                    ))

        except Exception as e:
            logging.error("Error in frequency hopping detection: %s", str(e))

        return threats

    def _detect_signal_injection(self, data: np.ndarray, 
                               time: np.ndarray) -> List[CyberThreatIndicator]:
        """Detect potential signal injection attacks"""
        threats = []
        try:
            # Decompose signal using wavelets
            coeffs = pywt.wavedec(data, 'db4', level=3)

            # Analyze detail coefficients for sudden changes
            for level, detail in enumerate(coeffs[1:], 1):
                threshold = np.std(detail) * 3
                anomalies = np.where(np.abs(detail) > threshold)[0]

                if len(anomalies) > 0:
                    metadata = {
                        'wavelet_level': float(level),
                        'magnitude': float(np.max(np.abs(detail[anomalies])))
                    }
                    safe_metadata = self.security_validator.sanitize_metadata(metadata)

                    threats.append(CyberThreatIndicator(
                        threat_type="Signal Injection",
                        confidence=min(0.85, len(anomalies) / len(detail)),
                        timestamp=time[anomalies[0]],
                        characteristics=safe_metadata,
                        recommendation="Implement signal authentication mechanisms"
                    ))

        except Exception as e:
            logging.error("Error in signal injection detection: %s", str(e))

        return threats

    def _detect_jamming(self, data: np.ndarray, 
                       time: np.ndarray) -> List[CyberThreatIndicator]:
        """Detect potential jamming attacks"""
        threats = []
        try:
            # Compute signal power in windows
            window_size = min(1000, len(data))
            n_windows = len(data) // window_size
            powers = np.array([np.mean(data[i*window_size:(i+1)*window_size]**2) 
                             for i in range(n_windows)])

            # Detect sustained high power levels
            threshold = np.mean(powers) + 2 * np.std(powers)
            jamming_windows = np.where(powers > threshold)[0]

            if len(jamming_windows) > 0:
                metadata = {
                    'power_level': float(np.mean(powers[jamming_windows])),
                    'duration': float(len(jamming_windows) * window_size / self.sampling_rate)
                }
                safe_metadata = self.security_validator.sanitize_metadata(metadata)

                threats.append(CyberThreatIndicator(
                    threat_type="Signal Jamming",
                    confidence=min(0.95, len(jamming_windows) / n_windows),
                    timestamp=time[jamming_windows[0] * window_size],
                    characteristics=safe_metadata,
                    recommendation="Implement frequency hopping or spread spectrum techniques"
                ))

        except Exception as e:
            logging.error("Error in jamming detection: %s", str(e))

        return threats

    def _detect_replay_attack(self, data: np.ndarray, 
                            time: np.ndarray) -> List[CyberThreatIndicator]:
        """Detect potential replay attacks through pattern matching"""
        threats = []
        try:
            window_size = min(500, len(data) // 4)

            # Look for repeated patterns
            for i in range(0, len(data) - 2*window_size):
                pattern = data[i:i+window_size]
                search_space = data[i+window_size:i+2*window_size]

                correlation = np.correlate(pattern, search_space, mode='valid')
                max_corr = np.max(np.abs(correlation))

                if max_corr > 0.95 * np.sum(pattern**2):
                    metadata = {
                        'pattern_length': float(window_size / self.sampling_rate),
                        'correlation': float(max_corr)
                    }
                    safe_metadata = self.security_validator.sanitize_metadata(metadata)

                    threats.append(CyberThreatIndicator(
                        threat_type="Replay Attack",
                        confidence=min(0.8, float(max_corr / np.sum(pattern**2))),
                        timestamp=time[i],
                        characteristics=safe_metadata,
                        recommendation="Implement temporal signature verification"
                    ))

        except Exception as e:
            logging.error("Error in replay attack detection: %s", str(e))

        return threats

    def generate_countermeasures(self, threats: List[CyberThreatIndicator]) -> Dict[str, List[str]]:
        """Generate countermeasures for detected threats"""
        try:
            countermeasures = {}

            for threat in threats:
                if threat.threat_type not in countermeasures:
                    countermeasures[threat.threat_type] = []

                if threat.threat_type == "Frequency Hopping":
                    countermeasures[threat.threat_type].extend([
                        "Implement frequency agility with secured hopping patterns",
                        "Monitor unauthorized spectrum usage",
                        "Deploy spread spectrum techniques"
                    ])
                elif threat.threat_type == "Signal Injection":
                    countermeasures[threat.threat_type].extend([
                        "Implement signal authentication protocols",
                        "Deploy temporal watermarking",
                        "Monitor signal integrity metrics"
                    ])
                elif threat.threat_type == "Signal Jamming":
                    countermeasures[threat.threat_type].extend([
                        "Activate frequency hopping protocols",
                        "Implement adaptive power control",
                        "Deploy spatial filtering techniques"
                    ])
                elif threat.threat_type == "Replay Attack":
                    countermeasures[threat.threat_type].extend([
                        "Implement temporal signatures",
                        "Deploy challenge-response protocols",
                        "Monitor signal timing patterns"
                    ])

            return countermeasures

        except Exception as e:
            logging.error("Error generating countermeasures: %s", str(e))
            return {}