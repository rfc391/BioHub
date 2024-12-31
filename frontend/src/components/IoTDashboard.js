
import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import { Card, Grid, Typography } from '@material-ui/core';

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

    useEffect(() => {
        const ws = new WebSocket('wss://your-replit-url/ws');
        ws.onmessage = (event) => {
            const newData = JSON.parse(event.data);
            setSensorData(prev => ({
                labels: [...prev.labels, new Date().toLocaleTimeString()],
                datasets: [{
                    ...prev.datasets[0],
                    data: [...prev.datasets[0].data, newData.value]
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
                <Card>
                    <Line data={sensorData} />
                </Card>
            </Grid>
            <Grid item xs={12} md={6}>
                <Card>
                    <Typography variant="h6">Device Status</Typography>
                    <Typography>Active Devices: 5</Typography>
                    <Typography>Alert Status: Normal</Typography>
                </Card>
            </Grid>
        </Grid>
    );
};

export default IoTDashboard;
