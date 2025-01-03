
const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Database connection
const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGO_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true
    });
    console.log('MongoDB connected successfully');
  } catch (error) {
    console.error('MongoDB connection error:', error);
    process.exit(1);
  }
};

connectDB();

// API Routes
const routes = {
  auth: require('./routes/authRoutes'),
  biosafety: require('./routes/biosafetyRoutes'),
  biostasis: require('./routes/biostasisRoutes'),
  iot: require('./routes/iotRoutes')
};

Object.entries(routes).forEach(([path, router]) => {
  app.use(`/api/${path}`, router);
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Server running on port ${port}`);
});

module.exports = app;
