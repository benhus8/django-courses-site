import React from 'react';
import '../App.css';
import { Link } from 'react-router-dom';
const Navbar = () => {
  return (
    <nav className="navbar">
      <ul className="navbar-list">
        <li className="navbar-item"> <Link reloadDocument  to="/shop"> Sklep </Link> </li>
        <li className="navbar-item"><Link reloadDocument  to="/my-courses"> Moje kursy </Link></li>
        <li className="navbar-item"><Link reloadDocument  to="/account"> Moje konto </Link></li>
        <li className="navbar-item"><Link reloadDocument to="/logout"> Wyloguj się</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;