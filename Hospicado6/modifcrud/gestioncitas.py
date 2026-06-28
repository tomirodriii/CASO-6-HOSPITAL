import flet as ft
import mysql.connector

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