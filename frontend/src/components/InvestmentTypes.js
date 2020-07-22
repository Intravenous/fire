// Dropbox of available exchanges to be used for srock searches
import React from 'react'
const InvestmentTypes = ({ handleDropDown }) => {
  return (
    <div className="field is-flex dropdown">
      <div className="container">
        <h1 className="title is-3 has-text-centered">Select Exchange</h1>
        <div className="control has-icons-left">
          <div className="select">
            <select name="category" onChange={handleDropDown}>
              <option value="CH">Cash</option>
              <option value="-CI">Cash Isa</option>
              <option value="-EC">Equity Crowdfunding</option>
              <option value="-PN">Pension</option>
              <option value="-SO">Stock Options</option>
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
export default InvestmentTypes
