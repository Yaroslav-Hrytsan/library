import type { BookType } from '../type/bookType';
import baseURL from "./baseAPI";


export async function getBooks() {
  try {
    const response = await baseURL.get("/books/");
    return response.data;
  } catch (error) {
    console.error('Error fetching books:', error);
    throw error;
  }
};

export async function createBook(book: BookType) {
  try {
    const response = await baseURL.post("/books/", book);
    return response.data;
  } catch (error) {
    console.error('Error creating book:', error);
    throw error;
  }
}

export async function updateBook(book: BookType) {
  try {
    const response = await baseURL.put(`/books/${book.id}`, book);
    return response.data;
  } catch (error) {
    console.error('Error updating book:', error);
    throw error;
  }
}

export async function deleteBook(id: number) {
  try {
    const response = await baseURL.delete(`/books/${id}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting book:', error);
    throw error;
  }
}