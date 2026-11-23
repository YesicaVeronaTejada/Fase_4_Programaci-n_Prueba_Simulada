
from datetime import datetime

#indica que es un evento informativo por defecto
def registrar_evento(mensaje, tipo="INFO"):

    #datetime.now() obtiene la fecha y hora actual y strftime() la organiza
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    registro = f"[{fecha_hora}] [{tipo}] {mensaje}\n"

    #open("logs.txt", "a") abre el archivo para agregar información sin borrar los registros anteriores
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        
        #archivo.write() escribe el evento en el archivo
        archivo.write(registro)

    print("Registro guardado:", mensaje)