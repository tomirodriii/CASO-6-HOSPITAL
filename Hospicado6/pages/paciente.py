import flet as ft
import mysql.connector
from pacientedb import get_patient


class Pacientes:
    def __init__(self, page: ft.Page, volver):
        self.page = page
        self.volver = volver
        self.page.clean()
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.bgcolor = "#F5F9FC"

        self.data = get_patient()  # Obtener datos de bd.

        encabezado = ft.Container(
            bgcolor="#E3F2FD",
            padding=10,
            border_radius=8,
            content=ft.Row(
                [
                    ft.Text("ID", width=50, weight=ft.FontWeight.BOLD),
                    ft.Text("DNI", width=110, weight=ft.FontWeight.BOLD),
                    ft.Text("Nombre", width=170, weight=ft.FontWeight.BOLD),
                    ft.Text("Apellido", width=170, weight=ft.FontWeight.BOLD),
                    ft.Text("Nacimiento", width=170, weight=ft.FontWeight.BOLD),
                    ft.Text("Sexo", width=170, weight=ft.FontWeight.BOLD),
                    ft.Text("Teléfono", width=170, weight=ft.FontWeight.BOLD),
                    ft.Text("Fecha de admisión", width=170, weight=ft.FontWeight.BOLD),
                    ft.Text("Estado", width=90, weight=ft.FontWeight.BOLD),
                    ft.Text("Detalles", weight=ft.FontWeight.BOLD),
                ]
            ),
        )

        header = ft.Container(
            bgcolor="#1976D2",
            border_radius=15,
            padding=20,
            content=ft.Row(
                [
                    ft.Icon(
                        ft.Icons.PEOPLE,
                        color="white",
                        size=45,
                    ),

                    ft.Column(
                        [
                            ft.Text(
                                "Pacientes",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color="white",
                            ),

                            ft.Text(
                                "Pacientes registrados.",
                                color="white70",
                            ),
                        ]
                    ),
                ]
            ),
        )

        self.buscar = ft.TextField(
            label="Buscar paciente...",
            prefix_icon=ft.Icons.SEARCH,
            width=400,
            border_radius=10,
            on_change=self.filter_pacientes,
        )

        self.lista_pacientes = ft.ListView(
            expand=True,
            spacing=10,
            padding=10,
        )

        self.page.add(
            header,
            ft.Container(height=20),
            ft.Row(
                [self.buscar],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            encabezado,
            self.lista_pacientes,
            ft.Container(height=20),
            ft.ElevatedButton("Volver al Menú", icon=ft.Icons.ARROW_BACK, on_click=self.volver_menu),
        )
        # Cargar pacientes en la lista
        self.load_pacientes(self.data)
        self.page.update()
        
    def load_pacientes(self, data):
        self.lista_pacientes.controls.clear()

        for i, paciente in enumerate(data):

            estado = ft.Text(
                paciente[8],
                color=ft.Colors.GREEN if paciente[8] == "Activo" else ft.Colors.RED,
                weight=ft.FontWeight.BOLD,
                width=90,
            )

            fila = ft.Container(
                bgcolor="#FFFFFF" if i % 2 == 0 else "#F7FAFC",
                padding=10,
                border=ft.border.only(
                    bottom=ft.BorderSide(
                        1,
                        ft.Colors.GREY_300,
                    )
                ),
                content=ft.Row(
                    [
                        ft.Text(str(paciente[0]), width=50), #ID.

                        ft.Text(str(paciente[1]), width=110), #DNI.

                        ft.Text(paciente[2], width=170), #Nombre.

                        ft.Text(paciente[3], width=170), #Apellido.

                        ft.Text(paciente[4], width=170), #Nacimiento.
                        
                        ft.Text(paciente[5], width=170), #Sexo
                        
                        ft.Text(paciente[6], width=170), #Teléfono.

                        ft.Text(paciente[7], width=170), #Fecha de admisión.

                        estado,

                        ft.IconButton(
                            icon=ft.Icons.VISIBILITY,
                            tooltip="Ver paciente",
                            on_click=lambda e, p=paciente: self.ver_paciente(p),
                        ),
                    ]
                ),
            )

            self.lista_pacientes.controls.append(fila)
            self.page.update()

    def filter_pacientes(self, e):
        
        text = self.buscar.value.lower().strip()
        
        if text == "":
            self.load_pacientes(self.data)
            return
        
        marks = []
        
        for paciente in self.data:
            
            if (
                text in str(paciente[0]).lower() #ID.
                or text in paciente[2].lower() #Nombre.
                or text in paciente[3].lower() #Apellido.
            ):
                marks.append(paciente)

        self.load_pacientes(marks)
        self.page.update()

    def ver_paciente(self, paciente):
        
        sexos = {"M": "Masculino", "F": "Femenino", "X": "No binario", "I": "Intersexual", "O": "Otro"}
        
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Row([
                ft.Icon(ft.Icons.PERSON, color=ft.Colors.BLUE),
                ft.Text(f"Paciente: {paciente[2]} {paciente[3]}", weight=ft.FontWeight.BOLD, size=19),
            ]),
            content=ft.Container(
                width=800,
                padding=15,
                content=ft.Row(
                    [
                        ft.Container(
                            width=350,
                            content=ft.Column([
                                ft.Icon(ft.Icons.DESCRIPTION, size=20, color=ft.Colors.BLACK),
                                ft.Text("Información personal.", weight=ft.FontWeight.BOLD),
                                ft.Divider(),
                                ft.Text(f"DNI: {paciente[1]}"),
                                ft.Text(f"Nombre: {paciente[2]}"),
                                ft.Text(f"Apellido: {paciente[3]}"),
                                ft.Text(f"Nacimiento: {paciente[4]}"),
                                ft.Text(f"Sexo: {sexos.get(paciente[5])}"),
                                
                                ft.Container(height=10),
                                
                                ft.Icon(ft.Icons.MEDICAL_SERVICES, size=20, color=ft.Colors.RED),
                                ft.Text("Emergencias.", weight=ft.FontWeight.BOLD),
                                ft.Divider(),
                                ft.Text(f"Contacto de emergencia: {paciente[12]}."),
                                ft.Text(f"Teléfono de emergencia: {paciente[13]}."),

                                ft.Container(height=10),
                                
                                ft.Icon(ft.Icons.WATER_DROP, size=20, color=ft.Colors.RED),
                                ft.Text("Datos médicos.", weight=ft.FontWeight.BOLD),
                                ft.Divider(),
                                ft.Text(f"Grupo sanguíneo: {paciente[11]}"),
                                ft.Text(f"Obra social: {paciente[14]} - N° {paciente[15]}."),
                            ], spacing=5),
                        ),
                        ft.VerticalDivider(width=15, color=ft.Colors.GREY_300),
                        ft.Container(
                            width=350,
                            content=ft.Column([
                                ft.Icon(ft.Icons.HOUSE, size=20, color=ft.Colors.GREY),
                                ft.Text("Datos adicionales.", weight=ft.FontWeight.BOLD),
                                ft.Divider(),
                                ft.Text(f"Teléfono: {paciente[6]}"),
                                ft.Text(f"Dirección: {paciente[9]}."),
                                ft.Text(f"Email: {paciente[10]}"),
                                
                                ft.Container(height=10),
                                
                                ft.Icon(ft.Icons.MENU_BOOK, size=20, color=ft.Colors.BLACK),
                                ft.Text("Registro", weight=ft.FontWeight.BOLD),
                                ft.Divider(),
                                ft.Text(f"Fecha de admisión: {paciente[7]}"),
                                ft.Text(
                                    f"Estado: {paciente[8]}",
                                    color=ft.Colors.GREEN if paciente[8] == "Activo" else ft.Colors.RED,
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ], spacing=5),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    tight=True,
                    spacing=10,
                ),
            ),
            actions=[ft.TextButton("Cerrar", on_click=lambda e: self.close_dialog(dialog))],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.page.open(dialog)
        
    def close_dialog(self, dialog):
        self.page.close(dialog)
            
    def volver_menu(self, e):
        self.page.clean()
        self.volver(self.page)