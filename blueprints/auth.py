from flask import Blueprint, request, jsonify, render_template, current_app, redirect
import sqlite3


auth = Blueprint('auth', __name__)

def get_db():
    conn = sqlite3.connect("meu_banco.db")
    conn.row_factory = sqlite3.Row  # permite acessar por nome da coluna
    return conn

@auth.route('/login', methods=['POST'])
def login():
    email = request.json["email"]
    password = request.json["password"]

    if len(email) > 0 and len(password) > 0:
        return redirect('/')
    else:
        return redirect('login')