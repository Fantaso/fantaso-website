from fantaso import db
from sqlalchemy.sql import func


class Product(db.Model):
    """All products available on the online store should be here"""
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Integer) # in cents
    stock = db.Column(db.Integer)
    description = db.Column(db.String(2500))
    image = db.Column(db.String(100))


class Order(db.Model):
    """All orders created from customers through the online store"""
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String(5))
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    phone_number = db.Column(db.Integer)
    email = db.Column(db.String(50))
    address = db.Column(db.String(100))
    city = db.Column(db.String(100))
    state = db.Column(db.String(20))
    country = db.Column(db.String(20))
    status = db.Column(db.String(10))
    payment_type = db.Column(db.String(10))
    # items = db.relationship('Order_Item', backref='order', lazy=True)
