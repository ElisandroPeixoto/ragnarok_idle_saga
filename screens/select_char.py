import flet as ft
from models.db_manager import SessionLocal, Character
from utils.ui_helpers import character_card
from components import buttons as btns

def select_char(page: ft.Page):
    database = SessionLocal()  # Open Database
    characters_query = database.query(Character).all()
    cards = [character_card(char) for char in characters_query]


    ### INTERFACE ###

    page.title = "Character Selection"
    page.bgcolor = "#E4E4E4"

    # Character List
    grid = ft.GridView(
        expand=True,
        max_extent=220,
        child_aspect_ratio=0.55,
        spacing=10,
        run_spacing=10,
        controls=cards
    )


    # Buttons
    btn_new_char = btns.ElevatedButton1.apply_button(text_input="New Character", on_click_input=lambda e: page.go("/create_char"))
    btn_delete_char = btns.ElevatedButton1.apply_button(text_input="Delete Character")
    btn_start_game = btns.ElevatedButton1.apply_button(text_input="Start Game")


    # Interface Components Building
    column1 = ft.Column(
        controls=[btn_new_char, btn_delete_char],
        spacing=20
    )

    column2 = ft.Column(
        controls=[ft.Container(height=45), btn_start_game],
        spacing=20
    )

    buttons_rows = ft.Row(
        controls=[column1, column2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )


    return ft.Column(
        controls=[ft.Container(height=20), grid, ft.Container(content=buttons_rows, alignment=ft.alignment.center, expand=True, padding=ft.padding.only(top=80))],
                  expand=True,
                  horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                  scroll=ft.ScrollMode.AUTO,
    )
