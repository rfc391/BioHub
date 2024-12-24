
const express = require('express');
const helmet = require('helmet');
const bodyParser = require('body-parser');
const cors = require('cors');
const biostasisRoutes = require('./routes/biostasisRoutes');
const app = express();

app.use(helmet());
app.use(cors());
app.use(bodyParser.json());

app.use('/api/biostasis', biostasisRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

module.exports = app;
