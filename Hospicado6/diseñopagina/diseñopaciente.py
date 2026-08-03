import flet as ft

# COLORES
COLOR_PRIMARIO = "#1976D2"
COLOR_SECUNDARIO = "#E3F2FD"

COLOR_FONDO = "#F5F9FC"
COLOR_TARJETA = "#FFFFFF"

COLOR_EXITO = "#4CAF50"
COLOR_ERROR = "#F44336"
COLOR_EDITAR = "#2196F3"
COLOR_ELIMINAR = "#E53935"

COLOR_TEXTO = "#263238"

# MEDIDAS
ANCHO_FORMULARIO = 520
RADIO = 15

SOMBRA = ft.BoxShadow(
    blur_radius=15,
    spread_radius=1,
    color=ft.Colors.BLACK12,
)

def header(titulo, subtitulo, icono):

    return ft.Container(
        bgcolor=COLOR_PRIMARIO,
        border_radius=15,
        padding=20,

        content=ft.Row(
            [
                ft.Icon(
                    icono,
                    size=45,
                    color="white",
                ),

                ft.Column(
                    [
                        ft.Text(
                            titulo,
                            size=26,
                            weight=ft.FontWeight.BOLD,
                            color="white",
                        ),

                        ft.Text(
                            subtitulo,
                            color="white70",
                        ),
                    ]
                ),
            ]
        ),
    )