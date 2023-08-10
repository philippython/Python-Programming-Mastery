from flet import *


class Counter(UserControl):
    def __init__(self, initial_count):
        super().__init__()
        self.initial_count = initial_count


    def add_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        self.counter = 0
        self.text = Text(str(self.counter))
        return Row([self.text, ElevatedButton("Add", on_click=self.add_click)])