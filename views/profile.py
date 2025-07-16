import flet as ft
from models.db_manager import SessionLocal, Character
from services.sprite_selector import get_char_image_by_job
from components.data_bars import build_hp_bar, build_sp_bar


def profile_character(page: ft.Page):
    page.title = "Profile"
    page.bgcolor = "#E4E4E4"
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT

    def on_navigation_change(e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            print("Profile Selected")  # Debug
        elif selected_index == 1:
            print("Inventory Selected")  # Debug
        elif selected_index == 2:
            print("Maps Selected")  # Debug

    page.navigation_bar = ft.NavigationBar(
        destinations=[ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Profile"),
                      ft.NavigationBarDestination(icon=ft.Icons.INVENTORY, label="Inventory"),
                      ft.NavigationBarDestination(icon=ft.Icons.MAP, label="Maps")],
        selected_index=0,
        on_change=on_navigation_change,
    )

    # Get the Character selected from the previous page
    database = SessionLocal()
    name_character_ingame = page.client_storage.get("character_ingame_name")
    character = database.query(Character).filter_by(name=name_character_ingame).first()
    

    ## Main Card - Character Data
    character_sprite = ft.Image(
        src=get_char_image_by_job(character.job),
        width=80,
        height=160,
        fit=ft.ImageFit.CONTAIN
    )

    column_main_data = ft.Column(controls=[
        ft.Text(character.name, color=ft.Colors.BLACK, size=20),
        ft.Text(f"Job: {character.job}", color=ft.Colors.BLACK), 
        ft.Text(f"Level: {character.level}", color=ft.Colors.BLACK), 
        ft.Text(f"EXP: {character.exp}", color=ft.Colors.BLACK),
        ft.Text(f"Zeny: {character.zeny}z", color=ft.Colors.BLACK)],
        
        alignment=ft.MainAxisAlignment.CENTER)

    main_card = ft.Row(controls=[character_sprite, column_main_data])

    character_data_card = ft.Container(
        content=main_card
        )

    ## HP and SP
    hp_and_sp_bars = ft.Container(
        content=ft.ResponsiveRow(
            controls=[ft.Column([build_hp_bar(character.hp, character.max_hp)], col={"sm": 12, "md": 6}), 
                      ft.Column([build_sp_bar(character.sp, character.max_sp)], col={"sm": 12, "md": 6})]),
        expand=True,
        width=600
        )

    ## Layout Building
    character_main_data = ft.Container(
        content=ft.Column(controls=[character_data_card, hp_and_sp_bars]),
        expand=True,
    )

    return ft.Column(
        controls=[character_main_data],
        expand=True,
        height=page.height,
    )
