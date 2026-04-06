import { Link } from "react-router-dom";
import s from "./index.module.css";
import React from "react";
import Search from "../../ui/search";


const Header: React.FC = () => {

  const [theme, setTheme]= React.useState<boolean>(false)

  const changeTheme = () => {
    setTheme(prev => !prev)
  }

return (
    <header className={s.header}>
      <div className={s.logoBlock}  >
        <Link to='/'><span className={s.logo}>📚 Library</span></Link>
        <span className={s.quote}> Книги - це ...</span>
      </div>
      <Search/>

      <div className={s.actions}>
        <button onClick={changeTheme} className={s.themeBtn}>
          {theme ? "🌙" : "☀️"}
        </button>

        <button className={s.loginBtn}>
          <Link to='/authPage'> Login</Link>
        </button>
      </div>
    </header>
  );
};

export default Header;
