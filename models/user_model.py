import mysql.connector

class UserModel:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="185.232.14.52",
            database="u760464709_tst_sep",
            user="u760464709_tst_sep_usr",
            password="dJ0CIAFF="
        )

    def get_all_users(self):
        if not self.con.is_connected():
            self.con.reconnect()
        cursor = self.con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tst0_usuarios ORDER BY Id_Usuario DESC")
        return cursor.fetchall()

    def add_user(self, username, password):
        if not self.con.is_connected():
            self.con.reconnect()
        cursor = self.con.cursor()
        sql = "INSERT INTO tst0_usuarios (Nombre_Usuario, Contrasena) VALUES (%s, %s)"
        cursor.execute(sql, (username, password))
        self.con.commit()
        return cursor.lastrowid
