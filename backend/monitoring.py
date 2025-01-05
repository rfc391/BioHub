from prometheus_client import start_http_server, Counter, Gauge
import psutil
import time
import threading
import asyncio
import websockets

class SystemMonitor:
    def __init__(self, port=8000, websocket_port=8765):
        self.request_count = Counter('request_count', 'Number of requests')
        self.cpu_usage = Gauge('cpu_usage', 'CPU Usage')
        self.memory_usage = Gauge('memory_usage', 'Memory Usage')
        start_http_server(port)
        self.websocket_port = websocket_port
        self.websocket_manager = WebSocketManager()

    def collect_metrics(self):
        return {
            'cpu_usage': psutil.cpu_percent(),
            'memory_usage': psutil.virtual_memory().percent
        }

    def store_metrics(self, metrics):
        self.cpu_usage.set(metrics['cpu_usage'])
        self.memory_usage.set(metrics['memory_usage'])

    async def update_metrics(self):
        metrics = self.collect_metrics()
        self.store_metrics(metrics)
        await self.websocket_manager.send_update(metrics)

    def start(self):
        thread = threading.Thread(target=self._start_monitoring)
        thread.daemon = True
        thread.start()
        asyncio.run(self.websocket_manager.start())


    def _start_monitoring(self):
        while True:
            asyncio.run(self.update_metrics())
            time.sleep(1)

    def log_request(self):
        self.request_count.inc()


class WebSocketManager:
    def __init__(self):
        self.clients = set()

    async def register(self, websocket):
        self.clients.add(websocket)
        print(f"Client connected: {websocket}")

    async def unregister(self, websocket):
        self.clients.remove(websocket)
        print(f"Client disconnected: {websocket}")

    async def send_update(self, metrics):
        if self.clients:
            await asyncio.wait([client.send(json.dumps(metrics)) for client in self.clients])

    async def handler(self, websocket, path):
        await self.register(websocket)
        try:
            while True:
                await asyncio.sleep(1) # Keep connection alive
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            await self.unregister(websocket)

    async def start(self):
        async with websockets.serve(self.handler, "localhost", self.websocket_port):
            await asyncio.Future() # run forever


from sklearn.metrics import accuracy_score, precision_score, recall_score
import numpy as np
import json
from datetime import datetime

class MLMonitor:
    def __init__(self):
        self.metrics_history = []
        
    def log_metrics(self, y_true, y_pred, model_name):
        metrics = {
            'timestamp': datetime.now().isoformat(),
            'model_name': model_name,
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred, average='weighted'),
            'recall': recall_score(y_true, y_pred, average='weighted')
        }
        self.metrics_history.append(metrics)
        self._save_metrics()
        
    def _save_metrics(self):
        with open('ml_metrics.json', 'w') as f:
            json.dump(self.metrics_history, f)