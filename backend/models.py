from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False) 

    def __repr__(self):
        return f"<User {self.name}>"

class Food(db.Model):
    __tablename__ = "foods"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)  # Links to restaurant owner

    user = db.relationship("User", backref="foods")

    def __repr__(self):
        return f"<Food {self.name}>"

class Order(db.Model):
    __tablename__ = "orders"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey("foods.id"), nullable=False)
    status = db.Column(db.String(50), default="Pending")  # "Pending", "Delivered", "Cancelled"

    user = db.relationship("User", backref="orders")
    food = db.relationship("Food", backref="orders")

    def __repr__(self):
        return f"<Order {self.id} - {self.status}>"
