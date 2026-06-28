import flet as ft
import mysql.connector
from pacientedb import get_patient


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
                        ft.DataCell(ft.Text((paciente[7]))),
                        ft.DataCell(ft.Text((paciente[8])))
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
        ft.DataColumn(ft.Text("Admisión")),
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