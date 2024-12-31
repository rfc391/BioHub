
const cache = require('memory-cache');

class BiostasisController {
  static async getMetrics(req, res) {
    const cachedMetrics = cache.get('metrics');
    if (cachedMetrics) {
      return res.json(cachedMetrics);
    }

    const metrics = await BiostasisService.getCurrentMetrics();
    cache.put('metrics', metrics, 5000);
    res.json(metrics);
  }

  static async simulateBiostasis(req, res) {
    const { temperature, duration } = req.body;
    const simulation = await BiostasisService.runSimulation(temperature, duration);
    res.status(201).json(simulation);
  }
}

module.exports = BiostasisController;
