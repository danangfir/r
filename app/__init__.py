from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import blueprint
    from app.router.mahasiswaRouter import mahasiswa_bp

    # Register blueprint dengan prefix /mahasiswa
    app.register_blueprint(mahasiswa_bp, url_prefix='/mahasiswa')

    return app
