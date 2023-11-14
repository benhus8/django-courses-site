import React from 'react';
import { Link } from 'react-router-dom';
import './navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-info justify-content-between">
      <div className="container">
        <ul className="navbar-nav">
          <li className="nav-item">
            <Link className="nav-link text-white fs-4" to="/shop">Shop</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link text-white fs-4" to="/my-courses">My Courses</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link text-white fs-4" to="/account">My account</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link text-white fs-4" to="/logout">Log out</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;