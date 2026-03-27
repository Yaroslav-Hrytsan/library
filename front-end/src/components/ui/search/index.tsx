import React from 'react'
import s from './index.module.css'
import { SearchContext } from '../../../context/searchContext'

const Search = () => {
    const { valueInput, setValueInput } = React.useContext(SearchContext);
  return (
    <div>      
      <input
        type="text"
        placeholder="Search books..."
        value={valueInput}
        onChange={(e) => setValueInput(e.target.value)}
        className={s.search}
      />
    </div>
  )
}
export default Search




