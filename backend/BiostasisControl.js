
import React, { useState } from 'react';

const BiostasisControl = () => {
    const [state, setState] = useState('Normal');
    const [duration, setDuration] = useState(0);
    const [temperature, setTemperature] = useState(0);

    const handleStartSimulation = () => {
        alert(`Starting biostasis simulation: ${state}, Duration: ${duration} mins, Temperature: ${temperature} °C`);
    };

    return (
        <div>
            <h2>Biostasis Control</h2>
            <select value={state} onChange={(e) => setState(e.target.value)}>
                <option value="Normal">Normal</option>
                <option value="Cryopreservation">Cryopreservation</option>
                <option value="Suspended Animation">Suspended Animation</option>
            </select>
            <input
                type="number"
                placeholder="Duration (mins)"
                value={duration}
                onChange={(e) => setDuration(e.target.value)}
            />
            <input
                type="number"
                placeholder="Temperature (°C)"
                value={temperature}
                onChange={(e) => setTemperature(e.target.value)}
            />
            <button onClick={handleStartSimulation}>Start Simulation</button>
        </div>
    );
};

export default BiostasisControl;
