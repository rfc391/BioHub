
import tensorflow as tf
from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)
        
    def train(self, data):
        self.model.fit(data)
        
    def detect_anomalies(self, data):
        return self.model.predict(data)

def create_prediction_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model
class ModelManager:
    def __init__(self):
        self.models = {}
        self.current_version = 0
        self.ab_tests = {}
        self.performance_metrics = {}
        self.retrain_threshold = 0.8
        
    def evaluate_model(self, model, test_data, test_labels):
        predictions = model.predict(test_data)
        metrics = {
            'accuracy': accuracy_score(test_labels, predictions),
            'f1': f1_score(test_labels, predictions, average='weighted')
        }
        return metrics
        
    def should_retrain(self, recent_metrics):
        if len(recent_metrics) < 10:
            return False
        avg_performance = sum(m['accuracy'] for m in recent_metrics) / len(recent_metrics)
        return avg_performance < self.retrain_threshold
        
    def auto_retrain(self, new_data, new_labels):
        if self.should_retrain(self.performance_metrics.get(self.current_version, [])):
            new_model = self.train_new_model(new_data, new_labels)
            self.save_model(new_model, self.evaluate_model(new_model, new_data, new_labels))
        
    def create_ab_test(self, model_a, model_b, test_name):
        self.ab_tests[test_name] = {
            'model_a': model_a,
            'model_b': model_b,
            'metrics_a': [],
            'metrics_b': []
        }
        
    def track_performance(self, test_name, model_version, metrics):
        if test_name in self.ab_tests:
            if model_version == 'a':
                self.ab_tests[test_name]['metrics_a'].append(metrics)
            else:
                self.ab_tests[test_name]['metrics_b'].append(metrics)
        
    def save_model(self, model, metrics):
        self.current_version += 1
        self.models[self.current_version] = {
            'model': model,
            'metrics': metrics,
            'timestamp': datetime.utcnow()
        }
        return self.current_version
        
    def get_model(self, version=None):
        if version is None:
            version = self.current_version
        return self.models.get(version)
