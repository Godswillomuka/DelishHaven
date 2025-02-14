import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import FoodCard from "./components/FoodCard";
import OrderCard from "./components/OrderCard";
import PrivateRoute from "./components/PrivateRoute";
import Home from "./pages/Home";
import Menu from "./pages/Menu";
import Orders from "./pages/Orders";
import Login from "./pages/Login";
import Register from "./pages/Register";
import NotFound from "./pages/NotFound";
import { CartProvider } from "./context/CartContext";
import { AuthProvider } from "./context/AuthContext";
import { OrderProvider } from "./context/OrderContext"; // 🔹 ADDED MISSING CONTEXT FILE
import "./App.css";

function App() {
  return (
    <AuthProvider>
      <CartProvider>
        <OrderProvider> {/* ✅ Now wrapping with OrderProvider too! */}
          <Router>
            <div className="app">
              <Navbar />
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/menu" element={<Menu />} />
                <Route path="/orders" element={<PrivateRoute><Orders /></PrivateRoute>} />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="*" element={<NotFound />} />
              </Routes>
              <div className="food-cards">
                <FoodCard />
                <OrderCard />
              </div>
              <Footer />
            </div>
          </Router>
        </OrderProvider>
      </CartProvider>
    </AuthProvider>
  );
}

export default App;
