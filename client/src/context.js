import React, { createContext, useState } from "react";
import data from "./data";
export const shopContext = createContext(null)
function getDefaultCart (){
    let cart = {}
    for (let i=1; i< data.length + 1; i++){
      cart[i] = 0  
    }
    return cart
 }
function ContextProvider(props){
    const [cartItems, setCartItems] = useState(getDefaultCart())
    function addToCart(itemId){
        setCartItems((prev) => ({...prev, [itemId]: prev[itemId] + 1}))
    }
    function removeFromCart(itemId){
        setCartItems((prev) => ({...prev, [itemId]: prev[itemId] - 1}))
 
    }
    const contextValue = {cartItems, addToCart, removeFromCart}
    console.log(cartItems)
    return (<shopContext.Provider value={contextValue}>{props.children}</shopContext.Provider>)
}

export default ContextProvider 