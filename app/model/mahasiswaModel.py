import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "mahasiswa_db")
}

class MahasiswaModel:

    @staticmethod
    def get_connection():
        return pymysql.connect(**db_config)

    @staticmethod
    def get_all():
        connection = MahasiswaModel.get_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_mahasiswa")
        result = cursor.fetchall()
        connection.close()
        return result

    @staticmethod
    def add(data):
        connection = MahasiswaModel.get_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO tbl_mahasiswa (npm, nama, tgl_lahir, alamat) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (data['npm'], data['nama'], data['tgl_lahir'], data['alamat']))
        connection.commit()
        connection.close()

    @staticmethod
    def update(data):
        connection = MahasiswaModel.get_connection()
        cursor = connection.cursor()
        sql = "UPDATE tbl_mahasiswa SET nama=%s, tgl_lahir=%s, alamat=%s WHERE npm=%s"
        cursor.execute(sql, (data['nama'], data['tgl_lahir'], data['alamat'], data['npm']))
        connection.commit()
        connection.close()