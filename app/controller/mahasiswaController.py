from flask import jsonify
from app.model.mahasiswaModel import MahasiswaModel

class MahasiswaController:

    @staticmethod
    def get_all():
        try:
            mahasiswa = MahasiswaModel.get_all()
            return jsonify(mahasiswa), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def add(data):
        try:
            MahasiswaModel.add(data)
            return jsonify({"message": "Data berhasil ditambahkan"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update(data):
        try:
            MahasiswaModel.update(data)
            return jsonify({"message": "Data berhasil diperbarui"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
