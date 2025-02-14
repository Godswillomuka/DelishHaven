from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from extensions import db, bcrypt
from models import User, Food, Order

routes = Blueprint("routes", __name__)

##User authentication

@routes.route("/users", methods=["POST"])
def register_user():
    data = request.json
    if not all(key in data for key in ["name", "email", "password", "confirm_password", "role"]):
        return jsonify({"error": "Missing required fields"}), 400

    if data["password"] != data["confirm_password"]:
        return jsonify({"error": "Passwords do not match"}), 400

    existing_user = User.query.filter_by(email=data["email"]).first()
    if existing_user:
        return jsonify({"error": "Email already registered"}), 400

    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

    new_user = User(name=data["name"], email=data["email"], password=hashed_password, role=data["role"])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully!", "user_id": new_user.id}), 201

@routes.route("/login", methods=["POST"])
def login():
    data = request.json
    if not all(key in data for key in ["email", "password"]):
        return jsonify({"error": "Missing email or password"}), 400

    user = User.query.filter_by(email=data["email"]).first()
    if not user or not bcrypt.check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity={"user_id": user.id, "role": user.role})

    return jsonify({
        "message": "Login successful!",
        "access_token": access_token,
        "user_id": user.id,
        "role": user.role
    }), 200

@routes.route("/users", methods=["GET"])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

##Food management

@routes.route("/foods", methods=["POST"])
@jwt_required()
def add_food():
    data = request.json
    if not all(key in data for key in ["name", "price", "description", "image_url"]):
        return jsonify({"error": "Missing required fields"}), 400

    new_food = Food(
        name=data["name"],
        price=data["price"],
        description=data["description"],
        image_url=data["image_url"]
    )
    db.session.add(new_food)
    db.session.commit()

    return jsonify({"message": "Food item added successfully!", "food_id": new_food.id}), 201

@routes.route("/foods", methods=["GET"])
def get_all_foods():
    foods = Food.query.all()
    return jsonify([food.to_dict() for food in foods]), 200

@routes.route("/foods/<int:food_id>", methods=["GET"])
def get_food_by_id(food_id):
    food = Food.query.get(food_id)
    if not food:
        return jsonify({"error": "Food not found"}), 404
    return jsonify(food.to_dict()), 200

@routes.route("/foods/<int:food_id>", methods=["PUT"])
@jwt_required()
def update_food(food_id):
    food = Food.query.get(food_id)
    if not food:
        return jsonify({"error": "Food not found"}), 404

    data = request.json
    food.name = data.get("name", food.name)
    food.price = data.get("price", food.price)
    food.description = data.get("description", food.description)
    food.image_url = data.get("image_url", food.image_url)

    db.session.commit()
    return jsonify({"message": "Food updated successfully!"}), 200

@routes.route("/foods/<int:food_id>", methods=["DELETE"])
@jwt_required()
def delete_food(food_id):
    food = Food.query.get(food_id)
    if not food:
        return jsonify({"error": "Food not found"}), 404

    db.session.delete(food)
    db.session.commit()
    return jsonify({"message": "Food deleted successfully!"}), 200

##Order management

@routes.route("/orders", methods=["POST"])
@jwt_required()
def place_order():
    data = request.json
    user_id = get_jwt_identity()["user_id"]
    
    if not all(key in data for key in ["total_price"]):
        return jsonify({"error": "Missing required fields"}), 400

    new_order = Order(user_id=user_id, total_price=data["total_price"])
    db.session.add(new_order)
    db.session.commit()

    return jsonify({"message": "Order placed successfully!", "order_id": new_order.id}), 201

@routes.route("/orders", methods=["GET"])
@jwt_required()
def get_orders():
    user_id = get_jwt_identity()["user_id"]
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify([order.to_dict() for order in orders]), 200

@routes.route("/orders/<int:order_id>", methods=["DELETE"])
@jwt_required()
def cancel_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order canceled successfully!"}), 200
