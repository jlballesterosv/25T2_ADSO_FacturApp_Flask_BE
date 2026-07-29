from flask import Blueprint, request, jsonify
from src.models.clientes import Clientes

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/', methods=['GET'])
def get_clientes():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=5, type=int)

    clientes, total = Clientes.paginate(page=page, per_page=per_page)

    total_pages = (total + per_page - 1) // per_page  # Calcular el número total de páginas

    return jsonify({
        'data': [cliente.to_dict() for cliente in clientes],
        'meta' : {
            'page': page,
            'per_page': per_page,
            'total': total,
            'total_pages': total_pages,
            'has_next': page < total_pages,
            'has_prev': page > 1
        }
    }), 200

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