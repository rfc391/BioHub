
const login = (req, res) => {
    res.status(200).json({ message: 'Login successful' });
};

const register = (req, res) => {
    res.status(201).json({ message: 'User registered successfully' });
};

module.exports = { login, register };
