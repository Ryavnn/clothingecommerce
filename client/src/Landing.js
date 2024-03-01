import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "./layout/Navbar";
import Footer from "./layout/Footer";
import "./Landing.css";


const Landing = () => {
  const [backgroundImages, setBackgroundImages] = useState([
    "https://img.freepik.com/free-photo/medium-shot-black-woman-running-small-business_23-2150171803.jpg?size=626&ext=jpg",

    "https://www.travelandleisure.com/thmb/aYdL-65LoBy8yHphhZEBxd3fvMc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/how-to-wear-sneakers-with-dress-DRESSSNEAK0918-b01f277ea03840d783928466b8cddcff.jpg",
    // Replace with your third image URL
  ]);

  const [currentBackgroundIndex, setCurrentBackgroundIndex] = useState(0);
  const navigate = useNavigate();

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentBackgroundIndex((prevIndex) =>
        prevIndex === backgroundImages.length - 1 ? 0 : prevIndex + 1
      );
    }, 5000); // Alternate interval set to 5 seconds

    return () => clearInterval(interval);
  }, [backgroundImages]);

  return (
    <>
      <Navbar />
      <div className="Landing">
        <div className="background-container">
          <img
            src={backgroundImages[currentBackgroundIndex]}
            alt={`Background ${currentBackgroundIndex + 1}`}
            className="background-image"
          />
        </div>
        <div className="text-container">
          <h1>Welcome to Our FentyWear Store</h1>
          <p>Discover a world of amazing products at your fingertips</p>
        </div>
      </div>
        <Footer />
    </>
  );
};

export default Landing;
