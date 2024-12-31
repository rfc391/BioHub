
import React, { useState } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { SafeAreaView, Text, TouchableOpacity, View, StyleSheet } from 'react-native';

const Stack = createStackNavigator();

const HomeScreen = ({ navigation }) => {
    return (
        <SafeAreaView style={styles.container}>
            <Text style={styles.title}>Biodefense Hub Mobile</Text>
            <TouchableOpacity 
                style={styles.button}
                onPress={() => navigation.navigate('Monitor')}>
                <Text style={styles.buttonText}>View Monitoring</Text>
            </TouchableOpacity>
            <TouchableOpacity 
                style={styles.button}
                onPress={() => navigation.navigate('Incidents')}>
                <Text style={styles.buttonText}>Report Incident</Text>
            </TouchableOpacity>
        </SafeAreaView>
    );
};

const MonitorScreen = () => (
    <SafeAreaView style={styles.container}>
        <Text style={styles.title}>Real-time Monitoring</Text>
        <View style={styles.statsContainer}>
            <Text>Temperature: 23°C</Text>
            <Text>Humidity: 45%</Text>
            <Text>Air Quality: Good</Text>
        </View>
    </SafeAreaView>
);

const IncidentsScreen = () => (
    <SafeAreaView style={styles.container}>
        <Text style={styles.title}>Report Incident</Text>
        {/* Add incident form here */}
    </SafeAreaView>
);

const App = () => {
    return (
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen name="Home" component={HomeScreen} />
                <Stack.Screen name="Monitor" component={MonitorScreen} />
                <Stack.Screen name="Incidents" component={IncidentsScreen} />
            </Stack.Navigator>
        </NavigationContainer>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 20,
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 20,
    },
    button: {
        backgroundColor: '#007AFF',
        padding: 15,
        borderRadius: 8,
        marginVertical: 10,
    },
    buttonText: {
        color: 'white',
        textAlign: 'center',
        fontSize: 16,
    },
    statsContainer: {
        padding: 20,
        backgroundColor: '#f5f5f5',
        borderRadius: 8,
    },
});

export default App;
