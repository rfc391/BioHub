
import React, { useState, useEffect } from 'react';
import { Card, TextField, Button, Typography } from '@material-ui/core';

const UserProfile = () => {
    const [profile, setProfile] = useState({
        name: '',
        email: '',
        role: ''
    });

    useEffect(() => {
        const fetchProfile = async () => {
            const response = await fetch('/api/users/profile', {
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            });
            if (response.ok) {
                const data = await response.json();
                setProfile(data);
            }
        };
        fetchProfile();
    }, []);

    const handleUpdate = async () => {
        const response = await fetch('/api/users/profile', {
            method: 'PUT',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify(profile)
        });
        if (response.ok) {
            alert('Profile updated successfully');
        }
    };

    return (
        <Card style={{ padding: 20 }}>
            <Typography variant="h5">User Profile</Typography>
            <TextField
                label="Name"
                value={profile.name}
                onChange={(e) => setProfile({...profile, name: e.target.value})}
                fullWidth
                margin="normal"
            />
            <TextField
                label="Email"
                value={profile.email}
                onChange={(e) => setProfile({...profile, email: e.target.value})}
                fullWidth
                margin="normal"
            />
            <TextField
                label="Role"
                value={profile.role}
                onChange={(e) => setProfile({...profile, role: e.target.value})}
                fullWidth
                margin="normal"
            />
            <Button variant="contained" color="primary" onClick={handleUpdate}>
                Update Profile
            </Button>
        </Card>
    );
};

export default UserProfile;
