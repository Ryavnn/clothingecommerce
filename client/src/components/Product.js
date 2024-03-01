import React, { useContext } from "react";
import { shopContext } from "../context";

function Product(props){
    const {id, productName, price, productImage} = props.data
    const {addToCart} = useContext(shopContext);
    return(
        <div className="product">
        <img src={productImage} alt="" />
        <h4>{productName}</h4>
        <p>Stylish cafe chair</p>
        <span className="price">{price}</span>
        <button className="add-cart" onClick={()=> addToCart(id)}>Add to Cart</button>
      </div>

    )
}
export default Product