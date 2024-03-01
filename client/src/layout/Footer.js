// import React from 'react';
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
// import { faFacebook, faTwitter, faInstagram } from '@fortawesome/free-brands-svg-icons';
// import '../App.css'; // Import your custom CSS file

// const Footer = () => {
//   return (
//     <footer className="custom-footer">
//       <div className="container text-center">
//         <div className="row">
//           <div className="col-md-4 mb-4">
//             <h4>Contact Us</h4>
//             <p>Email: info@fentywearke.com</p>
//             <p>Phone: +254711223344</p>
//           </div>
//           <div className="col-md-4 mb-4">
//             <h4>Follow Us</h4>
//             <div className="social-icons">
//               <a href="https://www.facebook.com/" target="_blank" rel="noopener noreferrer">
//                 <FontAwesomeIcon icon={faFacebook} size="2x" />
//               </a>
//               <a href="https://twitter.com/" target="_blank" rel="noopener noreferrer">
//                 <FontAwesomeIcon icon={faTwitter} size="2x" />
//               </a>
//               <a href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer">
//                 <FontAwesomeIcon icon={faInstagram} size="2x" />
//               </a>
//             </div>
//           </div>
//           <div className="col-md-4 mb-4">
//             <h4>Stay Updated</h4>
//             <p>Subscribe to our online platforms for the latest updates and promotions.</p>
//             <form>
//               <div className="input-group">
//                 <input type="email" className="form-control" placeholder="Your email" />
//                 <button type="submit" className="btn btn-outline-dark">
//                   Subscribe
//                 </button>
//               </div>
//             </form>
//           </div>
//         </div>
//       </div>
//       <div className="custom-footer-bottom">
//         <p className="mb-0" style={{ fontSize: '14px' }}>
//           © 2024 Your E-Commerce Beauty-Shop. All rights reserved.
//         </p>
//       </div>
//     </footer>
//   );
// };

// export default Footer;


import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFacebook, faTwitter, faInstagram } from '@fortawesome/free-brands-svg-icons';

const Footer = () => {
  return (
    <footer style={{ backgroundColor: '#f4f4f4', padding: '30px' }}>
      <div className="container text-center">
        <div className="row">
          <div className="col-md-4 mb-4">
            <h4>Contact Us</h4>
            <p>Email: info@fentywearke.com</p>
            <p>Phone: +254711223344</p>
          </div>
          <div className="col-md-4 mb-4">
            <h4>Follow Us</h4>
            <div className="social-icons">
              <a href="https://www.facebook.com/" target="_blank" rel="noopener noreferrer">
                <FontAwesomeIcon icon={faFacebook} size="2x" />
              </a>
              <a href="https://twitter.com/" target="_blank" rel="noopener noreferrer">
                <FontAwesomeIcon icon={faTwitter} size="2x" />
              </a>
              <a href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer">
                <FontAwesomeIcon icon={faInstagram} size="2x" />
              </a>
            </div>
          </div>
          <div className="col-md-4 mb-4">
            <h4>Stay Updated</h4>
            <p>Subscribe to our online platforms for the latest updates and promotions.</p>
            <form>
              <div className="input-group">
                <input type="email" className="form-control" placeholder="Your email" />
                <button type="submit" className="btn btn-outline-dark">
                  Subscribe
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <div style={{ backgroundColor: '#ddd', padding: '15px', textAlign: 'center' }}>
        <p style={{ margin: '0', fontSize: '14px' }}>
          © 2024 Your E-Commerce Beauty-Shop. All rights reserved.
        </p>
      </div>
    </footer>
  );
};

export default Footer;
