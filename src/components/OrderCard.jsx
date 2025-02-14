const OrderCard = ({ order }) => {
    return (
      <div className="card" style={{ width: "18rem" }}>
        <div className="card-body">
          <h5 className="card-title">Order #{order.id}</h5>
          <p className="card-text">Total: ${order.total.toFixed(2)}</p>
          <p className="card-text">Status: {order.status}</p>
        </div>
      </div>
    );
  };
  
  export default OrderCard;