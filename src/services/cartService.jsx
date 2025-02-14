const API_URL = "https://your-api-url.com";

// Fetch Menu Items
export const fetchMenu = async () => {
  try {
    const response = await fetch(`${API_URL}/menu`);
    return response.json();
  } catch (error) {
    console.error("Fetch Menu Error:", error);
    return { error: "Failed to fetch menu" };
  }
};

// Add Item to Cart
export const addToCart = (cart, item) => {
  return [...cart, item]; // Adds item to cart (state-based)
};

// Remove Item from Cart
export const removeFromCart = (cart, itemId) => {
  return cart.filter((item) => item.id !== itemId);
};

// Clear Cart
export const clearCart = () => {
  return [];
};
