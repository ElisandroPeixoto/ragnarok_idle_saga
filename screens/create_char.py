import flet as ft
from db_manager import SessionLocal, Character

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

            snack = ft.SnackBar(
            ft.Text(f"Personagem '{char_name}' criado com sucesso!"),
            bgcolor=ft.Colors.GREEN_700,
            duration=3000
            )
            page.overlay.append(snack)
            snack.open = True
            page.update()

    btn_create = ft.ElevatedButton(text="Create", on_click=new_char)
    btn_back = ft.ElevatedButton(text="Back", on_click=lambda e: page.go("/"))


    screen_container = ft.Column(
        controls=[sprite, input_name, btn_create, btn_back], 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    return screen_container
