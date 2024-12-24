
import React from 'react';
import { Grid, Typography, Card } from '@material-ui/core';

const Dashboard = () => {
    return (
        <Grid container spacing={3}>
            <Grid item xs={12}>
                <Typography variant="h4" align="center">
                    Professional Biodefense Hub Dashboard
                </Typography>
            </Grid>
            <Grid item xs={4}>
                <Card>
                    <Typography variant="h5">Biostasis Control</Typography>
                    <Typography>Manage biostasis simulations.</Typography>
                </Card>
            </Grid>
            <Grid item xs={4}>
                <Card>
                    <Typography variant="h5">Outbreak Monitoring</Typography>
                    <Typography>View real-time outbreak trends.</Typography>
                </Card>
            </Grid>
            <Grid item xs={4}>
                <Card>
                    <Typography variant="h5">IoT Data</Typography>
                    <Typography>Monitor connected devices.</Typography>
                </Card>
            </Grid>
        </Grid>
    );
};

export default Dashboard;
