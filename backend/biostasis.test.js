
const request = require('supertest');
const app = require('../../backend/app');

describe('Biostasis Integration Tests', () => {
  test('GET /api/biostasis/metrics', async () => {
    const response = await request(app).get('/api/biostasis/metrics');
    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('temperature');
    expect(response.body).toHaveProperty('pressure');
  });

  test('POST /api/biostasis/simulate', async () => {
    const response = await request(app)
      .post('/api/biostasis/simulate')
      .send({
        temperature: -50,
        duration: 120
      });
    expect(response.status).toBe(201);
  });
});
