from flask import Blueprint, request, jsonify
from src.models.clientes import Clientes

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/', methods=['GET'])
def get_clientes():
    clientes = Clientes.get()
    clientes_list = []
    for cliente in clientes:
        clientes_list.append({
            'id': cliente.id,
            'documento': cliente.documento,
            'nombre': cliente.nombre,
            'direccion': cliente.direccion,
            'telefono': cliente.telefono,
            'email': cliente.email
        })
    return jsonify(clientes_list), 200

@clientes_bp.route('/<int:id>', methods=['GET'])
def get_cliente(id):
    cliente = Clientes.get_by_id(id)
    if cliente:
        cliente_data = {
            'id': cliente.id,
            'documento': cliente.documento,
            'nombre': cliente.nombre,
            'direccion': cliente.direccion,
            'telefono': cliente.telefono,
            'email': cliente.email
        }
        return jsonify(cliente_data), 200
    else:
        return jsonify({'message': 'Cliente no encontrado'}), 404
    
@clientes_bp.route('/', methods=['POST'])
def create_cliente():
    data = request.get_json()
    cliente = Clientes(
        documento=data['documento'],
        nombre=data['nombre'],
        direccion=data['direccion'],
        telefono=data['telefono'],
        email=data['email']
    )
    cliente.save()
    return jsonify({'message': 'Cliente creado exitosamente'}), 201