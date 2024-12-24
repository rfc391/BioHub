
import React from 'react';
import { MapContainer, TileLayer, HeatmapLayer } from 'react-leaflet';

const Heatmap = ({ data }) => {
    return (
        <MapContainer center={[51.505, -0.09]} zoom={13} style={{ height: '500px', width: '100%' }}>
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution="&copy; OpenStreetMap contributors"
            />
            <HeatmapLayer
                points={data}
                latitudeExtractor={(m) => m.lat}
                longitudeExtractor={(m) => m.lng}
                intensityExtractor={(m) => m.intensity}
            />
        </MapContainer>
    );
};

export default Heatmap;
