
const express = require('express');
const router = express.Router();
const { simulateBiostasis, monitorBiostasis, reportBiostasis } = require('../controllers/biostasisController');

router.post('/simulate', simulateBiostasis);
router.get('/monitor', monitorBiostasis);
router.get('/report', reportBiostasis);

module.exports = router;
