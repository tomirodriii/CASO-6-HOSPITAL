import flet as ft

class Pacientes:
    def __init__(self, page: ft.Page, volver):
        self.page = page
        self.volver = volver
        self.page.clean()
        self.page.bgcolor = ft.Colors.BLACK

        self.page.add(
            ft.Text("Pacientes", size=24, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Base de datos no conectada.", color=ft.Colors.WHITE70),
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
        self.page.bgcolor = ft.Colors.BLACK

        self.page.add(
            ft.Text("Médicos", size=24, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Base de datos no conectada.", color=ft.Colors.WHITE70),
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
        self.page.bgcolor = ft.Colors.BLACK

        self.page.add(
            ft.Text("Citas", size=24, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Base de datos no conectada.", color=ft.Colors.WHITE70),
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
        self.page.bgcolor = ft.Colors.BLACK

        self.page.add(
            ft.Text("Tratamientos", size=24, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Base de datos no conectada.", color=ft.Colors.WHITE70),
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
        self.page.bgcolor = ft.Colors.BLACK

        self.page.add(
            ft.Text("Historial Médico", size=24, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Base de datos no conectada.", color=ft.Colors.WHITE70),
            ft.ElevatedButton("Volver al Menú", on_click=self.volver_menu),
        )
        self.page.update()

    def volver_menu(self, e):
        self.page.clean()
        self.volver(self.page)

def menu_principal(page: ft.Page):
    page.clean()
    page.bgcolor = ft.Colors.BLACK
    page.title = "Sistema de Gestión de Pacientes"
    page.theme_mode = ft.ThemeMode.DARK

    # Navegación
    def ir_pacientes(e):     Pacientes(page, menu_principal)
    def ir_medicos(e):       Medicos(page, menu_principal)
    def ir_citas(e):         Citas(page, menu_principal)
    def ir_tratamientos(e):  Tratamientos(page, menu_principal)
    def ir_historial(e):     HistorialMedico(page, menu_principal)

    # Barra de menús
    archivo_menu = ft.PopupMenuButton(
        content=ft.Text("Archivo"),
        items=[
            ft.PopupMenuItem(content="Salir", icon=ft.Icons.EXIT_TO_APP),
        ],
    )

    secciones_menu = ft.PopupMenuButton(
        content=ft.Text("Secciones"),
        items=[
            ft.PopupMenuItem(content="Pacientes",      icon=ft.Icons.PERSON,           on_click=ir_pacientes),
            ft.PopupMenuItem(content="Médicos",         icon=ft.Icons.LOCAL_HOSPITAL,   on_click=ir_medicos),
            ft.PopupMenuItem(content="Citas",           icon=ft.Icons.CALENDAR_MONTH,   on_click=ir_citas),
            ft.PopupMenuItem(content="Tratamientos",    icon=ft.Icons.MEDICATION,       on_click=ir_tratamientos),
            ft.PopupMenuItem(content="Historial Médico",icon=ft.Icons.HISTORY,          on_click=ir_historial),
        ],
    )

    # Botones de acceso rápido
    page.add(
        ft.Row([archivo_menu, secciones_menu], spacing=10),
        ft.Divider(),
        ft.Text("Acceso rápido", size=13, color=ft.Colors.WHITE54),
        ft.Row([
            ft.IconButton(icon=ft.Icons.HISTORY,    tooltip="Historial Médico", on_click=ir_historial),
            ft.IconButton(icon=ft.Icons.MEDICATION, tooltip="Tratamientos",     on_click=ir_tratamientos),
            ft.IconButton(icon=ft.Icons.PERSON,     tooltip="Pacientes",        on_click=ir_pacientes),
            ft.IconButton(icon=ft.Icons.LOCAL_HOSPITAL, tooltip="Médicos",      on_click=ir_medicos),
            ft.IconButton(icon=ft.Icons.CALENDAR_MONTH, tooltip="Citas",        on_click=ir_citas),
        ]),
    )
    page.update()

def main(page: ft.Page):
    page.window.maximized = True
    menu_principal(page)

ft.app(target=main)