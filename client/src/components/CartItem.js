import React from "react";

function CartItems(props) {
  const { id, productName, price, productImage } = props.data;

  return (
    <div className="cart-items" key={id}>
      <img src={productImage} alt="" />
      <div className="descriptiom">
        <h4>{productName}</h4>
        <p>Stylish cafe chair</p>
      </div>
      <span className="price">{price}</span>
    </div>
  );
}
export default CartItems;
