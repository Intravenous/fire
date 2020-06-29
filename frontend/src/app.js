import React, { useState, useEffect } from 'react'
import ReactDOM from 'react-dom'
import { HashRouter, Switch, Route } from 'react-router-dom'

import 'bulma'
import './style.scss'

import Home from './components/Home'
import NavBar from './components/NavBar'
import Register from './components/Register'
import Login from './components/Login'

const App = () => (
  <HashRouter>
    <NavBar />
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/login" component={Login} />
      <Route exact path="/register" component={Register} />
    </Switch>
  </HashRouter>
)

ReactDOM.render(<App />, document.getElementById('root'))
