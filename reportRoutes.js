
const express = require('express');
const router = express.Router();
const { generateBiostasisReport } = require('../controllers/reportController');

router.get('/biostasis/pdf', generateBiostasisReport);

module.exports = router;
