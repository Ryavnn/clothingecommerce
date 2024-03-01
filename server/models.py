from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import timedelta
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "wsddf542455r5rdd55d579j8f6f8yfrd57tru"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

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
    carts = db.relationship('Cart', back_populates='customer')
    
    profile = db.relationship('Profile', back_populates='customer', uselist=False)

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), unique=True, name='fk_profile_customer')

    customer = db.relationship('Customer', back_populates='profile', uselist=False)

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship('Product', back_populates='category', lazy='dynamic')

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
    category = db.relationship('Category', back_populates='products')

class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
    quantity = db.Column(db.Integer, nullable=False, default=1)
    total_price = db.Column(db.Float, nullable=False)
    delivery_address = db.Column(db.String(100))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    customer = db.relationship('Customer', back_populates='carts')

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    orderdate = db.Column(db.DateTime(), server_default=db.func.now())
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
    customer_id = db.Column(db.Integer(), db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer(), db.ForeignKey('products.id'))
    customer = db.relationship("Customer", backref=db.backref('orders', lazy=True))
    product = db.relationship("Product", backref=db.backref('orders', lazy=True))

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    customer = db.relationship("Customer", backref="customer_reviews", lazy=True, cascade="all, delete-orphan", single_parent=True)
    product = db.relationship("Product", backref="reviews_product", lazy=True, cascade="all, delete-orphan", single_parent=True)

cart_product_association = db.Table(
    'cart_product_association',
    db.Column('cart_id', db.Integer, db.ForeignKey('carts.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
    db.UniqueConstraint('cart_id', 'product_id', name='uq_cart_product')
)




# # Import necessary modules
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from datetime import timedelta
# from sqlalchemy_serializer import SerializerMixin


# db = SQLAlchemy()
# migrate = Migrate()

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
#     migrate.init_app(app, db)

#     return app, db


# class Customer(db.Model):
#     __tablename__ = 'customers'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(70), unique=True, nullable=False)
#     phone = db.Column(db.String(14), unique=True)
#     password = db.Column(db.String(450), nullable=False)
#     address = db.Column(db.String(70), nullable=False)
#     created_at = db.Column(db.DateTime(), server_default=db.func.now())
#     updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
#     carts = db.relationship('Cart', back_populates='customer')
    
#     profile = db.relationship('Profile', back_populates='customer', uselist=False)

# class Profile(db.Model):
#     __tablename__ = 'profiles'
#     id = db.Column(db.Integer, primary_key=True)
#     bio = db.Column(db.Text)
#     image_url = db.Column(db.String(255))
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), unique=True, name='fk_profile_customer')

#     customer = db.relationship('Customer', back_populates='profile', uselist=False)


# class Category(db.Model):
#     __tablename__ = 'categories'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True, nullable=False)
#     products = db.relationship('Product', back_populates='category')


# class Product(db.Model):
#     __tablename__ = 'products'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(85), nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
#     imageUrl = db.Column(db.Text, nullable=False)
#     size = db.Column(db.Integer, nullable=False)
#     created_at = db.Column(db.DateTime(), server_default=db.func.now())
#     updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
#     category = db.relationship('Category', back_populates='products')
    
#     def __init__(self, name, description, price, category_id, imageUrl, size):
#         self.name = name
#         self.description = description
#         self.price = price
#         self.category_id = category_id
#         self.imageUrl = imageUrl
#         self.size = size


# class Cart(db.Model):
#     __tablename__ = 'carts'
#     id = db.Column(db.Integer, primary_key=True)
#     created_at = db.Column(db.DateTime(), server_default=db.func.now())
#     updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
#     quantity = db.Column(db.Integer, nullable=False, default=1)
#     total_price = db.Column(db.Float, nullable=False)
#     delivery_address = db.Column(db.String(100))
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
#     customer = db.relationship('Customer', back_populates='carts')

# class Order(db.Model, SerializerMixin):
#     __tablename__ = 'orders'
#     id = db.Column(db.Integer, primary_key=True)
#     orderdate = db.Column(db.DateTime(), server_default=db.func.now())
#     price = db.Column(db.Float, nullable=False)
#     status = db.Column(db.String(50), nullable=False)
#     updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
#     customer_id = db.Column(db.Integer(), db.ForeignKey('customers.id'))
#     product_id = db.Column(db.Integer(), db.ForeignKey('products.id'))
#     customer = db.relationship("Customer", backref=db.backref('orders', lazy=True))
#     product = db.relationship("Product", backref=db.backref('orders', lazy=True))


# class Review(db.Model):
#     __tablename__ = 'reviews'
#     id = db.Column(db.Integer, primary_key=True)
#     rating = db.Column(db.Integer, nullable=False)
#     comment = db.Column(db.Text, nullable=False)
#     date = db.Column(db.DateTime, nullable=False)
#     created_at = db.Column(db.DateTime(), server_default=db.func.now())
#     updated_at = db.Column(db.DateTime(), onupdate=db.func.now())
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
#     customer = db.relationship("Customer", backref="customer_reviews", lazy=True, cascade="all, delete-orphan", single_parent=True)
#     product = db.relationship("Product", backref="reviews_product", lazy=True, cascade="all, delete-orphan", single_parent=True)


# cart_product_association = db.Table(
#     'cart_product_association',
#     db.Column('cart_id', db.Integer, db.ForeignKey('carts.id')),
#     db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
#     db.UniqueConstraint('cart_id', 'product_id', name='uq_cart_product')
# )
