
const errorHandler = (err, req, res, next) => {
  const status = err.status || 500;
  console.error(`[Error] ${err.message}`, {
    stack: err.stack,
    path: req.path,
    method: req.method
  });
  
  res.status(status).json({
    error: {
      message: err.message,
      status,
      timestamp: new Date().toISOString()
    }
  });
};

module.exports = errorHandler;
