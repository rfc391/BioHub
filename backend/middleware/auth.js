
const jwt = require('jsonwebtoken');

module.exports = (roles = []) => {
    return (req, res, next) => {
        const token = req.headers['authorization'];
        if (!token) return res.status(403).send('Access Denied');

        try {
            const verified = jwt.verify(token, process.env.JWT_SECRET);
            req.user = verified;
            if (roles.length && !roles.includes(req.user.role)) {
                return res.status(403).send('Insufficient permissions');
            }
            next();
        } catch (err) {
            res.status(400).send('Invalid Token');
        }
    };
};
