
import React from 'react';
import { Grid, Card, Typography, Box } from '@material-ui/core';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const AnalyticsDashboard = () => {
  const mockData = [
    { date: '2023-01', incidents: 4, compliance: 95 },
    { date: '2023-02', incidents: 3, compliance: 97 },
    { date: '2023-03', incidents: 5, compliance: 94 },
    { date: '2023-04', incidents: 2, compliance: 98 }
  ];

  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" gutterBottom>Analytics Dashboard</Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Card>
            <Box sx={{ p: 2 }}>
              <Typography variant="h6">Incident Trends</Typography>
              <LineChart width={500} height={300} data={mockData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="incidents" stroke="#8884d8" />
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
