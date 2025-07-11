import flet as ft
from models.db_manager import SessionLocal, Character
from services.sprite_selector import get_char_image_by_job


def profile_character(page: ft.Page):
    page.title = "Profile"
    page.bgcolor = "#E4E4E4"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Get the Character selected from the previous page
    database = SessionLocal()
    name_character_ingame = page.client_storage.get("character_ingame_name")
    character = database.query(Character).filter_by(name=name_character_ingame).first()
    
    # Interface Data
    character_sprite = ft.Image(
        src=get_char_image_by_job(character.job),
        width=80,
        height=160,
        fit=ft.ImageFit.CONTAIN
    )

    character_name =  ft.Text(character.name, color=ft.Colors.BLACK)
    character_job = ft.Text(character.job, color=ft.Colors.BLACK)
    character_zeny = ft.Text(character.zeny, color=ft.Colors.BLACK)
    character_hp = ft.Text(character.hp, color=ft.Colors.BLACK)
    character_sp = ft.Text(character.sp, color=ft.Colors.BLACK)


    return ft.Column(controls=[character_sprite, character_name, character_job, character_zeny, character_hp, character_sp], 
                     expand=True,
                     horizontal_alignment=ft.CrossAxisAlignment.CENTER)
