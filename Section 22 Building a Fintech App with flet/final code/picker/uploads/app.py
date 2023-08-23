from flet import *
from task import Task

class TodoApp(UserControl):
    def build(self):
        self.items_left = Text("0 items left")
        self.new_task = TextField(hint_text="What needs to be done?")
        self.tasks= Column()

        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_change,
            tabs = [Tab(text="active"), Tab(text="all"), Tab(text="completed")]
        )
        return Column(
            width=500,
            controls=[
                Row([ Text(value="Todos", style="headlineMedium")], alignment=MainAxisAlignment.CENTER),
                Row(
                    controls=[
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked)
                    ]
                ),
                Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                        Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                self.items_left,
                                OutlinedButton(
                                    text="Clear completed", on_click=self.clear_clicked
                                ),
                            ],
                        ),
                    ],
                ),
            ]
        )

    def add_clicked(self, e):
        task = Task(self.new_task.value, self.tabs_change, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def update(self):
        count = 0
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.tasks.controls:
            task.visible = (
                status == "all" 
                or (status == "active" and task.completed == False)
                or (status == "completed" and task.completed == True)
            )
            if task.completed == False:
                count += 1
        self.items_left.value = f"{count} items left"
        super().update()

    def tabs_change(self, e):
        self.update()

    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)