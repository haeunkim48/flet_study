import flet as ft
from flet import UserControl, TextField, InputBorder, Page, ControlEvent, app


class TextEditor(UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.textfield = TextField(
            multiline=True,
            autofocus=True,
            border=InputBorder.NONE,
            min_lines=40,
            on_change=self.save_text,
            content_padding=30,
            cursor_color='yellow'
        )

    def save_text(self, e: ControlEvent) -> None:
        with open('save.txt', 'w') as f:
            f.write(self.textfield.value)

    def read_text(self) -> str:
        try:
            with open('save.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            self.textfield.hint_text = "Welcome to the text editor!"
            return ""

    def build(self) -> TextField:
        self.textfield.value = self.read_text()
        return self.textfield


def main(page: Page) -> None:
    page.title = "texteditor"
    page.scroll = True
    page.add(TextEditor())


if __name__ == "__main__":
    ft.app(target=main)