
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { HomeScreen } from './screens/HomeScreen';
import { MonitorScreen } from './screens/MonitorScreen';
import { IncidentsScreen } from './screens/IncidentsScreen';

const Stack = createStackNavigator();

const App = () => (
  <NavigationContainer>
    <Stack.Navigator>
      <Stack.Screen name="Home" component={HomeScreen} />
      <Stack.Screen name="Monitor" component={MonitorScreen} />
      <Stack.Screen name="Incidents" component={IncidentsScreen} />
    </Stack.Navigator>
  </NavigationContainer>
);

export default App;
