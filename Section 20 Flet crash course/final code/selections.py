from flet import *

def main(page: Page):
    page.title = "Input & selections"
    page.bgcolor = "white"
    page.padding = 10
    page.scroll = ScrollMode.ALWAYS
    page.theme = Theme(font_family="Arial")

    def checkbox_clicked(e):
        print("checkbox value changed")

    def radio_clicked(e):
        print(radio_group.value)

    def slider_moved(event):
        print(event.control.value)

    def page_theme_switch(event):
        if event.control.value:
            page.bgcolor= "black"
            page.update()
        else:
            page.bgcolor = "white"
            page.update()

    c1 = Switch(label="Unchecked switch", value=False, label_position=LabelPosition.LEFT)
    c2 = Switch(label="Change page theme", on_change=page_theme_switch)
    c3 = Switch(label="Disabled switch", disabled=True)
    checkbox_1 = Checkbox(label="Are you a flet developer?", fill_color="blue", label_position= LabelPosition.LEFT)
    checkbox_2 = Checkbox(label="Are you proficient with python", on_change=checkbox_clicked)
    dropdown_obj = Dropdown(
        width=200,
        autofocus=False,
        label="size",
        hint_text="Choose shoe size",
        options=[
            dropdown.Option("small"),
            dropdown.Option("medium"),
            dropdown.Option("large"),
            dropdown.Option("xlarge"),
        ]
    )

    radio_group = RadioGroup(
        on_change=radio_clicked,
        content=Column(
            [
                Radio(label="join", value="joined"),
                Radio(label="leave", value="left"),
                Radio(label="report", value="reported")
            ]
        )
    )

    page.add(
        Text("Increase brightness"),
        Slider(
            max=100,
            min=10,
            divisions=10,
            value=80,
            active_color="green",
            inactive_color="#eeeeee",
            on_change=slider_moved
        ),
        TextField(label="Textfield 1", hint_text="Job title",multiline=False),
        TextField(label="hobbies", hint_text="Your hobbies...", border="underline", border_radius=10),
        TextField(label="password", hint_text="enter your password", password=True, can_reveal_password=True),
        TextField(label="With prefix", prefix_text="https://"),
        TextField(icon=icons.ACCESS_ALARM ,label="With suffix", suffix_text=".com"),


    )
    page.update()
    page.add(checkbox_1, checkbox_2, dropdown_obj, radio_group, c1, c2, c3)

app(target=main, view=AppView.FLET_APP_WEB)