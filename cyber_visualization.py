import plotly.graph_objects as go
import plotly.colors as pc
import numpy as np
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class CyberThreatIndicator:
    timestamp: float
    threat_type: str
    confidence: float

def get_risk_color(confidence: float) -> str:
    """Generate color based on threat confidence/risk level"""
    if not isinstance(confidence, (int, float)):
        raise TypeError("Confidence must be a number")
    if not 0 <= confidence <= 1:
        raise ValueError("Confidence must be between 0 and 1")

    # Create a continuous color scale from green to red
    r = int(confidence * 255)
    g = int((1 - confidence) * 255)
    b = 0
    return f'rgb({r},{g},{b})'

def create_cyber_threat_plot(time: np.ndarray, signal_data: np.ndarray, 
                           threats: List[CyberThreatIndicator],
                           highlight_threats: Optional[List[int]] = None,
                           title: str = "Interactive Cyber Threat Analysis") -> go.Figure:
    """Create an interactive plot highlighting detected cyber threats"""
    # Input validation
    if not isinstance(time, np.ndarray) or not isinstance(signal_data, np.ndarray):
        raise TypeError("time and signal_data must be numpy arrays")
    if not isinstance(threats, list):
        raise TypeError("threats must be a list of CyberThreatIndicator")
    if len(time) != len(signal_data):
        raise ValueError("time and signal_data must have the same length")

    try:
        fig = go.Figure()

        # Plot main signal
        fig.add_trace(go.Scatter(
            x=time,
            y=signal_data,
            mode='lines',
            name='Signal',
            line=dict(color='#1f77b4', width=1)
        ))

        # Add threat markers
        if threats:
            for i, threat in enumerate(threats):
                if not isinstance(threat, CyberThreatIndicator):
                    raise TypeError(f"Invalid threat type at index {i}")

                if 0 <= threat.timestamp <= time[-1]:
                    time_idx = int(threat.timestamp * len(signal_data) / time[-1])
                    time_idx = min(time_idx, len(signal_data) - 1)
                    color = get_risk_color(threat.confidence)

                    fig.add_trace(go.Scatter(
                        x=[threat.timestamp],
                        y=[signal_data[time_idx]],
                        mode='markers',
                        name=f'Threat {i+1}',
                        marker=dict(
                            size=10,
                            color=color
                        )
                    ))

        fig.update_layout(
            title=title,
            xaxis_title="Time",
            yaxis_title="Amplitude",
            template="plotly_dark",
            showlegend=True
        )

        return fig
    except Exception as e:
        print(f"Error in create_cyber_threat_plot: {str(e)}")
        raise

def create_threat_confidence_plot(threats: List[CyberThreatIndicator]) -> go.Figure:
    """Create a bar plot of threat confidence levels"""
    if not isinstance(threats, list):
        raise TypeError("threats must be a list of CyberThreatIndicator")

    try:
        threat_types = []
        confidence_levels = []

        for i, threat in enumerate(threats):
            if not isinstance(threat, CyberThreatIndicator):
                raise TypeError(f"Invalid threat type at index {i}")
            threat_types.append(threat.threat_type)
            confidence_levels.append(threat.confidence)

        colors = [get_risk_color(conf) for conf in confidence_levels]

        fig = go.Figure(data=[
            go.Bar(
                x=threat_types,
                y=confidence_levels,
                marker_color=colors
            )
        ])

        fig.update_layout(
            title="Threat Confidence Levels",
            xaxis_title="Threat Type",
            yaxis_title="Confidence",
            template="plotly_dark",
            showlegend=False
        )

        return fig
    except Exception as e:
        print(f"Error in create_threat_confidence_plot: {str(e)}")
        raise