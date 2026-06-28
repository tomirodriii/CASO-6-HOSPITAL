import flet as ft
from pages.paciente import Pacientes
from pages.medicos import Medicos
from pages.citas import Citas
from pages.tratamientos import Tratamientos
from pages.historial import HistorialMedico
from pages.especialidades import EspecialidadesMedicos

from modifcrud.gestionpaciente import ModificarPacientes
from modifcrud.gestionmedico import ModificarMedicos
from modifcrud.gestioncitas import ModificarCitas

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