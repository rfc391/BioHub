
const simulateSensorData = (req, res) => {
    res.status(200).json({ data: 'Simulated phage-triggered ion cascades' });
};

module.exports = { simulateSensorData };
