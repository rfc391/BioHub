
const express = require('express');
const multer = require('multer');
const cors = require('cors');
const { convert } = require('@microsoft/markitdown');

// Initialize app and middleware
const app = express();
const upload = multer({ storage: multer.memoryStorage() });

// Global middleware
app.use(cors());
app.use(express.json());

// File conversion endpoint
app.post('/convert', upload.single('file'), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ 
        success: false,
        error: 'No file uploaded' 
      });
    }

    const result = await convert(req.file.buffer);
    res.json({ 
      success: true,
      markdown: result 
    });
  } catch (error) {
    res.status(500).json({ 
      success: false,
      error: error.message 
    });
  }
});

// Server configuration
const PORT = 3000;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running at http://0.0.0.0:${PORT}`);
});
