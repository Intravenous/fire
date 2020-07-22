import React, { useState, useEffect } from 'react'
import ReactDOM from 'react-dom'
import { HashRouter, Switch, Route } from 'react-router-dom'

import 'bulma'
import './style.scss'

import Home from './components/Home'
import NavBar from './components/NavBar'
import Register from './components/Register'
import Login from './components/Login'
import Profile from './components/Profile'
import Discover from './components/Discover'
import Investment from './components/Investment'
import Trade from './components/Trade'

const App = () => (
  <HashRouter>
    <NavBar />
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/login" component={Login} />
      <Route exact path="/register" component={Register} />
      <Route exact path="/profile" component={Profile} />
      <Route exact path="/discover" component={Discover} />
      <Route exact path="/investment" component={Investment} />
      <Route exact path="/trade" component={Trade} />
    </Switch>
  </HashRouter>
)

ReactDOM.render(<App />, document.getElementById('root'))
