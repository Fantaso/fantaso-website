from flask import Blueprint, render_template, redirect, url_for, flash


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
    return render_template('bp_shop/index.html')

##################
# search
##################
@shop.route('/search', methods=['GET'])
def search():
    return render_template('bp_shop/search.html')

##################
# product
##################
@shop.route('/product', methods=['GET'])
def product():
    return render_template('bp_shop/product.html')

##################
# cart
##################
@shop.route('/cart', methods=['GET'])
def cart():
    return render_template('bp_shop/cart.html')

##################
# chechout
##################
@shop.route('/chechout', methods=['GET'])
def chechout():
    return render_template('bp_shop/chechout.html')
