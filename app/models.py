
from app import db
from datetime import date, datetime
from hashlib import md5



class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default = datetime.now)

    def __self__(self):
        return self.username

class Customer (db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String)
    mobile_no = db.Column(db.String)
    aadharno = db.Column(db.String(12),unique=True,nullable=False)
    regis_no = db.Column(db.String(15),unique=True)

    def __self__(self):
        return self.username

class Cylinder(db.Model):
    __tablename__ = "cylinders"
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float)
    customer = db.Column(db.ForeignKey('customers.id'))
    booking = db.Column(db.ForeignKey('bookings.id'))
    price = db.Column(db.Float,default=1000.0)
    added_on= db.Column(db.DateTime, default = datetime.now)
    def __self__(self):
        return self.customer

class  Booking(db.Model):
    __tablename__ = "bookings"
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.ForeignKey('customers.id'))
    booking_date = db.Column(db.DateTime, default = datetime.now)
    def __self__(self):
        return self.id

class  Payment(db.Model):
    __tablename__ = "payment"
    id = db.Column(db.Integer, primary_key=True)
    booking= db.Column(db.Integer, db.ForeignKey('bookings.id'))
    customer = db.Column(db.ForeignKey('customers.id'))
    createdon = db.Column(db.Boolean)

    def __self__(self):
        return self.id







