
const ingestData = (req, res) => {
    const { symptoms, location, timestamp } = req.body;
    res.status(201).json({
        message: 'Data ingested successfully',
        symptoms, location, timestamp,
    });
};

const getOutbreakTrends = (req, res) => {
    res.status(200).json({ trends: 'Outbreak trends visualization data' });
};

const triggerAlert = (req, res) => {
    const { region, severity } = req.body;
    res.status(200).json({ message: 'Alert triggered', region, severity });
};

module.exports = { ingestData, getOutbreakTrends, triggerAlert };


const getHistoricalData = (req, res) => {
    res.status(200).json({
        message: 'Historical data retrieved successfully',
        data: [
            { date: '2023-01-01', cases: 50 },
            { date: '2023-02-01', cases: 75 },
            { date: '2023-03-01', cases: 100 }
        ]
    });
};

module.exports = { ingestData, getOutbreakTrends, triggerAlert, getHistoricalData };
