
import React from 'react';

import { 
    Grid, 
    Card, 
    CardContent, 
    Typography, 
    Button,
    Box 
} from '@mui/material';
import { TrendingUp, Notifications, Security } from '@mui/icons-material';

const Dashboard = () => {
    return (
        <Box sx={{ p: 3 }}>
            <Typography variant="h4" gutterBottom>
                Welcome to Biodefense Hub
            </Typography>
            <Grid container spacing={3}>
                <Grid item xs={12} md={4}>
                    <Card>
                        <CardContent>
                            <TrendingUp color="primary" sx={{ fontSize: 40 }} />
                            <Typography variant="h6">Monitoring</Typography>
                            <Typography variant="body2" color="textSecondary">
                                Real-time sensor data and alerts
                            </Typography>
                            <Button variant="contained" color="primary" sx={{ mt: 2 }}>
                                View Data
                            </Button>
                        </CardContent>
                    </Card>
                </Grid>
                <Grid item xs={12} md={4}>
                    <Card>
                        <CardContent>
                            <Notifications color="secondary" sx={{ fontSize: 40 }} />
                            <Typography variant="h6">Alerts</Typography>
                            <Typography variant="body2" color="textSecondary">
                                Configure and manage notifications
                            </Typography>
                            <Button variant="contained" color="secondary" sx={{ mt: 2 }}>
                                Setup Alerts
                            </Button>
                        </CardContent>
                    </Card>
                </Grid>
                <Grid item xs={12} md={4}>
                    <Card>
                        <CardContent>
                            <Security color="success" sx={{ fontSize: 40 }} />
                            <Typography variant="h6">Compliance</Typography>
                            <Typography variant="body2" color="textSecondary">
                                Track and manage compliance
                            </Typography>
                            <Button variant="contained" color="success" sx={{ mt: 2 }}>
                                View Reports
                            </Button>
                        </CardContent>
                    </Card>
                </Grid>
            </Grid>
        </Box>
    );
};

export default Dashboard;
