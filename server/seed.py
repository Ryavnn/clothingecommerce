# Import necessary modules
from app import db
from models import Category, Product, Customer, Profile, Cart, Order, Review
from sqlalchemy import func

# Function to create sample data
def create_sample_data():
    try:
        # Print a message indicating that categories are being added
        print("Adding categories...")
        # Create a list of category names
        category_names = ['CASUAL WEAR', 'SPORTS WEAR', 'FORMAL WEAR', 'FOOT WEAR']
        # Create a dictionary to store categories
        categories = {}
        # Loop through each category name
        for category_name in category_names:
            # Query the database to check if the category already exists
            existing_category = Category.query.filter(func.lower(Category.name) == func.lower(category_name)).first()
            # If the category already exists, add it to the dictionary
            if existing_category:
                categories[category_name] = existing_category
            # If the category does not exist, create a new category and add it to the database and the dictionary
            else:
                new_category = Category(name=category_name)
                db.session.add(new_category)
                categories[category_name] = new_category
        # Commit the changes to the database
        db.session.commit()
        # Print a message indicating that categories were added successfully
        print("Categories added successfully!")

        # Print a message indicating that products are being added
        print("Adding products...")
        # Loop through each category name and category
        for category_name, category in categories.items():
            # If the category is CASUAL WEAR, create a list of products and add them to the database
            if category_name == 'CASUAL WEAR':
                products = [
                    Product(name='Red T-Shirt', description='A simple red t-shirt', price=1999, category_id=category.id, imageUrl='https://th.bing.com/th/id/OIP.7n5TOdEGuHQrmQA-DC88PQHaLW?w=736&h=1128&rs=1&pid=ImgDetMain', size=1),
                    Product(name='Blue Jeans', description='A pair of blue jeans', price=2999, category_id=category.id, imageUrl='https://th.bing.com/th/id/OIP.VLUh08_Gc30ObixQgf6lbQHaJ4?w=1080&h=1440&rs=1&pid=ImgDetMain', size=2)
                ]
            # If the category is FORMAL WEAR, create a list of products and add them to the database
            elif category_name == 'FORMAL WEAR':
                products = [
                    Product(name='Dress', description='Elegent dress for formal events', price=3999, category_id=category.id, imageUrl='https://th.bing.com/th/id/R.4fc853a0ba16699313a93391c7416f4b?rik=uHMVensdv7JncA&riu=http%3a%2f%2fdzasv7x7a867v.cloudfront.net%2fproduct_photos%2f46820830%2fQQ_E5_9B_BE_E7_89_8720161226102324_original.jpg&ehk=%2bRgXk1t0Bx%2baR%2fRwo%2b9e21H%2fcovKeGvnFMG8RmOAOSU%3d&risl=&pid=ImgRaw&r=0', size=6),
                    Product(name='Skirt', description='This skirt can be paired with any dark colored of your choice', price=2000, category_id=category.id, imageUrl='https://ae01.alicdn.com/kf/HTB117FxXIrrK1RjSspaq6AREXXav/Skirt-Women-Fashion-Solid-Flared-Retro-Casual-Knee-Length-Pleated-Midi-Office-Work-Skirt-Gonna-femminile.jpg', size=1),
                    Product(name='skirt', description='casual stylish skirt', price=1500, category_id=category.id, imageUrl='https://i.pinimg.com/originals/80/ab/12/80ab12f6767e629e444a17ab50fbffcb.png', size=6),
                    Product(name='Trouser', description='This trouser can be paired with any dark colored of your choice', price=2000, category_id=category.id, imageUrl='https://images2.drct2u.com/pdp_main_desktop_x2/products/lf/lf458/m01lf458500w.jpg', size=8)
                ]
            # If the category is not CASUAL WEAR or FORMAL WEAR, create an empty list of products
            else:
                products = []
            # Add the products to the database
            db.session.add_all(products)
            # Commit the changes to the database
            db.session.commit()
            # Print a message indicating that products for the category were added successfully
            print("Products for category '{}' added successfully".format(category_name))

        # Print a message indicating that profiles are being added
        print("Adding profiles...")
        # Create a list of customers
        customers = [
            Customer(name='Basil Itumbi', email='basilitumbi@example.com', phone='123456789', password='hashedpassword', address='1234 Main St'),
            Customer(name='Jane Doe', email='janedoe@example.com', phone='987654321', password='hashedpassword', address='5678 Elm St'),
            Customer(name='John Smith', email='johnsmith@example.com', phone='111223344', password='hashedpassword', address='789 Broadway St'),
            Customer(name='Alice Johnson', email='alicejohnson@example.com', phone='555666777', password='hashedpassword', address='456 Pine St')
        ]
        # Loop through each customer
        for customer in customers:
            # Add the customer to the database
            db.session.add(customer)
            # Commit the changes to the database
            db.session.commit()
            # Create a profile for the customer
            profile = Profile(bio='', image_url='', customer_id=customer.id)
            # Add the profile to the database
            db.session.add(profile)
            # Commit the changes to the database
            db.session.commit()
            # Print a message indicating that the profile was added successfully
            print("Profile for customer '{}' added successfully".format(customer.name))

        # Print a message indicating that carts are being added
        print("Adding carts...")
        # Create a list of carts
        carts = [
            Cart(customer=customers[0], total_price=49.98, delivery_address='1234 Main St'),
            Cart(customer=customers[1], total_price=29.99, delivery_address='5678 Elm St')
        ]
        # Loop through each cart
        for cart in carts:
            # Add the cart to the database
            db.session.add(cart)
            # Commit the changes
            db.session.commit()

    except Exception as e:
        # Rollback changes if an exception occurs
        db.session.rollback()
        # Print the error message
        print(f"Error: {str(e)}")
