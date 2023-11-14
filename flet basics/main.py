import flet as ft 

def main (page: ft.Page):
    page.title = 'HELLO WORLD'
    
    def on_click_handler(e):
        print ("You pushed the button", text_field.value)
        row.controls.append(ft.Text (text_field.value))
        text_field.value = ""
        page.update()

    page.add(ft.Text ('HELLO'))
    row = ft.Row()
    page.add(row)
    
    text_field = ft.TextField (hint_text ="Please write your name.", on_submit=on_click_handler)
    page.add (text_field)

  
    page.add(ft. ElevatedButton("Push", on_click = on_click_handler))


    page.update()
ft.app(target = main)