
import React, { useState } from 'react';

const IncidentLogger = () => {
    const [location, setLocation] = useState('');
    const [description, setDescription] = useState('');
    const [severity, setSeverity] = useState('');

    const handleSubmit = () => {
        alert(`Incident logged: ${location}, ${description}, Severity: ${severity}`);
    };

    return (
        <div>
            <h2>Log an Incident</h2>
            <input
                type="text"
                placeholder="Location"
                value={location}
                onChange={(e) => setLocation(e.target.value)}
            />
            <input
                type="text"
                placeholder="Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />
            <input
                type="number"
                placeholder="Severity (1-10)"
                value={severity}
                onChange={(e) => setSeverity(e.target.value)}
            />
            <button onClick={handleSubmit}>Log Incident</button>
        </div>
    );
};

export default IncidentLogger;
