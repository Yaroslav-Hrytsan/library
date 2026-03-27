
import React from 'react'
import { Link } from 'react-router-dom'

const LoginPage: React.FC = () => {
  return (
    <div>
        <button>
          <Link to='/'>НАЗАД</Link>
        </button>
        Login page
    </div>
  )
}

export default LoginPage
