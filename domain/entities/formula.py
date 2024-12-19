class Formula:
    """
    Representa una prescripción médica para un paciente.

    Atributos:
        id (int): ID único de la prescripción.
        paciente_id (int): ID del paciente asociado.
        medicamento_id (int): ID del medicamento asociado.
        descripcion (str): Descripción de la prescripción.
        cantidad (int): Cantidad de medicamento recetada.
    """

    def __init__(self, id: int, paciente_id: int, medicamento_id: int, descripcion: str, cantidad: int):
        """
        Inicializa una nueva prescripción médica.

        :param id: ID único de la prescripción.
        :param paciente_id: ID del paciente asociado.
        :param medicamento_id: ID del medicamento asociado.
        :param descripcion: Descripción de la prescripción.
        :param cantidad: Cantidad de medicamento recetada.
        """
        self.id = id
        self.paciente_id = paciente_id
        self.medicamento_id = medicamento_id
        self.descripcion = descripcion
        self.cantidad = cantidad

    def __str__(self) -> str:
        """
        Representación en texto de la prescripción médica.
        """
        return (f"Formula(id={self.id}, paciente_id={self.paciente_id}, "
                f"medicamento_id={self.medicamento_id}, descripcion='{self.descripcion}', "
                f"cantidad={self.cantidad})")

    def __repr__(self) -> str:
        """
        Representación detallada de la prescripción médica para depuración.
        """
        return (f"Formula(id={self.id}, paciente_id={self.paciente_id}, "
                f"medicamento_id={self.medicamento_id}, descripcion='{self.descripcion}', "
                f"cantidad={self.cantidad})")

    def actualizar_cantidad(self, nueva_cantidad: int) -> None:
        """
        Actualiza la cantidad de medicamento recetado en la fórmula.

        :param nueva_cantidad: Nueva cantidad de medicamento.
        """
        if nueva_cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self.cantidad = nueva_cantidad

    def actualizar_descripcion(self, nueva_descripcion: str) -> None:
        """
        Actualiza la descripción de la prescripción.

        :param nueva_descripcion: Nueva descripción de la prescripción.
        """
        if not nueva_descripcion:
            raise ValueError("La descripción no puede estar vacía.")
        self.descripcion = nueva_descripcion
