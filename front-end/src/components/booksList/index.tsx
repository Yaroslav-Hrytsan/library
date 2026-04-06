import React, { useEffect } from 'react'
// import { books } from '../../data/books'
import { Link } from 'react-router-dom'
import { createBook, getBooks } from '../../api/books'
import { books } from '../../data/books'

const bookFirst = {
  title: "Angel",
  year: 2020,
  author_id: 1
};


const BooksList: React.FC<{ categoryTitle: string }> = ( ) => {

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const [booksList, setBooksList] = React.useState()
  // const {valueInput} = React.useContext(SearchContext)
  // const debouncedValue = useDebounce( {valueSearch: valueInput, time: 400} )
  // const normalizeSearch = debouncedValue.trim().toLowerCase()

  useEffect(() => {
    createBook(bookFirst).then(res => {
      console.log(res)
    }).catch(err => {
      console.log(err)
    })
    
    getBooks().then(res => {
      setBooksList(res)
    })

  }, [])
  console.log(booksList)

  // React.useEffect(() => {
  //   const filteredBooks = books.filter( book => {
  //     const booksByCategory = categoryTitle === "all-books" ? books : books.filter(b => b.category === categoryTitle)
  //     const booksBySearch = 
  //     book.title.toLowerCase().includes(normalizeSearch) ||
  //     book.author.toLowerCase().includes(normalizeSearch) ||
  //     book.year.toString().includes(normalizeSearch)
  //     return booksByCategory && booksBySearch
  //     }
  //   )
  //   setBooksList(filteredBooks)
  // }, [normalizeSearch, categoryTitle])
  
  return (
    <div>
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
