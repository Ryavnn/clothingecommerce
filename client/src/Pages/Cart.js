import React,{useContext} from "react";
import data from "../data";
import { shopContext } from "../context";
import CartItems from "../components/CartItem";


function Cart(){
  const {cartItems} = useContext(shopContext);

  return(
    <div className="cart">
      <div>
        <h1>Your cart Items</h1>
      </div>
      <div className="cart-items">
        {
          data.map((item) =>{
            if (cartItems[item.id] !== 0 ){
              return(<CartItems  data={item}/>)
            }else{
              console.log("not in the cart");
            }
          })
        }
      </div>
    </div>
  )
}

export default Cart