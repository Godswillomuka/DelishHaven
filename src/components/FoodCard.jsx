const FoodCard = ({ food }) => {
    return (
      <div className="card" style={{ width: "18rem" }}>
        <img src={food.image} className="card-img-top" alt={food.name} />
        <div className="card-body">
          <h5 className="card-title">{food.name}</h5>
          <p className="card-text">${food.price.toFixed(2)}</p>
          <button className="btn btn-primary">Order Now</button>
        </div>
      </div>
    );
  };
  
  export default FoodCard;