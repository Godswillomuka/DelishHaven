import React, { useEffect, useState } from "react";
import { Container, Row, Col } from "react-bootstrap";
import FoodCard from "../components/FoodCard";

const Menu = () => {
  const [foods, setFoods] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/foods")
      .then((res) => res.json())
      .then((data) => setFoods(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <Container className="mt-4">
      <h2 className="text-center mb-4">Menu</h2>
      <Row>
        {foods.map((food) => (
          <Col key={food.id} md={4} className="mb-3">
            <FoodCard food={food} />
          </Col>
        ))}
      </Row>
    </Container>
  );
};

export default Menu;
