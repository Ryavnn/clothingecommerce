<<<<<<< HEAD
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import timedelta
from sqlalchemy_serializer import SerializerMixin

=======
# models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates
from sqlalchemy.orm import relationship
>>>>>>> c1956225c43407abd84813f4f93d2b5fd7f0b7ca

db = SQLAlchemy()

<<<<<<< HEAD
def create_app():
    # Create the Flask app
    app = Flask(__name__)

    # Configure the app
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "wsddf542455r5rdd55d579j8f6f8yfrd57tru"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

    # Initialize SQLAlchemy with the app
    db.init_app(app)
    migrate.init_app(app, db)

    return app, db


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    phone = db.Column(db.String(14), unique=True)
    password = db.Column(db.String(450), nullable=False)
    address = db.Column(db.String(70), nullable=False)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
    #carts = db.relationship('Cart', back_populates='customer')
    
    #profile = db.relationship('Profile', back_populates='customer', uselist=False)

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    #customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), unique=True)
    
    #customer = db.relationship('Customer', back_populates='profile', uselist=False)
=======
# Association Table for many-to-many relationship between Product and Order
product_order_association = db.Table(
    'product_order_association',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'))
)

cart_product_association = db.Table(
    'cart_product_association',
    db.Column('cart_id', db.Integer, db.ForeignKey('carts.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'))
)

class TokenBlocklist(db.Model):
    __tablename__ = 'token_blocklist'

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f"<TokenBlocklist {self.id} {self.token}>"

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text)
    avatar_url = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)

    user = db.relationship("User", back_populates="profile")
    customer_reviews = db.relationship("Review", back_populates="user_profile", lazy=True, cascade="all, delete-orphan", single_parent=True)
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    full_name = db.Column(db.String(100))  # New attribute

    profile = db.relationship("UserProfile", back_populates="user", uselist=False)
>>>>>>> c1956225c43407abd84813f4f93d2b5fd7f0b7ca

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
<<<<<<< HEAD
    #products = db.relationship('Product', back_populates='category')


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(85), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    imageUrl = db.Column(db.Text, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
    #category = db.relationship('Category', back_populates='products')


class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
    quantity = db.Column(db.Integer, nullable=False, default=1)
    total_price = db.Column(db.Float, nullable=False)
    delivery_address = db.Column(db.String(100))
    #customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    #customer = db.relationship('Customer', back_populates='carts')
=======
    products = db.relationship('Product', back_populates='category')

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    imageUrl = db.Column(db.String(255))
    size = db.Column(db.Integer)  # Added size attribute

    category = db.relationship("Category", back_populates="products")
    orders = db.relationship("Order", secondary=product_order_association, back_populates="products")
    reviews = db.relationship("Review", back_populates="product")
    carts = db.relationship('Cart', secondary=cart_product_association, back_populates='products')
    reviews_product = db.relationship("Review", back_populates="product", overlaps="reviews")

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    password_hash = db.Column(db.String(128))

    created_at = db.Column(db.DateTime, default=db.func.now())

    carts = db.relationship('Cart', back_populates='customer')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError('Invalid email address')
        return email
>>>>>>> c1956225c43407abd84813f4f93d2b5fd7f0b7ca

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    orderdate = db.Column(db.DateTime, server_default=db.func.now())
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
<<<<<<< HEAD
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
    customer_id = db.Column(db.Integer(), db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer(), db.ForeignKey('products.id'))
    #customer = db.relationship("Customer", backref=db.backref('orders', lazy=True))
    #product = db.relationship("Product", backref=db.backref('orders', lazy=True))
=======
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
>>>>>>> c1956225c43407abd84813f4f93d2b5fd7f0b7ca

    products = db.relationship("Product", secondary=product_order_association, back_populates="orders")
    customer = db.relationship("Customer", backref=db.backref('orders', lazy=True))

    def __repr__(self):
        return f"<Order {self.id} - {self.customer.name} - {self.product.name}>"

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
<<<<<<< HEAD
    date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    #customer = db.relationship("Customer", backref="customer_reviews", lazy=True, cascade="all, delete-orphan", single_parent=True)
    #product = db.relationship("Product", backref="reviews_product", lazy=True, cascade="all, delete-orphan", single_parent=True)

# Define the many-to-many association table
# cart_product_association = db.Table(
#     'cart_product_association',
#     db.Column('cart_id', db.Integer, db.ForeignKey('carts.id')),
#     db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
#     db.UniqueConstraint('cart_id', 'product_id', name='uq_cart_product')
# )
=======
    date = db.Column(db.DateTime, default=datetime.now())
    user_profile_id = db.Column(db.Integer, db.ForeignKey('user_profiles.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    user_profile = db.relationship("UserProfile", back_populates="customer_reviews", lazy=True, cascade="all, delete-orphan", single_parent=True)
    product = db.relationship("Product", back_populates="reviews")

class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    quantity = db.Column(db.Integer, nullable=False, default=1)
    total_price = db.Column(db.Float, nullable=False)
    delivery_address = db.Column(db.String(100))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    customer = db.relationship('Customer', back_populates='carts')
    products = db.relationship('Product', secondary=cart_product_association, back_populates='carts')


>>>>>>> c1956225c43407abd84813f4f93d2b5fd7f0b7ca
