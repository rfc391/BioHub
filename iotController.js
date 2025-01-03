
const ingestIoTData = (req, res) => {
    const { deviceId, sensorData, timestamp } = req.body;
    res.status(201).json({ message: 'IoT Data ingested successfully', deviceId, sensorData, timestamp });
};

module.exports = { ingestIoTData };
