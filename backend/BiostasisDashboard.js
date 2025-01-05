
import React from 'react';
import { Card, Typography, Grid } from '@material-ui/core';

const BiostasisDashboard = () => {
    return (
        <Grid container spacing={3}>
            <Grid item xs={12}>
                <Typography variant="h4" align="center">
                    Biostasis Dashboard
                </Typography>
            </Grid>
            <Grid item xs={6}>
                <Card>
                    <Typography variant="h5">Simulation Control</Typography>
                    <Typography>Start or manage simulations.</Typography>
                </Card>
            </Grid>
            <Grid item xs={6}>
                <Card>
                    <Typography variant="h5">Monitoring</Typography>
                    <Typography>View real-time data from active simulations.</Typography>
                </Card>
            </Grid>
        </Grid>
    );
};

export default BiostasisDashboard;
