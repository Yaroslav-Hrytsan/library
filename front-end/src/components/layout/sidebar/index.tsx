import React from "react";
import s from "./index.module.css";
import { categoryBooks } from "../../../data/categoriesBooks";
import { Link } from "react-router-dom";

const Sidebar: React.FC = () => {
  return (
    <div className={s.sidebar}>
      <ul>
        {categoryBooks.map((cat) => (
          <li key={cat.id}>
            <Link to={`/category/${cat.id}`}>{cat.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;
