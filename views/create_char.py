import flet as ft
from flet.core.types import CrossAxisAlignment

from models.db_manager import SessionLocal, Character
from components import buttons as btns
from services.character_services import CharacterService


def create_character(page: ft.Page):
    page.title = "Create Character"
    page.bgcolor = "#E4E4E4"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0F131C"
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = CrossAxisAlignment.CENTER

    sprite = ft.Image(
        src="char_sprites/0.Novice_Sprite.png",
        width=80,
        height=160,
        fit=ft.ImageFit.CONTAIN
    )
    
    input_name = ft.TextField(
        label="Character Name",
        width=200,
        label_style=ft.TextStyle(color="#E0E0E0"),
        border_color="#E0E0E0",
        )
    
    confirmation_text = ft.Text(
        "",
        size=16,
        weight=ft.FontWeight.BOLD,
        visible=False
    )


    def handle_character_creation(event):

        char_name = input_name.value.strip()
        results = CharacterService.create_character(char_name)

        if results["success"]:
            confirmation_text.value = results["message"]
            confirmation_text.visible = True
            confirmation_text.color = ft.Colors.GREEN_700
            input_name.value = ""

        else:
            confirmation_text.value = results["message"]
            confirmation_text.visible = True
            confirmation_text.color = ft.Colors.RED_700   

        page.update() 
    

    btn_create = btns.ElevatedButton1.apply_button(text_input="Create", on_click_input=handle_character_creation)
    btn_back = btns.ElevatedButton1.apply_button(text_input="Back", on_click_input=lambda e: page.go("/"))

    screen_content = ft.Column(controls=[sprite, input_name, confirmation_text, btn_create, btn_back],
                               horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    return ft.Container(content=screen_content,
                        border=ft.border.all(1, "#4B4B4B"),
                        margin=ft.margin.only(top=120),
                        padding=70,
                        border_radius=5
                        )
