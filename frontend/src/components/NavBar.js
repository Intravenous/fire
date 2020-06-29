import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import auth from '../lib/auth'

class NavBar extends React.Component {
  constructor() {
    super()
    this.state = {
      // navMobileOpen: false
    }
  }

  handleLogout() {
    auth.logout()
    this.props.history.push('/')
  }

  // Mobile NavBar code to comback to and review
  // componentDidUpdate(prevProps) {
  //   if (this.props.location.pathname !== prevProps.location.pathname) {
  //     this.setState({ navMobileOpen: false })
  //   }
  // }

  render() {
    const isLoggedIn = auth.isLoggedIn()
    return (
      <nav className="navbar" role="navigation" aria-label="main navigation">
        <div className="container navbar-container">
          <div className="navbar-brand">
            <Link className="navbar-item" to="/">Home</Link>

            <a
              role="button"
              className={`navbar-burger burger ${
                this.state.navMobileOpen ? 'is-active' : ''
              }`}
              aria-label="menu"
              aria-expanded="false"
              onClick={() =>
                this.setState({ navMobileOpen: !this.state.navMobileOpen })
              }
            >
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
            </a>
          </div>

          <div
            className={`navbar-menu ${
              this.state.navMobileOpen ? 'is-active' : ''
            }`}>

            <div className="navbar-end">
              {isLoggedIn && <div className="navbar-item">
                <Link to="/crate">Portfolio</Link>
              </div>}
              <div className="navbar-item">
                <Link to="/discover">Discover</Link>
              </div>
              {!isLoggedIn && <div className="navbar-item">
                <Link to="/register">Register</Link>
              </div>}
              {!isLoggedIn && <div className="navbar-item">
                <Link to="/login">Login</Link>
              </div>}
              {isLoggedIn && <div className="navbar-item">
                <Link to="/profile/:user_id">Profile</Link>
              </div>}
              {isLoggedIn && <div
                onClick={() => this.handleLogout()}
                className="navbar-item">
                <Link to="/">Log out</Link>
              </div>}

            </div>
          </div>
        </div>
      </nav>
    )
  }
}

export default withRouter(NavBar)