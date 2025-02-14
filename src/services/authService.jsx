const API_URL = "https://your-api-url.com"; // Replace with your backend URL

// User Signup
export const signup = async (userData) => {
  try {
    const response = await fetch(`${API_URL}/signup`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(userData),
    });
    return response.json();
  } catch (error) {
    console.error("Signup Error:", error);
    return { error: "Failed to sign up" };
  }
};

// User Login
export const login = async (credentials) => {
  try {
    const response = await fetch(`${API_URL}/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(credentials),
    });
    return response.json();
  } catch (error) {
    console.error("Login Error:", error);
    return { error: "Failed to log in" };
  }
};

// User Logout
export const logout = () => {
  localStorage.removeItem("user");
  localStorage.removeItem("token");
};
