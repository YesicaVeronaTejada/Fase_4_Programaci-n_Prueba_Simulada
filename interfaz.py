import tkinter as tk
from tkinter import ttk, messagebox
from entidades import Cliente
from servicios import SalaServicio, EquipoServicio, AsesoriaServicio
from reservas import Reserva
from tkfontawesome import icon_to_image


# Configuración principal
ventana = tk.Tk()
ventana.title("Software FJ - Sistema de Reservas")
ventana.geometry("1100x700")
ventana.minsize(900, 600)
ventana.config(bg="#F0F4F8")

# Iconos del menú lateral
iconos_menu = {
    "Inicio": icon_to_image("house", fill="#FFFFFF", scale_to_width=20),
    "Clientes": icon_to_image("users", fill="#FFFFFF", scale_to_width=20),
    "Servicios": icon_to_image("screwdriver-wrench", fill="#FFFFFF", scale_to_width=20),
    "Reservas": icon_to_image("calendar-check", fill="#FFFFFF", scale_to_width=20),
    "Registros": icon_to_image("clipboard-list", fill="#FFFFFF", scale_to_width=20),
    "Salir": icon_to_image("right-from-bracket", fill="#FFFFFF", scale_to_width=20)
}

# Iconos del botón hamburguesa
icono_abrir = icon_to_image("bars", fill="#17365D", scale_to_width=22)
icono_cerrar = icon_to_image("xmark", fill="#17365D", scale_to_width=22)


# Listas del sistema

clientes = []

servicios = [
    SalaServicio("S001", "Sala de reuniones", 30000),
    EquipoServicio("E001", "Alquiler de computadores", 50000),
    AsesoriaServicio("A001", "Asesoría profesional", 80000)
]

reservas = []

# Diseño general

menu_lateral = tk.Frame(ventana, bg="#17365D", width=220)

menu_lateral.pack(side="left", fill="y")
menu_lateral.pack_propagate(False)

area_trabajo = tk.Frame(ventana, bg="#F0F4F8")

area_trabajo.pack(side="right", fill="both", expand=True)

# Barra superior y area de contenido

barra_superior = tk.Frame(area_trabajo, bg="white", height=55)

barra_superior.pack(fill="x")
barra_superior.pack_propagate(False)


contenido = tk.Frame(area_trabajo, bg="#F0F4F8")

contenido.pack(fill="both", expand=True)

# Estado del menú lateral
menu_visible = True

def alternar_menu():
    global menu_visible

    if menu_visible:
        menu_lateral.pack_forget()
        menu_visible = False
        boton_menu.config(image=icono_abrir)
    else:
        menu_lateral.pack(side="left", fill="y", before=area_trabajo)
        menu_visible = True
        boton_menu.config(image=icono_cerrar)

# Botón hamburguesa
boton_menu = tk.Button(barra_superior, image=icono_cerrar, bg="white", activebackground="#F0F4F8", relief="flat", cursor="hand2", command=alternar_menu)

boton_menu.pack(side="left", padx=10)

# FUNCIONES GENERALES

def limpiar_area():

    for elemento in contenido.winfo_children():
        elemento.destroy()

def crear_titulo(titulo, descripcion):

    tk.Label(contenido, text=titulo, font=("Arial", 23, "bold"), bg="#F0F4F8", fg="#17365D").pack(anchor="w", padx=30, pady=(25, 5))

    tk.Label(contenido, text=descripcion, font=("Arial", 11), bg="#F0F4F8", fg="#555555"
    ).pack(anchor="w", padx=30, pady=(0, 20))


# Pantalla de Inicio, lo primero que aparece cuando iniciamos el probrama


def mostrar_inicio():

    limpiar_area()

    # Panel de bienvenida
    bienvenida = tk.Frame(contenido, bg="#F0F4F8", padx=30, pady=25)
    bienvenida.pack(fill="x", padx=30, pady=(25, 20))

    tk.Label(bienvenida, text="¡Bienvenido a Software FJ!", font=("Arial", 18, "bold"), bg="#F0F4F8", fg="black").pack(anchor="w")

    tk.Label(bienvenida, text="Administra tus clientes, servicios y reservas desde un solo lugar.",
            font=("Arial", 11), bg="#F0F4F8", fg="black").pack(anchor="w", pady=(8, 0))

    # Título de estadísticas
    tk.Label(contenido, text="Resumen general", font=("Arial", 16, "bold"), bg="#F0F4F8", fg="#17365D").pack(anchor="w", padx=30, pady=(5, 10))
   
    # Contenedor de tarjetas
    tarjetas = tk.Frame(contenido, bg="#F0F4F8")
    tarjetas.pack(fill="x", padx=22, pady=5)
    
    for columna in range(3):
        tarjetas.grid_columnconfigure(columna, weight=1)

    
    # Información de las tarjetas
    datos = [
        {
            "titulo": "Clientes registrados",
            "cantidad": len(clientes),
            "icono": "👥",
            "color": "#DCEBFA",
            "texto": "#174A7E"
        },
        {
            "titulo": "Servicios disponibles",
            "cantidad": len([s for s in servicios if s.disponible]),
            "icono": "🛠️",
            "color": "#DDF3E8",
            "texto": "#176B48"
        },
        {
            "titulo": "Reservas registradas",
            "cantidad": len(reservas),
            "icono": "📅",
            "color": "#EEE5FA",
            "texto": "#69429A"
        }
    ]

    # Crear las tarjetas
    for dato in datos:

        tarjeta = tk.Canvas(
            tarjetas,
            width=280,
            height=165,
            bg="#F0F4F8",
            highlightthickness=0,
            bd=0
        )

        tarjeta.grid(row=0, column=len(tarjetas.winfo_children()) - 1, sticky="nsew", padx=5, pady=5)

        # Sombra de la tarjeta
        tarjeta.create_rectangle(
            5, 7, 275, 160,
            fill="#D9E0E8",
            outline="#D9E0E8"
        )

        # Fondo de la tarjeta con esquinas rectas
        tarjeta.create_rectangle(
            5, 3, 275, 156,
            fill=dato["color"],
            outline=dato["color"]
        )

        # Icono
        tarjeta.create_text(
            35, 42,
            text=dato["icono"],
            font=("Segoe UI Emoji", 27),
            fill=dato["texto"]
        )

        # Cantidad
        tarjeta.create_text(
            35, 91,
            text=str(dato["cantidad"]),
            font=("Arial", 27, "bold"),
            fill=dato["texto"],
            anchor="w"
        )

        # Título
        tarjeta.create_text(
            35, 130,
            text=dato["titulo"],
            font=("Arial", 10, "bold"),
            fill=dato["texto"],
            anchor="w"
        )


    # Sección de accesos rápidos
    tk.Label(contenido, text="Accesos rápidos", font=("Arial", 16, "bold"), bg="#F0F4F8", fg="#17365D").pack(anchor="w", padx=30, pady=(25, 10))

    accesos = tk.Frame(contenido, bg="#F0F4F8")
    accesos.pack(fill="x", padx=30, pady=5)

    # Botón registrar cliente
    tk.Button(
        accesos,
        text="  Registrar cliente",
        font=("Arial", 11, "bold"),
        bg="#DCEBFA",
        fg="#174A7E",
        activebackground="#C5DDF5",
        relief="flat",
        cursor="hand2",
        padx=15,
        pady=15,
        command=mostrar_clientes
    ).pack(side="left", fill="x", expand=True, padx=5)
    
    # Botón gestionar servicios
    tk.Button(
        accesos,
        text="  Gestionar servicios",
        font=("Arial", 11, "bold"),
        bg="#DDF3E8",
        fg="#176B48",
        activebackground="#C6E9D6",
        relief="flat",
        cursor="hand2",
        padx=15,
        pady=15,
        command=mostrar_servicios
    ).pack(side="left", fill="x", expand=True, padx=5)
   
    # Botón crear reserva
    tk.Button(
        accesos,
        text="  Crear reserva",
        font=("Arial", 11, "bold"),
        bg="#EEE5FA",
        fg="#69429A",
        activebackground="#DDCEF2",
        activeforeground="#69429A",
        relief="flat",
        cursor="hand2",
        padx=15,
        pady=15,
        command=mostrar_reservas
    ).pack(side="left", fill="x", expand=True, padx=5)

# Módulo de Clientes

def mostrar_clientes():

    limpiar_area()

    crear_titulo(
        "Gestión de Clientes",
        "Registra nuevos clientes y consulta sus datos."
    )

    formulario = tk.LabelFrame(contenido, text="Datos del cliente", font=("Arial", 11, "bold"), bg="white", padx=20,pady=15)

    formulario.pack(fill="x", padx=30, pady=10)

    campos = [
        "Identificación",
        "Nombre",
        "Correo electrónico",
        "Teléfono"
    ]

    entradas = {}

    for fila, campo in enumerate(campos):

        tk.Label(formulario, text=campo + ":", font=("Arial", 10), bg="white").grid(row=fila, column=0, sticky="w", padx=10, pady=8)

        entrada = tk.Entry(formulario, width=40, font=("Arial", 10))
        entrada.grid(row=fila, column=1, padx=10, pady=8)

        entradas[campo] = entrada

    tabla_marco = tk.Frame(contenido, bg="#F0F4F8")
    tabla_marco.pack(fill="both", expand=True, padx=30, pady=15)

    tk.Label(tabla_marco, text="Clientes registrados", font=("Arial", 14, "bold"), bg="#F0F4F8", fg="#17365D").pack(anchor="w", pady=8)

    tabla = ttk.Treeview(tabla_marco, columns=("ID", "Nombre", "Correo", "Telefono"), show="headings")

    tabla.heading("ID", text="Identificación")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Correo", text="Correo electrónico")
    tabla.heading("Telefono", text="Teléfono")

    tabla.column("ID", width=120)
    tabla.column("Nombre", width=170)
    tabla.column("Correo", width=220)
    tabla.column("Telefono", width=130)

    tabla.pack(fill="both", expand=True)

    # Mostrar los clientes existentes
    for cliente in clientes:

        tabla.insert("", "end",
            values=(cliente.identificacion, cliente.nombre, cliente.correo, cliente.telefono)
        )

    def guardar_cliente():

        try:

            nuevo_cliente = Cliente(
                entradas["Identificación"].get(),
                entradas["Nombre"].get(),
                entradas["Correo electrónico"].get(),
                entradas["Teléfono"].get()
            )

            clientes.append(nuevo_cliente)

            tabla.insert("","end",
                values=(nuevo_cliente.identificacion, nuevo_cliente.nombre, nuevo_cliente.correo, nuevo_cliente.telefono
                )
            )

            messagebox.showinfo("Registro exitoso", "Cliente registrado correctamente.")

            for entrada in entradas.values():
                entrada.delete(0, tk.END)

        except ValueError as error:

            messagebox.showerror("Error de registro", str(error))

    tk.Button(formulario, text="Guardar cliente",command=guardar_cliente, bg="#2878C8", fg="white", font=("Arial", 10, "bold"), width=20, cursor="hand2"
    ).grid(row=4, column=1, pady=15, sticky="e")



# Módulo de servicios
def mostrar_servicios():

    limpiar_area()

    crear_titulo(
        "Gestión de Servicios",
        "Consulta los servicios disponibles y sus precios."
    )

    # Tabla de servicios
    tabla_marco = tk.Frame(contenido, bg="white")
    tabla_marco.pack(fill="both", expand=True, padx=30, pady=15)

    tk.Label(tabla_marco, text="Servicios registrados", font=("Arial", 14, "bold"), bg="white", fg="#17365D"
    ).pack(anchor="w", padx=15, pady=15)

    tabla = ttk.Treeview(tabla_marco, columns=("ID", "Nombre", "Precio", "Disponibilidad"), show="headings")

    tabla.heading("ID", text="Código")
    tabla.heading("Nombre", text="Nombre del servicio")
    tabla.heading("Precio", text="Precio por unidad")
    tabla.heading("Disponibilidad", text="Estado")

    tabla.column("ID", width=100, anchor="center")
    tabla.column("Nombre", width=250)
    tabla.column("Precio", width=160, anchor="center")
    tabla.column("Disponibilidad", width=150, anchor="center")

    tabla.pack(fill="both", expand=True, padx=15, pady=10)

    # Mostrar los servicios existentes
    for servicio in servicios:

        estado = "Disponible" if servicio.disponible else "No disponible"

        tabla.insert("", "end",
            values=(servicio.identificacion, servicio.nombre, f"${servicio.precio_base:,.0f}", estado)
        )

# Módulo de Reservas 

def mostrar_reservas():

    limpiar_area()

    crear_titulo(
        "Gestión de Reservas",
        "Crea y administra las reservas de tus clientes."
    )

    # Formulario de reserva
    formulario = tk.LabelFrame(
        contenido,
        text="Datos de la reserva",
        font=("Arial", 11, "bold"),
        bg="white",
        padx=20,
        pady=15
    )

    formulario.pack(fill="x", padx=30, pady=10)

    # Selección del cliente
    tk.Label(
        formulario,
        text="Cliente:",
        bg="white",
        font=("Arial", 10)
    ).grid(row=0, column=0, sticky="w", padx=10, pady=8)

    selector_cliente = ttk.Combobox(
        formulario,
        width=35,
        state="readonly",
        values=[
            f"{cliente.identificacion} - {cliente.nombre}"
            for cliente in clientes
        ]
    )

    selector_cliente.grid(row=0, column=1, padx=10, pady=8)

    # Selección del servicio
    tk.Label(
        formulario,
        text="Servicio:",
        bg="white",
        font=("Arial", 10)
    ).grid(row=1, column=0, sticky="w", padx=10, pady=8)

    selector_servicio = ttk.Combobox(
        formulario,
        width=35,
        state="readonly",
        values=[
            f"{servicio.identificacion} - {servicio.nombre}"
            for servicio in servicios
        ]
    )

    selector_servicio.grid(row=1, column=1, padx=10, pady=8)

    # Duración
    tk.Label(
        formulario,
        text="Duración:",
        bg="white",
        font=("Arial", 10)
    ).grid(row=2, column=0, sticky="w", padx=10, pady=8)

    entrada_duracion = tk.Entry(
        formulario,
        width=38,
        font=("Arial", 10)
    )

    entrada_duracion.grid(row=2, column=1, padx=10, pady=8)

    tk.Label(
        formulario,
        text="Ingresa la duración en horas o unidades según el servicio.",
        bg="white",
        fg="#777777",
        font=("Arial", 9)
    ).grid(row=3, column=1, sticky="w", padx=10)

    # Tabla de reservas
    tabla_marco = tk.Frame(contenido, bg="#F0F4F8")
    tabla_marco.pack(fill="both", expand=True, padx=30, pady=15)

    tk.Label(
        tabla_marco,
        text="Reservas registradas",
        font=("Arial", 14, "bold"),
        bg="#F0F4F8",
        fg="#17365D"
    ).pack(anchor="w", pady=8)

    tabla = ttk.Treeview(
        tabla_marco,
        columns=("Numero", "Cliente", "Servicio", "Duracion", "Costo", "Estado"),
        show="headings"
    )

    columnas = [
        ("Numero", "N.º", 60),
        ("Cliente", "Cliente", 150),
        ("Servicio", "Servicio", 180),
        ("Duracion", "Duración", 90),
        ("Costo", "Costo", 120),
        ("Estado", "Estado", 120)
    ]

    for columna, titulo, ancho in columnas:
        tabla.heading(columna, text=titulo)
        tabla.column(columna, width=ancho, anchor="center")

    tabla.pack(fill="both", expand=True)
    

    # Mostrar reservas existentes
    for indice, reserva in enumerate(reservas, start=1):

        tabla.insert(
            "",
            "end",
            iid=str(id(reserva)),
            values=(
                indice,
                reserva.cliente.nombre,
                reserva.servicio.nombre,
                reserva.duracion,
                f"${reserva.costo:,.0f}",
                reserva.estado
            )
        )

    
    def crear_reserva():
        try:
            if not clientes:
                raise ValueError("Primero debes registrar un cliente.")

            if not selector_cliente.get():
                raise ValueError("Debes seleccionar un cliente.")

            if not selector_servicio.get():
                raise ValueError("Debes seleccionar un servicio.")

            if not entrada_duracion.get().strip():
                raise ValueError("Debes ingresar la duración de la reserva.")

            cliente_seleccionado = clientes[selector_cliente.current()]
            servicio_seleccionado = servicios[selector_servicio.current()]

            duracion = int(entrada_duracion.get())

            # Generar un código automático para la reserva
            codigo_reserva = f"R{len(reservas) + 1:03d}"

            # Crear la reserva con los cuatro argumentos requeridos
            nueva_reserva = Reserva(
                codigo_reserva,
                cliente_seleccionado,
                servicio_seleccionado,
                duracion
            )

            reservas.append(nueva_reserva)

            tabla.insert(
                "",
                "end",
                iid=str(id(nueva_reserva)),
                values=(
                    nueva_reserva.codigo,
                    nueva_reserva.cliente.nombre,
                    nueva_reserva.servicio.nombre,
                    nueva_reserva.duracion,
                    nueva_reserva.costo,
                    nueva_reserva.estado
                )
            )

            messagebox.showinfo(
                "Reserva creada",
                f"La reserva {codigo_reserva} se creó correctamente."
            )

            entrada_duracion.delete(0, tk.END)

        except (ValueError, TypeError, IndexError) as error:
            messagebox.showerror("Error al crear reserva", str(error))

        except Exception as error:
            messagebox.showerror("Error", str(error))


    def obtener_reserva():

        seleccion = tabla.selection()

        if not seleccion:
            messagebox.showwarning(
                "Selección requerida",
                "Selecciona una reserva de la tabla."
            )
            return None

        identificador = int(seleccion[0])

        for reserva in reservas:
            if id(reserva) == identificador:
                return reserva

        return None

    def actualizar_tabla(reserva):

        identificador = str(id(reserva))

        indice = next(
            i for i, elemento in enumerate(reservas, start=1)
            if elemento is reserva
        )

        tabla.item(
            identificador,
            values=(
                indice,
                reserva.cliente.nombre,
                reserva.servicio.nombre,
                reserva.duracion,
                f"${reserva.costo:,.0f}",
                reserva.estado
            )
        )

    def procesar_reserva():

        reserva = obtener_reserva()

        if reserva is None:
            return

        try:
            reserva.procesar()

            actualizar_tabla(reserva)

            messagebox.showinfo(
                "Reserva procesada",
                "La reserva fue procesada correctamente."
            )

        except Exception as error:

            messagebox.showerror(
                "Error al procesar",
                str(error)
            )

    def confirmar_reserva():

        reserva = obtener_reserva()

        if reserva is None:
            return

        try:
            reserva.confirmar()

            actualizar_tabla(reserva)

            messagebox.showinfo(
                "Reserva confirmada",
                "La reserva fue confirmada correctamente."
            )

        except Exception as error:

            messagebox.showerror(
                "Error al confirmar",
                str(error)
            )

    def cancelar_reserva():

        reserva = obtener_reserva()

        if reserva is None:
            return

        respuesta = messagebox.askyesno(
            "Cancelar reserva",
            "¿Estás seguro de cancelar esta reserva?"
        )

        if not respuesta:
            return

        try:
            reserva.cancelar()

            actualizar_tabla(reserva)

            messagebox.showinfo(
                "Reserva cancelada",
                "La reserva fue cancelada correctamente."
            )

        except Exception as error:

            messagebox.showerror(
                "Error al cancelar",
                str(error)
            )

    
    
    # Marco para los botones de gestión de reservas
    marco_botones = tk.Frame(contenido, bg="#F0F4F8")

    marco_botones.pack(
        fill="x",
        padx=30,
        pady=10,
        before=tabla_marco
    )

    # Botón crear reserva
    tk.Button(
        marco_botones,
        text="Crear reserva",
        command=crear_reserva,
        bg="#2878C8",
        fg="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        padx=15,
        pady=8,
        cursor="hand2"
    ).pack(side="left", padx=5)

    # Botón procesar reserva
    tk.Button(
        marco_botones,
        text="Procesar reserva",
        command=procesar_reserva,
        bg="#17365D",
        fg="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        padx=15,
        pady=8,
        cursor="hand2"
    ).pack(side="left", padx=5)

    # Botón confirmar reserva
    tk.Button(
        marco_botones,
        text="Confirmar reserva",
        command=confirmar_reserva,
        bg="#198754",
        fg="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        padx=15,
        pady=8,
        cursor="hand2"
    ).pack(side="left", padx=5)

    # Botón cancelar reserva
    tk.Button(
        marco_botones,
        text="Cancelar reserva",
        command=cancelar_reserva,
        bg="#DC3545",
        fg="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        padx=15,
        pady=8,
        cursor="hand2"
    ).pack(side="left", padx=5)
   

def mostrar_registros():
    limpiar_area()
    crear_titulo(
        "Registros del Sistema",
        "Consulta los eventos y errores registrados en la aplicación."
    )

    # Marco principal
    marco_registros = tk.Frame(contenido, bg="#F0F4F8")
    marco_registros.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=15
    )

    # Área de texto
    area_texto = tk.Text(
        marco_registros,
        font=("Arial", 10),
        bg="white",
        fg="#333333",
        wrap="word",
        padx=10,
        pady=10,
        state="disabled"
    )
    area_texto.pack(side="left", fill="both", expand=True)

    # Barra de desplazamiento
    barra_desplazamiento = ttk.Scrollbar(
        marco_registros,
        orient="vertical",
        command=area_texto.yview
    )
    barra_desplazamiento.pack(side="right", fill="y")

    area_texto.config(
        yscrollcommand=barra_desplazamiento.set
    )

    # Función para cargar los registros
    def cargar_registros():
        area_texto.config(state="normal")
        area_texto.delete("1.0", tk.END)

        try:
            with open("logs.txt", "r", encoding="utf-8") as archivo:
                contenido_logs = archivo.read()

            if contenido_logs.strip():
                area_texto.insert(tk.END, contenido_logs)
            else:
                area_texto.insert(
                    tk.END,
                    "Todavía no hay registros disponibles."
                )

        except FileNotFoundError:
            area_texto.insert(
                tk.END,
                "El archivo logs.txt todavía no existe."
            )

        area_texto.config(state="disabled")

    # Botón para actualizar
    boton_actualizar = tk.Button(
        contenido,
        text="Actualizar registros",
        font=("Arial", 10, "bold"),
        bg="#17365D",
        fg="white",
        activebackground="#244A78",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        command=cargar_registros,
        padx=15,
        pady=8
    )
    boton_actualizar.pack(pady=10)

    # Cargar registros al abrir el módulo
    cargar_registros()

# Menú lateral

tk.Label(menu_lateral, text="SOFTWARE FJ", font=("Arial", 16, "bold"), bg="#17365D", fg="white", pady=30).pack()

#Función para cerrar el programa
def salir():
    respuesta = messagebox.askyesno(
        "Salir del sistema",
        "¿Estás seguro de que deseas cerrar Software FJ?"
    )

    if respuesta:
        ventana.destroy()
#Opciones del Menú
opciones = [
    ("Inicio", mostrar_inicio),
    ("Clientes", mostrar_clientes),
    ("Servicios", mostrar_servicios),
    ("Reservas", mostrar_reservas),
    ("Registros", mostrar_registros),
    ("Salir", salir)
]

botones_menu = {}

def seleccionar_opcion(nombre, funcion):
    for nombre_boton, boton in botones_menu.items():
        if nombre_boton == nombre:
            boton.config(bg="#2878C8")
        else:
            boton.config(bg="#17365D")

    funcion()


for nombre, funcion in opciones:

    boton = tk.Button(menu_lateral, text="  " + nombre, image=iconos_menu[nombre], compound="left", 
                      font=("Segoe UI", 11), bg="#17365D", fg="white", activebackground="#2878C8", activeforeground="white",
                      relief="flat", anchor="w", padx=15, pady=12, cursor="hand2", command=lambda n=nombre, f=funcion: seleccionar_opcion(n, f))

    boton.pack(fill="x", padx=10, pady=3)
    botones_menu[nombre] = boton


seleccionar_opcion("Inicio", mostrar_inicio)

#Inicia la aplicación
mostrar_inicio()

ventana.mainloop()