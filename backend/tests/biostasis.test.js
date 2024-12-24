
const request = require('supertest');
const app = require('../app');

describe('Biostasis API', () => {
    test('Simulate biostasis', async () => {
        const response = await request(app).post('/api/biostasis/simulate').send({
            state: 'Cryopreservation',
            duration: 120,
            temperature: -196,
        });
        expect(response.statusCode).toBe(201);
        expect(response.body.message).toBe('Biostasis simulation initiated');
    });

    test('Monitor biostasis', async () => {
        const response = await request(app).get('/api/biostasis/monitor');
        expect(response.statusCode).toBe(200);
        expect(response.body.message).toBe('Real-time monitoring data');
    });

    test('Report biostasis', async () => {
        const response = await request(app).get('/api/biostasis/report');
        expect(response.statusCode).toBe(200);
        expect(response.body.message).toBe('Biostasis report generated');
    });
});
