# Portal de Biblioteca - Examen Práctico TEM-742
# Este archivo contiene toda la lógica del servidor Flask

from flask import Flask, render_template, request, redirect, url_for, session, make_response

# Creamos la aplicación Flask
app = Flask(__name__)

# Esta clave es necesaria para poder usar sesiones (session)
# Flask la usa para encriptar los datos de la sesión
app.secret_key = "clave_secreta_super_segura"

# Diccionario con los usuarios permitidos y sus contraseñas
usuarios = {
    "Juan": "1111",
    "Ariel": "2222",
    "Carlos": "3333"
}

# Lista de libros disponibles en la biblioteca
libros = [
    {"titulo": "Python desde cero", "autor": "Juan Pérez", "disponibles": 4},
    {"titulo": "Desarrollo Web", "autor": "María López", "disponibles": 2},
    {"titulo": "Inteligencia Artificial", "autor": "Pedro García", "disponibles": 0}
]


# Página principal
@app.route('/')
def index():
    # Revisamos si existe la cookie "ultimo_usuario"
    ultimo_usuario = request.cookies.get('ultimo_usuario')
    return render_template('index.html', ultimo_usuario=ultimo_usuario)


# Formulario de inicio de sesión
# 2 COMMIT
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    # Si el usuario envió el formulario (POST)
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Verificamos que el usuario exista y la contraseña sea correcta
        if usuario in usuarios and usuarios[usuario] == contrasena:
            # Guardamos el usuario en la sesión para saber que está logueado
            session['usuario'] = usuario

            # Preparamos la redirección a /libros
            resp = make_response(redirect(url_for('libros_view')))

            # Guardamos una cookie con el nombre del último usuario que entró
            resp.set_cookie('ultimo_usuario', usuario)

            return resp
        else:
            error = "Usuario o contraseña incorrectos."

    return render_template('login.html', error=error)


# Lista de libros - solo visible si el usuario inició sesión
@app.route('/libros')
def libros_view():
    if 'usuario' not in session:
        # Si no hay sesión activa, lo mandamos al login
        return redirect(url_for('login'))

    return render_template('libros.html', libros=libros, usuario=session['usuario'])


# Perfil del usuario - ruta protegida
@app.route('/perfil')
def perfil():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    return render_template('perfil.html', usuario=session['usuario'])


# Cerrar sesión
@app.route('/logout')
def logout():
    # Eliminamos el usuario de la sesión
    session.pop('usuario', None)
    return redirect(url_for('index'))


# Ruta extra para poder borrar la cookie manualmente
@app.route('/eliminar_cookie')
def eliminar_cookie():
    resp = make_response(redirect(url_for('index')))
    resp.delete_cookie('ultimo_usuario')
    return resp


# Ejecutamos la aplicación en modo debug (útil para ver errores mientras desarrollamos)
if __name__ == '__main__':
    app.run(debug=True)