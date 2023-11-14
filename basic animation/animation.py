import flet as ft
from flet import *

def main(page: Page):
    page.title = 'Flet Animation Icons'

    # alignment
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    # main row
    _main_row = Container(
        width=280,
        height=50,
        border_radius=35,
        bgcolor='pink',

        content=Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[],
        ),
    )

    # icon list
    _icon_list = [
        icons.PERSON_ADD,
        icons.SEARCH_ROUNDED,
        icons.FAVORITE_ROUNDED,
        icons.MAP_ROUNDED,
        icons.DISCORD_ROUNDED
    ]

    def _animate_icon(e):
        if e.data:  # Check if e.data is True
            if e.control.scale != transform.Scale(0.75):
                e.control.scale = transform.Scale(0.75)
                e.control.scale.update()
            else:
                e.control.scale = 1
                e.control.scale.update()
        else:
            e.control.scale = 1
            e.control.scale.update()

    for icon in _icon_list:
        _main_row.content.controls.append(
            Container(
                on_hover=lambda e: _animate_icon(e),
                animate=animation.Animation(duration=600, curve='decelerated'),
                scale=transform.Scale(1),
                content=IconButton(
                    icon=icon,
                    icon_size=22,
                )
            )
        )

    _main_container = Container(
        width=290,
        height=590,
        border_radius=35,
        bgcolor='black',
        alignment=alignment.bottom_center,
        padding=20,
        content=_main_row
    )

    page.add(_main_container)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
