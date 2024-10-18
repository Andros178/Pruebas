# tests/test_user_registration.py

import pytest
from app import create_app
from app.models import User
from app.database import db

@pytest.fixture
def test_client():
    # Configurar una instancia temporal de la aplicación
    flask_app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    testing_client = flask_app.test_client()

    # Crear base de datos temporal
    with flask_app.app_context():
        db.create_all()

    yield testing_client

    # Eliminar base de datos temporal
    with flask_app.app_context():
        db.drop_all()

def test_user_registration(test_client):
    response = test_client.post('/register', json={'username': 'newuser', 'password': 'mypassword'})
    assert response.status_code == 201

    user = User.query.filter_by(username='newuser').first()
    assert user is not None
