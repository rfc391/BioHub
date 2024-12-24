
import React, { useState } from 'react';

const AlertTrigger = () => {
    const [region, setRegion] = useState('');
    const [severity, setSeverity] = useState('');

    const handleTriggerAlert = () => {
        alert(`Alert triggered for region: ${region}, Severity: ${severity}`);
    };

    return (
        <div>
            <h2>Trigger Alert</h2>
            <input
                type="text"
                placeholder="Region"
                value={region}
                onChange={(e) => setRegion(e.target.value)}
            />
            <input
                type="number"
                placeholder="Severity (1-10)"
                value={severity}
                onChange={(e) => setSeverity(e.target.value)}
            />
            <button onClick={handleTriggerAlert}>Trigger Alert</button>
        </div>
    );
};

export default AlertTrigger;
