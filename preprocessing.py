import numpy as np
from scipy import signal
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler
import pywt

@dataclass
class FilterRecommendation:
    filter_type: str
    parameters: Dict
    reason: str
    score: float

class SignalPreprocessor:
    """Advanced signal preprocessing toolkit with intelligent filter recommendations"""
    
    def __init__(self):
        self.available_filters = {
            'butterworth': self._butterworth_filter,
            'savgol': self._savgol_filter,
            'wavelet': self._wavelet_denoise,
            'median': self._median_filter
        }
    
    def analyze_signal(self, data: np.ndarray, sampling_rate: float) -> List[FilterRecommendation]:
        """
        Analyze signal characteristics and recommend appropriate filters
        """
        recommendations = []
        
        # Compute signal characteristics
        noise_level = self._estimate_noise_level(data)
        frequency_content = self._analyze_frequency_content(data, sampling_rate)
        spikes = self._detect_spikes(data)
        
        # Recommend filters based on signal characteristics
        if noise_level > 0.2:  # High noise level
            recommendations.append(FilterRecommendation(
                filter_type='wavelet',
                parameters={'wavelet': 'db4', 'level': 3},
                reason='High noise level detected',
                score=0.9
            ))
            
        if frequency_content['high_freq_ratio'] > 0.3:
            recommendations.append(FilterRecommendation(
                filter_type='butterworth',
                parameters={'order': 4, 'cutoff': 0.1},
                reason='Significant high-frequency content',
                score=0.8
            ))
            
        if spikes['count'] > 0:
            recommendations.append(FilterRecommendation(
                filter_type='median',
                parameters={'kernel_size': 5},
                reason='Spike artifacts detected',
                score=0.7
            ))
        
        return sorted(recommendations, key=lambda x: x.score, reverse=True)
    
    def apply_filter(self, data: np.ndarray, filter_type: str, 
                    parameters: Dict, sampling_rate: Optional[float] = None) -> np.ndarray:
        """Apply selected filter to the signal"""
        if filter_type not in self.available_filters:
            raise ValueError(f"Unknown filter type: {filter_type}")
            
        filter_func = self.available_filters[filter_type]
        return filter_func(data, sampling_rate, **parameters)
    
    def _estimate_noise_level(self, data: np.ndarray) -> float:
        """Estimate noise level using wavelet decomposition"""
        coeffs = pywt.wavedec(data, 'db1', level=1)
        detail = coeffs[-1]
        return np.std(detail) / np.std(data)
    
    def _analyze_frequency_content(self, data: np.ndarray, 
                                 sampling_rate: float) -> Dict:
        """Analyze frequency content of the signal"""
        freqs, psd = signal.welch(data, fs=sampling_rate)
        total_power = np.sum(psd)
        high_freq_power = np.sum(psd[freqs > sampling_rate/4])
        
        return {
            'high_freq_ratio': high_freq_power / total_power,
            'dominant_freq': freqs[np.argmax(psd)]
        }
    
    def _detect_spikes(self, data: np.ndarray) -> Dict:
        """Detect spike artifacts in the signal"""
        threshold = np.std(data) * 3
        spikes = np.where(np.abs(data) > threshold)[0]
        
        return {
            'count': len(spikes),
            'locations': spikes
        }
    
    def _butterworth_filter(self, data: np.ndarray, sampling_rate: float,
                          order: int, cutoff: float) -> np.ndarray:
        """Apply Butterworth low-pass filter"""
        nyquist = sampling_rate / 2
        b, a = signal.butter(order, cutoff, btype='low', fs=sampling_rate)
        return signal.filtfilt(b, a, data)
    
    def _savgol_filter(self, data: np.ndarray, sampling_rate: Optional[float],
                      window_length: int, polyorder: int) -> np.ndarray:
        """Apply Savitzky-Golay filter"""
        return signal.savgol_filter(data, window_length, polyorder)
    
    def _wavelet_denoise(self, data: np.ndarray, sampling_rate: Optional[float],
                        wavelet: str, level: int) -> np.ndarray:
        """Apply wavelet denoising"""
        coeffs = pywt.wavedec(data, wavelet, level=level)
        threshold = np.std(coeffs[-1]) * np.sqrt(2*np.log(len(data)))
        
        coeffs[1:] = [pywt.threshold(c, threshold, mode='soft') for c in coeffs[1:]]
        return pywt.waverec(coeffs, wavelet)
    
    def _median_filter(self, data: np.ndarray, sampling_rate: Optional[float],
                      kernel_size: int) -> np.ndarray:
        """Apply median filter"""
        return signal.medfilt(data, kernel_size)
import numpy as np
from scipy import signal
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class FilterRecommendation:
    filter_type: str
    parameters: Dict
    reason: str
    score: float

class SignalPreprocessor:
    def __init__(self):
        self.available_filters = {
            'lowpass': self._lowpass_filter,
            'highpass': self._highpass_filter,
            'bandpass': self._bandpass_filter,
            'notch': self._notch_filter
        }

    def analyze_signal(self, data: np.ndarray, sampling_rate: float) -> List[FilterRecommendation]:
        recommendations = []
        
        # Analyze frequency content
        freqs, psd = signal.welch(data, fs=sampling_rate)
        peak_freq = freqs[np.argmax(psd)]
        noise_floor = np.median(psd)
        
        # Check for high-frequency noise
        if np.mean(psd[len(psd)//2:]) > noise_floor * 2:
            recommendations.append(FilterRecommendation(
                filter_type='lowpass',
                parameters={'cutoff': sampling_rate/4},
                reason='High frequency noise detected',
                score=0.8
            ))
            
        # Check for low-frequency drift
        if np.mean(psd[:len(psd)//10]) > noise_floor * 3:
            recommendations.append(FilterRecommendation(
                filter_type='highpass',
                parameters={'cutoff': 1.0},
                reason='Low frequency drift detected',
                score=0.7
            ))
            
        return sorted(recommendations, key=lambda x: x.score, reverse=True)

    def apply_filter(self, data: np.ndarray, filter_type: str, 
                    parameters: Dict, sampling_rate: float) -> np.ndarray:
        if filter_type not in self.available_filters:
            raise ValueError(f"Unknown filter type: {filter_type}")
            
        return self.available_filters[filter_type](data, parameters, sampling_rate)

    def _lowpass_filter(self, data: np.ndarray, parameters: Dict, 
                       sampling_rate: float) -> np.ndarray:
        nyquist = sampling_rate / 2
        cutoff = parameters.get('cutoff', nyquist/4)
        b, a = signal.butter(4, cutoff/nyquist, btype='low')
        return signal.filtfilt(b, a, data)

    def _highpass_filter(self, data: np.ndarray, parameters: Dict, 
                        sampling_rate: float) -> np.ndarray:
        nyquist = sampling_rate / 2
        cutoff = parameters.get('cutoff', 1.0)
        b, a = signal.butter(4, cutoff/nyquist, btype='high')
        return signal.filtfilt(b, a, data)

    def _bandpass_filter(self, data: np.ndarray, parameters: Dict, 
                        sampling_rate: float) -> np.ndarray:
        nyquist = sampling_rate / 2
        low_cutoff = parameters.get('low_cutoff', 1.0)
        high_cutoff = parameters.get('high_cutoff', nyquist/4)
        b, a = signal.butter(4, [low_cutoff/nyquist, high_cutoff/nyquist], btype='band')
        return signal.filtfilt(b, a, data)

    def _notch_filter(self, data: np.ndarray, parameters: Dict, 
                     sampling_rate: float) -> np.ndarray:
        nyquist = sampling_rate / 2
        freq = parameters.get('freq', 50.0)  # Default to power line frequency
        Q = parameters.get('Q', 30.0)
        w0 = freq/(nyquist)
        b, a = signal.iirnotch(w0, Q)
        return signal.filtfilt(b, a, data)
