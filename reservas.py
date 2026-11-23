
from entidades import Cliente
from servicios import Servicio
from excepciones import (ServicioNoDisponible, ReservaInvalida, OperacionNoPermitida)
from registro import registrar_evento

class Reserva:
    
    #Crea la reserva y verifica que el cliente, el servicio y la duración sean válidos.
    def __init__(self, codigo, cliente, servicio, duracion):

        if not isinstance(cliente, Cliente):
            raise ReservaInvalida("Debe seleccionar un cliente válido")

        if not isinstance(servicio, Servicio):
            raise ReservaInvalida("Debe seleccionar un servicio válido")
        
        try:
            servicio.validar_parametros(duracion)

        except ValueError as error:
            raise ReservaInvalida("La duración de la reserva no es válida") from error

        self.codigo = codigo
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.costo = 0
        
        registrar_evento(f"Reserva creada: {self.codigo} - Cliente: {self.cliente.nombre}")

    #Calcula el costo y cambia el estado a Procesada. Si la reserva está cancelada, no se puede procesar.
    def procesar(self):

        if self.estado == "Cancelada":
            raise OperacionNoPermitida("No se puede procesar una reserva cancelada")

        if not self.servicio.disponible:
            raise ServicioNoDisponible("El servicio seleccionado no está disponible")

        self.costo = self.servicio.calcular_costo(self.duracion)
        self.estado = "Procesada"
        
        registrar_evento(f"Reserva procesada: {self.codigo} - Costo: ${self.costo:,.2f}")

        return self.costo

    #Confirma una reserva que ya fue procesada y cambia el estado a Confirmada. Si la reserva está cancelada, no se puede confirmar.
    def confirmar(self):

        if self.estado == "Cancelada":
            raise OperacionNoPermitida("No se puede confirmar una reserva cancelada")

        if self.estado != "Procesada":
            raise OperacionNoPermitida("Primero debe procesar la reserva")

        self.estado = "Confirmada"
        
        registrar_evento(f"Reserva confirmada: {self.codigo}")

        return "Reserva confirmada correctamente"

    #Cambia el estado de la reserva a Cancelada 
    def cancelar(self):

        if self.estado == "Cancelada":
            raise OperacionNoPermitida("La reserva ya está cancelada")

        self.estado = "Cancelada"
        
        registrar_evento(f"Reserva cancelada: {self.codigo}")

        return "Reserva cancelada correctamente"

    #Muestra los datos completos de la reserva
    def mostrar_reserva(self):

        return (
            f"\nCódigo de reserva: {self.codigo}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion}\n"
            f"Costo: ${self.costo:,.2f}\n"
            f"Estado: {self.estado}"
        )
