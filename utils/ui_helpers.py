import flet as ft
from models.db_manager import Character, SessionLocal


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
            shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.BLACK12, offset=ft.Offset(2, 2))
        )

        return interface
