import flet as ft
from views.create_char import create_character
from views.select_char import char_selection


def route_handler(route, page: ft.Page):
    page.controls.clear()

    if route == "/":
        page.add(char_selection(page))
    elif route == "/create_char":
        page.add(create_character(page))
    else:
        page.add(ft.Text("404 - Not Found"))

    page.update()