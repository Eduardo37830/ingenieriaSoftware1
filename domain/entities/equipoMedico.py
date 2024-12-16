class EquipoMedico:
    def __init__(self, id, tipo_equipo, funcionalidad=None, disponibilidad=True):
        """
        Clase para representar un equipo médico.
        :param id: Identificador único del equipo.
        :param tipo_equipo: Tipo de equipo médico.
        :param funcionalidad: Funcionalidad del equipo (opcional).
        :param disponibilidad: Indica si el equipo está disponible (bool).
        """
        self.id = id
        self.tipo_equipo = tipo_equipo
        self.funcionalidad = funcionalidad
        self.disponibilidad = disponibilidad
