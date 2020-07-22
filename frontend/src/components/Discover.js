import React from 'react'
import axios from 'axios'

import Exchanges from './Exchanges'
import SearchBar from './SearchBar'

class Discover extends React.Component {
  constructor() {
    super()
    this.state = {
      query: '',
      dropDownOption: '',
      stock: {}
    }
  }

  handleDropdown(event) {
    const dropDownSelection = event.target.value
    this.setState({ dropDownOption: dropDownSelection })
    // console.log(dropDownSelection)
  }

  handleChange(event) {
    const searchQuery = event.target.value
    this.setState({ query: searchQuery })
    // console.log(event)
    // console.log(searchQuery)
  }

  handleSubmit(event) {
    event.preventDefault()
    // console.log(event)
    const { query } = this.state
    const { dropDownOption } = this.state
    axios.get(`https://sandbox.iexapis.com/stable/stock/${query}${dropDownOption}/quote?token=Tpk_eea777c2ab7e4988a9f7463236c35f71`)
      .then(res => {
        this.setState({ stock: res })
        console.log(this.state.stock, 'stock')
      })
      .catch(err => console.error(err))
  }

  render() {
    if (stock === null) return null
    const { stock } = this.state
    // const symbol = stock.data.symbol
    return (
      <section className="Hero hero is-fullheight">
        <div className="hero-body">
          <div className="container">
            <div className="dropWrap">
              <Exchanges handleDropDown={() => this.handleDropdown(event)} />
            </div>
          </div>
          <div className="container">
            <SearchBar handleSubmit={(event) => this.handleSubmit(event)} handleChange={(event) => this.handleChange(event)} />
            <div>
              {/* <h1>{symbol}</h1> */}
            </div>
          </div>
          
        </div>
      </section>
    )
  }
}

export default Discover