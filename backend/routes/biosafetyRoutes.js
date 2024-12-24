
const express = require('express');
const router = express.Router();
const { getProtocols, addProtocol } = require('../controllers/biosafetyController');

router.get('/', getProtocols);
router.post('/', addProtocol);

module.exports = router;
