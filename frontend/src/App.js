
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import BiostasisDashboard from './components/BiostasisDashboard';
import Login from './components/Login';

const ROUTES = [
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard },
  { path: '/biostasis', component: BiostasisDashboard }
];

function App() {
  return (
    <Router>
      <Routes>
        {ROUTES.map(({ path, component: Component }) => (
          <Route key={path} path={path} element={<Component />} />
        ))}
      </Routes>
    </Router>
  );
}

export default App;
