import flet as ft
from conexion import guardar_reserva_en_db
from datetime import datetime, timedelta
from precios import PRECIOS_HABITACIONES
import mysql.connector


def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="1234",          
            database="hotelsheldonmsql"  
        )
        print("✅ Conectado a MySQL")
        return conexion
    except mysql.connector.Error as err:
        print(f"❌ Error de conexión: {err}")
        return None


def guardar_usuario(nombre,email,telefono):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("INSERT IGNORE INTO usuarios (nombre_completo, email, telefono) VALUES (%s, %s, %s)", (nombre, email, telefono))
    conexion.commit()
    cursor.close()
    conexion.close()


def guardar_reserva(id_usuario,id_habitacion, fecha_ingreso, fecha_salida,total):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute(
    "INSERT INTO reservas (id_usuario, id_habitacion, fecha_ingreso, fecha_salida, total) VALUES (%s, %s, %s, %s, %s)",
    (id_usuario, id_habitacion, fecha_ingreso, fecha_salida, total)
)
    conexion.commit()
    cursor.close()
    conexion.close()

def guardar_habitacion(numero_habitacion, tipo_habitacion, precio_por_noche, descripcion, servicios):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO habitaciones (numero_habitacion, tipo_habitacion, precio_por_noche, descripcion, servicios) VALUES (%s, %s, %s, %s, %s)",
        (numero_habitacion, tipo_habitacion, precio_por_noche, descripcion, servicios)
    )
    conexion.commit()
    cursor.close()
    conexion.close()


def obtener_fechas_ocupadas():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT tipo_habitacion, fecha_ingreso, fecha_salida FROM reservas")
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()

    fechas_ocupadas = {}
    for tipo, fi, fs in datos:
        fechas_ocupadas.setdefault(tipo, [])
        actual = fi
        while actual <= fs:
            fechas_ocupadas[tipo].append(actual)
            actual += timedelta(days=1)
    return fechas_ocupadas

fechas_ocupadas = {}
PRECIOS_HABITACIONES = {
    "Individual": 100,
    "Doble": 150,
    "Suite": 250,
    "Servicio Familiar": 180,
    "Servicio Spa": 220,
    "Servicio Suite de lujo": 300,
    "Servicio Estandar": 120
}

fechas_ocupadas = {
    "Individual": [datetime(2025, 11, 15).date(), datetime(2025, 11, 16).date()],
    "Doble": [datetime(2025, 11, 20).date(), datetime(2025, 11, 21).date()],
    "Suite": [],
    "Servicio Familiar": [],
    "Servicio Spa": [],
    "Servicio Suite de lujo": [],
    "Servicio Estandar": []
}

def reserva(page: ft.Page):
    COLOR_PRIMARIO = "#625956" 
    COLOR_SECUNDARIO = "#475569"  
    COLOR_ACENTO = "#d89c6c"  
    COLOR_FONDO = "#ede8e4" 
    COLOR_TEXTO = "#152540" 
    COLOR_CARD = "#edebeb"

    check_in_picker = ft.DatePicker(
        first_date=datetime(2025, 1, 1),
        last_date=datetime(2027, 12, 31)
    )
    check_out_picker = ft.DatePicker(
        first_date=datetime(2025, 1, 1),
        last_date=datetime(2027, 12, 31)
    )

    check_in_field = ft.TextField(
        label="Fecha de ingreso",
        read_only=True,
        width=240,
        border_color=ft.Colors.with_opacity(0.2, COLOR_TEXTO),
        focused_border_color=COLOR_ACENTO,
        border_radius=12,
    )
    check_out_field = ft.TextField(
        label="Fecha de salida",
        read_only=True,
        width=240,
        border_color=ft.Colors.with_opacity(0.2, COLOR_TEXTO),
        focused_border_color=COLOR_ACENTO,
        border_radius=12,
    )

    check_in_button = ft.IconButton(
        icon=ft.Icons.CALENDAR_TODAY,
        on_click=lambda _: page.open(check_in_picker),
        icon_color=COLOR_ACENTO,
        bgcolor=ft.Colors.with_opacity(0.1, COLOR_ACENTO),
        icon_size=20,
    )
    check_out_button = ft.IconButton(
        icon=ft.Icons.CALENDAR_TODAY,
        on_click=lambda _: page.open(check_out_picker),
        icon_color=COLOR_ACENTO,
        bgcolor=ft.Colors.with_opacity(0.1, COLOR_ACENTO),
        icon_size=20,
    )

    tipo_habitacion = ft.Dropdown(
        label="Tipo de habitación",
        options=[ft.dropdown.Option(t) for t in PRECIOS_HABITACIONES.keys()],
        width=520,
        border_color=ft.Colors.with_opacity(0.2, COLOR_TEXTO),
        focused_border_color=COLOR_ACENTO,
        border_radius=12,
    )

    fechas_ocupadas_text = ft.Text("", color="#EF4444", size=13)

    def actualizar_fechas_ocupadas(e=None):
        if tipo_habitacion.value and tipo_habitacion.value in fechas_ocupadas:
            fechas_list = [f.strftime("%d/%m/%Y") for f in fechas_ocupadas[tipo_habitacion.value]]
            fechas_ocupadas_text.value = (
                f"Fechas ocupadas: " + ", ".join(fechas_list)
                if fechas_list else "✓ Todas las fechas disponibles"
            )
        else:
            fechas_ocupadas_text.value = ""
        page.update()

    tipo_habitacion.on_change = actualizar_fechas_ocupadas

    def handle_check_in(e):
        if not tipo_habitacion.value:
            page.snack_bar = ft.SnackBar(ft.Text("Selecciona un tipo de habitación primero."), bgcolor="#EF4444")
            page.snack_bar.open = True
            page.update()
            return
        fecha = e.control.value.date()
        if fecha in fechas_ocupadas.get(tipo_habitacion.value, []):
            page.snack_bar = ft.SnackBar(ft.Text("Esa fecha ya está ocupada."), bgcolor="#EF4444")
            page.snack_bar.open = True
            page.update()
            return
        check_in_field.value = fecha.strftime("%d/%m/%Y")
        actualizar_resumen()
        page.update()

    def handle_check_out(e):
        if not tipo_habitacion.value:
            page.snack_bar = ft.SnackBar(ft.Text("Selecciona un tipo de habitación primero."), bgcolor="#EF4444")
            page.snack_bar.open = True
            page.update()
            return
        fecha = e.control.value.date()
        if fecha in fechas_ocupadas.get(tipo_habitacion.value, []):
            page.snack_bar = ft.SnackBar(ft.Text("Esa fecha ya está ocupada."), bgcolor="#EF4444")
            page.snack_bar.open = True
            page.update()
            return
        check_out_field.value = fecha.strftime("%d/%m/%Y")
        actualizar_resumen()
        page.update()

    check_in_picker.on_change = handle_check_in
    check_out_picker.on_change = handle_check_out

    nombre = ft.TextField(
        label="Nombre completo",
        width=520,
        border_color=ft.Colors.with_opacity(0.2, COLOR_TEXTO),
        focused_border_color=COLOR_ACENTO,
        border_radius=12,
    )
    telefono = ft.TextField(
        label="Teléfono",
        width=520,
        border_color=ft.Colors.with_opacity(0.2, COLOR_TEXTO),
        focused_border_color=COLOR_ACENTO,
        border_radius=12,
    )
    email = ft.TextField(
        label="Email",
        width=520,
        border_color=ft.Colors.with_opacity(0.2, COLOR_TEXTO),
        focused_border_color=COLOR_ACENTO,
        border_radius=12,
    )

    preferencias_opcionales = {
        "Fumadores": {"switch": ft.Switch(label="Fumadores", label_position=ft.LabelPosition.LEFT, value=False, active_color=COLOR_ACENTO), "valor": "No"},
        "Cama extra": {"switch": ft.Switch(label="Cama extra", label_position=ft.LabelPosition.LEFT, value=False, active_color=COLOR_ACENTO), "valor": "No"},
        "Piso alto": {"switch": ft.Switch(label="Piso alto", label_position=ft.LabelPosition.LEFT, value=False, active_color=COLOR_ACENTO), "valor": "No"}
    }

    def toggle_preferencia(preferencia):
        def _toggle_preferencia(e):
            preferencias_opcionales[preferencia]["valor"] = "Sí" if preferencias_opcionales[preferencia]["switch"].value else "No"
            actualizar_resumen()
            page.update()
        return _toggle_preferencia

    def limpiar_preferencia(preferencia):
        def _limpiar_preferencia(e):
            preferencias_opcionales[preferencia]["valor"] = "No"
            preferencias_opcionales[preferencia]["switch"].value = False
            actualizar_resumen()
            page.update()
        return _limpiar_preferencia

    preferencias_controls = []
    for preferencia, data in preferencias_opcionales.items():
        data["switch"].on_change = toggle_preferencia(preferencia)
        preferencias_controls.append(data["switch"])

    preferencias_container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Preferencias", size=16, weight="w600", color=COLOR_TEXTO),
                *preferencias_controls
            ],
            spacing=16,
        ),
        padding=24,
        bgcolor=COLOR_CARD,
        border_radius=16,
        border=ft.border.all(1, ft.Colors.with_opacity(0.1, COLOR_TEXTO)),
        width=520
    )

    resumen_container = ft.Column([], spacing=12)
    total_reserva = ft.Text("$0 ARS", size=32, weight="w700", color=COLOR_TEXTO)

    def calcular_total():
        total = 0
        if check_in_field.value and check_out_field.value:
            try:
                ingreso = datetime.strptime(check_in_field.value, "%d/%m/%Y").date()
                salida = datetime.strptime(check_out_field.value, "%d/%m/%Y").date()
                noches = (salida - ingreso).days
                if tipo_habitacion.value:
                    total = noches * PRECIOS_HABITACIONES[tipo_habitacion.value]
            except:
                pass
        return total

    def actualizar_resumen():
        resumen_container.controls.clear()
        total = calcular_total()
        
        items = []
        if check_in_field.value:
            items.append(("Ingreso", check_in_field.value, ft.Icons.LOGIN, lambda e: limpiar_campo(check_in_field, check_in_picker)))
        if check_out_field.value:
            items.append(("Salida", check_out_field.value, ft.Icons.LOGOUT, lambda e: limpiar_campo(check_out_field, check_out_picker)))
        if tipo_habitacion.value:
            items.append(("Habitación", tipo_habitacion.value, ft.Icons.HOTEL, None))
        if nombre.value:
            items.append(("Huésped", nombre.value, ft.Icons.PERSON, lambda e: limpiar_campo(nombre)))
        if telefono.value:
            items.append(("Teléfono", telefono.value, ft.Icons.PHONE, lambda e: limpiar_campo(telefono)))
        if email.value:
            items.append(("Email", email.value, ft.Icons.EMAIL, lambda e: limpiar_campo(email)))
        
        for preferencia, data in preferencias_opcionales.items():
            if data["valor"] == "Sí":
                items.append((preferencia, "Sí", ft.Icons.CHECK_CIRCLE, limpiar_preferencia(preferencia)))
        
        for label, valor, icon, on_delete in items:
            resumen_container.controls.append(
                ft.Container(
                    content=ft.Row([
                        ft.Icon(icon, size=18, color=COLOR_ACENTO),
                        ft.Column([
                            ft.Text(label, size=11, color=COLOR_SECUNDARIO, weight="w500"),
                            ft.Text(valor, size=14, color=COLOR_TEXTO, weight="w600"),
                        ], spacing=2),
                        ft.Container(expand=True),
                        ft.IconButton(ft.Icons.CLOSE, icon_size=16, on_click=on_delete, icon_color=COLOR_SECUNDARIO) if on_delete else ft.Container(),
                    ]),
                    padding=16,
                    bgcolor=ft.Colors.with_opacity(0.03, COLOR_TEXTO),
                    border_radius=12,
                )
            )
        
        total_reserva.value = f"${total} ARS"
        page.update()

    def limpiar_campo(campo, picker=None):
        campo.value = ""
        if picker:
            picker.value = None
        actualizar_resumen()
        page.update()

    def enviar_reserva(e):
        if not all([nombre.value, email.value, telefono.value, tipo_habitacion.value, check_in_field.value, check_out_field.value]):
            page.snack_bar = ft.SnackBar(ft.Text("Completa todos los campos obligatorios."), bgcolor="#EF4444")
            page.snack_bar.open = True
            page.update()
            return
        
        if len(email.value) > 100:
            page.snack_bar = ft.SnackBar(ft.Text("El correo electrónico es demasiado largo."), bgcolor="#EF4444")
            page.snack_bar.open = True
            page.update()
            return

        fecha_ingreso = datetime.strptime(check_in_field.value, "%d/%m/%Y").strftime("%Y-%m-%d")
        fecha_salida = datetime.strptime(check_out_field.value, "%d/%m/%Y").strftime("%Y-%m-%d")

        id_usuario = 1
        tipo_a_id = {"Individual": 1, "Doble": 2, "Suite": 3}
        id_habitacion = tipo_a_id.get(tipo_habitacion.value, 1)

        guardar_reserva_en_db(
            fecha_ingreso=fecha_ingreso,
            fecha_salida=fecha_salida,
            nombre=nombre.value,
            telefono=telefono.value,
            email=email.value,
            tipo_habitacion=tipo_habitacion.value,
            total=calcular_total(),
            id_usuario=id_usuario,
            id_habitacion=id_habitacion
        )

        ingreso = datetime.strptime(check_in_field.value, "%d/%m/%Y").date()
        salida = datetime.strptime(check_out_field.value, "%d/%m/%Y").date()
        fechas_ocupadas.setdefault(tipo_habitacion.value, [])
        actual = ingreso
        while actual <= salida:
            fechas_ocupadas[tipo_habitacion.value].append(actual)
            actual += timedelta(days=1)

        page.snack_bar = ft.SnackBar(ft.Text("✓ Reserva confirmada"), bgcolor="#10B981")
        page.snack_bar.open = True
        page.update()

    main_container = ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Column([
                        ft.Text("Formulario!!", size=36, weight="w700", color=COLOR_PRIMARIO),
                        ft.Text("Complete con sus datos para confirmar su estadía", size=15, color=COLOR_SECUNDARIO),
                    ], spacing=8),
                    padding=ft.padding.only(bottom=40, top=20),
                ),
                
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Container(
                                    content=ft.Column([
                                        ft.Text("Detalles de Reserva", size=18, weight="w600", color=COLOR_TEXTO),
                                        tipo_habitacion,
                                        fechas_ocupadas_text,
                                        ft.Row([check_in_field, check_in_button], spacing=8),
                                        ft.Row([check_out_field, check_out_button], spacing=8),
                                    ], spacing=20),
                                    padding=24,
                                    bgcolor=COLOR_CARD,
                                    border_radius=16,
                                    border=ft.border.all(1, ft.Colors.with_opacity(0.1, COLOR_TEXTO)),
                                ),
                                
                                ft.Container(
                                    content=ft.Column([
                                        ft.Text("Información Personal", size=18, weight="w600", color=COLOR_TEXTO),
                                        nombre,
                                        telefono,
                                        email,
                                    ], spacing=20),
                                    padding=24,
                                    bgcolor=COLOR_CARD,
                                    border_radius=16,
                                    border=ft.border.all(1, ft.Colors.with_opacity(0.1, COLOR_TEXTO)),
                                ),
                                
                                preferencias_container,
                                
                                ft.ElevatedButton(
                                    "Confirmar Reserva",
                                    bgcolor=COLOR_ACENTO,
                                    color=COLOR_CARD,
                                    height=56,
                                    width=520,
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                                    on_click=enviar_reserva
                                )
                            ],
                            spacing=24,
                        ),
                        
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text("Resumen", size=24, weight="w700", color=COLOR_TEXTO),
                                    resumen_container,
                                    ft.Divider(height=1, color=ft.Colors.with_opacity(0.1, COLOR_TEXTO)),
                                    ft.Column([
                                        ft.Text("Total", size=14, color=COLOR_SECUNDARIO, weight="w500"),
                                        total_reserva,
                                    ], spacing=4),
                                ],
                                spacing=20,
                                scroll=ft.ScrollMode.AUTO,
                            ),
                            padding=32,
                            bgcolor=COLOR_CARD,
                            border_radius=16,
                            border=ft.border.all(1, ft.Colors.with_opacity(0.1, COLOR_TEXTO)),
                            width=420,
                            height=800,
                        )
                    ],
                    spacing=32,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        ),
        padding=48,
        bgcolor=COLOR_FONDO,
    )

    nombre.on_change = lambda e: actualizar_resumen()
    telefono.on_change = lambda e: actualizar_resumen()
    email.on_change = lambda e: actualizar_resumen()


    return main_container
