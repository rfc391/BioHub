
import React, { useState } from 'react';
import { Card, Grid, Typography, Button } from '@material-ui/core';
import { Notifications, LocationOn, Assessment } from '@material-ui/icons';

const OutbreakDashboard = () => {
    const [alerts, setAlerts] = useState([
        { id: 1, zone: 'Zone A', severity: 'High', timestamp: new Date().toLocaleString() },
        { id: 2, zone: 'Zone B', severity: 'Medium', timestamp: new Date().toLocaleString() }
    ]);

    const triggerAlert = () => {
        const newAlert = {
            id: alerts.length + 1,
            zone: `Zone ${String.fromCharCode(65 + Math.floor(Math.random() * 4))}`,
            severity: ['Low', 'Medium', 'High'][Math.floor(Math.random() * 3)],
            timestamp: new Date().toLocaleString()
        };
        setAlerts([...alerts, newAlert]);
    };

    return (
        <Grid container spacing={3}>
            <Grid item xs={12}>
                <Typography variant="h4">Outbreak Monitoring</Typography>
            </Grid>
            <Grid item xs={12} md={4}>
                <Card style={{ padding: 20 }}>
                    <Typography variant="h6">
                        <Notifications /> Active Alerts
                    </Typography>
                    {alerts.map(alert => (
                        <Card key={alert.id} style={{ margin: '10px 0', padding: 10 }}>
                            <Typography>Zone: {alert.zone}</Typography>
                            <Typography>Severity: {alert.severity}</Typography>
                            <Typography>Time: {alert.timestamp}</Typography>
                        </Card>
                    ))}
                </Card>
            </Grid>
            <Grid item xs={12} md={4}>
                <Card style={{ padding: 20 }}>
                    <Typography variant="h6">
                        <LocationOn /> Location Tracking
                    </Typography>
                    <Button 
                        variant="contained" 
                        color="primary" 
                        onClick={triggerAlert}
                        style={{ marginTop: 10 }}
                    >
                        Trigger Test Alert
                    </Button>
                </Card>
            </Grid>
            <Grid item xs={12} md={4}>
                <Card style={{ padding: 20 }}>
                    <Typography variant="h6">
                        <Assessment /> Analytics
                    </Typography>
                    <Typography>Active Incidents: {alerts.length}</Typography>
                    <Typography>Response Rate: 92%</Typography>
                    <Typography>Average Resolution Time: 45 min</Typography>
                </Card>
            </Grid>
        </Grid>
    );
};

export default OutbreakDashboard;
