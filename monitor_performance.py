
import psutil
import time
import json
import os
from datetime import datetime

def collect_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
        "timestamp": datetime.now().isoformat()
    }

def monitor_performance(interval=300):  # 5 minutes
    metrics_file = "performance_metrics.json"
    
    while True:
        metrics = collect_metrics()
        
        # Load existing metrics
        if os.path.exists(metrics_file):
            with open(metrics_file, 'r') as f:
                all_metrics = json.load(f)
        else:
            all_metrics = []
            
        # Add new metrics
        all_metrics.append(metrics)
        
        # Keep only last 24 hours of data
        all_metrics = all_metrics[-288:]  # 288 = 24 hours of 5-minute intervals
        
        # Save metrics
        with open(metrics_file, 'w') as f:
            json.dump(all_metrics, f)
            
        time.sleep(interval)

if __name__ == "__main__":
    monitor_performance()
