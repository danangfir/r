from flask import Blueprint, request
from app.controller.mahasiswaController import MahasiswaController

mahasiswa_bp = Blueprint('mahasiswa', __name__)

@mahasiswa_bp.route('/', methods=['GET'])
def get_all_mahasiswa():
    return MahasiswaController.get_all()

@mahasiswa_bp.route('/', methods=['POST'])
def add_mahasiswa():
    data = request.json
    return MahasiswaController.add(data)

@mahasiswa_bp.route('/', methods=['PUT'])
def update_mahasiswa():
    data = request.json
    return MahasiswaController.update(data)
