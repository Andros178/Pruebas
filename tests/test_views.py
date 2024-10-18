import sys
import os

# Añadir la raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora Python debería poder encontrar el módulo 'app'
from app.views import login_user

# Aquí puedes agregar tus pruebas
def test_login_success():|
    result = login_user("admin", "secret")
    assert result["status"] == "success"
    assert result["message"] == "Login correcto"

def test_login_failure():
    result = login_user("user", "wrongpassword")
    assert result["status"] == "failure"
    assert result["message"] == "Login fallido"
