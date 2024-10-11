import sys
sys.path.insert(0, '/workspaces/freshbot')
from app import app, db, User
import unittest
from flask import json

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

        user = User(username='testuser', email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register(self):
        response = self.app.post('/register', data=json.dumps({
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'User registered successfully', response.data)

    def test_login(self):
        response = self.app.post('/login', data=json.dumps({
            'email': 'test@example.com',
            'password': 'password'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful', response.data)

    def test_login_failed(self):
        response = self.app.post('/login', data=json.dumps({
            'email': 'test@example.com',
            'password': 'wrongpassword'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Login failed', response.data)

    def test_logout(self):
        self.app.post('/login', data=json.dumps({
            'email': 'test@example.com',
            'password': 'password'
        }), content_type='application/json')
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logout successful', response.data)

    def test_account(self):
        self.app.post('/login', data=json.dumps({
            'email': 'test@example.com',
            'password': 'password'
        }), content_type='application/json')
        response = self.app.get('/account')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'testuser', response.data)
        self.assertIn(b'test@example.com', response.data)

if __name__ == '__main__':
    unittest.main()