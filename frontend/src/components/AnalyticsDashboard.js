
import React from 'react';
import { Box, Typography, Grid, Card } from '@mui/material';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, Legend } from 'recharts';

const AnalyticsDashboard = () => {
  const mockData = [
    { date: '2023-01', incidents: 4, compliance: 95, predicted: 3 },
    { date: '2023-02', incidents: 3, compliance: 97, predicted: 4 },
    { date: '2023-03', incidents: 5, compliance: 94, predicted: 4 },
    { date: '2023-04', incidents: 2, compliance: 98, predicted: 3 },
    { date: '2023-05', predicted: 2 },
    { date: '2023-06', predicted: 3 }
  ];

  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" gutterBottom>Analytics Dashboard</Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Card>
            <Box sx={{ p: 2 }}>
              <Typography variant="h6">Incident Trends & Predictions</Typography>
              <LineChart width={500} height={300} data={mockData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="incidents" stroke="#8884d8" name="Actual Incidents" />
                <Line type="monotone" dataKey="predicted" stroke="#82ca9d" strokeDasharray="5 5" name="Predicted Incidents" />
              </LineChart>
            </Box>
          </Card>
        </Grid>
        <Grid item xs={12} md={6}>
          <Card>
            <Box sx={{ p: 2 }}>
              <Typography variant="h6">Compliance Metrics</Typography>
              <LineChart width={500} height={300} data={mockData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="compliance" stroke="#82ca9d" />
              </LineChart>
            </Box>
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
};

export default AnalyticsDashboard;
