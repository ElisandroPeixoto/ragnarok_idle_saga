import flet as ft
from dataclasses import dataclass


@dataclass
class ElevatedButton1:
    text: str
    width = 180
    height = 45
    bgcolor = "#1E3A8A"
    color="#E0E0E0"

    @classmethod
    def apply_button(cls, text_input: str, on_click_input=None, **kwargs):
        """Create a new ElevatedButton1"""

        return ft.ElevatedButton(
            text=text_input,
            width=kwargs.pop("width", cls.width),
            height=kwargs.pop("heigh",cls.height),
            bgcolor=kwargs.pop("bgcolor",cls.bgcolor),
            color=kwargs.pop("color",cls.color),
            on_click=on_click_input,
            **kwargs
        )
