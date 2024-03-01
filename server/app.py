from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from datetime import timedelta
from flask_jwt_extended import JWTManager
from models import create_app
from views.product_view import products_bp
from views.order_view import order_bp
from views.review_view import review_bp
from views.cart_view import cart_bp
from views.customer_view import customer_bp
from views.categories_cart import categories_cart_bp


# Create the Flask app and db object
app, db = create_app()

# Initialize Migrate with the app and db
migrate = Migrate(app, db)

# Initialize CORS with the app
CORS(app)

# Initialize JWTManager with the app
jwt = JWTManager(app)

# Import and register your blueprints
app.register_blueprint(review_bp, url_prefix='/')
app.register_blueprint(order_bp, url_prefix='/')
app.register_blueprint(products_bp, url_prefix='/')
app.register_blueprint(cart_bp, url_prefix='/')
app.register_blueprint(customer_bp, url_prefix='/')
app.register_blueprint(categories_cart_bp, url_prefix="/")

# Run the app
if __name__ == '__main__':
    app.run(port=5000, debug=True)

# # app.py
# from flask import Flask
# from flask_migrate import Migrate
# from flask_cors import CORS
# from datetime import timedelta
# from flask_jwt_extended import JWTManager
# from models import db  # Import db from models.py
# from views.product_view import products_bp
# from views.order_view import order_bp
# from views.review_view import review_bp
# from views.cart_view import cart_bp
# from views.customer_view import customer_bp
# from views.categories_cart import categories_cart_bp

# def create_app():
#     # Create the Flask app
#     app = Flask(__name__)

#     # Configure the app
#     app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#     app.config["JWT_SECRET_KEY"] = "wsddf542455r5rdd55d579j8f6f8yfrd57tru"
#     app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

#     # Initialize SQLAlchemy with the app
#     db.init_app(app)
#     migrate = Migrate(app, db)

#     # Initialize CORS with the app
#     CORS(app)

#     # Initialize JWTManager with the app
#     jwt = JWTManager(app)

#     # Import and register your blueprints
#     app.register_blueprint(review_bp, url_prefix='/')
#     app.register_blueprint(order_bp, url_prefix='/')
#     app.register_blueprint(products_bp, url_prefix='/')
#     app.register_blueprint(cart_bp, url_prefix='/')
#     app.register_blueprint(customer_bp, url_prefix='/')
#     app.register_blueprint(categories_cart_bp, url_prefix="/")

#     return app

# if __name__ == '__main__':
#     app = create_app()
#     app.run(port=5000, debug=True)

