import React, { useEffect, useState } from "react";
import { Container, Row } from "react-bootstrap";
import OrderCard from "../components/OrderCard";

const Orders = () => {
  const [orders, setOrders] = useState([]);
  const token = localStorage.getItem("token");

  useEffect(() => {
    fetch("http://localhost:5000/api/orders", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((res) => res.json())
      .then((data) => setOrders(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <Container className="mt-4">
      <h2>My Orders</h2>
      <Row>
        {orders.map((order) => (
          <OrderCard key={order.id} order={order} />
        ))}
      </Row>
    </Container>
  );
};

export default Orders;
