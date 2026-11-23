#Es la excepción general del programa
class ErrorSistema(Exception):
    pass

#Cuando los datos de un cliente no cumplen las validaciones
class ClienteInvalido(ErrorSistema):
    pass

#Cuando se intenta utilizar un servicio que no está disponible.
class ServicioNoDisponible(ErrorSistema):
    pass

#Cuando una reserva tiene información incorrecta
class ReservaInvalida(ErrorSistema):
    pass

#Cuando se intenta confirmar, cancelar o procesar una reserva de manera incorrecta
class OperacionNoPermitida(ErrorSistema):
    pass