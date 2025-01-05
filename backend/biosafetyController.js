
const getProtocols = (req, res) => {
    res.status(200).json({ message: 'Retrieve biosafety protocols' });
};

const addProtocol = (req, res) => {
    res.status(201).json({ message: 'Biosafety protocol added' });
};

module.exports = { getProtocols, addProtocol };
