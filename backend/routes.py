from flask import Blueprint, request, jsonify
from models import db, User, Food, Order

api = Blueprint("api", __name__)

# Register a new user
@api.route("/users", methods=["POST"])
def register_user():
    data = request.json
    new_user = User(name=data["name"], email=data["email"], password=data["password"], role=data["role"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"}), 201

# Get all food items
@api.route("/foods", methods=["GET"])
def get_foods():
    foods = Food.query.all()
    return jsonify([{"id": food.id, "name": food.name, "price": food.price} for food in foods])

# Place an order
@api.route("/orders", methods=["POST"])
def place_order():
    data = request.json
    new_order = Order(user_id=data["user_id"], food_id=data["food_id"])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order placed successfully!"}), 201
