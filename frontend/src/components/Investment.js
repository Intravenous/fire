import React from 'react'
import axios from 'axios'
import auth from '../lib/auth'
// import { Link } from 'react-router-dom'

class Investment extends React.Component {
  constructor() {
    super()
    this.state = {
      data: {
        date: '',
        investment_type: '',
        investment_name: '',
        initial_value: '',
        comment: '',
        investment_sold: ''
      },
      errors: {}
    }
  }

  handleChange(event) {
    const { name, value } = event.target
    const data = { ...this.state.data, [name]: value }
    this.setState({ data })
  }

  handleSubmit(event) {
    event.preventDefault()
    axios
      .post('/investment', this.state.data)
      .then((res) => console.log('response', res))
      .then((res) => {
        // Auto login after registration code to be completed. After registrstion want to auto login, rather than have to manually login
        // const token = res.data.token
        // console.log(token)
        // auth.setToken(token)
        this.props.history.push('/portfolio') // Once auto login completed, what page should i push to - Home?
      })

      .catch((error) => {
        this.setState({ errors: error.response.data })
      })
  }

  render() {
    // const { errors } = this.state

    return (
      <main className="hero is-fullheight">
        <div className="hero-body">
          <div className="container">
            <section className="section">
              <div className="container has-text-centered">
                <div className="columns">
                  <div className="column is-one-third"></div>
                  <div className="column is-block">
                    <div className="box">
                      <h1 className="title">Add Investment</h1>
                      <form
                        className="form has text-left"
                        onSubmit={(event) => this.handleSubmit(event)}
                      >
                        <div className="field">
                          <label className="label">Investment Date</label>
                          <div className="control">
                            <input
                              onChange={(event) => this.handleChange(event)}
                              type="datetime-local"
                              name="investment_date"
                              className="input"
                            />
                          </div>
                          {/* {errors.email && (
                            <small className="help is-danger">{errors.email}</small>
                          )} */}
                        </div>
                        <div className="field">
                          <label className="label">Investment Type</label>
                          <div className="control">
                            <input
                              onChange={(event) => this.handleChange(event)}
                              type="text"
                              name="investment_type"
                              className="input"
                            />
                          </div>
                          {/* {errors.username && (
                            <small className="help is-danger">
                              {errors.username}
                            </small>
                          )} */}
                        </div>
                        <div className="field">
                          <label className="label">Investment Name</label>
                          <div className="control">
                            <input
                              onChange={(event) => this.handleChange(event)}
                              type="text"
                              name="investment_name"
                              className="input"
                            />
                          </div>
                          {/* {errors.first_name && (
                            <small className="help is-danger">
                              {errors.first_name}
                            </small>
                          )} */}
                        </div>
                        <div className="field">
                          <label className="label">Initial Value</label>
                          <div className="control">
                            <input
                              onChange={(event) => this.handleChange(event)}
                              type="text"
                              name="initial_value"
                              className="input"
                            />
                          </div>
                          {/* {errors.last_name && (
                            <small className="help is-danger">
                              {errors.last_name}
                            </small>
                          )} */}
                        </div>
                        <div className="field">
                          <label className="label">Comment</label>
                          <div className="control">
                            <textarea
                              onChange={(event) => this.handleChange(event)}
                              type="text"
                              rows="5"
                              name="comment"
                              className="input"
                            />
                          </div>
                          {/* {errors.password && (
                            <small className="help is-danger">
                              {errors.password}
                            </small>
                          )} */}
                        </div>
                        <div className="field">
                          <label className="label">Sold</label>
                          <div className="control">
                            <input
                              onChange={(event) => this.handleChange(event)}
                              type="checkbox"
                              name="sold"
                              className="input"
                            />
                          </div>
                          {/* {errors.password_confirmation && (
                            <small className="help is-danger">
                              {errors.password_confirmation}
                            </small>
                          )} */}
                        </div>
                        <button className="button is-success is-large">
                          Submit
                        </button>
                      </form>
                    </div>
                  </div>

                  <div className="column"></div>
                </div>
              </div>
            </section>
          </div>
        </div >
      </main >
    )
  }

}
export default Investment
