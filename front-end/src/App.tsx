import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Layout from './components/layout'
import HomePage from './components/pages/homePage'
import LoginPage from './components/pages/loginPage'
import BookPage from './components/pages/bookPage'
import { SearchProvider } from './context/SearchContext'

function App() {

  return (
    <BrowserRouter>
    <SearchProvider>
    <Routes>
        <Route path="/" element={<Layout/>}>
          <Route index element={<HomePage/>}/>
          <Route path='category/:id' element={<HomePage/>}/>
          <Route path='book/:id' element={<BookPage/>}/>
        </Route>
        <Route path='/login' element={<LoginPage/>} />
    </Routes>
    </SearchProvider>
    </BrowserRouter>
  )
}

export default App
