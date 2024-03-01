
import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";
const Navbar = () => {
  const { logout, email } = useContext(AuthContext);
  const handleLogout = () => {
    logout();
  }
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light fixed-top" style={{ height: "60px", padding: "10px"}}>
      <div className="container-fluid">
        <div className="navbar-brand" >
          <img 
          src="https://api.logo.com/api/v2/images?logo=logo_29bd977c-eb97-4e63-a6b2-4579403a7a01&u=1708550256&width=500&height=400&fit=contain&margins=100&format=webp&quality=60" 
          alt="logo" 
          width="30" 
          height="30"
         />
        </div>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link className="nav-link active" aria-current="page" to="/">Home</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/products">Products</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/cart">Cart</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/category">Category</Link>
            </li>
            {  email !== null ?
             <li className="nav-item" onClick={()=>{
              handleLogout();
            }}>
              <button className="nav-link" style={{ color: "red"}}>Logout</button>
            </li> 
            :
            <li className="nav-item">
              <Link className="nav-link" to="/login">Login</Link>
            </li>
            }
            
          </ul>
          
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
