
const express = require('express');
const router = express.Router();
const { ingestIoTData } = require('../controllers/iotController');

router.post('/ingest', ingestIoTData);

module.exports = router;
