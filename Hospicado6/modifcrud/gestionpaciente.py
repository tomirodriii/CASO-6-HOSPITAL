import flet as ft
import mysql.connector
from pacientedb import add_paciente
from diseñopagina.validaciones import validar_nombre, validar_apellido, validar_dni, validar_telefono, validar_fecha


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

        except Exception as ex:
            print("ERROR MYSQL:")
            print(ex)
            snack = ft.SnackBar(
                content=ft.Text(str(ex)),
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
