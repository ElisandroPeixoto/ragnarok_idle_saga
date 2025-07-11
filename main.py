import flet as ft
from utils.routes import route_handler
from models.db_manager import init_db
import os


def main(page: ft.Page):
    # Start Database
    init_db()

    def on_route_change(event):
        route_handler(page.route, page)

    page.on_route_change = on_route_change
    page.go(page.route)


ft.app(target=main, assets_dir="assets")  # Dev Mode
# ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER, port=8080)  # Dev Mode
# ft.app(target=main, port=int(os.getenv("PORT", 8080)))  # Prod Mode
