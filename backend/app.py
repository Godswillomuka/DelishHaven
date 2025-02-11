from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from extensions import db, jwt, bcrypt  # ✅ Import from extensions.py
from routes import routes  # ✅ Import AFTER initializing extensions
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
jwt.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# ✅ Register Blueprints AFTER app initialization
app.register_blueprint(routes, url_prefix="/api")

@app.route("/")
def home():
    return jsonify({"message": "Welcome to DelishHaven API"})

# Handle 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
