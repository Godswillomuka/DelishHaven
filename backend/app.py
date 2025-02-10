from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db  # Import db from models
from routes import api  # Import API routes

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///delishhaven.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database and migration
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

# Register Blueprints
app.register_blueprint(api, url_prefix="/api")

@app.route("/")
def home():
    return {"message": "Welcome to DelishHaven API"}

if __name__ == "__main__":
    app.run(debug=True)
