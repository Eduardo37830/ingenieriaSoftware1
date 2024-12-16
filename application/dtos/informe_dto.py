# application/dtos/informe_dto.py

class InformeDTO:
    def __init__(self, total_depositos: float, total_retiros: float, saldo_promedio: float):
        self.total_depositos = total_depositos
        self.total_retiros = total_retiros
        self.saldo_promedio = saldo_promedio
