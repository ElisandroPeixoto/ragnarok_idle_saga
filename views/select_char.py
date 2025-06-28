import flet as ft
from models.db_manager import SessionLocal, Character
from components import buttons as btns
from services.character_services import CharacterService

def select_char(page: ft.Page):
    database = SessionLocal()  # Open Database
    characters_query = database.query(Character).all()

    selected_character = None

    ### INTERFACE ###

    page.title = "Character Selection"
    page.bgcolor = "#E4E4E4"

    # Character Cards
    def character_card(char: Character):
        image = "char_sprites/0.Novice_Sprite.png"

        interface = ft.Container(
            content=ft.Column(controls=[
                    ft.Image(src=image, width=80, height=160, fit=ft.ImageFit.CONTAIN),
                    ft.Text(char.name, size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ft.Text(char.job, size=14, color=ft.Colors.BLACK),
                    ft.Text(f"Level: {char.level}", size=14, color=ft.Colors.BLACK),
                    ft.Text(f"EXP: {char.exp}", size=14, color=ft.Colors.BLACK),
                    ft.Text(f"HP: {char.hp}", size=14, color=ft.Colors.BLACK)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                tight=True,
                spacing=2,
                scroll=ft.ScrollMode.AUTO
            ),
            padding=10,
            margin=10,
            border_radius=10,
            bgcolor=ft.Colors.WHITE,
            width=180,
            height=450,
            alignment=ft.alignment.center,
            shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.BLACK12, offset=ft.Offset(2, 2)),
            border=ft.border.all(3, ft.Colors.TRANSPARENT),
            data=char,
            on_click=lambda e, character_selected=char: select_char(character_selected),
        )

        return interface

    # Character List
    cards = [character_card(char) for char in characters_query]
    grid = ft.GridView(
        expand=True,
        max_extent=220,
        child_aspect_ratio=0.55,
        spacing=10,
        run_spacing=10,
        controls=cards
    )


    # Character Selection
    def select_char(character: Character):
         
        nonlocal selected_character
        selected_character = character

        for card in cards:
            if card.data == character:
                card.border = ft.border.all(3, ft.Colors.BLUE)
                card.bgcolor = ft.Colors.BLUE_50
            else:
                card.border = ft.border.all(3, ft.Colors.TRANSPARENT)
                card.bgcolor = ft.Colors.WHITE
        
        page.update()


    # Character Delete
    def handle_character_delete(e):
        if selected_character:    
            CharacterService.delete_character(selected_character.name)

        page.update()

    # Buttons
    btn_new_char = btns.ElevatedButton1.apply_button(text_input="New Character", on_click_input=lambda e: page.go("/create_char"))
    btn_delete_char = btns.ElevatedButton1.apply_button(text_input="Delete Character", on_click_input=handle_character_delete)
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
