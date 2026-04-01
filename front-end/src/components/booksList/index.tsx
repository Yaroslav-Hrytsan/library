import React from 'react'
import { books } from '../../data/books'
import { Link, useParams } from 'react-router-dom'
import { categoryBooks } from '../../data/categoriesBooks'
import { SearchContext } from '../../context/SearchContext'
import { useDebounce } from '../../hooks/DebounceHooks'

const BooksList: React.FC = () => {
  const [booksList, setBooksList] = React.useState(books) 
  const {id} = useParams<{id?: string}>()

  const {valueInput} = React.useContext(SearchContext)
  const debouncedValue = useDebounce( {valueSearch: valueInput, time: 400} )
  const normalizeSearch = debouncedValue.trim().toLowerCase()
  React.useEffect(() => {
    const filteredBooks = books.filter( book => {
      const booksByCategory = id && id !== "all-books" ? book.category === id : books
      const booksBySearch = 
      book.title.toLowerCase().includes(normalizeSearch) ||
      book.author.toLowerCase().includes(normalizeSearch) ||
      book.year.toString().includes(normalizeSearch)
      return booksByCategory && booksBySearch
      }
    )
    setBooksList(filteredBooks)
  }, [normalizeSearch, id])

    const categoryTitle = categoryBooks.find(category => category.id === id)?.name ?? 'Всі книги'
  
  return (
    <div>
      <h2>{categoryTitle}</h2>
      { !booksList ? <p>Книги не знайдено</p> :
      (booksList.map(book => (
        <Link key={book.id} to={`/book/${book.id}`}>
          <ul>
            <li>{book.cover}</li>
            <li>{book.title}</li>
            <li>{book.author}</li>
            <li>{book.year}</li>
            <li>{book.category}</li>
            </ul>
        </Link>))) }
    </div>
  )
}

export default BooksList
