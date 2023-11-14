# We are learning the basics of flet 

import flet as ft 

def main (page: ft.Page):
    page.window_width = 500
    page.window_height = 500
    page.bgcolor = '#FFC5C5'
    textField = ft.TextField()
    addBtn = ft.ElevatedButton(text="Add")

    page.add(textField,
             addBtn)

ft.app(target=main)