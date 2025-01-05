
const express = require('express');
const router = express.Router();
const biostasisRoutes = require('./biostasisRoutes');
router.use('/biostasis', biostasisRoutes);
module.exports = router;
