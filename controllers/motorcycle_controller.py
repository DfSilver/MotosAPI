from flask import Blueprint, request, jsonify, render_template_string
from services.motorcycle_service import MotorcycleService
from config.database import get_db_session

motorcycle_bp = Blueprint("motorcycle_bp", __name__)

def get_service() -> MotorcycleService:
    # Se crea una sesión por request para evitar sesiones largas
    return MotorcycleService(get_db_session())

@motorcycle_bp.route("/motorcycles", methods=["GET"])
def get_motorcycles():
    """
    GET /motorcycles
    Lista todas las motocicletas.
    """
    service = get_service()
    motos = service.listar_motos()
    return jsonify([{"id": m.id, "brand": m.brand, "reference": m.reference} for m in motos]), 200

@motorcycle_bp.route("/motorcycles/<int:moto_id>", methods=["GET"])
def get_motorcycle(moto_id: int):
    """
    GET /motorcycles/<id>
    """
    service = get_service()
    moto = service.obtener_moto(moto_id)
    if not moto:
        return jsonify({"error": "Motocicleta no encontrada"}), 404
    return jsonify({"id": moto.id, "brand": moto.brand, "reference": moto.reference}), 200

@motorcycle_bp.route("/motorcycles", methods=["POST"])
def create_motorcycle():
    """
    POST /motorcycles
    Body JSON: { "brand": "...", "reference": "..." }
    """
    data = request.get_json() or {}
    brand = data.get("brand")
    reference = data.get("reference")

    if not brand or not reference:
        return jsonify({"error": "brand y reference son obligatorios"}), 400

    service = get_service()
    moto = service.crear_moto(brand, reference)
    return jsonify({"id": moto.id, "brand": moto.brand, "reference": moto.reference}), 201

@motorcycle_bp.route("/motorcycles/<int:moto_id>", methods=["PUT"])
def update_motorcycle(moto_id: int):
    """
    PUT /motorcycles/<id>
    Body JSON (al menos uno): { "brand": "...", "reference": "..." }
    """
    data = request.get_json() or {}
    brand = data.get("brand")
    reference = data.get("reference")

    if brand is None and reference is None:
        return jsonify({"error": "Proporcione brand y/o reference"}), 400

    service = get_service()
    moto = service.actualizar_moto(moto_id, brand, reference)
    if not moto:
        return jsonify({"error": "Motocicleta no encontrada"}), 404

    return jsonify({"id": moto.id, "brand": moto.brand, "reference": moto.reference}), 200

@motorcycle_bp.route("/motorcycles/<int:moto_id>", methods=["DELETE"])
def delete_motorcycle(moto_id: int):
    """
    DELETE /motorcycles/<id>
    """
    service = get_service()
    moto = service.eliminar_moto(moto_id)
    if not moto:
        return jsonify({"error": "Motocicleta no encontrada"}), 404
    return jsonify({"message": "Motocicleta eliminada"}), 200


# ---------- Vista HTML para “ver la tabla” ----------
@motorcycle_bp.route("/motorcycles/tabla", methods=["GET"])
def motorcycles_table():
    """
    GET /motorcycles/tabla
    Renderiza una tabla HTML simple con los registros de SQLite.
    """
    service = get_service()
    motos = service.listar_motos()

    template = """
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Motocicletas</title>
        <style>
          body{font-family: system-ui, Arial; padding:24px;}
          table{border-collapse: collapse; width: 720px; max-width: 100%;}
          th, td{border:1px solid #ddd; padding:8px; text-align:left;}
          th{background:#f4f4f4;}
          caption{margin-bottom:10px; font-weight:700; font-size:1.1rem;}
          .empty{margin-top:10px; color:#666;}
        </style>
      </head>
      <body>
        <h2>Tabla de Motocicletas (SQLite)</h2>
        <table>
          <caption>motorcycles_local.db → tabla <code>motorcycles</code></caption>
          <thead>
            <tr><th>ID</th><th>Marca</th><th>Referencia</th></tr>
          </thead>
          <tbody>
            {% for m in motos %}
              <tr><td>{{m.id}}</td><td>{{m.brand}}</td><td>{{m.reference}}</td></tr>
            {% endfor %}
          </tbody>
        </table>
        {% if motos|length == 0 %}
          <p class="empty">No hay motocicletas registradas (la tabla existe pero está vacía).</p>
        {% endif %}
      </body>
    </html>
    """
    return render_template_string(template, motos=motos), 200


# (Opcional) Semilla rápida para demo
@motorcycle_bp.route("/motorcycles/seed", methods=["POST"])
def seed_motorcycles():
    """
    POST /motorcycles/seed
    Crea algunos registros de ejemplo si la tabla está vacía.
    """
    service = get_service()
    if service.listar_motos():
        return jsonify({"message": "La tabla ya tiene datos; no se insertó semilla."}), 200

    ejemplos = [
        ("Yamaha", "MT-07"),
        ("Honda", "CB500F"),
        ("Kawasaki", "Z650"),
    ]
    creadas = [service.crear_moto(brand, ref) for brand, ref in ejemplos]
    return jsonify(
        [{"id": m.id, "brand": m.brand, "reference": m.reference} for m in creadas]
    ), 201
