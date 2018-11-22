from flask import Blueprint, render_template, redirect, url_for, flash
from fantaso.bp_shop.models import Product

shop = Blueprint(
    'shop',
    __name__,
    template_folder='templates',
    static_folder='static',
)


##################
# index
##################
@shop.route('/', methods=['GET'])
def index():
    db_products = Product.query.all()
    products = []
    for product in db_products:
        print(product)
        if product.images.first():
            image = product.images.first().image
            products.append({'name': product.name, 'price': product.price, 'id': product.id, 'image': image})
    for product in products:
        print(product)
        print()
        print(product['name'])



    return render_template('bp_shop/index.html', products = products)

##################
# search
##################
@shop.route('/search', methods=['GET'])
def search():

    return render_template('bp_shop/search.html')

##################
# product
##################
@shop.route('/product/<id>', methods=['GET'])
def product(id):
    product = Product.query.filter_by(id = id).first()
    images = product.images.all()
    for image in images:
        image = image
    print(images)
    return render_template('bp_shop/product.html', product = product, images=images)

##################
# cart
##################
@shop.route('/cart', methods=['GET'])
def cart():
    return render_template('bp_shop/cart.html')

##################
# checkout
##################
@shop.route('/checkout', methods=['GET'])
def checkout():
    return render_template('bp_shop/checkout.html')
