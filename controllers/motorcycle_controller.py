from flask import Blueprint, request, jsonify
from config.database import get_db_session
from services.motor_service import MotorService

motorcycle_bp = Blueprint('motorcycle_bp', __name__)


# ---------- GET ALL MOTORCYCLES ----------
@motorcycle_bp.route('/motorcycles', methods=['GET'])
def get_motorcycles():
    with get_db_session() as db:
        svc = MotorService(db)
        motorcycles = svc.list_motorcycles()
        return jsonify([
            {'id': m.id, 'model': m.model, 'brand_id': m.brand_id}
            for m in motorcycles
        ])

# ---------- GET MOTORCYCLE BY ID ----------
@motorcycle_bp.route('/motorcycles/<int:motorcycle_id>', methods=['GET'])
def get_motorcycle(motorcycle_id):
    with get_db_session() as db:
        svc = MotorService(db)
        motorcycle = svc.get_motorcycle(motorcycle_id)
        if motorcycle:
            return jsonify({'id': motorcycle.id, 'model': motorcycle.model, 'brand_id': motorcycle.brand_id})
        return jsonify({'error': 'Motorcycle not found'}), 404

# ---------- CREATE MOTORCYCLE ----------
@motorcycle_bp.route('/motorcycles', methods=['POST'])
def create_motorcycle():
    data = request.get_json()
    with get_db_session() as db:
        svc = MotorService(db)
        new_motorcycle = svc.create_motorcycle(
            model=data['model'],
            brand_id=data['brand_id']
        )
        return jsonify({
            'id': new_motorcycle.id,
            'model': new_motorcycle.model,
            'brand_id': new_motorcycle.brand_id
        }), 201

# ---------- DELETE MOTORCYCLE ----------
@motorcycle_bp.route('/motorcycles/<int:motorcycle_id>', methods=['DELETE'])
def delete_motorcycle(motorcycle_id):
    with get_db_session() as db:
        svc = MotorService(db)
        deleted = svc.delete_motorcycle(motorcycle_id)
        if deleted:
            return jsonify({'message': f'Motorcycle {motorcycle_id} deleted successfully'})
        return jsonify({'error': 'Motorcycle not found'}), 404
