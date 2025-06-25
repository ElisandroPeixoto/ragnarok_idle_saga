import flet as ft
from models.db_manager import SessionLocal, Character
from utils.ui_helpers import character_card

def select_char(page: ft.Page):
    page.title = "Character Selection"
    page.bgcolor = "#E4E4E4"

    database = SessionLocal()  # Open Database
    characters_query = database.query(Character).all()
    cards = [character_card(char) for char in characters_query]


    ### INTERFACE

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
    new_char = ft.ElevatedButton(
        text="New Character",
        width=180,
        height=45,
        bgcolor=ft.Colors.BLUE_300,
        color=ft.Colors.BLACK,
        on_click=lambda e: page.go("/create_char"))
    
    delete_char = ft.ElevatedButton(
        text="Delete Character",
        width=180,
        height=45,
        bgcolor=ft.Colors.BLUE_300,
        color=ft.Colors.BLACK)
    
    start_game = ft.ElevatedButton(
        text="Start Game",
        width=180,
        height=45,
        bgcolor=ft.Colors.BLUE_300,
        color=ft.Colors.BLACK)

    column1 = ft.Column(
        controls=[new_char, delete_char],
        spacing=20
    )

    column2 = ft.Column(
        controls=[ft.Container(height=45), start_game],
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
