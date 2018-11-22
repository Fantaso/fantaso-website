from flask import Blueprint, render_template, redirect, url_for, flash
# from app
from fantaso import db # app or database
from fantaso import photos, photos_folder, photos_folder_rel_path, photos_folder_full_path # flask-uploads
# models and forms
from fantaso.bp_shop.models import Product, ProductImage
from fantaso.bp_admin.forms import AddProduct, AddImage
# extra
from os.path import join


bp_admin = Blueprint(
    'bp_admin',
    __name__,
    template_folder='templates',
    static_folder='static',
)


##################
# index
##################
@bp_admin.route('/', methods=['GET'])
def index():
    products = Product.query.all()
    total_products = 0
    out_of_stock = []
    for product in products:
        if product.stock == 0:
            out_of_stock.append({'product_id': product.id})

    out_of_stock = len(out_of_stock)
    total_products = len(products)

    return render_template('bp_admin/index.html', products = products, total_products = total_products, out_of_stock = out_of_stock)

##################
# add_product
##################
@bp_admin.route('/add-product', methods=['GET', 'POST'])
def add_product():
    form = AddProduct()

    if form.validate_on_submit():
        # if not form.image1.data == None: image_url1 = photos.url(photos.save(form.image1.data))
        # if not form.image2.data == None: image_url2 = photos.url(photos.save(form.image2.data))
        # if not form.image3.data == None: image_url3 = photos.url(photos.save(form.image3.data))
        # if not form.image4.data == None: image_url4 = photos.url(photos.save(form.image4.data))
        # if not form.image5.data == None: image_url5 = photos.url(photos.save(form.image5.data))
        # if not form.image6.data == None: image_url6 = photos.url(photos.save(form.image6.data))


        new_product = Product(  name=form.name.data,
                                price=form.price.data,
                                stock=form.stock.data,
                                description=form.description.data,
                                )

        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for('bp_admin.index'))

    return render_template('bp_admin/add-product.html', admin=True, form=form)

##################
# view_order
##################
@bp_admin.route('/add-image', methods=['GET', 'POST'])
def add_image():

    products = Product.query.all()
    form = AddImage()
    products_choices = []
    for product in products:
        products_choices.append(product)

    form.products_choices.choices = [ (product.id, product.name) for product in products_choices ]
    form.products_choices.choices.insert(0, (0 ,'Choose:'))

    if form.validate_on_submit():
        if not form.image.data == None:
            filename = photos.save(form.image.data)
            filename_url = join(photos_folder_full_path, photos_folder_rel_path, photos_folder, filename)

        new_image = ProductImage(image = filename, product_id = form.products_choices.data,
        )

        db.session.add(new_image)
        db.session.commit()
        return redirect(url_for('bp_admin.index'))
    return render_template('bp_admin/add-image.html', form = form)


##################
# view_order
##################
@bp_admin.route('/view-order', methods=['GET'])
def view_order():
    return render_template('bp_admin/view-order.html')
