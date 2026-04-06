import React from 'react'
import BooksList from '../../booksList'
import { useParams } from 'react-router-dom'
import { categoryBooks } from '../../../data/categoriesBooks'

const HomePage: React.FC = () => {
  const id = useParams<{id?: string}>()

  const categoryTitle = categoryBooks.find(category => category.id === id.id)?.name ?? 'Всі книги'
  return (
    <div>
      <h2>{categoryTitle}</h2>
      <BooksList categoryTitle={categoryTitle} />
    </div>
  )
}

export default HomePage
