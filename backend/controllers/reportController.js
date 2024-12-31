
const PDFDocument = require('pdfkit');
const fs = require('fs');

const generateReport = async (req, res) => {
    const doc = new PDFDocument();
    const filename = `report-${Date.now()}.pdf`;
    const stream = fs.createWriteStream(filename);

    doc.pipe(stream);
    doc.fontSize(25).text('Compliance Report', 100, 100);
    doc.fontSize(12).text('Generated: ' + new Date().toLocaleString(), 100, 150);
    
    // Add report content
    doc.fontSize(14).text('Incident Summary', 100, 200);
    doc.fontSize(12).text('Total Incidents: 25', 120, 230);
    doc.fontSize(12).text('Resolution Rate: 92%', 120, 250);

    doc.end();

    stream.on('finish', () => {
        res.download(filename, (err) => {
            fs.unlinkSync(filename);
            if (err) {
                res.status(500).json({ error: 'Error downloading file' });
            }
        });
    });
};

module.exports = { generateReport };
