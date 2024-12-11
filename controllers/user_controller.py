from flask import Blueprint, render_template, request, jsonify
from models.user_model import UserModel

user_controller = Blueprint("user_controller", __name__)
user_model = UserModel()

@user_controller.route("/")
def index():
    return render_template("app.html")

@user_controller.route("/usuarios")
def get_users():
    users = user_model.get_all_users()
    return jsonify(users)

@user_controller.route("/usuarios/guardar", methods=["POST"])
def save_user():
    username = request.form["txtUsuarioFA"]
    password = request.form["txtContrasenaFA"]
    user_id = user_model.add_user(username, password)
    return jsonify({"status": "success", "user_id": user_id, "username": username})

