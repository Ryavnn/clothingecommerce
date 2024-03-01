import React, { useContext } from "react";
import { shopContext } from "../context";
import Navbar from "../layout/Navbar";
import "../layout/"

function CartItems(props) {
  const { id, productName, price, productImage } = props.data;
  const { removeFromCart } = useContext(shopContext);

  return (
    <>
      <Navbar />
      <div className="cart-items" key={id}>
        <img src={productImage} alt="" />
        <div className="descriptiom">
          <h4>{productName}</h4>
          <p>Stylish cafe chair</p>
        </div>
        <span className="price">{price}</span>
        <button className="add-cart" onClick={() => removeFromCart(id)}>
          Remove from cart
        </button>
      </div>
    </>
  );
}
export default CartItems;
