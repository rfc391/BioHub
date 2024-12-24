
const express = require('express');
const router = express.Router();
const { ingestData, getOutbreakTrends, triggerAlert } = require('../controllers/rodsController');

router.post('/ingest', ingestData);
router.get('/trends', getOutbreakTrends);
router.post('/alert', triggerAlert);

module.exports = router;
