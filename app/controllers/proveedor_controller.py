from flask import Blueprint, request, jsonify

from application.dtos.proveedor_dto import ProveedorDTO
from application.services.proveedor_service import ProveedorApplicationService
from domain.entities.proveedor import Proveedor

proveedor_bp = Blueprint('proveedor_bp', __name__)
service = ProveedorApplicationService("hospital.db")

@proveedor_bp.route('/proveedores', methods=['POST'])
def registrar_proveedor():
    data = request.get_json()
    proveedor = ProveedorDTO(
        id=None,
        nombre=data.get("nombre"),
        fecha_entrega=data.get("fecha_entrega"),
        costo=data.get("costo"),
        telefono_vendedor=data.get("telefono_vendedor"),
    )
    service.registrar_proveedor(proveedor)
    return jsonify({"mensaje": "Proveedor registrado exitosamente"}), 201

@proveedor_bp.route('/proveedores', methods=['GET'])
def listar_proveedores():
    proveedores = service.listar_proveedores()
    return jsonify([p.to_dict() for p in proveedores]), 200
