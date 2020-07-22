import React from 'react'

const SearchBar = ({ handleChange, handleSubmit }) => {
  return (
    <div className="Search">
      <div className="container">
        <h1 className="title is-3 has-text-centered">Search by Symbol</h1>
        <div className="field is-horizontal has-addons">
          <div className="control is-expanded"></div>
          <input
            className="input is-medium"
            type="search"
            placeholder="Search by stock symbol"
            onChange={handleChange}
          />
          <div className="control">
            <button onClick={handleSubmit} className="button is-primary is-medium">Search</button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default SearchBar