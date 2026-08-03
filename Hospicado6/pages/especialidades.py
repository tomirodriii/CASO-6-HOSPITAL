import flet as ft
import mysql.connector

class EspecialidadesMedicos:
    def __init__(self, page: ft.Page, volver):
        self.page = page
        self.volver = volver
        self.page.clean()
        self.page.bgcolor = ft.Colors.WHITE

        self.page.add(
            ft.Text("Especialidades", size=24, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Base de datos no conectada.", color=ft.Colors.BLACK),
            ft.ElevatedButton("Volver al Menú", on_click=self.volver_menu),
        )
        self.page.update()

    def volver_menu(self, e):
        self.page.clean()
        self.volver(self.page)