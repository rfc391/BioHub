
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { HomeScreen } from './screens/HomeScreen';
import { MonitorScreen } from './screens/MonitorScreen';
import { IncidentsScreen } from './screens/IncidentsScreen';

const Stack = createStackNavigator();

const SCREENS = [
  { name: 'Home', component: HomeScreen },
  { name: 'Monitor', component: MonitorScreen },
  { name: 'Incidents', component: IncidentsScreen }
];

const App = () => (
  <NavigationContainer>
    <Stack.Navigator>
      {SCREENS.map(({ name, component }) => (
        <Stack.Screen key={name} name={name} component={component} />
      ))}
    </Stack.Navigator>
  </NavigationContainer>
);

export default App;
