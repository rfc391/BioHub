import streamlit as st
import numpy as np
import pandas as pd
from utils.signal_processing import (preprocess_signal, compute_psd,
                                  compute_fluctuation_analysis, compute_hurst_exponent,
                                  compute_correlation_matrix)
from utils.visualization import (create_signal_plot, create_psd_plot, create_dfa_plot,
                              create_correlation_heatmap)
from utils.anomaly_detection import detect_anomalies, get_anomaly_segments
from utils.preprocessing import SignalPreprocessor
from utils.cyber_analysis import CyberWarfareAnalyzer # Added import
from utils.cyber_visualization import create_cyber_threat_plot, create_threat_confidence_plot # Added imports


def perform_analysis(time: np.ndarray, signal_data: np.ndarray, params: dict):
    """
    Perform signal analysis and display results.
    
    Args:
        time: Time array for the signal
        signal_data: Signal amplitude data
        params: Dictionary of analysis parameters
        
    Raises:
        ValueError: If input arrays have invalid dimensions
        RuntimeError: If analysis computations fail
    """
    # Validate inputs
    if len(time) != len(signal_data):
        raise ValueError("Time and signal arrays must have same length")
    if len(time) == 0:
        raise ValueError("Input arrays cannot be empty")
    try:
        # Initialize preprocessing
        preprocessor = SignalPreprocessor()
        processed_signal = signal_data.copy()

        # Apply preprocessing if enabled
        if params.get("enable_preprocessing", False):
            if params["filter_type"] == "Auto (Recommended)":
                try:
                    # Get filter recommendations
                    recommendations = preprocessor.analyze_signal(signal_data, params["sampling_rate"])
                    if recommendations:
                        st.info(f"Recommended filter: {recommendations[0].filter_type} - {recommendations[0].reason}")
                        processed_signal = preprocessor.apply_filter(
                            signal_data,
                            recommendations[0].filter_type,
                            recommendations[0].parameters,
                            params["sampling_rate"]
                        )

                        # Display all recommendations
                        st.expander("All Filter Recommendations").write(
                            "\n".join([f"- {r.filter_type}: {r.reason} (score: {r.score:.2f})"
                                    for r in recommendations])
                        )
                except Exception as e:
                    st.error(f"Error in signal preprocessing: {str(e)}")
                    processed_signal = signal_data.copy()
            else:
                # Apply user-selected filter
                try:
                    processed_signal = preprocessor.apply_filter(
                        signal_data,
                        params["filter_type"].lower(),
                        params["filter_params"],
                        params["sampling_rate"]
                    )
                except Exception as e:
                    st.error(f"Error applying filter: {str(e)}")
                    processed_signal = signal_data.copy()

        # Standard preprocessing with error handling
        try:
            processed_signal = preprocess_signal(processed_signal, params["sampling_rate"])
        except Exception as e:
            st.error(f"Error in standard preprocessing: {str(e)}")
            processed_signal = signal_data.copy()

        # Detect anomalies if enabled
        anomaly_mask = None
        anomaly_segments = None
        anomaly_scores = None

        if params.get("enable_anomaly_detection", False):
            try:
                anomaly_mask, anomaly_scores = detect_anomalies(
                    processed_signal,
                    contamination=params["contamination"]
                )
                if anomaly_mask is not None:
                    anomaly_segments = get_anomaly_segments(
                        anomaly_mask,
                        min_segment_length=params["min_segment_length"]
                    )
            except Exception as e:
                st.error(f"Error in anomaly detection: {str(e)}")

        # Add cyber warfare analysis
        st.subheader("Cyber Warfare Analysis")

        try:
            cyber_analyzer = CyberWarfareAnalyzer(sampling_rate=params["sampling_rate"])
            threats = cyber_analyzer.analyze_threats(processed_signal, time)

            if threats:
                st.plotly_chart(create_cyber_threat_plot(time, processed_signal, threats),
                            use_container_width=True)

                st.plotly_chart(create_threat_confidence_plot(threats),
                            use_container_width=True)

                # Display threat details and countermeasures
                countermeasures = cyber_analyzer.generate_countermeasures(threats)

                with st.expander("Detailed Threat Analysis"):
                    for threat in threats:
                        st.markdown(f"""
                        **{threat.threat_type}** (Confidence: {threat.confidence:.2f})
                        - Time: {threat.timestamp:.2f}s
                        - Characteristics: {', '.join(f'{k}: {v:.2f}' for k, v in threat.characteristics.items())}
                        - Recommendation: {threat.recommendation}
                        """)

                with st.expander("Countermeasures"):
                    for threat_type, measures in countermeasures.items():
                        st.markdown(f"**{threat_type}**")
                        for measure in measures:
                            st.markdown(f"- {measure}")
            else:
                st.info("No cyber threats detected in the current signal")
        except Exception as e:
            st.error(f"Error in cyber warfare analysis: {str(e)}")

        # Display original and processed signals
        st.subheader("Signal Visualization")
        try:
            col1, col2 = st.columns(2)

            with col1:
                st.plotly_chart(create_signal_plot(time, signal_data, 
                                                title="Original Signal"),
                            use_container_width=True)

            with col2:
                st.plotly_chart(create_signal_plot(time, processed_signal,
                                                anomaly_mask=anomaly_mask,
                                                anomaly_segments=anomaly_segments,
                                                title="Processed Signal with Anomalies"),
                            use_container_width=True)
        except Exception as e:
            st.error(f"Error in signal visualization: {str(e)}")

        # Compute and display correlation heatmap
        st.subheader("Signal Correlation Analysis")
        try:
            # Create signal segments for correlation analysis
            n_segments = 4
            segment_length = len(processed_signal) // n_segments
            signal_segments = [processed_signal[i*segment_length:(i+1)*segment_length] 
                            for i in range(n_segments)]

            correlation_matrix = compute_correlation_matrix(signal_segments)
            segment_labels = [f"Segment {i+1}" for i in range(n_segments)]

            st.plotly_chart(create_correlation_heatmap(correlation_matrix, segment_labels),
                        use_container_width=True)
        except Exception as e:
            st.error(f"Error in correlation analysis: {str(e)}")

        # Compute and display PSD
        st.subheader("Spectral Analysis")
        try:
            frequencies, psd = compute_psd(processed_signal, params["sampling_rate"])
            st.plotly_chart(create_psd_plot(frequencies, psd), use_container_width=True)
        except Exception as e:
            st.error(f"Error in spectral analysis: {str(e)}")

        # Perform DFA
        st.subheader("Fluctuation Analysis")
        try:
            window_sizes, fluctuations = compute_fluctuation_analysis(processed_signal)
            hurst_exponent = compute_hurst_exponent(window_sizes, fluctuations)

            st.plotly_chart(create_dfa_plot(window_sizes, fluctuations, hurst_exponent),
                        use_container_width=True)
        except Exception as e:
            st.error(f"Error in fluctuation analysis: {str(e)}")

        # Display numerical results
        st.subheader("Analysis Results")
        try:
            col1, col2, col3 = st.columns(3)

            with col1:
                if 'hurst_exponent' in locals():
                    st.metric("Hurst Exponent", f"{hurst_exponent:.3f}")
                else:
                    st.metric("Hurst Exponent", "N/A")

            with col2:
                st.metric("Signal Length", len(signal_data))

            with col3:
                if anomaly_segments:
                    n_anomalies = len(anomaly_segments)
                    st.metric("Anomaly Segments", n_anomalies)
                else:
                    st.metric("Anomaly Segments", 0)

            # Export results
            if st.button("Export Results"):
                results_dict = {
                    "Time": time,
                    "Original_Signal": signal_data,
                    "Processed_Signal": processed_signal,
                }

                if 'frequencies' in locals() and 'psd' in locals():
                    results_dict.update({
                        "Frequency": frequencies,
                        "PSD": psd
                    })

                if 'window_sizes' in locals() and 'fluctuations' in locals():
                    results_dict.update({
                        "Window_Sizes": window_sizes,
                        "Fluctuations": fluctuations
                    })

                if anomaly_mask is not None and anomaly_scores is not None:
                    results_dict.update({
                        "Anomaly_Mask": anomaly_mask,
                        "Anomaly_Scores": anomaly_scores
                    })

                results_df = pd.DataFrame(results_dict)

                st.download_button(
                    label="Download Results CSV",
                    data=results_df.to_csv(index=False),
                    file_name="fes_analysis_results.csv",
                    mime="text/csv"
                )
        except Exception as e:
            st.error(f"Error in displaying results: {str(e)}")

    except Exception as e:
        st.error(f"Critical error in analysis: {str(e)}")
        raise e