from flet import *
import data
import random

COLORS = ("red", "blue", "green", "white", "black")

def main(page: Page):
    page.title = "GridView"
    page.bgcolor = "white"
    page.padding = 10
    page.scroll = ScrollMode.ALWAYS

    page.add(
        ResponsiveRow(
            controls=[
                Container(
                    Text("Column 1"),
                    padding=5,
                    bgcolor=colors.YELLOW,
                    col = {"sm": 12, "lg":6, "xs": 3}
                ),
                Container(
                    Text("Column 2"),
                    padding=5,
                    bgcolor=colors.GREEN,
                    col = 6
                ),
                Container(
                    Text("Column 3"),
                    padding=5,
                    bgcolor=colors.BLUE,
                    col = 6
                ),
                Container(
                    Text("Column 4"),
                    padding=5,
                    bgcolor=colors.PINK_300,
                    col = 6
                ),
            ],
        ),
        ResponsiveRow(
            controls=[
                TextField(label="TextField 1"),
                TextField(label="TextField 2"),
                TextField(label="TextField 3"),
            ],
        ),
    )

    data_table = DataTable(
        columns=[
            DataColumn(Text("official name")),
            DataColumn(Text("common name")),
            DataColumn(Text("flag"))
        ],
    )

    for country in data.json_data:
        flag = country["flags"]["png"]
        official_name = country["name"]["official"]
        common_name = country["name"]["official"]

        data_table.rows.append(
            DataRow(
            cells=[
                DataCell(Text(official_name)),
                DataCell(Text(common_name)),
                DataCell(Text(flag))
            ]
            )
        )
    page.add(data_table)
    # grid_view = GridView(
    #     expand=1,
    #     child_aspect_ratio=1.0,
    #     max_extent=100,
    #     padding=5,
    #     auto_scroll=True,
    #     spacing=20
    # )

    # for i in range(1, 91):
    #     grid_view.controls.append(
    #         Container(
    #         content=Text(f"Container {i}"),
    #         padding=10,
    #         bgcolor=random.choice(COLORS),
    #         )
    #     )
    #     page.update()

    # page.update()
    # page.add(grid_view)
    
app(target=main, view=AppView.FLET_APP_WEB)











