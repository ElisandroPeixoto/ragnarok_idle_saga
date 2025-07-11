import flet as ft


def build_hp_bar(current_hp: int, max_hp: int, bar_width: int = 300):
    hp_percent = current_hp/max_hp

    if hp_percent > 0.6:
        color = ft.Colors.RED_200
    elif hp_percent > 0.3:
        color = ft.Colors.RED_400
    else:
        color = ft.Colors.RED_800

    
    hp_bar = ft.Container(
        width=bar_width,
        padding=10,
        bgcolor=ft.Colors.GREY_300,
        border_radius=5,
        content=ft.Column([
            ft.Container(
                width=bar_width * hp_percent,
                height=15,
                bgcolor=color,
                border_radius=5
            ),
            ft.Text(f"{current_hp}/{max_hp}", size=12, color=ft.Colors.BLACK)
        ])
    )

    return hp_bar


def build_sp_bar(current_sp: int, max_sp: int, bar_width: int = 300):
    sp_percent = current_sp/max_sp

    if sp_percent > 0.6:
        color = ft.Colors.BLUE_200
    elif sp_percent > 0.3:
        color = ft.Colors.BLUE_400
    else:
        color = ft.Colors.BLUE_800

    
    sp_bar = ft.Container(
        width=bar_width,
        padding=10,
        bgcolor=ft.Colors.GREY_300,
        border_radius=5,
        content=ft.Column([
            ft.Container(
                width=bar_width * sp_percent,
                height=15,
                bgcolor=color,
                border_radius=5
            ),
            ft.Text(f"{current_sp}/{max_sp}", size=12, color=ft.Colors.BLACK)
        ])
    )

    return sp_bar