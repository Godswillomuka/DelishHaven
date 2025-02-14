import React, { createContext, useState } from "react";

const OrderContext = createContext();

export const OrderProvider = ({ children }) => {
  const [orders, setOrders] = useState([]);

  // Place an order
  const placeOrder = (cartItems, userId) => {
    const newOrder = { id: Date.now(), userId, items: cartItems, status: "pending" };
    setOrders((prevOrders) => [...prevOrders, newOrder]);
  };

  return (
    <OrderContext.Provider value={{ orders, placeOrder }}>
      {children}
    </OrderContext.Provider>
  );
};

export default OrderContext;
