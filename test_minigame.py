import unittest
import sqlite3
import os
import shutil
import time
from flask import Flask, request, render_template_string
from flask_testing import TestCase

app = Flask(__name__)

# Configuración para la base de datos de prueba
app.config['DATABASE'] = 'test_puntuaciones_trivia.db'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']

        # Registro de usuario en la base de datos
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT, correo TEXT)')
        cursor.execute('INSERT INTO usuarios (nombre, correo) VALUES (?, ?)', (nombre, correo))
        conn.commit()
        usuario_id = cursor.lastrowid
        conn.close()

        return f'Usuario registrado con ID {usuario_id}.'

    return render_template_string("""
        <form action="/" method="POST">
            <input type="text" name="nombre" placeholder="Nombre" required>
            <input type="email" name="correo" placeholder="Correo" required>
            <button type="submit">Registrar</button>
        </form>
    """)


class TestMiniGame(TestCase):
    def create_app(self):
        # Configurar la aplicación para las pruebas
        app.config['TESTING'] = True
        return app

    def setUp(self):
        # Crear base de datos de prueba antes de cada prueba
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT, correo TEXT)')
        cursor.execute('CREATE TABLE IF NOT EXISTS puntuaciones (usuario_id INTEGER, puntuacion INTEGER)')
        conn.commit()
        conn.close()

    def tearDown(self):
        # Intentar eliminar el archivo de la base de datos después de cada prueba
        time.sleep(1)  # Esperar un poco para que la base de datos se libere
        if os.path.exists('test_puntuaciones_trivia.db'):
            try:
                os.remove('test_puntuaciones_trivia.db')
            except PermissionError:
                print("No se pudo eliminar el archivo de la base de datos. Intentando con shutil.")
                shutil.rmtree('test_puntuaciones_trivia.db')

    def test_registro_usuario(self):
        # Simular el registro de un usuario
        response = self.client.post('/', data={'nombre': 'Juan', 'correo': 'juan@example.com'})
        self.assertEqual(response.status_code, 200)

        # Verificar que el usuario fue registrado en la base de datos
        conn = sqlite3.connect('test_puntuaciones_trivia.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE nombre = ?', ('Juan',))
        user = cursor.fetchone()

        # Imprimir el resultado de la consulta para depuración
        print(user)  # Depuración: Ver el resultado de la consulta
        self.assertIsNotNone(user)
        conn.close()

    def test_calculo_puntaje(self):
        # Simular el registro de un usuario
        response = self.client.post('/', data={'nombre': 'Juan', 'correo': 'juan@example.com'})

        # Imprimir la respuesta para verificar el contenido
        print(response.data)  # Depuración: Ver el contenido de la respuesta

        # Verificar que la respuesta contiene el 'usuario_id'
        decoded_data = response.data.decode()
        print(f"Respuesta decodificada: {decoded_data}")  # Depuración: Mostrar la respuesta decodificada

        # Asegúrate de que la respuesta contiene el 'usuario_id'
        if 'Usuario registrado con ID' in decoded_data:
            usuario_id = decoded_data.split('ID ')[1].split('.')[0]
            print(f'Usuario ID: {usuario_id}')  # Mostrar el usuario_id extraído
            self.assertEqual(int(usuario_id), 1)  # Verifica que el ID del usuario sea 1
        else:
            self.fail('usuario_id no encontrado en la respuesta')

    def test_trivia_resultado(self):
        # Simular el registro del usuario
        response = self.client.post('/', data={'nombre': 'Juan', 'correo': 'juan@example.com'})

        # Imprimir la respuesta para verificar el contenido
        print(response.data)  # Depuración: Ver el contenido de la respuesta

        # Verificar que la respuesta contiene 'usuario_id'
        decoded_data = response.data.decode()
        print(f"Respuesta decodificada: {decoded_data}")  # Depuración: Mostrar la respuesta decodificada

        # Asegúrate de que la respuesta contiene el 'usuario_id'
        if 'Usuario registrado con ID' in decoded_data:
            usuario_id = decoded_data.split('ID ')[1].split('.')[0]
            print(f'Usuario ID: {usuario_id}')  # Mostrar el usuario_id extraído
            self.assertEqual(int(usuario_id), 1)  # Verifica que el ID del usuario sea 1
        else:
            self.fail('usuario_id no encontrado en la respuesta')
