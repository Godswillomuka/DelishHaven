const API_URL = "https://your-api-url.com";

// Place Order
export const placeOrder = async (userId, cartItems) => {
  try {
    const response = await fetch(`${API_URL}/orders`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ userId, items: cartItems }),
    });
    return response.json();
  } catch (error) {
    console.error("Order Error:", error);
    return { error: "Failed to place order" };
  }
};

// Fetch Orders
export const fetchOrders = async (userId) => {
  try {
    const response = await fetch(`${API_URL}/orders?userId=${userId}`);
    return response.json();
  } catch (error) {
    console.error("Fetch Orders Error:", error);
    return { error: "Failed to fetch orders" };
  }
};
