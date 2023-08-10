import flet as ft

COLORS = ("red", "blue", "green")
STATES_IN_US = [
                "Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", 
                "California", "Colorado", "Connecticut", "District ", "of Columbia",
                "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho",
                "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts",
                "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", 
                "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire",
                "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota",
                "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington",
                "Wisconsin", "West Virginia", "Wyoming"
            ]

def main(page: ft.Page):

    def container_clicked(e):
        clicked = ft.Text("Container clicked")
        page.add(clicked)

    page.title = "Flet App"
    page.bgcolor = ft.colors.AMBER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    text = ft.Text("Hello this is my first flet APP")

    container_list = []
    for i in range(0, 3):
        container_color = COLORS[i]
        container_list.append(
            ft.Container(
                content=ft.Text(f"Container at position {i}"),
                bgcolor=container_color,
                padding=10
            )
        )

    page.controls.append(
            ft.Row(
            controls=container_list,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.END,
            scroll=True,
            wrap=True
            )
    )
    page.update()

    test_column = ft.Column()
    listtile_column = ft.Column(
        controls=[
            ft.ListTile(
                title=ft.Text("Update location"),
                subtitle=ft.Text("Edit your current location"),
                trailing=ft.Icon(ft.icons.EDIT_LOCATION),
                leading=ft.Icon(ft.icons.EDIT_LOCATION_ALT_ROUNDED),
                selected=True
            ),
            ft.ListTile(
                        leading=ft.Icon(ft.icons.ALBUM),
                        title=ft.Text("One-line with leading and trailing controls"),
                        selected=True
            )
        ]
    )

    test_container = ft.Container(
        content=listtile_column,
        padding= 50,
        bgcolor="#FFFFFF",
        on_click=container_clicked
    )

    test_column.controls.append(test_container)

    test_container.border = ft.border.all(20, ft.colors.PINK_200)
    test_container.border_radius = ft.border_radius.all(30)

    # listView
    list_view = ft.ListView(height=300, width=300, scale=1.0)
    for state in STATES_IN_US:
        list_view.controls.append(ft.Text(state))
        page.update()

    list_view_container = ft.Container(
        content=list_view,
        bgcolor="white",
        padding=5
    )

    page.add(
        text,
        test_column,
        list_view_container
    )

    # page.controls.append(text)
    # page.update()

    # print(page.platform)

ft.app(target=main, view=ft.AppView.FLET_APP_WEB)