#Importamos ABC y abstractmethod
from abc import ABC, abstractmethod
#importamos la clase Entidad
from entidades import Entidad
#importamos la función registrar_evento para registrar eventos en un archivo de registro
from registro import registrar_evento

#Creamos la clase abstracta Servicio que recibe las características generales de Entidad
class Servicio(Entidad):

    #creamos el método que se ejecuta cuando creamos un objeto
    def __init__(self, identificacion, nombre, precio_base):

        super().__init__(identificacion, nombre)

        #Validamos el precio
        if not isinstance(precio_base, (int, float)):
            raise ValueError("El precio debe ser numérico")

        if isinstance(precio_base, bool) or precio_base <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        self.precio_base = precio_base

        #Establecer disponibilidad, inicialmente el servicio está disponible para los clientes.
        self.disponible = True
        
        #permite registrar automáticamente la creación de las salas, los equipos y las asesorías
        registrar_evento(f"Servicio creado: {self.nombre} - ID: {self.identificacion}")

    #Creamos los métodos abstractos
    #Obliga a cada servicio especializado a calcular sus propios costos
    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    #Explica las características del servicio    
    @abstractmethod
    def describir(self):
        pass
    
    #Comprueba que los datos recibidos sean correctos    
    @abstractmethod
    def validar_parametros(self, duracion):
        pass

    def mostrar_informacion(self):

        return (
            f"Servicio: {self.nombre}\n"
            f"Código: {self.identificacion}\n"
            f"Precio base: ${self.precio_base:,.2f}\n"
            f"Disponible: {self.disponible}"
        )
        
    
    def calcular_precio(self, duracion, descuento=0, impuesto=0):

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ValueError("La duración debe ser un número positivo")

        if isinstance(descuento, bool) or not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100")

        if isinstance(impuesto, bool) or not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 100:
            raise ValueError("El impuesto debe estar entre 0 y 100")

        subtotal = self.calcular_costo(duracion)

        valor_descuento = subtotal * (descuento / 100)

        total_con_descuento = subtotal - valor_descuento

        valor_impuesto = total_con_descuento * (impuesto / 100)

        total = total_con_descuento + valor_impuesto

        return total

#Creamos los tres servicios especializados
#Creamos SalaServicio que permite calcular el costo de alquilar una sala por horas.
class SalaServicio(Servicio):

    def calcular_costo(self, duracion):

        self.validar_parametros(duracion)

        if not self.disponible:
            raise RuntimeError("El servicio no está disponible")

        return self.precio_base * duracion

    def describir(self):

        return (
            f"Reserva de sala de reuniones. "
            f"Precio por hora: ${self.precio_base:,.2f}"
        )

    def validar_parametros(self, duracion):

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ValueError("La duración debe ser numérica")

        if duracion <= 0:
            raise ValueError("Las horas deben ser mayores que cero")

        return True

#Creamos EquipoServicio que permite que el alquiler de equipos se calculare por días completos
class EquipoServicio(Servicio):

    def calcular_costo(self, duracion):

        self.validar_parametros(duracion)

        if not self.disponible:
            raise RuntimeError("El servicio no está disponible")

        return self.precio_base * duracion

    def describir(self):

        return (
            f"Alquiler de equipos tecnológicos. "
            f"Precio por día: ${self.precio_base:,.2f}"
        )

    def validar_parametros(self, duracion):

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ValueError("La duración debe ser numérica")

        if isinstance(duracion, bool) or not isinstance(duracion, int) or duracion <= 0:
            raise ValueError("Los días deben ser un número entero positivo")

        return True

#Creamos AsesoriaServicio que permite calcular el costo de una asesoría por horas.
class AsesoriaServicio(Servicio):

    def calcular_costo(self, duracion):

        self.validar_parametros(duracion)

        if not self.disponible:
            raise RuntimeError("El servicio no está disponible")

        return self.precio_base * duracion

    def describir(self):

        return (
            f"Asesoría especializada. "
            f"Precio por hora: ${self.precio_base:,.2f}"
        )

    def validar_parametros(self, duracion):

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ValueError("La duración debe ser numérica")

        if duracion <= 0:
            raise ValueError("Las horas de asesoría deben ser mayores que cero")

        return True