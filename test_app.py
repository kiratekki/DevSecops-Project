import os

os.environ['username'] = 'testuser'
os.environ['password'] = 'testpass'


from app import app

def test_valid_login():
	client = app.test_client()
	response = client.post('/login', data={'username': 'testuser', 'password': 'testpass'})
	assert response.status_code == 302


def test_invalid_login():
	client = app.test_client()
	response = client.post('/login', data={'username': 'test1', 'password': 'testpass1'})
	assert response.status_code == 200
