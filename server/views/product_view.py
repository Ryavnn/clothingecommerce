from flask import Blueprint,jsonify,request
from flask_jwt_extended import jwt_required

from models import Product,db,Review


products_bp=Blueprint('/products',__name__)

def get_review(id):
    reviews=Review.query.filter_by(id=id).all()
    
    if reviews:
        review_list=[]
        
        for review in reviews:
            review_list.append({
                'id':review.id,
                'comment':review.comment,
                'customer_id':review.customer_id,
                'product_id':review.product_id
            })
        return jsonify({'reviews':review_list})
    else:
        return "No Review Found"

@products_bp.route('/products', methods=['GET'])
def get_products():
    """Returns a list of all products"""
    products=Product.query.all()
    if products:
        products_list=[]
        
        for product in products:
            products_list.append(
                {
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    'description':product.description,
                    #'category':product.category,
                    'size':product.size,
                    'image_url':product.imageUrl,
                    #'reviews':[get_review(product.id)]
                }
            )
        return {'products':products_list},200
    else:
        return {'message':'No product found 😞'}
    
@products_bp.route("/products/<int:id>")
def get_one_product(id):
    """ Returns details about one specific product by its id """
    product=Product.query.filter_by(id=id).first()
    if product:
        return jsonify({
            'id':product.id,
            'name':product.name,
            'price':product.price,
            'description':product.description,
            'size':product.size,
            'category':product.category,
            'imageUrl':product.imageUrl
        })
    else:
        return jsonify({'message':'Product does not exist❗'})
    
# @auth.login_required

@products_bp.route('/add-product', methods=['POST'])
# @jwt_required
def add_a_product():
    data = request.get_json()

    if data and all(key in data for key in ['name', 'price', 'description', 'category', 'size', 'imageUrl']):
        new_product = Product(
            name=data['name'],
            price=data['price'],
            description=data['description'],
            category=data['category'],
            size=data['size'],
            imageUrl=data['imageUrl']
        )

        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully😉'})
    else:
        return jsonify({'error': 'Enter all product information❗'}), 400



@products_bp.route('/products/<int:id>',methods=["PUT",'DELETE','PATCH'])
# @jwt_required


def modify_product(id):
    product= Product.query.filter_by(id=id).first()
    
    if product:
        
            if request.method == 'DELETE':
                db.session.delete(product)
                db.session.commit()
                
                return jsonify({
                    'message':'User has been deleted!!'
                })
                
            elif request.method == 'PATCH':
                data=request.form
                
                product.name=data.get('name',product.name)
                product.price = data.get('price',product.price)
                product.description=data.get('description',product.description)
                product.category=data.get('category',product.category)
                product.size=data.get('size',product.size)
                product.imageUrl=data.get('imageUrl',product.imageUrl)
                
                db.session.commit()
                
                return jsonify({"message":"The product has been updated!"}),201
            
            
    else:  
        return jsonify({
            'message':'product not found'
    })
        
# Fetch all products by category
@products_bp.route('/products/<string:category>', methods=['GET'])
def get_products_by_category(category):
    products = Product.query.filter_by(category=category).all()

    if products:
        products_list = []

        for product in products:
            products_list.append(
                {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'description': product.description,
                    'category': product.category,
                    'size': product.size,
                    'image_url': product.imageUrl,
                    'reviews': [get_review(product.id)]
                }
            )

        return {'products': products_list}
    else:
        return jsonify({"error": f"No products found for the category: {category}"}), 404
