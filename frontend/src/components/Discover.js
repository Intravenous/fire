import React from 'react'
import axios from 'axios'

import Exchanges from './Exchanges'

import SearchBar from './SearchBar'

class Discover extends React.Component {
  constructor() {
    super()
    this.state = {
      query: '',
      exchange: '',
      dropDownOption: '',
      stock: {}
    }
  }

  // Need to modify
  handleDropdown(event) {
    const dropDownSelection = event.target.value
    this.setState({ dropDownOption: dropDownSelection })
    console.log(dropDownSelection)
  }

  handleChange(event) {
    const searchQuery = event.target.value
    this.setState({ query: searchQuery })
    // console.log(event)
    console.log(searchQuery)
  }

  handleSubmit(event) {
    event.preventDefault()
    // console.log(event)
    const { query } = this.state
    const { dropDownOption } = this.state
    // axios.get(`https://api.discogs.com/releases/${query}`)
    axios.get(`https://sandbox.iexapis.com/stable/stock/${query}${dropDownOption}/quote?token=Tpk_eea777c2ab7e4988a9f7463236c35f71`)
      // .then(res => console.log(res))
      .then(res => {
        this.setState({ release: res })
        console.log(this.state.stock)
      })
      .catch(err => console.error(err))
  }

  render() {
    const { value } = this.state
    return (
      <section className="Hero hero is-fullheight">
        <div className="hero-body">
          <div className="container">
            <div className="dropWrap">
              <Exchanges handleDropDown={() => this.handleDropdown(event)} />
            </div>
          </div>
          <div className="container">
            <SearchBar value={value} handleSubmit={(event) => this.handleSubmit(event)} handleChange={(event) => this.handleChange(event)} />
            <div>
              {/* Hello */}
              {/* <h1>{this.state.release.artist.name}</h1> */}
            </div>
          </div>
        </div>
      </section>
    )
  }
}

export default Discover