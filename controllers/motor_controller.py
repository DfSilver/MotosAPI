from flask import Blueprint, request, jsonify, render_template
from services.motor_service import MotorService
from config.database import get_db_session

motor_bp = Blueprint('motor_bp', __name__)
service = MotorService(get_db_session())

# ----------- Brands -----------
@motor_bp.route('/brands', methods=['GET'])
def get_brands():
    brands = service.list_brands()
    return jsonify([{'id': b.id, 'name': b.name} for b in brands])

@motor_bp.route('/brands', methods=['POST'])
def create_brand():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'El nombre es obligatorio'}), 400
    brand = service.create_brand(name)
    return jsonify({'id': brand.id, 'name': brand.name}), 201

# ----------- Motorcycles JSON -----------
@motor_bp.route('/motorcycles', methods=['GET'])
def get_motorcycles():
    motos = service.list_motorcycles()
    return jsonify([{'id': m.id, 'model': m.model, 'brand': m.brand.name} for m in motos])

@motor_bp.route('/motorcycles', methods=['POST'])
def create_motorcycle():
    data = request.get_json()
    model = data.get('model')
    brand_id = data.get('brand_id')
    if not model or not brand_id:
        return jsonify({'error': 'Modelo y brand_id son obligatorios'}), 400
    moto = service.create_motorcycle(model, brand_id)
    return jsonify({'id': moto.id, 'model': moto.model, 'brand': moto.brand.name}), 201

# ----------- Motorcycles HTML -----------
@motor_bp.route('/motorcycles/view', methods=['GET'])
def view_motorcycles():
    motos = service.list_motorcycles()
    return render_template("motorcycles.html", motorcycles=motos)
