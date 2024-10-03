from flask import Flask, render_template, request, redirect, url_for
import pymysql
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos usando variables de entorno
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

app = Flask(__name__)

# Función para crear la base de datos si no existe
def create_database():
    connection = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        cursorclass=pymysql.cursors.DictCursor
    )
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config['database']}")
    connection.close()

# Función para crear las tablas si no existen
def create_tables():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                description TEXT
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                done BOOLEAN DEFAULT FALSE,
                user_id INT,
                project_id INT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
            );
        """)
    connection.close()

# Función para obtener la conexión a la base de datos
def get_db_connection():
    return pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database'],
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route('/')
def index():
    return render_template('index.html')

# Rutas para gestionar Usuarios
@app.route('/users', methods=['GET', 'POST'])
def users():
    connection = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
            connection.commit()
        return redirect(url_for('users'))
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    connection.close()
    return render_template('users.html', users=users)

# Rutas para gestionar Proyectos
@app.route('/projects', methods=['GET', 'POST'])
def projects():
    connection = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO projects (name, description) VALUES (%s, %s)", (name, description))
            connection.commit()
        return redirect(url_for('projects'))
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM projects")
        projects = cursor.fetchall()
    connection.close()
    return render_template('projects.html', projects=projects)

# Rutas para gestionar Tareas
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    connection = get_db_connection()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        done = request.form.get('done', False)
        user_id = request.form['user_id']
        project_id = request.form['project_id']
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO tasks (title, description, done, user_id, project_id) 
                VALUES (%s, %s, %s, %s, %s)
            """, (title, description, done, user_id, project_id))
            connection.commit()
        return redirect(url_for('tasks'))
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.execute("SELECT * FROM projects")
        projects = cursor.fetchall()
    connection.close()
    return render_template('tasks.html', tasks=tasks, users=users, projects=projects)

if __name__ == '__main__':
    # Crear la base de datos y las tablas si no existen
    create_database()
    create_tables()

    # Ejecutar la aplicación Flask
    app.run(debug=True)
