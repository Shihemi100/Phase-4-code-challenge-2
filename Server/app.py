from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .config import SQLALCHEMY_DATABASE_URI

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["JWT_SECRET_KEY"] = "your-secret-key"

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from server.controllers import guest_controller, episode_controller, appearance_controller, auth_controller
    app.register_blueprint(guest_controller.bp)
    app.register_blueprint(episode_controller.bp)
    app.register_blueprint(appearance_controller.bp)
    app.register_blueprint(auth_controller.bp)

    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
