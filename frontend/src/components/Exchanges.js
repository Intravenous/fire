// Dropbox of available exchanges to be used for srock searches
import React from 'react'
const Exchanges = ({ handleDropDown }) => {
  return (
    <div className="field is-flex dropdown">
      <div className="container">
        <h1 className="title is-3 has-text-centered">Select Exchange</h1>
        <div className="control has-icons-left">
          <div className="select">
            <select name="category" onChange={handleDropDown}>
              <option value="">United States</option>
              <option value="-DH">Abu Dhabi Securities Exchange</option>
              <option value="-IT">Tel Aviv Stock Exchange</option>
              <option value="-IB">BSE Ltd.</option>
              <option value="-KP">Korea Exchange</option>
              <option value="-BB">Euronext Brussels</option>
              <option value="-GY">XETRA</option>
              <option value="-FP">Euronext Paris</option>
              <option value="-LN">London Stock Exchange</option>
              <option value="-ID">Euronext Dublin</option>
              <option value="-NA">Euronext Amsterdam</option>
              <option value="-PL">Euronext Lisbon</option>
              <option value="-CT">Toronto Stock Exchange</option>
              <option value="-CV">TSX Venture Exchange</option>
              <option value="-MM">Mexican Stock Exchange</option>
            </select>
          </div>
          <div className="icon is-small is-left">
            <i className="fas fa-globe"></i>
          </div>
        </div>
      </div>
    </div>
  )
}
export default Exchanges
