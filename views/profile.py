import flet as ft


def profile_character(page: ft.Page):
    page.title = "Profile"
    page.bgcolor = "#000000"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    first_text = ft.Text("Profile Page")

    return ft.Column(controls=[first_text], 
                     expand=True,
                     horizontal_alignment=ft.CrossAxisAlignment.CENTER)
