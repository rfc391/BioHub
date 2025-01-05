
const express = require('express');
const router = express.Router();
const { getSurveillanceData, logIncident, generateReport } = require('../controllers/biosurveillanceController');

router.get('/data', getSurveillanceData);
router.post('/incident', logIncident);
router.get('/report', generateReport);

module.exports = router;
