from flask import Blueprint, request, jsonify, render_template, current_app
import sqlite3


page = Blueprint('page', __name__)


def get_db():
    conn = sqlite3.connect("meu_banco.db")
    conn.row_factory = sqlite3.Row  # permite acessar por nome da coluna
    return conn

@page.route('/')
def home():

    conn = get_db()
    usuarios = conn.execute("SELECT id, email, role, created_at FROM users").fetchall()
    conn.close()
    return render_template("home.html", usuarios=usuarios)

@page.route('/login')
def login():
    return render_template('login.html')