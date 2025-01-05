
import React from 'react';
import { MapContainer, TileLayer, HeatmapLayer } from 'react-leaflet';
import 'leaflet.markercluster';

const Heatmap = ({ data }) => {
    const options = {
        radius: 20,
        blur: 15,
        maxZoom: 18,
        minOpacity: 0.4,
        gradient: { 0.4: 'blue', 0.65: 'lime', 1: 'red' }
    };

    return (
        <MapContainer center={[51.505, -0.09]} zoom={13} style={{ height: '500px', width: '100%' }}>
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution="&copy; OpenStreetMap contributors"
            />
            <HeatmapLayer
                points={data}
                longitudeExtractor={m => m.lng}
                latitudeExtractor={m => m.lat}
                intensityExtractor={m => m.intensity}
                options={options}
            />
            <MarkerClusterGroup>
                {data.map((point, index) => (
                    <Marker key={index} position={[point.lat, point.lng]}>
                        <Popup>
                            Intensity: {point.intensity}<br />
                            Date: {point.date}
                        </Popup>
                    </Marker>
                ))}
            </MarkerClusterGroup>
        </MapContainer>
    );
};

export default Heatmap;
