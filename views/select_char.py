import flet as ft
from models.db_manager import SessionLocal, Character
from components import buttons as btns
from services.character_services import CharacterService

def char_selection(page: ft.Page):

    # Initialization
    database = SessionLocal()
    selected_character = None


    ### Interface ###
    page.title = "Character Selection"
    page.bgcolor = "#E4E4E4"

    grid = ft.GridView(
        expand=True,
        max_extent=220,
        child_aspect_ratio=0.55,
        spacing=10,
        run_spacing=10,
        controls=[]
    )

    def load_characters():

        nonlocal grid
        characters_query = database.query(Character).all()
        
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

        cards = [character_card(char) for char in characters_query]
        grid.controls = cards
        page.update()
        

    # Character Selection
    def select_char(character: Character):
        
        nonlocal selected_character
        selected_character = character

        for card in grid.controls:
            if card.data == character:
                card.border = ft.border.all(3, ft.Colors.BLUE)
                card.bgcolor = ft.Colors.BLUE_50
            else:
                card.border = ft.border.all(3, ft.Colors.TRANSPARENT)
                card.bgcolor = ft.Colors.WHITE
        
        page.update()
    

    # Character Delete
    def handle_character_delete(e):
        if not selected_character:
            return
        
        def confirm_delete(e):
            CharacterService.delete_character(selected_character.name)
            load_characters()
            page.close(delete_dialog)
            page.update()

        def cancel_delete(e):
            page.close(delete_dialog)

        delete_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Delete Confirmation"),
            content=ft.Text(f"Are you sure you want to delete '{selected_character.name}'?\n\nThis action cannot be undone."),
            actions=[
                ft.TextButton("Cancel", on_click=cancel_delete),
                ft.TextButton("Confirm", on_click=confirm_delete, style=ft.ButtonStyle(color=ft.Colors.RED))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.open(delete_dialog)


    # Buttons
    btn_new_char = btns.ElevatedButton1.apply_button(text_input="New Character", on_click_input=lambda e: page.go("/create_char"))
    btn_delete_char = btns.ElevatedButton1.apply_button(text_input="Delete Character", on_click_input=handle_character_delete)
    btn_start_game = btns.ElevatedButton1.apply_button(text_input="Start Game")


    # Interface Components Building
    column1 = ft.Column(controls=[btn_new_char, btn_delete_char], spacing=20)
    column2 = ft.Column(controls=[ft.Container(height=45), btn_start_game], spacing=20)
    buttons_rows = ft.Row(controls=[column1, column2], alignment=ft.MainAxisAlignment.CENTER, spacing=20)


    # Load the Characters Grid
    load_characters()

    return ft.Column(
        controls=[ft.Container(height=20), grid, ft.Container(content=buttons_rows, alignment=ft.alignment.center, expand=True, padding=ft.padding.only(top=80))],
                  expand=True,
                  horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                  scroll=ft.ScrollMode.AUTO,
    )
