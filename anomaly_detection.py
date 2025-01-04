import numpy as np
from sklearn.ensemble import IsolationForest
from typing import Tuple, Optional

def detect_anomalies(signal_data: np.ndarray, 
                    contamination: float = 0.1,
                    random_state: int = 42) -> Tuple[np.ndarray, np.ndarray]:
    """
    Detect anomalies in the signal using Isolation Forest algorithm
    
    Parameters:
    -----------
    signal_data : np.ndarray
        Input signal data
    contamination : float
        Expected proportion of outliers in the data
    random_state : int
        Random state for reproducibility
        
    Returns:
    --------
    anomaly_mask : np.ndarray
        Boolean array indicating anomalies
    anomaly_scores : np.ndarray
        Anomaly scores for each point
    """
    # Reshape data for sklearn
    X = signal_data.reshape(-1, 1)
    
    # Initialize and fit the model
    iso_forest = IsolationForest(contamination=contamination,
                               random_state=random_state)
    
    # Predict returns 1 for inliers, -1 for outliers
    predictions = iso_forest.fit_predict(X)
    
    # Convert predictions to boolean mask (True for anomalies)
    anomaly_mask = predictions == -1
    
    # Get anomaly scores
    anomaly_scores = -iso_forest.score_samples(X)
    
    return anomaly_mask, anomaly_scores

def get_anomaly_segments(anomaly_mask: np.ndarray, 
                        min_segment_length: int = 3) -> list:
    """
    Group consecutive anomaly points into segments
    
    Parameters:
    -----------
    anomaly_mask : np.ndarray
        Boolean array indicating anomalies
    min_segment_length : int
        Minimum length of anomaly segments to consider
        
    Returns:
    --------
    segments : list
        List of tuples containing (start_idx, end_idx) for each anomaly segment
    """
    segments = []
    start_idx = None
    
    for i in range(len(anomaly_mask)):
        if anomaly_mask[i] and start_idx is None:
            start_idx = i
        elif not anomaly_mask[i] and start_idx is not None:
            if i - start_idx >= min_segment_length:
                segments.append((start_idx, i))
            start_idx = None
            
    # Handle case where anomaly extends to end of signal
    if start_idx is not None and len(anomaly_mask) - start_idx >= min_segment_length:
        segments.append((start_idx, len(anomaly_mask)))
        
    return segments
