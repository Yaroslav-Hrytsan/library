import React from "react";
import { books } from "../../../data/books";
import { useParams } from "react-router-dom";

const BookPage: React.FC = () => {
  const { id } = useParams<{ id?: string }>();
  const book = books.find((book) => book.id === Number(id));

  return (
    <div>
      {book ? 
      ( <div>
        <div>{book.cover}</div>
        <div>
          <h2>{book.title} </h2>
          <div>{book.year}</div>
          <h3>{book.author}</h3>
          <div>{book.category}</div>
          <div>{book.description}</div>

        </div>
        
          

        </div>) 
      : (
        "Книгу не знайдено"
      )}
    </div>
  );
};

export default BookPage;
