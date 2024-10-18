# app/views.py

def login_user(username, password):
    # Lógica de autenticación (simplificada)
    if username == "admin" and password == "secret":
        return {"status": "success", "message": "Login correcto"}
    else:
        return {"status": "failure", "message": "Login fallido"}
