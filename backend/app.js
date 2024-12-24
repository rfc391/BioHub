
const express = require('express');
const helmet = require('helmet');
const bodyParser = require('body-parser');
const cors = require('cors');
const biostasisRoutes = require('./routes/biostasisRoutes');
const rodsRoutes = require('./routes/rodsRoutes');
const iotRoutes = require('./routes/iotRoutes');
const app = express();

app.use(helmet());
app.use(cors());
app.use(bodyParser.json());

// Define routes for various modules
app.use('/api/biostasis', biostasisRoutes);
app.use('/api/rods', rodsRoutes);
app.use('/api/iot', iotRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

module.exports = app;
