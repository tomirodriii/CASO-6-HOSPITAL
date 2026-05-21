import flet as ft

def main(page: ft.Page):
    page.title = "Sistema de Gestión de pacientes."
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    contenido = ft.Text("", size=14)

    def mostrar(e):
        contenido.value = f"Sección: {dropdown.value}\n\n(Base de datos no conectada)"
        page.update()

    dropdown = ft.Dropdown(
        label="Todas las secciones",
        width=250,
        options=[
            ft.dropdown.Option("Pacientes"),
            ft.dropdown.Option("Médicos"),
            ft.dropdown.Option("Citas"),
            ft.dropdown.Option("Tratamientos"),
            ft.dropdown.Option("Historial Médico"),
        ]
    )

    dropdown.on_change = mostrar

    page.add(
        ft.Column(
            controls=[
                ft.Text("Sistema de Gestión de pacientes", size=24),
                ft.Divider(),
                dropdown,
                ft.Divider(),
                contenido
            ]
        )
    )

ft.run(main)