import flet as ft
from models.db_manager import SessionLocal, Character
from components import buttons as btns
from services.character_services import CharacterService
from services.sprite_selector import get_char_image_by_job

def char_selection(page: ft.Page):

    # Initialization
    database = SessionLocal()
    selected_character = None


    ### Interface ###
    page.title = "Character Selection"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0F131C"
    page.scroll = True

    grid = ft.GridView(
        max_extent=220,
        child_aspect_ratio=0.55,
        spacing=10,
        run_spacing=10,
        controls=[]
    )

    def load_characters():

        nonlocal grid
        characters_query = database.query(Character).all()

        # Limit the number of characters in 6
        if len(characters_query) >= 6:
            btn_new_char.disabled = True
            btn_new_char.tooltip = "You reached the limit of characters"
            btn_new_char.bgcolor = "#555555"
        else:
            btn_new_char.disabled = False
            btn_new_char.tooltip = ""
            btn_new_char.bgcolor = "#1E3A8A"
        
        # Character Cards
        def character_card(char: Character):
            image = get_char_image_by_job(char.job)

            interface = ft.Container(
                content=ft.Column(controls=[
                        ft.Image(src=image, width=80, height=160, fit=ft.ImageFit.CONTAIN),
                        ft.Text(char.name, size=18, weight=ft.FontWeight.BOLD),
                        ft.Text(char.job, size=14),
                        ft.Text(f"Level: {char.level}", size=14),
                        ft.Text(f"EXP: {char.exp}", size=14),
                        ft.Text(f"HP: {char.hp}", size=14)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    tight=True,
                    spacing=2,
                    scroll=ft.ScrollMode.AUTO
                ),
                padding=10,
                margin=10,
                border_radius=10,
                bgcolor="#2A2C3A",
                width=180,
                height=450,
                alignment=ft.alignment.center,
                shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.BLACK12, offset=ft.Offset(2, 2)),
                border=ft.border.all(3, ft.Colors.TRANSPARENT),
                data=char,
                on_click=lambda e, character_selected=char: select_char(character_selected),
            )

            return interface

        def empty_card():
            return ft.Container(
                content=ft.Text("Empty", size=16, italic=True),
                padding=10,
                margin=10,
                border_radius=10,
                bgcolor="#2A2C3A",
                width=180,
                height=450,
                alignment=ft.alignment.center,
                shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.BLACK12, offset=ft.Offset(2, 2)),
                border=ft.border.all(3, ft.Colors.TRANSPARENT),
            )

        cards = [character_card(char) for char in characters_query]

        while len(cards) < 6:
            cards.append(empty_card())  # Complete the grid with empty cards
        cards = cards[:6]  # Limit to 6 characters

        grid.controls = cards
        page.update()
        

    # Character Selection
    def select_char(character: Character):
        
        nonlocal selected_character
        selected_character = character

        page.client_storage.set("character_ingame_name", character.name)

        for card in grid.controls:
            if card.data == character:
                card.border = ft.border.all(3, ft.Colors.BLUE)
                card.bgcolor = "#111217"
            else:
                card.border = ft.border.all(3, ft.Colors.TRANSPARENT)
                card.bgcolor = "#2A2C3A"
        
        page.update()
    

    # Character Delete
    def handle_character_delete(e):
        if not selected_character:
            return
        
        def confirm_delete(e):
            CharacterService.delete_character(selected_character.name)
            page.close(delete_dialog)
            load_characters()
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
    btn_new_char = btns.ElevatedButton1.apply_button(text_input="New Character",
                                                     on_click_input=lambda e: page.go("/create_char"))
    btn_delete_char = btns.ElevatedButton1.apply_button(text_input="Delete Character",
                                                        on_click_input=handle_character_delete)
    btn_start_game = btns.ElevatedButton1.apply_button(text_input="Start Game",
                                                       on_click_input=lambda e: page.go("/profile"),
                                                       bgcolor="#3B82F6",
                                                       color="#000000")


    # Interface Components Building
    column1 = ft.Column(controls=[btn_new_char, btn_delete_char], spacing=20)
    column2 = ft.Column(controls=[ft.Container(height=45), btn_start_game], spacing=20)
    buttons_rows = ft.Row(controls=[column1, column2], alignment=ft.MainAxisAlignment.CENTER, spacing=20)


    # Load the Characters Grid
    load_characters()

    return ft.Column(
        controls=[ft.Container(content=ft.Text("Characters", size=38),
                               padding=30,
                               margin=10),
                  ft.Row(controls=[ft.Container(content=grid,
                                                width=1200,
                                                alignment=ft.alignment.center)],
                         alignment=ft.MainAxisAlignment.CENTER,
                         expand=True,
                         scroll=ft.ScrollMode.AUTO),
                  ft.Container(content=buttons_rows,
                               alignment=ft.alignment.center,
                               expand=True,
                               padding=ft.padding.only(top=80))],
                  expand=True,
                  horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                  scroll=ft.ScrollMode.AUTO,
    )
