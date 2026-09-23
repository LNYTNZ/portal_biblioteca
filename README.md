# Portal de Biblioteca

Aplicación web hecha con Flask para el examen práctico de TEM-742.
Simula el acceso de usuarios a un sistema de biblioteca, usando sesiones,
cookies y plantillas Jinja2.

## Cómo correrlo

1. Crear el entorno virtual:
   python -m venv venv

2. Activarlo:
   - Windows: venv\Scripts\activate
   - Mac/Linux: source venv/bin/activate

3. Instalar Flask:
   pip install flask

4. Ejecutar:
   python app.py

5. Abrir en el navegador:
   http://127.0.0.1:5000

## Usuarios de prueba

| Usuario | Contraseña |
|---------|------------|
| carlos  | 1111       |
| laura   | 2222       |
| diego   | 3333       |

## Funcionalidades implementadas

- Rutas: /, /login, /libros, /perfil, /logout
- Autenticación con sesiones (session)
- Protección de la ruta /perfil
- Cookie "ultimo_usuario" al iniciar sesión
- Plantillas Jinja2 con herencia (base.html)
- Ciclo {% for %} e {% if %} para mostrar disponibilidad de libros