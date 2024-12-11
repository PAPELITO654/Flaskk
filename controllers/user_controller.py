from flask import Blueprint, render_template, request, jsonify
from models.user_model import UserModel

# Crear un Blueprint para el controlador de usuarios
user_blueprint = Blueprint("user", __name__)

# Instancia del modelo
user_model = UserModel()

@user_blueprint.route("/")
def index():
    return render_template("app.html")

@user_blueprint.route("/usuarios")
def usuarios():
    usuarios = user_model.get_all_users()
    return render_template("usuarios.html", usuarios=usuarios)

@user_blueprint.route("/usuarios/guardar", methods=["POST"])
def guardar_usuario():
    usuario = request.form["txtUsuarioFA"]
    contrasena = request.form["txtContrasenaFA"]

    # Guardar el usuario utilizando el modelo
    user_model.create_user(usuario, contrasena)
    
    return jsonify({"status": "success", "usuario": usuario})

@user_blueprint.route("/buscar")
def buscar():
    usuarios = user_model.get_all_users()
    return jsonify(usuarios)
