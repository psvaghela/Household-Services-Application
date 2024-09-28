from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)

class Customer(db.Model):
    __tablename__ = 'customers'
    customer_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    services = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

class Professional(db.Model):
    __tablename__ = 'professionals'
    professional_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    service_type = db.Column(db.String, nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Numeric)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

class Service(db.Model):
    __tablename__ = 'services'
    service_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    service_name = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    time_required = db.Column(db.Numeric)
    description = db.Column(db.String)

class Request(db.Model):
    __tablename__ = 'service_requests'
    request_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.service_id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    professional_id = db.Column(db.Integer, db.ForeignKey('professionals.professional_id'), nullable=False)
    date_of_request = db.Column(db.String, nullable=False)
    date_of_completion = db.Column(db.String)
    service_status = db.Column(db.String, nullable=False)
    remarks = db.Column(db.String)

