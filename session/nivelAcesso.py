from functools import wraps
from flask import jsonify, make_response, redirect, session

def access_required(required_level):
    try:
        def login_required(func):
            @wraps(func)
            def decorated_function(*args, **kwargs):
                if not session.get('loggedin'):
                    return redirect('/login')  # Redireciona para a página de login
                if session.get('role', 0) < required_level:
                    return jsonify({"message": "Acesso negado. Permissão insuficiente."}), 403
                return func(*args, **kwargs)
            return decorated_function
        return login_required
    except Exception as ex:
        print(ex)
        return make_response(jsonify(message="Erro interno."), 400)
