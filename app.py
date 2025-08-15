from flask import Flask
from flask_session import Session
from flask_compress import Compress
from blueprints.page import page
from blueprints.auth import auth
import sqlite3


app = Flask(__name__, static_url_path='', static_folder='static')

app.register_blueprint(page)
app.register_blueprint(auth)

def init_db():
    conn = sqlite3.connect("meu_banco.db")  # abre/conecta ao banco (se não existir, cria)
    with open("schema.sql", "r", encoding="utf-8") as f:
        conn.executescript(f.read())  # lê e executa todos os comandos SQL do arquivo
    conn.commit()  # salva as alterações no banco
    conn.close()   # fecha a conexão


if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=5000)