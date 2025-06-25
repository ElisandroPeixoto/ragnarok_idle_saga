import flet as ft
from screens.create_char import create_character
from screens.select_char import select_char


def route_handler(route, page: ft.Page):
    page.controls.clear()

    if route == "/":
        page.add(select_char(page))
    elif route == "/create_char":
        page.add(create_character(page))
    else:
        page.add(ft.Text("404 - Not Found"))

    page.update()