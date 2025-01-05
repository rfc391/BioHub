import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils.data_streaming import DataStreamSimulator, RealTimeAnalyzer
import time

def create_live_plot() -> tuple:
    """Create and return a Plotly figure and its container for live updates"""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[], y=[], mode='lines', name='Signal'))
    
    fig.update_layout(
        title="Live Signal",
        xaxis_title="Time",
        yaxis_title="Amplitude",
        template="plotly_dark",
        showlegend=True,
        hovermode='x unified'
    )
    
    return fig, st.empty()

def main():
    st.set_page_config(page_title="Live FES Analysis", layout="wide")
    st.title("Real-time FES Analysis Dashboard")
    
    # Sidebar controls
    st.sidebar.title("Stream Settings")
    sampling_rate = st.sidebar.slider("Sampling Rate (Hz)", 
                                    min_value=100, 
                                    max_value=1000, 
                                    value=500,
                                    step=100)
    
    noise_level = st.sidebar.slider("Noise Level", 
                                  min_value=0.0,
                                  max_value=1.0,
                                  value=0.1,
                                  step=0.1)
    
    window_size = st.sidebar.slider("Analysis Window Size",
                                  min_value=100,
                                  max_value=2000,
                                  value=1000,
                                  step=100)
    
    # Initialize components
    if 'stream_active' not in st.session_state:
        st.session_state.stream_active = False
        
    # Start/Stop button
    if st.sidebar.button('Start' if not st.session_state.stream_active else 'Stop'):
        st.session_state.stream_active = not st.session_state.stream_active
    
    # Create layout
    signal_col, metrics_col = st.columns([2, 1])
    
    with signal_col:
        fig, plot_container = create_live_plot()
        plot_placeholder = plot_container.empty()
    
    with metrics_col:
        metrics_container = st.container()
        
    # Initialize streaming components
    simulator = DataStreamSimulator(
        sampling_rate=sampling_rate,
        noise_level=noise_level
    )
    analyzer = RealTimeAnalyzer(window_size=window_size)
    
    # Main streaming loop
    if st.session_state.stream_active:
        buffer_size = 50  # Points per update
        x_data = []
        y_data = []
        
        try:
            for buffer in simulator.stream(buffer_size=buffer_size):
                if not st.session_state.stream_active:
                    break
                    
                # Update data
                new_x = np.linspace(len(x_data), len(x_data) + len(buffer), len(buffer)) / sampling_rate
                x_data.extend(new_x)
                y_data.extend(buffer)
                
                # Keep only the last window_size points
                if len(x_data) > window_size:
                    x_data = x_data[-window_size:]
                    y_data = y_data[-window_size:]
                
                # Update plot
                fig.data[0].x = x_data
                fig.data[0].y = y_data
                plot_placeholder.plotly_chart(fig, use_container_width=True)
                
                # Update metrics
                metrics = analyzer.update(buffer)
                if metrics:
                    with metrics_container:
                        cols = st.columns(len(metrics))
                        for col, (key, value) in zip(cols, metrics.items()):
                            col.metric(key.capitalize(), f"{value:.3f}")
                
                time.sleep(0.1)  # Prevent excessive updates
                
        except Exception as e:
            st.error(f"Streaming error: {str(e)}")
            st.session_state.stream_active = False

if __name__ == "__main__":
    main()
