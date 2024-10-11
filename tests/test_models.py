import sys
sys.path.insert(0, '/workspaces/freshbot')
from models import db, User, Account, Transaction, Loan
import unittest
from datetime import datetime

class TestModels(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_creation(self):
        user = User(username='testuser', email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()
        self.assertEqual(User.query.count(), 1)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

    def test_account_creation(self):
        user = User(username='testuser', email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()
        account = Account(account_number='1234567890', balance=100.0, owner=user)
        db.session.add(account)
        db.session.commit()
        self.assertEqual(Account.query.count(), 1)
        self.assertEqual(account.account_number, '1234567890')
        self.assertEqual(account.balance, 100.0)
        self.assertEqual(account.owner.username, 'testuser')

    def test_transaction_creation(self):
        user = User(username='testuser', email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()
        account = Account(account_number='1234567890', balance=100.0, owner=user)
        db.session.add(account)
        db.session.commit()
        transaction = Transaction(transaction_type='deposit', amount=50.0, date=datetime.utcnow(), account=account)
        db.session.add(transaction)
        db.session.commit()
        self.assertEqual(Transaction.query.count(), 1)
        self.assertEqual(transaction.transaction_type, 'deposit')
        self.assertEqual(transaction.amount, 50.0)
        self.assertEqual(transaction.account.account_number, '1234567890')

    def test_loan_creation(self):
        user = User(username='testuser', email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()
        account = Account(account_number='1234567890', balance=100.0, owner=user)
        db.session.add(account)
        db.session.commit()
        loan = Loan(loan_type='personal', amount=1000.0, interest_rate=5.0, start_date=datetime.utcnow(), end_date=datetime.utcnow(), account=account)
        db.session.add(loan)
        db.session.commit()
        self.assertEqual(Loan.query.count(), 1)
        self.assertEqual(loan.loan_type, 'personal')
        self.assertEqual(loan.amount, 1000.0)
        self.assertEqual(loan.interest_rate, 5.0)
        self.assertEqual(loan.account.account_number, '1234567890')

if __name__ == '__main__':
    unittest.main()