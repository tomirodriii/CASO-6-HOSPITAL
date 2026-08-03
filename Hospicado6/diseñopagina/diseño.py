import flet as ft

#COLORES.
COLOR_PRIMARIO = "#1976D2"
COLOR_SECUNDARIO = "#E3F2FD"

COLOR_FONDO = "#F5F9FC"
COLOR_TARJETA = "#FFFFFF"

COLOR_EXITO = "#4CAF50"
COLOR_ERROR = "#F44336"
COLOR_EDITAR = "#2196F3"
COLOR_ELIMINAR = "#E53935"

COLOR_TEXTO = "#263238"

#MEDIDAS.
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
    
    
#Formato x de formulario.    
def tarjeta(control, ancho=520):

    return ft.Container(
        width=ancho,

        bgcolor=COLOR_TARJETA,

        border_radius=RADIO,

        padding=25,

        shadow=SOMBRA,

        content=control,
    )

# Botones de la página.    
def boton_guardar(click):

    return ft.ElevatedButton(
        "Guardar",
        icon=ft.Icons.SAVE,
        bgcolor=COLOR_EXITO,
        color="white",
        width=140,
        on_click=click,
    )
    
def boton_actualizar(click):

    return ft.ElevatedButton(
        "Actualizar",
        icon=ft.Icons.EDIT,
        bgcolor=COLOR_EDITAR,
        color="white",
        width=140,
        on_click=click,
    )

def boton_limpiar(click):

    return ft.ElevatedButton(
        "Limpiar",
        icon=ft.Icons.CLEAR,
        width=140,
        on_click=click,
    )
    
def boton_volver(click):

    return ft.ElevatedButton(
        "Volver",
        icon=ft.Icons.ARROW_BACK,
        width=140,
        on_click=click,
    )

def boton_editar(click):

    return ft.IconButton(
        icon=ft.Icons.EDIT,
        icon_color=COLOR_EDITAR,
        tooltip="Editar",
        on_click=click,
    )

def boton_eliminar(click):

    return ft.IconButton(
        icon=ft.Icons.DELETE,
        icon_color=COLOR_ELIMINAR,
        tooltip="Eliminar",
        on_click=click,
    )

def titulo(texto):

    return ft.Text(
        texto,
        size=22,
        weight=ft.FontWeight.BOLD,
        color=COLOR_TEXTO,
    )

def espacio(alto=30):
    return ft.Container(height=alto)

