import React from 'react';
import Navbar from './components/Navbar';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './components/pages/Home';
import SignUp from './components/pages/SignUp';
import userPantry from './components/pages/Products';
import Recipes from './components/pages/Services';
import Profile from './components/pages/Profile';
import Auth from './components/Auth';
import "bootstrap/dist/css/bootstrap.min.css"

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Switch>
          <Route path='/auth' element={<Auth />} />
          <Route path='/' exact component={Home} />
          <Route path='/pantry' component={userPantry} />
          <Route path='/recipes' component={Recipes} />
          <Route path='/sign-up' component={SignUp} />
        </Switch>
      </Router>
    </>
  );
}

export default App;
