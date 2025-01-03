
const PDFDocument = require('pdfkit');
const fs = require('fs');

const generateReport = async (req, res) => {
    const doc = new PDFDocument();
    const filename = `report-${Date.now()}.pdf`;
    const stream = fs.createWriteStream(filename);

    doc.pipe(stream);
    
    // Header
    doc.fontSize(25).text('Comprehensive Biosurveillance Report', 100, 100);
    doc.fontSize(12).text('Generated: ' + new Date().toLocaleString(), 100, 150);
    
    // Summary Section
    doc.fontSize(16).text('Executive Summary', 100, 200);
    doc.fontSize(12).text('Total Incidents: 25', 120, 230);
    doc.fontSize(12).text('Resolution Rate: 92%', 120, 250);
    doc.fontSize(12).text('Average Response Time: 45 minutes', 120, 270);
    
    // Detailed Statistics
    doc.fontSize(16).text('Detailed Statistics', 100, 320);
    doc.fontSize(12).text('High Priority Incidents: 5', 120, 350);
    doc.fontSize(12).text('Medium Priority Incidents: 12', 120, 370);
    doc.fontSize(12).text('Low Priority Incidents: 8', 120, 390);
    
    // Location Analysis
    doc.fontSize(16).text('Location Analysis', 100, 440);
    doc.fontSize(12).text('Zone A: 8 incidents', 120, 470);
    doc.fontSize(12).text('Zone B: 6 incidents', 120, 490);
    doc.fontSize(12).text('Zone C: 11 incidents', 120, 510);

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

const generateWeeklySummary = async (req, res) => {
    res.json({
        week: new Date().toISOString().slice(0, 10),
        totalIncidents: 25,
        resolvedIncidents: 23,
        avgResponseTime: '45 minutes',
        criticalAreas: ['Zone A', 'Zone C'],
        recommendations: [
            'Increase monitoring in Zone A',
            'Update response protocols for high-priority incidents'
        ]
    });
};

module.exports = { generateReport, generateWeeklySummary };
const PDFDocument = require('pdfkit');

const generateBiostasisReport = async (req, res) => {
  const doc = new PDFDocument();
  const stream = res.writeHead(200, {
    'Content-Type': 'application/pdf',
    'Content-Disposition': 'attachment;filename=biostasis-report.pdf'
  });

  doc.pipe(stream);
  doc.fontSize(25).text('Biostasis Simulation Report', 100, 100);
  doc.fontSize(12).text(`Generated: ${new Date().toISOString()}`, 100, 150);
  doc.end();
};

module.exports = { generateBiostasisReport };
