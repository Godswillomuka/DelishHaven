import React from "react";
import { Link } from "react-router-dom";
import { Container, Button } from "react-bootstrap";

const Home = () => {
  return (
    <Container className="text-center mt-5">
      <h1>Welcome to Delish Haven</h1>
      <p>Order delicious meals from the comfort of your home!</p>
      <Link to="/menu">
        <Button variant="primary">View Menu</Button>
      </Link>
    </Container>
  );
};

export default Home;
