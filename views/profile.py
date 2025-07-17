import flet as ft
from models.db_manager import SessionLocal, Character
from services.sprite_selector import get_char_image_by_job
from components.data_bars import build_hp_bar, build_sp_bar


def profile_character(page: ft.Page):
    page.title = "Profile"
    page.bgcolor = "#E4E4E4"
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.CrossAxisAlignment.START


    # Sidebar
    def on_sidebar_change(e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            page.go("/"),
        elif selected_index == 1:
            pass
        elif selected_index == 2:
            pass

    sidebar_drawer = ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerDestination(label="Change Character",
                                           icon=ft.Icons.PERSON),
            ft.NavigationDrawerDestination(label="Future Menu 2",
                                           icon=ft.Icons.SQUARE),
            ft.NavigationDrawerDestination(label="Future Menu 3",
                                           icon=ft.Icons.SQUARE),
        ],
        on_change=on_sidebar_change,
    )

    sidebar_button = ft.IconButton(icon=ft.Icons.MENU, on_click=lambda e: page.open(sidebar_drawer))

    def on_navigation_change(e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            pass
        elif selected_index == 1:
            pass
        elif selected_index == 2:
            pass

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
        ft.Text(character.name, color=ft.Colors.BLACK, size=40, weight=ft.FontWeight.BOLD),

        ft.Row([ft.Icon(name=ft.Icons.MILITARY_TECH, color=ft.Colors.BLACK),
                ft.Text(f"Job: {character.job}", color=ft.Colors.BLACK, size=20)]),

        ft.Row([ft.Icon(name=ft.Icons.STAR, color=ft.Colors.BLACK),
                ft.Text(f"Level: {character.level}", color=ft.Colors.BLACK, size=20),]),

        ft.Row([ft.Icon(name=ft.Icons.TRENDING_UP, color=ft.Colors.BLACK),
                ft.Text(f"EXP: {character.exp}", color=ft.Colors.BLACK, size=20)]),

        ft.Row([ft.Icon(name=ft.Icons.PAID, color=ft.Colors.BLACK),
                ft.Text(f"Zeny: {character.zeny}z", color=ft.Colors.BLACK, size=20)]),
    ],

    )

    main_card = ft.Container(
        content=ft.Row(controls=[character_sprite, column_main_data], spacing=30),
        bgcolor=ft.Colors.GREY_300,
        border=ft.border.all(1, ft.Colors.BLACK),
        border_radius=10,
        padding=30,
        width=600,)

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
        controls=[sidebar_button, character_main_data],
        expand=True,
        height=page.height,
    )
