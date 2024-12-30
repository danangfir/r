from flask import Flask

def create_app():
    app = Flask(__name__)
    from app.router.mahasiswaRouter import mahasiswa_bp
    app.register_blueprint(mahasiswa_bp)
    return app
