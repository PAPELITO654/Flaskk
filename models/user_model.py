import mysql.connector

class UserModel:
    def __init__(self):
        # Configuración de conexión a la base de datos
        self.con = mysql.connector.connect(
            host="185.232.14.52",
            database="u760464709_tst_sep",
            user="u760464709_tst_sep_usr",
            password="dJ0CIAFF="
        )
    
    def create_user(self, username, password):
        """Crea un nuevo usuario en la base de datos."""
        if not self.con.is_connected():
            self.con.reconnect()
        cursor = self.con.cursor()
        sql = "INSERT INTO tst0_usuarios (Nombre_Usuario, Contrasena) VALUES (%s, %s)"
        cursor.execute(sql, (username, password))
        self.con.commit()
    
    def get_all_users(self):
        """Obtiene todos los usuarios de la base de datos."""
        if not self.con.is_connected():
            self.con.reconnect()
        cursor = self.con.cursor()
        cursor.execute("SELECT * FROM tst0_usuarios ORDER BY Id_Usuario DESC")
        return cursor.fetchall()
