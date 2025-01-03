
import React, { useState, useEffect } from 'react';

const RealTimeMonitor = () => {
  const [metrics, setMetrics] = useState({
    temperature: 0,
    pressure: 0,
    humidity: 0
  });

  useEffect(() => {
    const updateMetrics = setInterval(() => {
      fetch('/api/biostasis/metrics')
        .then(res => res.json())
        .then(data => setMetrics(data));
    }, 5000);
    return () => clearInterval(updateMetrics);
  }, []);

  return (
    <div className="monitor-container">
      <h2>Real-Time Monitoring</h2>
      <div className="metrics-grid">
        <div className="metric-card">
          <h3>Temperature</h3>
          <p>{metrics.temperature}°C</p>
        </div>
        <div className="metric-card">
          <h3>Pressure</h3>
          <p>{metrics.pressure} kPa</p>
        </div>
        <div className="metric-card">
          <h3>Humidity</h3>
          <p>{metrics.humidity}%</p>
        </div>
      </div>
    </div>
  );
};

export default RealTimeMonitor;
