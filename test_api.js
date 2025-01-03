
const axios = require('axios');

const baseURL = 'http://localhost:5000/api';

async function testBiostasis() {
    try {
        console.log('Testing Biostasis Simulation...');
        let response = await axios.post(`${baseURL}/biostasis/simulate`, {
            state: 'suspended',
            duration: 120,
            temperature: -80
        });
        console.log('Simulate Response:', response.data);

        console.log('Testing Biostasis Monitor...');
        response = await axios.get(`${baseURL}/biostasis/monitor`);
        console.log('Monitor Response:', response.data);

        console.log('Testing Biostasis Report...');
        response = await axios.get(`${baseURL}/biostasis/report`);
        console.log('Report Response:', response.data);
    } catch (err) {
        console.error('Biostasis Test Error:', err.message);
    }
}

async function testIoT() {
    try {
        console.log('Testing IoT Data Ingestion...');
        const response = await axios.post(`${baseURL}/iot/ingest`, {
            deviceId: 'sensor123',
            sensorData: { temperature: 22, humidity: 45 },
            timestamp: Date.now()
        });
        console.log('IoT Response:', response.data);
    } catch (err) {
        console.error('IoT Test Error:', err.message);
    }
}

async function testRods() {
    try {
        console.log('Testing RODS Data Ingestion...');
        let response = await axios.post(`${baseURL}/rods/ingest`, {
            symptoms: ['fever', 'cough'],
            location: 'Region-1',
            timestamp: Date.now()
        });
        console.log('RODS Ingest Response:', response.data);

        console.log('Testing RODS Trends...');
        response = await axios.get(`${baseURL}/rods/trends`);
        console.log('RODS Trends Response:', response.data);

        console.log('Testing RODS Alert...');
        response = await axios.post(`${baseURL}/rods/alert`, {
            region: 'Region-1',
            severity: 'High'
        });
        console.log('RODS Alert Response:', response.data);
    } catch (err) {
        console.error('RODS Test Error:', err.message);
    }
}

(async function runTests() {
    console.log('Starting API Tests...');
    await testBiostasis();
    await testIoT();
    await testRods();
    console.log('API Tests Completed.');
})();


async function testHistoricalData() {
    try {
        console.log('Testing RODS Historical Data...');
        const response = await axios.get(`${baseURL}/rods/historical`);
        console.log('Historical Data Response:', response.data);
    } catch (err) {
        console.error('Historical Data Test Error:', err.message);
    }
}

// Include the new test in the test suite
(async function runTests() {
    console.log('Starting API Tests...');
    await testBiostasis();
    await testIoT();
    await testRods();
    await testHistoricalData(); // New test added here
    console.log('API Tests Completed.');
})();
