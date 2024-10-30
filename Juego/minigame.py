from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Conectar a la base de datos
def get_db_connection():
    conn = sqlite3.connect('puntuaciones_trivia.db')
    conn.row_factory = sqlite3.Row
    return conn

# Preguntas de trivia
preguntas = [
    {
        "pregunta": "¿En qué año fue inaugurado el Museo Nacional de Antropología?",
        "opciones": ["1960", "1964", "1970", "1980"],
        "respuesta_correcta": "1964"
    },
    {
        "pregunta": "¿Quién fue el arquitecto encargado del diseño del museo?",
        "opciones": ["Teodoro González de León", "Pedro Ramírez Vázquez", "Luis Barragán", "Ricardo Legorreta"],
        "respuesta_correcta": "Pedro Ramírez Vázquez"
    },
    # Añadir más preguntas...
]

# Ruta principal para manejar todas las fases
@app.route('/', methods=['GET', 'POST'])
def trivia():
    if request.method == 'POST':
        # Si el formulario de registro fue enviado
        if 'nombre' in request.form:
            nombre = request.form['nombre']
            correo = request.form.get('correo', '')

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO usuarios (nombre, correo) VALUES (?, ?)
            ''', (nombre, correo))
            conn.commit()
            usuario_id = cursor.lastrowid
            conn.close()

            # Renderizar la trivia
            return render_template('trivia.html', preguntas=preguntas, usuario_id=usuario_id)

        # Si el formulario de trivia fue enviado
        elif 'usuario_id' in request.form:
            usuario_id = request.form['usuario_id']
            puntaje = 0
            respuestas = request.form

            for idx, pregunta in enumerate(preguntas):
                respuesta_correcta = pregunta["respuesta_correcta"]
                respuesta_usuario = respuestas.get(f"pregunta_{idx}")
                if respuesta_usuario == respuesta_correcta:
                    puntaje += 1

            # Guardar el puntaje en la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO puntajes (usuario_id, puntaje) VALUES (?, ?)
            ''', (usuario_id, puntaje))
            conn.commit()
            conn.close()

            # Renderizar el resultado
            return render_template('trivia.html', resultado=True, puntaje=puntaje, total_preguntas=len(preguntas))

    # Renderizar la página de registro si es GET
    return render_template('trivia.html')

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
