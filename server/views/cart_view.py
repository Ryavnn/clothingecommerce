from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Product, Cart, db

cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/add-to-cart/<int:product_id>', methods=['POST'])
@jwt_required()
def add_to_cart(product_id):
    product = Product.query.get(product_id)

    if product:
        customer_id = get_current_user_id()

        cart = Cart.query.filter_by(customer_id=customer_id).first()

        if not cart:
            cart = Cart(customer_id=customer_id)

        cart.products.append(product)
        cart.total_price += product.price

        db.session.add(cart)
        db.session.commit()

        return jsonify({'message': 'Product added to the cart successfully'}), 200
    else:
        return jsonify({'error': 'Product not found'}), 404

@cart_bp.route('/view-cart', methods=['GET'])
@jwt_required()
def view_cart():
    customer_id = get_current_user_id()

    cart = Cart.query.filter_by(customer_id=customer_id).first()

    if cart:
        cart_info = {
            'cart_id': cart.id,
            'total_price': cart.total_price,
            'products': [
                {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'description': product.description,
                    'category': product.category,
                    'size': product.size,
                    'image_url': product.image_url,
                } for product in cart.products
            ]
        }

        return jsonify(cart_info), 200
    else:
        return jsonify({'message': 'Cart is empty'}), 200

@cart_bp.route('/remove-from-cart/<int:product_id>', methods=['DELETE'])
@jwt_required()
def remove_from_cart(product_id):
    customer_id = get_current_user_id()

    cart = Cart.query.filter_by(customer_id=customer_id).first()

    if cart:
        product = Product.query.get(product_id)

        if product in cart.products:
            cart.products.remove(product)
            cart.total_price -= product.price

            db.session.commit()

            return jsonify({'message': 'Product removed from the cart successfully'}), 200
        else:
            return jsonify({'error': 'Product not found in the cart'}), 404
    else:
        return jsonify({'error': 'Cart not found'}), 404

@cart_bp.route('/checkout', methods=['POST'])
@jwt_required()
def checkout():
    customer_id = get_current_user_id()

    cart = Cart.query.filter_by(customer_id=customer_id).first()

    if cart:
        cart.products = []
        cart.total_price = 0

        db.session.commit()

        return jsonify({'message': 'Checkout successful'}), 204
    else:
        return jsonify({'error': 'Cart not found'}), 404

def get_current_user_id():
    return get_jwt_identity()  # Assuming you're using Flask JWT Extended for authentication
