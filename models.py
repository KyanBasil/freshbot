from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    accounts = db.relationship('Account', backref='owner', lazy=True)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    transactions = db.relationship('Transaction', backref='account', lazy=True)
    loans = db.relationship('Loan', backref='account', lazy=True)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_type = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_type = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    interest_rate = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
