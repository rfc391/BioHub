
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

const SALT_ROUNDS = 10;

const login = async (req, res) => {
    const { email, password, totpCode } = req.body;
    
    if (!totpCode) {
        return res.status(400).json({ 
            success: false,
            message: 'TOTP code required' 
        });
    }

    const user = {
        id: 1,
        email,
        role: 'admin',
        permissions: ['read', 'write', 'admin']
    };

    const token = jwt.sign(user, process.env.JWT_SECRET, { 
        expiresIn: '1h' 
    });
    
    res.status(200).json({ 
        success: true,
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
    
    const hashedPassword = await bcrypt.hash(password, SALT_ROUNDS);
    
    const user = {
        id: Date.now(),
        email,
        role,
        hashedPassword
    };
    
    res.status(201).json({ 
        success: true,
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
        res.json({ 
            success: true,
            valid: true, 
            user: decoded 
        });
    } catch (error) {
        res.json({ 
            success: false,
            valid: false 
        });
    }
};

module.exports = { login, register, verifyToken };
