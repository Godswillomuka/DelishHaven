from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with backend

# Sample restaurants data
restaurants = [
    {"id": 1, "name": "Pizza Palace", "image": "https://source.unsplash.com/200x150/?pizza"},
    {"id": 2, "name": "Burger Bliss", "image": "https://source.unsplash.com/200x150/?burger"},
    {"id": 3, "name": "Sushi Spot", "image": "https://source.unsplash.com/200x150/?sushi"}
]

@app.route("/restaurants", methods=["GET"])
def get_restaurants():
    return jsonify(restaurants)

if __name__ == "__main__":
    app.run(debug=True)
