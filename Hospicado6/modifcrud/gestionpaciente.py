import flet as ft
import mysql.connector
from pacientedb import( get_patient , add_paciente , update_paciente , delete_paciente)
from diseñopagina.validaciones import validar_nombre, validar_apellido, validar_dni, validar_telefono, validar_fecha
from diseñopagina.diseño import (header, tarjeta, boton_guardar, boton_limpiar, boton_volver, boton_editar, boton_eliminar, titulo, espacio)

class ModificarPacientes:
    def __init__(self, page: ft.Page, volver):
        self.page = page
        self.volver = volver
        self.page.clean()
        self.page.bgcolor = "#F5F9FC"
        self.id_paciente = None  # Almacena el ID del paciente a modificar
        
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
        self.boton_guardar = boton_guardar(self.save_or_change,)
        self.boton_limpiar = boton_limpiar(self.limpiar_formulario,)
        self.boton_volver = boton_volver(self.volver_menu,)

        #  HEADER. 
        header_pagina = header(
            titulo="Gestión de Pacientes",
            subtitulo="Agregar, modificar y eliminar pacientes",
            icono=ft.Icons.PERSON_ADD
        )

        self.tabla = ft.Column(
            spacing=8,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

        # FORMULARIO.
        formulario = tarjeta(
            control=ft.Column(
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
                            self.boton_guardar,
                            self.boton_limpiar,
                            self.boton_volver,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=15,
                    ),
                ],
                spacing=15,
            ),
            ancho=520
        )

        #Interfaz. 
        self.page.add(
            header_pagina,
            ft.Container(height=30),
            ft.Row(
                [formulario],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            
            ft.Container(height=30),
            ft.Text(
                "Pacientes en lista.",
                size=20,
                weight=ft.FontWeight.BOLD,
            ),
            ft.Divider(),
            self.tabla,
        )
        self.tabla_pacientes()
        self.page.update()

    def tabla_pacientes(self):
        data = get_patient()
        
        self.tabla.controls.clear()

        self.tabla.controls.append(
            ft.Container(
                bgcolor="#1976D2",
                padding=10,
                border_radius=10,
                content=ft.Row(
                    [
                        ft.Text("ID", width=40, color="white", weight=ft.FontWeight.BOLD),
                        ft.Text("DNI", width=100, color="white", weight=ft.FontWeight.BOLD),
                        ft.Text("Nombre", width=150, color="white", weight=ft.FontWeight.BOLD),
                        ft.Text("Apellido", width=150, color="white", weight=ft.FontWeight.BOLD),
                        ft.Text("Nacimiento", width=120, color="white", weight=ft.FontWeight.BOLD),
                        ft.Text("Sexo", width=50, color="white", weight=ft.FontWeight.BOLD),
                        ft.Text("Teléfono", width=120, color="white", weight=ft.FontWeight.BOLD),
                        ft.Text("Acciones", width=90, color="white", weight=ft.FontWeight.BOLD),
                    ]
                )
            )
        )
        for paciente in data:
            self.tabla.controls.append(
                ft.Row(
                    [
                        ft.Text(str(paciente[0]), width=40),
                        ft.Text(paciente[1], width=100),
                        ft.Text(paciente[2], width=150),
                        ft.Text(paciente[3], width=150),
                        ft.Text(str(paciente[4]), width=120),
                        ft.Text(paciente[5], width=50),
                        ft.Text(paciente[6], width=120),
                        ft.IconButton(
                            ft.Icons.EDIT,
                            on_click=lambda _, p=paciente: self.editar_paciente(p),
                        ),
                        ft.IconButton(
                            ft.Icons.DELETE,
                            icon_color=ft.Colors.RED,
                            on_click=lambda _, id=paciente[0]: self.eliminar_paciente(id),
                        ),
                    ]
                )
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
        if not validar_nombre(self.nombre.value):
            return "El nombre solo puede contener letras."

        if not validar_apellido(self.apellido.value):
            return "El apellido solo puede contener letras."

        if not validar_dni(self.dni.value):
            return "El DNI debe tener exactamente 8 números."

        if not validar_telefono(self.telefono.value):
            return "El teléfono debe tener al menos 10 números."

        if not validar_fecha(self.fecha_nacimiento.value):
            return "La fecha de nacimiento no es válida."

        return None

    def adds_paciente(self, e):
        print("Entró al botón Guardar")

        error = self.validar_datos()

        print("Resultado de validar_datos:", error)

        if error:
            print("Hay error")
            snack = ft.SnackBar(
                content=ft.Text(error),
                bgcolor=ft.Colors.ORANGE,
            )
            self.page.open(snack)
            return
        print("No hubo errores")

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
            self.tabla_pacientes()

        except Exception as ex:
            print("ERROR MYSQL:")
            print(ex)
            snack = ft.SnackBar(
                content=ft.Text(str(ex)),
                bgcolor=ft.Colors.RED,
            )

            self.page.open(snack)
        self.page.update()

    def save_or_change(self, e):
        if self.id_paciente is None:
            self.adds_paciente(e)
        else:
            self.modificar_paciente(e)

    def editar_paciente(self, paciente):

        self.id_paciente = paciente[0]

        self.dni.value = paciente[1]
        self.nombre.value = paciente[2]
        self.apellido.value = paciente[3]
        self.fecha_nacimiento.value = str(paciente[4])
        self.sexo.value = paciente[5]
        self.telefono.value = paciente[6]

        self.boton_guardar.text = "Actualizar"
        self.boton_guardar.icon = ft.Icons.EDIT
        self.boton_guardar.bgcolor = ft.Colors.BLUE

        self.page.update()

    def modificar_paciente(self, e):

        error = self.validar_datos()

        if error:

            self.page.open(
                ft.SnackBar(
                    content=ft.Text(error),
                    bgcolor=ft.Colors.ORANGE,
                )
            )

            return

        try:

            update_paciente(
                self.id_paciente,
                self.nombre.value,
                self.apellido.value,
                self.dni.value,
                self.fecha_nacimiento.value,
                self.sexo.value,
                self.telefono.value,
            )

            self.page.open(
                ft.SnackBar(
                    content=ft.Text("Paciente actualizado correctamente."),
                    bgcolor=ft.Colors.GREEN,
                )
            )

            self.limpiar_formulario()

            self.tabla_pacientes()

        except Exception as ex:

            self.page.open(
                ft.SnackBar(
                    content=ft.Text(str(ex)),
                    bgcolor=ft.Colors.RED,
                )
            )

    def eliminar_paciente(self, id_paciente):

        try:

            delete_paciente(id_paciente)

            self.page.open(
                ft.SnackBar(
                    content=ft.Text("Paciente eliminado correctamente."),
                    bgcolor=ft.Colors.RED,
                )
            )

            self.tabla_pacientes()

        except Exception as ex:

            self.page.open(
                ft.SnackBar(
                    content=ft.Text(str(ex)),
                    bgcolor=ft.Colors.RED,
                )
            )

    def limpiar_formulario(self, e=None):
        self.nombre.value = ""
        self.apellido.value = ""
        self.dni.value = ""
        self.fecha_nacimiento.value = ""
        self.sexo.value = None
        self.telefono.value = ""
        
        
        self.id_paciente = None
        
        self.boton_guardar.text = "Guardar"
        self.boton_guardar.icon = ft.Icons.SAVE
        self.boton_guardar.bgcolor = ft.Colors.GREEN
        self.page.update()
        
    def volver_menu(self, e):
        self.page.clean()
        self.volver(self.page)
