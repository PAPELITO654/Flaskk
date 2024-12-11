from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
import pusher

# Conexión a la base de datos MySQL
con = mysql.connector.connect(
    host="185.232.14.52",
    database="u760464709_tst_sep",
    user="u760464709_tst_sep_usr",
    password="dJ0CIAFF="
)

app = Flask(__name__)

# Configuración de Pusher
pusher_client = pusher.Pusher(
    app_id='1767934',
    key='ffa9ea426828188c22c1',
    secret='628348e447718a9eec1f',
    cluster='us2',
    ssl=True
)

@app.route("/")
def index():
    return render_template("app.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

# Ruta para guardar un nuevo usuario
@app.route("/usuarios/guardar", methods=["POST"])
def usuarios_guardar():
    usuario = request.form["txtUsuarioFA"]
    contrasena = request.form["txtContrasenaFA"]

    if not con.is_connected():
        con.reconnect()
    cursor = con.cursor()

    # Insertar el usuario en la base de datos
    sql = "INSERT INTO tst0_usuarios (Nombre_Usuario, Contrasena) VALUES (%s, %s)"
    val = (usuario, contrasena)
    cursor.execute(sql, val)

    con.commit()

    # Disparar evento de Pusher (para actualizaciones en tiempo real)
    pusher_client.trigger("registrosTiempoReal", "registroTiempoReal", {
        "usuario": usuario,
        "contrasena": contrasena
    })

    # Retorna un JSON indicando éxito (para AJAX)
    return jsonify({"status": "success", "usuario": usuario})

# Ruta para buscar usuarios y listarlos
@app.route("/buscar")
def buscar():
    if not con.is_connected():
        con.reconnect()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM tst0_usuarios ORDER BY Id_Usuario DESC")
    registros = cursor.fetchall()

    return jsonify(registros)

# Ruta para actualizar un usuario
@app.route('/usuarios/actualizar/<int:id>', methods=['POST'])
def actualizar_usuario(id):
    nombre_usuario = request.form['nombre']
    contrasena = request.form['contrasena']

    if not con.is_connected():
        con.reconnect()
    cursor = con.cursor()

    sql = """
        UPDATE tst0_usuarios
        SET Nombre_Usuario = %s, Contrasena = %s
        WHERE Id_Usuario = %s
    """
    val = (nombre_usuario, contrasena, id)
    cursor.execute(sql, val)
    con.commit()

    return jsonify({'mensaje': 'Usuario actualizado correctamente'})

# Ruta para eliminar un usuario
@app.route('/usuarios/eliminar/<int:id>', methods=['POST'])
def eliminar_usuario(id):
    if not con.is_connected():
        con.reconnect()
    cursor = con.cursor()

    sql = "DELETE FROM tst0_usuarios WHERE Id_Usuario = %s"
    val = (id,)
    cursor.execute(sql, val)
    con.commit()

    return jsonify({'mensaje': 'Usuario eliminado correctamente'})

if __name__ == "__main__":
    app.run(debug=True)
