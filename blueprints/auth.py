from flask import Blueprint, request, jsonify, render_template, current_app, redirect, session, make_response
import sqlite3


auth = Blueprint('auth', __name__)

def get_db():
    conn = sqlite3.connect("meu_banco.db")
    return conn

@auth.route('/login', methods=['POST'])
def login():
    email = request.json["email"]
    password = request.json["password"]

    if len(email) > 0 and len(password) > 0:
        
        conn = get_db()
        consulta = conn.execute(f'''SELECT email, password_hash, role FROM users
                                        WHERE email = '{email}' and password_hash = '{password}' ''').fetchall()
        conn.close()

        
        if len(consulta) > 0:
            session['loggedin'] = True
            session['role'] = int(consulta[0][2])
            return redirect('/')
        else:
            return redirect('/login')
        
@auth.route('/logout')
def logout():
    try:
        session.clear()
        return redirect("/")
    except Exception as ex:
        return make_response(jsonify(message="Erro interno."), 400)