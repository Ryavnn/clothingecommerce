
// import React from "react";

// const Navbar = () => {
//   return (
//     <nav className="navbar navbar-expand-lg navbar-light bg-light fixed-top">
        
//       <div className="container-fluid">
//         <a className="navbar-brand" href="/">
//           <img src="https://api.logo.com/api/v2/images?logo=logo_29bd977c-eb97-4e63-a6b2-4579403a7a01&u=1708550256&width=500&height=400&fit=contain&margins=100&format=webp&quality=60" alt="Fenty wear logo"style={{ width: '100px', height: 'auto' }} />
//         </a>
//         <button
//           className="navbar-toggler"
//           type="button"
//           data-bs-toggle="collapse"
//           data-bs-target="#navbarSupportedContent"
//           aria-controls="navbarSupportedContent"
//           aria-expanded="false"
//           aria-label="Toggle navigation"
//         >
//           <span className="navbar-toggler-icon"></span>
//         </button>
//         <div className="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
//           <ul className="navbar-nav">
//             <li className="nav-item">
//               <a className="nav-link active" aria-current="page" href="/">
//                 Home
//               </a>
//             </li>
//             <li className="nav-item">
//               <a className="nav-link" href="/products">
//                 Products
//               </a>
//             </li>
//             <li className="nav-item">
//               <a className="nav-link" href="/cart">
//                 Cart
//               </a>
//             </li>
<<<<<<< HEAD
<<<<<<< HEAD
//             <li className="nav-item">
//               <a className="nav-link" href="/cartegory">
//                 cartegory
//               </a>
//             </li>
=======
>>>>>>> 01fc9cf (Logo added)
=======
//             <li className="nav-item">
//               <a className="nav-link" href="/category">
//                 Category
//               </a>
//             </li>
>>>>>>> 602a5ef (Authentication added)
//           </ul>
//           <form className="form-inline my-2 my-lg-0">
//             <input className="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" />
//             <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
//           </form>
//         </div>
//       </div>
//     </nav>
//   );
// };

// export default Navbar;

<<<<<<< HEAD
<<<<<<< HEAD
=======

import React from "react";
>>>>>>> 01fc9cf (Logo added)
=======
import React from "react";
import { Link } from "react-router-dom";

>>>>>>> 602a5ef (Authentication added)
const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light fixed-top">
      <div className="container-fluid">
<<<<<<< HEAD
        <div className="navbar-brand">
          <img src="https://api.logo.com/api/v2/images?logo=logo_29bd977c-eb97-4e63-a6b2-4579403a7a01&u=1708550256&width=500&height=400&fit=contain&margins=100&format=webp&quality=60" alt="logo" width="120" height="90"/>
        </div>
=======
        <a className="navbar-brand" href="/">
          <img src="https://api.logo.com/api/v2/images?logo=logo_29bd977c-eb97-4e63-a6b2-4579403a7a01&u=1708550256&width=500&height=400&fit=contain&margins=100&format=webp&quality=60" alt="Fenty wear logo" style={{ width: '100px', height: 'auto' }} />
        </a>
>>>>>>> 01fc9cf (Logo added)
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
            <li className="nav-item">
              <a className="nav-link" href="/cartegory">
                Category
              </a>
            </li>
          </ul>
          <form className="form-inline my-2 my-lg-0">
            <input className="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" />
            <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
