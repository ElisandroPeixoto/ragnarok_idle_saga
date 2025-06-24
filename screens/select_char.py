import flet as ft
from db_manager import SessionLocal, Character


def select_char(page: ft.Page):
    page.title = "Character Selection"
    page.bgcolor = "#E4E4E4"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    database = SessionLocal()  # Open Database
    characters_query = database.query(Character).all()

    def character_card(char: Character):
        image = "char_sprites/0.Novice_Sprite.png"

        interface = ft.Container(
            content=ft.Column(controls=[
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

    row1 = ft.Row(
        controls=[column1, column2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )


    return ft.Column(
        controls=[ft.Container(height=20), grid, ft.Container(content=row1, alignment=ft.alignment.center, expand=True, padding=ft.padding.only(top=80))],
                  expand=True,
                  horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                  scroll=ft.ScrollMode.AUTO,
    )
