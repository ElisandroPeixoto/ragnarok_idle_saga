import flet as ft
from db_manager import SessionLocal, Character


def select_char(page: ft.Page):
    page.title = "Character Selection"
    page.bgcolor = "#E4E4E4"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    database = SessionLocal()  # Open Database
    characters_query = database.query(Character).all()

    def character_card(char: Character):
        image = "char_sprites/0.Novice_Sprite.png"

        interface = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(src=image, width=80, height=160, fit=ft.ImageFit.CONTAIN),
                    ft.Text(char.name, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(char.job, size=14, color=ft.Colors.GREY),
                    ft.Text(f"Level: {char.level}", size=14),
                    ft.Text(f"EXP: {char.exp}", size=14),
                    ft.Text(f"HP: {char.hp}", size=14)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                tight=True,
                spacing=2
            ),
            padding=10,
            margin=10,
            border_radius=10,
            bgcolor=ft.Colors.WHITE,
            width=180,
            height=280,
            alignment=ft.alignment.center,
            shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.BLACK12, offset=ft.Offset(2, 2))
        )

        return interface
    
    cards = [character_card(char) for char in characters_query]

    grid = ft.GridView(
        expand=True,
        max_extent=220,
        child_aspect_ratio=0.65,
        spacing=10,
        run_spacing=10,
        controls=cards
    )


    button = ft.ElevatedButton(text="New Char", on_click=lambda e: page.go("/create_char"))

    return ft.Column(
        controls=[button,
                  ft.Container(height=20),
                  grid],
                  expand=True,
                  horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                  scroll=ft.ScrollMode.AUTO,
    )
