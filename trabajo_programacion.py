import datetime
import flet as ft
import re
import mysql.connector
from pacientedb import get_patient, add_paciente

# Se hacen las clases de cada apartado para visualizar cada tabla.
class Pacientes:
    def __init__(self, page: ft.Page, volver):
        self.page = page
        self.volver = volver
        self.page.clean()
        self.page.bgcolor = ft.Colors.WHITE

        data = get_patient()  # Obtener datos de bd.
        
        filas = [ ]
        
        for paciente in data:
            filas.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text((paciente[0]))),
                        ft.DataCell(ft.Text((paciente[1]))),
                        ft.DataCell(ft.Text((paciente[2]))),
                        ft.DataCell(ft.Text((paciente[3]))),
                        ft.DataCell(ft.Text((paciente[4]))),
                        ft.DataCell(ft.Text((paciente[5]))),
                        ft.DataCell(ft.Text((paciente[6]))),
                        ft.DataCell(ft.Text((paciente[7])))
                    ]
                )
            )
        table = ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text("ID")),
        ft.DataColumn(ft.Text("DNI")),
        ft.DataColumn(ft.Text("Nombre")),
        ft.DataColumn(ft.Text("Apellido")),
        ft.DataColumn(ft.Text("Nacimiento")),
        ft.DataColumn(ft.Text("Sexo")),
        ft.DataColumn(ft.Text("Teléfono")),
        ft.DataColumn(ft.Text("Estado")),
    ],
    rows=filas,
)
        self.page.add(
            ft.Text(
                "Pacientes",
                size=24,
                color=ft.Colors.BLACK,
                weight=ft.FontWeight.BOLD
            ),
            ft.Divider(),
            table,
            ft.ElevatedButton("Volver al Menú", on_click=self.volver_menu),
        )
        
        self.page.update()


    def volver_menu(self, e):
        self.page.clean()
        self.volver(self.page)

class Medicos:
    def __init__(self, page: ft.Page, volver):
        self.page = page
        self.volver = volver
        self.page.clean()
        self.page.bgcolor = ft.Colors.WHITE

        self.page.add(
            ft.Text("Médicos", size=24, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Base de datos no conectada.", color=ft.Colors.BLACK70),
            ft.ElevatedButton("Volver al Menú", on_click=self.volver_menu),
        )
        self.page.update()

    def volver_menu(self, e):
        self.page.clean()
        self.volver(self.page)

class EspecialidadesMedicos:
    def __init__(self, page: ft.Page, volver):
        self.page = page
        self.volver = volver
        self.page.clean()
        self.page.bgcolor = ft.Colors.WHITE

        self.page.add(
            ft.Text("Especialidades", size=24, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Base de datos no conectada.", color=ft.Colors.BLACK70),
            ft.ElevatedButton("Volver al Menú", on_click=self.volver_menu),
        )
        self.page.update()

    def volver_menu(self, e):
        self.page.clean()
        self.volver(self.page)

class Citas:
    def __init__(self, page: ft.Page, volver):
        self.page = page
        self.volver = volver
        self.page.clean()
        self.page.bgcolor = ft.Colors.WHITE

        self.page.add(
            ft.Text("Citas", size=24, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Base de datos no conectada.", color=ft.Colors.BLACK70),
            ft.ElevatedButton("Volver al Menú", on_click=self.volver_menu),
        )
        self.page.update()

    def volver_menu(self, e):
        self.page.clean()
        self.volver(self.page)

class Tratamientos:
    def __init__(self, page: ft.Page, volver):
        self.page = page
        self.volver = volver
        self.page.clean()
        self.page.bgcolor = ft.Colors.WHITE

        self.page.add(
            ft.Text("Tratamientos", size=24, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Base de datos no conectada.", color=ft.Colors.BLACK70),
            ft.ElevatedButton("Volver al Menú", on_click=self.volver_menu),
        )
        self.page.update()

    def volver_menu(self, e):
        self.page.clean()
        self.volver(self.page)

class HistorialMedico:
    def __init__(self, page: ft.Page, volver):
        self.page = page
        self.volver = volver
        self.page.clean()
        self.page.bgcolor = ft.Colors.WHITE

        self.page.add(
            ft.Text("Historial Médico", size=24, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Base de datos no conectada.", color=ft.Colors.BLACK70),
            ft.ElevatedButton("Volver al Menú", on_click=self.volver_menu),
        )
        self.page.update()

    def volver_menu(self, e):
        self.page.clean()
        self.volver(self.page)

# Tablas de gestión de datos, (paciente, médico y citas).
class ModificarPacientes:
    def __init__(self, page: ft.Page, volver):
        self.page = page
        self.volver = volver
        self.page.clean()
        self.page.bgcolor = "#F5F9FC"

        #Campos. 
        self.nombre = ft.TextField(
            label="Nombre",
            width=350
        )

        self.apellido = ft.TextField(
            label="Apellido",
            width=350
        )

        self.dni = ft.TextField(
            label="DNI",
            width=250,
            keyboard_type=ft.KeyboardType.NUMBER,
            input_filter=ft.NumbersOnlyInputFilter(),
            max_length=8,
        )

        self.fecha_nacimiento = ft.TextField(
            label="Fecha de nacimiento",
            width=320,
            read_only=True,
        )

        self.date_picker = ft.DatePicker(
            on_change=self.on_date_change,
        )

        self.page.overlay.append(self.date_picker)

        self.boton_fecha = ft.IconButton(
            icon=ft.Icons.CALENDAR_MONTH,
            tooltip="Seleccionar fecha",
            on_click=lambda e: self.page.open(self.date_picker),
        )

        self.sexo = ft.Dropdown(
            label="Sexo",
            width=250,
            options=[
                ft.dropdown.Option(key="M", text="Masculino"),
                ft.dropdown.Option(key="F", text="Femenino"),
                ft.dropdown.Option(key="X", text="No binario"),
                ft.dropdown.Option(key="I", text="Intersexual"),
                ft.dropdown.Option(key="O", text="Otro"),
            ],
        )

        self.telefono = ft.TextField(
            label="Teléfono",
            width=300,
            keyboard_type=ft.KeyboardType.NUMBER,
            input_filter=ft.NumbersOnlyInputFilter(),
            max_length=10,
        )

        #  Buttons. 

        boton_guardar = ft.ElevatedButton(
            "Guardar",
            icon=ft.Icons.SAVE,
            bgcolor=ft.Colors.GREEN,
            color=ft.Colors.WHITE,
            width=140,
            on_click=self.adds_paciente,
        )

        boton_limpiar = ft.ElevatedButton(
            "Limpiar",
            icon=ft.Icons.CLEAR,
            width=140,
            on_click=self.limpiar_formulario,
        )

        boton_volver = ft.ElevatedButton(
            "Volver",
            icon=ft.Icons.ARROW_BACK,
            width=140,
            on_click=self.volver_menu,
        )

        #  HEADER. 
        header = ft.Container(
            bgcolor="#1976D2",
            border_radius=15,
            padding=20,
            content=ft.Row(
                [
                    ft.Icon(
                        ft.Icons.PERSON_ADD,
                        color="white",
                        size=45,
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                "Gestión de Pacientes",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color="white",
                            ),
                            ft.Text(
                                "Agregar, modificar y eliminar pacientes",
                                color="white70",
                            ),
                        ]
                    ),
                ]
            ),
        )

        # FORMULARIO.
        formulario = ft.Container(
            width=520,
            padding=25,
            bgcolor="white",
            border_radius=15,
            shadow=ft.BoxShadow(
                blur_radius=15,
                spread_radius=1,
                color=ft.Colors.BLACK12,
            ),
            content=ft.Column(
                [
                    self.nombre,
                    self.apellido,
                    self.dni,
                    ft.Row(
                        [
                            self.fecha_nacimiento,
                            self.boton_fecha,
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=5,
                    ),
                    self.sexo,
                    self.telefono,

                    ft.Row(
                        [
                            boton_guardar,
                            boton_limpiar,
                            boton_volver,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=15,
                    ),
                ],
                spacing=15,
            ),
        )

        #Interfaz. 
        self.page.add(
            header,
            ft.Container(height=30),
            ft.Row(
                [formulario],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )
        self.page.update()

    def on_date_change(self, e):  # Calendario acción.
        if self.date_picker.value:
            self.fecha_nacimiento.value = self.date_picker.value.strftime("%Y-%m-%d")
            self.page.update()

    def validar_datos(self):
        # Campos obligatorios.
        if (
            not self.nombre.value
            or not self.apellido.value
            or not self.dni.value
            or not self.fecha_nacimiento.value
            or not self.sexo.value
            or not self.telefono.value
        ):
            return "Complete todos los campos."

        # Nombre
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", self.nombre.value):
            return "El nombre solo puede contener letras."

        # Apellido
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", self.apellido.value):
            return "El apellido solo puede contener letras."

        # DNI
        if len(self.dni.value) != 8:
            return "El DNI debe tener exactamente 8 números."

        # Teléfono
        if len(self.telefono.value) < 10:
            return "El teléfono debe tener al menos 10 números."

        try:
            fecha = datetime.datetime.strptime(
                self.fecha_nacimiento.value,
                "%Y-%m-%d"
            ).date()

            if fecha > datetime.datetime.today().date():
                return "La fecha de nacimiento no puede ser futura."

        except ValueError:
            return "La fecha no es válida."

        return None

    def adds_paciente(self, e):
        print("Entró al botón Guardar")
        error = self.validar_datos()
        if error:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(error),
                bgcolor=ft.Colors.ORANGE,
            )

            self.page.snack_bar.open = True
            self.page.update()
            return

        try:
            add_paciente(
                self.nombre.value,
                self.apellido.value,
                self.dni.value,
                self.fecha_nacimiento.value,
                self.sexo.value,
                self.telefono.value,
            )

            snack = ft.SnackBar(
                content=ft.Text("Paciente agregado correctamente."),
                bgcolor=ft.Colors.GREEN,
            )

            self.page.open(snack)
            self.limpiar_formulario()

        except Exception as ex:
            print(f"Error al agregar paciente: {ex}")
            print(ex)
            snack = ft.SnackBar(
                content=ft.Text(f"Error: {ex}"),
                bgcolor=ft.Colors.RED,
            )

            self.page.open(snack)
        self.page.update()

    def limpiar_formulario(self, e=None):
        self.nombre.value = ""
        self.apellido.value = ""
        self.dni.value = ""
        self.fecha_nacimiento.value = ""
        self.sexo.value = None
        self.telefono.value = ""
        self.page.update()

    def volver_menu(self, e):
        self.page.clean()
        self.volver(self.page)

class ModificarMedicos:
    def __init__(self, page: ft.Page, volver):
        self.page = page
        self.volver = volver
        self.page.clean()
        self.page.bgcolor = ft.Colors.WHITE

        self.page.add(
            ft.Text("Gestión de Médicos", size=24, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Base de datos no conectada.", color=ft.Colors.BLACK70),
            ft.Text("Aca van a ir los formularios para agregar, editar y borrar médicos.", color=ft.Colors.BLACK54),
            ft.ElevatedButton("Volver al Menú", on_click=self.volver_menu),
        )
        self.page.update()

    def volver_menu(self, e):
        self.page.clean()
        self.volver(self.page)

class ModificarCitas:
    def __init__(self, page: ft.Page, volver):
        self.page = page
        self.volver = volver
        self.page.clean()
        self.page.bgcolor = ft.Colors.WHITE

        self.page.add(
            ft.Text("Gestión de Citas", size=24, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Base de datos no conectada.", color=ft.Colors.BLACK70),
            ft.Text("Aca van a ir los formularios para agregar, editar y borrar citas.", color=ft.Colors.BLACK54),
            ft.ElevatedButton("Volver al Menú", on_click=self.volver_menu),
        )
        self.page.update()

    def volver_menu(self, e):
        self.page.clean()
        self.volver(self.page)

# Menú principal
def menu_principal(page: ft.Page):
    page.clean()
    page.bgcolor = "#F5F9FC"
    page.title = "Sistema de Gestión de Pacientes"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Rutas definidas.
    def ir_pacientes(e):      Pacientes(page, menu_principal)
    def ir_medicos(e):        Medicos(page, menu_principal)
    def ir_citas(e):          Citas(page, menu_principal)
    def ir_tratamientos(e):   Tratamientos(page, menu_principal)
    def ir_historial(e):      HistorialMedico(page, menu_principal)
    def ir_especialidades(e): EspecialidadesMedicos(page, menu_principal)
    def ir_mod_pacientes(e):  ModificarPacientes(page, menu_principal)
    def ir_mod_medicos(e):    ModificarMedicos(page, menu_principal)
    def ir_mod_citas(e):      ModificarCitas(page, menu_principal)

    # Menús desplegables
    seccion_menu1 = ft.PopupMenuButton(
        content=ft.Text("Archivos"),
        items=[
            ft.PopupMenuItem(content=ft.Text("Pacientes"), icon=ft.Icons.PERSON, on_click=ir_pacientes),
            ft.PopupMenuItem(content=ft.Text("Médicos"), icon=ft.Icons.LOCAL_HOSPITAL, on_click=ir_medicos),
            ft.PopupMenuItem(content=ft.Text("Especialidades"), icon=ft.Icons.MEDICAL_SERVICES, on_click=ir_especialidades),
        ],
    )

    seccion_menu2 = ft.PopupMenuButton(
        content=ft.Text("Administración"),
        items=[
            ft.PopupMenuItem(content=ft.Text("Citas"), icon=ft.Icons.CALENDAR_MONTH, on_click=ir_citas),
            ft.PopupMenuItem(content=ft.Text("Tratamientos"), icon=ft.Icons.MEDICATION, on_click=ir_tratamientos),
            ft.PopupMenuItem(content=ft.Text("Historial Médico"), icon=ft.Icons.HISTORY, on_click=ir_historial),
        ],
    )

    seccion_menu3 = ft.PopupMenuButton(
        content=ft.Text("Gestión de tablas"),
        items=[
            ft.PopupMenuItem(content=ft.Text("Gestión de Pacientes"), icon=ft.Icons.PERSON_ADD, on_click=ir_mod_pacientes),
            ft.PopupMenuItem(content=ft.Text("Gestión de Médicos"), icon=ft.Icons.EDIT, on_click=ir_mod_medicos),
            ft.PopupMenuItem(content=ft.Text("Gestión de Citas"), icon=ft.Icons.EDIT_CALENDAR, on_click=ir_mod_citas),
        ],
    )

    # Encabezado
    header = ft.Container(
        bgcolor="#1976D2",
        border_radius=15,
        padding=20,
        content=ft.Row(
            [
                ft.Icon(
                    ft.Icons.LOCAL_HOSPITAL,
                    size=50,
                    color="white"
                ),
                ft.Column(
                    [
                        ft.Text(
                            "Sistema de Gestión de Pacientes",
                            size=26,
                            weight=ft.FontWeight.BOLD,
                            color="white"
                        ),
                        ft.Text(
                            "Administración hospitalaria",
                            color="white70"
                        )
                    ]
                )
            ]
        )
    )

    # Bienvenida
    bienvenida = ft.Container(
        padding=10,
        content=ft.Column(
            [
                ft.Text(
                    "Bienvenido",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color="#263238"
                ),
                ft.Text(
                    "Seleccione una opción para comenzar.",
                    color="#546E7A"
                )
            ]
        )
    )

    # Tarjetas
    tarjetas = ft.Row(
        [
            ft.Card(
                content=ft.Container(
                    width=180,
                    height=120,
                    padding=15,
                    content=ft.Column(
                        [
                            ft.Icon(ft.Icons.PERSON, size=40, color="#1976D2"),
                            ft.Text("Pacientes", weight=ft.FontWeight.BOLD)
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                )
            ),

            ft.Card(
                content=ft.Container(
                    width=180,
                    height=120,
                    padding=15,
                    content=ft.Column(
                        [
                            ft.Icon(ft.Icons.LOCAL_HOSPITAL, size=40, color="#1976D2"),
                            ft.Text("Médicos", weight=ft.FontWeight.BOLD)
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                )
            ),

            ft.Card(
                content=ft.Container(
                    width=180,
                    height=120,
                    padding=15,
                    content=ft.Column(
                        [
                            ft.Icon(ft.Icons.CALENDAR_MONTH, size=40, color="#1976D2"),
                            ft.Text("Citas", weight=ft.FontWeight.BOLD)
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                )
            )
        ],
        spacing=20
    )

    page.add(
        header,

        ft.Container(height=20),

        bienvenida,

        ft.Container(height=20),

        tarjetas,

        ft.Container(height=25),

        ft.Row(
            [seccion_menu1, seccion_menu2, seccion_menu3],
            spacing=10
        ),

        ft.Divider(),

        ft.Text(
            "Acceso rápido",
            size=14,
            weight=ft.FontWeight.BOLD,
            color="#546E7A"
        ),

        ft.Row([
            ft.IconButton(icon=ft.Icons.HISTORY, tooltip="Historial Médico", on_click=ir_historial),
            ft.IconButton(icon=ft.Icons.MEDICATION, tooltip="Tratamientos", on_click=ir_tratamientos),
            ft.IconButton(icon=ft.Icons.PERSON, tooltip="Pacientes", on_click=ir_pacientes),
            ft.IconButton(icon=ft.Icons.LOCAL_HOSPITAL, tooltip="Médicos", on_click=ir_medicos),
            ft.IconButton(icon=ft.Icons.CALENDAR_MONTH, tooltip="Citas", on_click=ir_citas),
            ft.IconButton(icon=ft.Icons.MEDICAL_SERVICES, tooltip="Especialidades", on_click=ir_especialidades),
        ])
    )

    page.update()

def main(page: ft.Page):
    page.window.maximized = True
    menu_principal(page)

ft.app(target=main)
