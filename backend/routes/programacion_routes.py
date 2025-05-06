# backend/routes/programacion_routes.py
from flask import Blueprint, request, jsonify
from ..data import NUM_RUTA_TO_PROGRAMA, PROGRAMA_TO_NOMBRE_RUTA, NOMBRE_RUTA_TO_SECTOR

bp = Blueprint('programacion', __name__, url_prefix='/api')

@bp.route('/get_programas_by_num_ruta', methods=['GET'])
def get_programas_by_num_ruta():
    num_ruta = request.args.get('num_ruta', type=int)
    if num_ruta is None:
        return jsonify({"error": "Falta el parámetro num_ruta"}), 400

    programas = NUM_RUTA_TO_PROGRAMA.get(num_ruta, [])
    return jsonify({"programas": programas})

@bp.route('/get_nombres_ruta_by_programa', methods=['GET'])
def get_nombres_ruta_by_programa():
    programa = request.args.get('programa')
    if programa is None:
        return jsonify({"error": "Falta el parámetro programa"}), 400

    nombres_ruta = PROGRAMA_TO_NOMBRE_RUTA.get(programa, [])
    return jsonify({"nombres_ruta": nombres_ruta})

@bp.route('/get_sectores_by_nombre_ruta', methods=['GET'])
def get_sectores_by_nombre_ruta():
    nombre_ruta = request.args.get('nombre_ruta')
    if nombre_ruta is None:
        return jsonify({"error": "Falta el parámetro nombre_ruta"}), 400

    sectores = NOMBRE_RUTA_TO_SECTOR.get(nombre_ruta, [])
    return jsonify({"sectores": sectores})

@bp.route('/guardar_programacion', methods=['POST'])
def guardar_programacion():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se recibieron datos en el cuerpo de la petición"}), 400

    # Aquí deberías implementar la lógica para guardar los datos en tu base de datos
    # Por ahora, solo imprimiremos los datos recibidos y devolveremos una respuesta de éxito

    print("Datos de programación recibidos:")
    for key, value in data.items():
        print(f"{key}: {value}")

    # Aquí iría la lógica real para guardar en DB (SQLAlchemy, etc.)
    # Ejemplo: db.session.add(NuevaProgramacion(data))
    # db.session.commit()

    return jsonify({"message": "Datos recibidos correctamente. Lógica de guardado pendiente de implementar."}), 200