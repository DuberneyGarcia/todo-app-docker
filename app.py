from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conexion = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="tareas"
        )

        cursor = conexion.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100)
        )
        """)

        conexion.commit()

        return "Conexion exitosa entre Flask y MySQL"

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0')