import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import Landing from "./Landing";
import LoginForm from "./components/LoginForm";
import SignupForm from "./components/SignupForm";

import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

import Cart from "./Pages/Cart";
import Products from "./Pages/Products";
import Category from "./Pages/Category";
import ContextProvider from "./context";

function App() {
  return (
    <div className="App">
      <ContextProvider>
        <Router>
          <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/login" element={<LoginForm />} />
            <Route path="/signup" element={<SignupForm />} />
            <Route path="/products" element={<Products />} />
            <Route path="/category" element={<Category />} />
            <Route path="/cart" element={<Cart />} />
          </Routes>
        </Router>
      </ContextProvider>
    </div>
  );
}

export default App;
