from flet import *

class Task(UserControl):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.task_name = task_name
        self.completed = False
        self.task_status_change = task_status_change
        self.task_delete = task_delete

    def build(self):
        self.new_chat = Container(
                border_radius=10,
                border = border.all(1, colors.GREY_500),
                padding=5,
                content = TextButton(
                    icon=icons.ADD,
                    icon_color= colors.GREY_500,
                    style= ButtonStyle(
                        color= colors.GREY_500
                )
            )
        )

        self.new_chat = Container(
                border_radius=10,
                border = border.all(1, colors.GREY_500),
                padding=5,
                content = TextButton(
                    text="New chat",
                    icon=icons.ADD,
                    icon_color= colors.GREY_500,
                    style= ButtonStyle(
                        color= colors.GREY_500
                )
            )
        )
        self.display_task = Checkbox(label=self.task_name, value=False, on_change=self.status_changed)
        self.edit_name = TextField(expand=1)

        self.display_view = Row(
            alignment = MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment = CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Edit ToDo",
                            on_click=self.edit_clicked
                        ),
                        IconButton(
                            icon=icons.DELETE_OUTLINED,
                            tooltip="Delete ToDo",
                            on_click=self.delete_clicked
                        )
                    ]
                )
            ]
        )

        self.edit_view = Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            visible=False,
            controls=[
                self.edit_name,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                )
            ]
        )
        return Column(controls=[self.display_view, self.edit_view])

    def status_changed(self, e):
        self.completed = self.display_task.value
        self.task_status_change(self)

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.task_delete(self)