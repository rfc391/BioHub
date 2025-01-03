
import React from 'react';
import { SafeAreaView, Text, View } from 'react-native';
import { styles } from '../styles';

export const MonitorScreen = () => (
  <SafeAreaView style={styles.container}>
    <Text style={styles.title}>Real-time Monitoring</Text>
    <View style={styles.statsContainer}>
      <Text>Temperature: 23°C</Text>
      <Text>Humidity: 45%</Text>
      <Text>Air Quality: Good</Text>
    </View>
  </SafeAreaView>
);
