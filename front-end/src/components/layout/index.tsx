import React from 'react'
import s from './index.module.css'
import Header from './header/index'
import { Outlet } from 'react-router-dom'
import Sidebar from './sidebar'

const Layout: React.FC = () => {
  return (
    <div className={s.wrapper}>
      <Header />
      <div className={s.content}>
        <Sidebar/>
        <main>
            <Outlet/>
        </main>
      </div>
    </div>
  )
}

export default Layout
