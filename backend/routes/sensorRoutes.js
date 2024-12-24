
const express = require('express');
const router = express.Router();
const { simulateSensorData } = require('../controllers/sensorController');

router.get('/simulate', simulateSensorData);

module.exports = router;
