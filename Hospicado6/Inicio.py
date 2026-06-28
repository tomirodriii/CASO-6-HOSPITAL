import flet as ft
from pages.menu import menu_principal

def main(page: ft.Page):
    page.window.maximized = True
    menu_principal(page)

ft.app(target=main)