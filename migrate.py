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

def migrate():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_mahasiswa (
            npm VARCHAR(15) PRIMARY KEY,
            nama VARCHAR(100) NOT NULL,
            tgl_lahir DATE NOT NULL,
            alamat TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

if __name__ == '__main__':
    migrate()
    print("Migrasi selesai!")
