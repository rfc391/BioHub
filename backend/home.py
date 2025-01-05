import streamlit as st

def main():
    st.set_page_config(
        page_title="FES Analysis Platform - Home",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("Welcome to FES Analysis Platform")
    
    st.markdown("""
    ## Getting Started Guide
    
    Welcome to the Fluctuation-Enhanced Sensing (FES) Analysis Platform. This guide will help you get started with analyzing your sensor data.
    
    ### Quick Start
    1. Navigate to the **Live Dashboard** using the sidebar
    2. Upload your signal data file (CSV or TXT format)
    3. Adjust analysis parameters as needed
    4. View results in real-time
    
    ### Understanding Your Data
    
    #### Data Requirements
    - **File Format**: CSV or TXT files
    - **Content**: Single column (signal values) or two columns (time and signal)
    - **Sampling Rate**: Must be consistent throughout the data
    
    #### Example Data Structure
    ```
    Time,Signal
    0.0,0.123
    0.001,0.456
    0.002,0.789
    ```
    
    ### Analysis Features
    
    #### 1. Signal Processing
    - **Preprocessing**: Clean and prepare your data
    - **Filtering**: Remove noise and unwanted components
    - **Spectral Analysis**: Understand frequency content
    
    #### 2. Anomaly Detection
    - Identify unusual patterns
    - Adjust sensitivity to your needs
    - Visual highlighting of anomalies
    
    #### 3. Advanced Analysis
    - Fluctuation analysis
    - Correlation studies
    - Statistical metrics
    
    ### Tips for Best Results
    
    1. **Data Quality**
       - Remove missing values
       - Check for outliers
       - Ensure consistent sampling
    
    2. **Parameter Selection**
       - Start with recommended settings
       - Adjust based on your specific needs
       - Use tooltips for guidance
    
    3. **Performance Optimization**
       - Use appropriate window sizes
       - Enable preprocessing when needed
       - Export results for large datasets
    
    ### Need Help?
    
    - Hover over parameters for detailed explanations
    - Check the documentation in the sidebar
    - Export results for further analysis
    
    Ready to start? Head to the **Live Dashboard** in the sidebar!
    """)
    
    # Add example data download
    st.sidebar.markdown("### Example Data")
    if st.sidebar.button("Download Example Dataset"):
        import numpy as np
        import pandas as pd
        
        # Generate example data
        t = np.linspace(0, 10, 1000)
        signal = np.sin(2*np.pi*1*t) + 0.5*np.sin(2*np.pi*2.5*t) + 0.25*np.random.randn(len(t))
        
        # Create DataFrame
        df = pd.DataFrame({
            'Time': t,
            'Signal': signal
        })
        
        # Convert to CSV
        csv = df.to_csv(index=False)
        st.sidebar.download_button(
            label="Download CSV",
            data=csv,
            file_name="example_signal.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()
