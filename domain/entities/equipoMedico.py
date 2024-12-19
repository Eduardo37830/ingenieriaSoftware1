from typing import Optional

class EquipoMedico:
    def __init__(self, id: int, tipo_equipo: str, funcionalidad: Optional[str] = None, disponibilidad: bool = True):
        """
        Clase para representar un equipo médico.
        :param id: Identificador único del equipo.
        :param tipo_equipo: Tipo de equipo médico.
        :param funcionalidad: Funcionalidad del equipo (opcional).
        :param disponibilidad: Indica si el equipo está disponible (por defecto True).
        """
        self.id = id
        self.tipo_equipo = tipo_equipo
        self.funcionalidad = funcionalidad
        self.disponibilidad = disponibilidad

    def __str__(self):
        """
        Representación en texto del equipo médico.
        """
        return (f"EquipoMedico(id={self.id}, tipo_equipo='{self.tipo_equipo}', "
                f"funcionalidad='{self.funcionalidad or 'N/A'}', disponibilidad={self.disponibilidad})")

    def __repr__(self):
        """
        Representación detallada del equipo médico para depuración.
        """
        return (f"EquipoMedico(id={self.id}, tipo_equipo='{self.tipo_equipo}', "
                f"funcionalidad='{self.funcionalidad or 'N/A'}', disponibilidad={self.disponibilidad})")

    def cambiar_disponibilidad(self, disponibilidad: bool) -> None:
        """
        Cambia el estado de disponibilidad del equipo médico.
        :param disponibilidad: Nuevo estado de disponibilidad (True o False).
        """
        self.disponibilidad = disponibilidad

    def actualizar_funcionalidad(self, nueva_funcionalidad: str) -> None:
        """
        Actualiza la funcionalidad del equipo médico.
        :param nueva_funcionalidad: Nueva descripción de la funcionalidad.
        """
        self.funcionalidad = nueva_funcionalidad
