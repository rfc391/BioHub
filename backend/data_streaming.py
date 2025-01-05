import numpy as np
from typing import Generator, Optional
import time

class DataStreamSimulator:
    """
    Simulates real-time data streaming for FES analysis
    """
    def __init__(self, 
                sampling_rate: float = 1000.0,
                noise_level: float = 0.1,
                base_frequency: float = 1.0):
        self.sampling_rate = sampling_rate
        self.noise_level = noise_level
        self.base_frequency = base_frequency
        self.t = 0
        
    def generate_sample(self) -> float:
        """Generate a single data point"""
        signal = np.sin(2 * np.pi * self.base_frequency * self.t)
        noise = self.noise_level * np.random.randn()
        self.t += 1.0 / self.sampling_rate
        return signal + noise
        
    def stream(self, buffer_size: int = 100) -> Generator[np.ndarray, None, None]:
        """
        Generate streaming data points
        
        Parameters:
        -----------
        buffer_size : int
            Number of points to generate in each iteration
            
        Yields:
        -------
        np.ndarray
            Array of generated data points
        """
        while True:
            buffer = np.array([self.generate_sample() for _ in range(buffer_size)])
            yield buffer
            time.sleep(buffer_size / self.sampling_rate)  # Simulate real-time delay

class RealTimeAnalyzer:
    """
    Performs real-time analysis on streaming data
    """
    def __init__(self, window_size: int = 1000):
        self.window_size = window_size
        self.buffer = np.zeros(window_size)
        self.position = 0
        
    def update(self, new_data: np.ndarray) -> dict:
        """
        Update analysis with new data
        
        Parameters:
        -----------
        new_data : np.ndarray
            New data points to analyze
            
        Returns:
        --------
        dict
            Dictionary containing analysis results
        """
        # Update buffer with new data
        n_new = len(new_data)
        if self.position + n_new > self.window_size:
            # Buffer is full, shift data
            self.buffer = np.roll(self.buffer, -n_new)
            self.buffer[-n_new:] = new_data
            self.position = self.window_size
        else:
            # Buffer still has space
            self.buffer[self.position:self.position + n_new] = new_data
            self.position += n_new
            
        # Compute real-time metrics
        if self.position >= 100:  # Minimum data points for analysis
            active_data = self.buffer[:self.position]
            return {
                'mean': np.mean(active_data),
                'std': np.std(active_data),
                'min': np.min(active_data),
                'max': np.max(active_data),
                'rms': np.sqrt(np.mean(active_data**2))
            }
        return {}
import numpy as np
from typing import Generator, Tuple

class SignalGenerator:
    def __init__(self, sampling_rate: float = 1000.0, noise_level: float = 0.1):
        self.sampling_rate = sampling_rate
        self.noise_level = noise_level
        self.t = 0
        
    def generate_sample(self) -> Tuple[float, float]:
        """Generate a single sample of synthetic signal"""
        signal = (np.sin(2 * np.pi * 1.0 * self.t) + 
                 0.5 * np.sin(2 * np.pi * 2.5 * self.t) +
                 self.noise_level * np.random.randn())
        
        current_time = self.t
        self.t += 1.0/self.sampling_rate
        
        return current_time, signal
        
    def reset(self):
        """Reset the generator"""
        self.t = 0
