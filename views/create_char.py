import flet as ft
from models.db_manager import SessionLocal, Character
from components import buttons as btns


def create_character(page: ft.Page):
    page.title = "Character Selection"
    page.bgcolor = "#E4E4E4"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    sprite = ft.Image(
        src="char_sprites/0.Novice_Sprite.png",
        width=80,
        height=160,
        fit=ft.ImageFit.CONTAIN
    )
    
    input_name = ft.TextField(
        label="Character Name",
        color="#000000",
        width=200,
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        focused_border_color="#0000FF"
        )
    
    confirmation_text = ft.Text(
        "",
        color=ft.Colors.GREEN_700,
        size=16,
        weight=ft.FontWeight.BOLD,
        visible=False
    )

    def new_char(event):
        char_name = input_name.value.strip()
        if char_name:
            db = SessionLocal()

            new_character = Character(
                name=char_name,
                job="Novice"
            )

            db.add(new_character)
            db.commit()
            db.refresh(new_character)
            db.close()

            confirmation_text.value = f"Personagem '{char_name}' criado com sucesso!"
            confirmation_text.visible = True

            page.update()

    btn_create = btns.ElevatedButton1.apply_button(text_input="Create", on_click_input=new_char)
    btn_back = btns.ElevatedButton1.apply_button(text_input="Back", on_click_input=lambda e: page.go("/"))

    screen_container = ft.Column(
        controls=[sprite, input_name, confirmation_text, btn_create, btn_back], 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    return screen_container
