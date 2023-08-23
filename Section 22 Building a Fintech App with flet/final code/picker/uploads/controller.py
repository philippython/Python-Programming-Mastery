import flet as ft
from app import TodoApp

def main( page : ft.Page):

    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp()
    page.add(todo)

ft.app(target=main, view=ft.AppView.FLET_APP_WEB)