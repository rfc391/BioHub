
const ingestIoTData = (req, res) => {
    const { deviceId, sensorData, timestamp } = req.body;
    res.status(201).json({
        message: 'IoT data ingested',
        deviceId, sensorData, timestamp,
    });
};

module.exports = { ingestIoTData };
