import React from "react";
import Products from "src/pages/Products";
import Cart from "src/pages/Cart";
const ParentComponent = () => {
  const [cart, setCart] = React.useState([]);

  const addToCart = (productId) => {
    // Check if the product is already in the cart
    const existingProductIndex = cart.findIndex(item => item.id === productId);

    if (existingProductIndex !== -1) {
      // If the product is already in the cart, update the quantity
      const updatedCart = [...cart];
      updatedCart[existingProductIndex].quantity += 1;
      setCart(updatedCart);
    } else {
      // If the product is not in the cart, add it with quantity 1
      const productToAdd = { id: productId, quantity: 1 };
      setCart([...cart, productToAdd]);
    }
  };

  return (
    <div>
      {/* Pass addToCart and the cart state as props to the Products component */}
      <Products addToCart={addToCart} />
      {/* Pass the cart state as props to the Cart component */}
      <Cart cartItems={cart} />
    </div>
  );
};

export default ParentComponent;
