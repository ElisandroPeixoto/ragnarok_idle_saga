import flet as ft
from dataclasses import dataclass


@dataclass
class ElevatedButton1:
    text: str
    width = 180
    height = 45
    bgcolor = ft.Colors.BLUE_300
    color=ft.Colors.BLACK

    @classmethod
    def apply_button(self, text_input: str, on_click_input=None, **kwargs):
        """Create a new ElevatedButton1"""

        return ft.ElevatedButton(
            text=text_input,
            width=self.width,
            height=self.height,
            bgcolor=self.bgcolor,
            color=self.color,
            on_click=on_click_input,
            **kwargs
        )
