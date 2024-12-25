
const request = require('supertest');
const app = require('../app');

describe('Biostasis Routes', () => {
    test('Simulate Biostasis - Valid Input', async () => {
        const response = await request(app).post('/api/biostasis/simulate').send({
            state: 'active',
            duration: 120,
            temperature: -50
        });
        expect(response.status).toBe(201);
        expect(response.body.message).toBe('Biostasis simulation initiated');
    });
});
