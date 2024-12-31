
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

const login = async (req, res) => {
    const { email, password, totpCode } = req.body;
    
    // Multi-factor authentication check
    if (!totpCode) {
        return res.status(400).json({ message: 'TOTP code required' });
    }

    // Simulate user verification
    const user = {
        id: 1,
        email,
        role: 'admin',
        permissions: ['read', 'write', 'admin']
    };

    const token = jwt.sign(user, process.env.JWT_SECRET, { expiresIn: '1h' });
    
    res.status(200).json({ 
        message: 'Login successful',
        token,
        user: {
            email: user.email,
            role: user.role,
            permissions: user.permissions
        }
    });
};

const register = async (req, res) => {
    const { email, password, role } = req.body;
    
    // Hash password
    const hashedPassword = await bcrypt.hash(password, 10);
    
    // Simulate user creation
    const user = {
        id: Date.now(),
        email,
        role,
        hashedPassword
    };
    
    res.status(201).json({ 
        message: 'User registered successfully',
        user: {
            email: user.email,
            role: user.role
        }
    });
};

const verifyToken = (req, res) => {
    const token = req.headers.authorization?.split(' ')[1];
    
    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        res.json({ valid: true, user: decoded });
    } catch (error) {
        res.json({ valid: false });
    }
};

module.exports = { login, register, verifyToken };
