
import React from 'react';
import { SafeAreaView, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { styles } from '../styles';

export const HomeScreen = ({ navigation }) => (
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
