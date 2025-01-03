
import React, { useState, useEffect } from 'react';
import { Grid, Card, Typography } from '@material-ui/core';
import { Line, Bar } from 'react-chartjs-2';
import 'chart.js/auto';

const IoTDashboard = () => {
    const [sensorData, setSensorData] = useState({
        labels: [],
        datasets: [{
            label: 'Sensor Readings',
            data: [],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    });

    const [deviceHealth, setDeviceHealth] = useState({
    labels: ['Online', 'Offline', 'Warning'],
    datasets: [{
        label: 'Device Status',
        data: [85, 10, 5],
        backgroundColor: [
            'rgba(75, 192, 192, 0.5)',
            'rgba(255, 99, 132, 0.5)',
            'rgba(255, 206, 86, 0.5)'
        ]
    }]
});

const [outbreakData, setOutbreakData] = useState({
        labels: ['Zone A', 'Zone B', 'Zone C', 'Zone D'],
        datasets: [{
            label: 'Incident Count',
            data: [12, 19, 3, 5],
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
        }]
    });

    useEffect(() => {
        const ws = new WebSocket('wss://0.0.0.0:3000/ws');
        ws.onmessage = (event) => {
            const newData = JSON.parse(event.data);
            setSensorData(prev => ({
                labels: [...prev.labels, new Date().toLocaleTimeString()].slice(-20),
                datasets: [{
                    ...prev.datasets[0],
                    data: [...prev.datasets[0].data, newData.value].slice(-20)
                }]
            }));
        };
        return () => ws.close();
    }, []);

    return (
        <Grid container spacing={3}>
            <Grid item xs={12}>
                <Typography variant="h4">IoT Monitoring Dashboard</Typography>
            </Grid>
            <Grid item xs={12} md={6}>
                <Card style={{ padding: 20 }}>
                    <Typography variant="h6">Real-time Sensor Data</Typography>
                    <Line data={sensorData} options={{ responsive: true }} />
                </Card>
            </Grid>
            <Grid item xs={12} md={6}>
                <Card style={{ padding: 20 }}>
                    <Typography variant="h6">Outbreak Distribution</Typography>
                    <Bar data={outbreakData} options={{ responsive: true }} />
                </Card>
            </Grid>
            <Grid item xs={12} md={6}>
                <Card style={{ padding: 20 }}>
                    <Typography variant="h6">Device Health Status</Typography>
                    <Bar data={deviceHealth} options={{ responsive: true }} />
                </Card>
            </Grid>
        </Grid>
    );
};

export default IoTDashboard;
