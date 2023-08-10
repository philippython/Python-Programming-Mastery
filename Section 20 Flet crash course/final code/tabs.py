from flet import *


def main(page: Page):

    page.title = "Tabs"
    page.bgcolor = "white"
    page.padding = 10
    page.scroll = ScrollMode.ALWAYS
    page.theme = Theme(font_family="Verdana")

    def elevated_button_clicked(e):
        page.add(Text("Elevated button has been clicked"))

    def change_avatar(e):
        pass

    avatar = Stack(
        controls=[
            CircleAvatar(
            foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
            content= Icon(icons.IMAGE)
            ),
            Container(
                content=CircleAvatar(bgcolor="green", radius=5),
                alignment=alignment.bottom_left,
                width=40,
                height=40
            )
        ]
    )
    
    
    tabs = Tabs(
        selected_index=1,
        animation_duration=50,
        divider_color="red",
        tabs=[
            Tab(
                content=Column(
                    controls=[
                        avatar,
                        FloatingActionButton(icon="image", on_click=change_avatar),
                        Text(
                            "$4,500USD",
                            size=50,
                            color="white",
                            italic=False,
                            bgcolor=colors.BLUE_300,
                            weight=FontWeight.W_100,
                            style=TextThemeStyle.HEADLINE_SMALL,
                            font_family="consolas",
                            selectable=False
                        ),
                        Row(
                            [
                                IconButton(
                                    icon=icons.PAUSE_CIRCLE_FILLED_ROUNDED,
                                    icon_color="blue400",
                                    icon_size=40,
                                    tooltip="Pause record",
                                ),
                                IconButton(
                                    icon=icons.DELETE_FOREVER_ROUNDED,
                                    icon_color="pink600",
                                    icon_size=40,
                                    tooltip="Delete record",
                                ),
                            ]
                        ),
                        PopupMenuButton(
                            # icon=icons.ABC,
                            items=[
                                PopupMenuItem(
                                    text="rich"
                                ),
                                PopupMenuItem(
                                    text="average"
                                ),
                                PopupMenuItem(
                                    text="poor"
                                )
                            ]
                        )
                    ]
                ),
                text = "Check Balance",
                icon = icons.ACCOUNT_BALANCE
            ),
            Tab(
                content=Column(
                    controls = [
                        Image(
                            src= "assets/images/fintech app.PNG",
                            height=300,
                            width=400,
                            border_radius=40,
                            # color="green",
                            error_content= Text("Image not found")
                        ),
                        Text("Helping ",
                             size=25,
                             bgcolor="pink200",
                             spans=[
                                TextSpan(
                                    text="dreams",
                                    style = TextStyle(
                                        bgcolor="green",
                                        italic=True,  
                                    )
                                ),
                                TextSpan(
                                    text=" come true, one "
                                ),
                                TextSpan(
                                    text="account",
                                    style = TextStyle(
                                        bgcolor="green",
                                        italic=True, 
                                    )
                                ),
                                TextSpan(
                                    text=" at a time"
                                )
                             ]
                            ),
                            Row(
                                controls=[
                                    ElevatedButton(text="Get Started", icon=icons.START, on_click=elevated_button_clicked),
                                    ElevatedButton(text="Logout", disabled=False),
                                    FilledButton(text="Move to the next page"),
                                    FilledTonalButton("Button with icon", icon="add"),

                                ],
                                wrap=True
                            )

                    ]
                ),
                text = "Top-up Account",
                # icon= Icon(icons.BALANCE)
            ),
            Tab(
                content=Container(
                    content=Column(
                            controls=[
                                Text("Make a withdrawal"),
                                Icon(icons.ACCOUNT_BALANCE_WALLET, color="blue", tooltip="Wallet balance"),
                                Text("Determinate Progress Bar"),
                                ProgressBar(bgcolor="#eeeeee", color="blue", value=0.4, bar_height=20),
                                Text("Indeterminate Progress Ring"),
                                ProgressBar(bgcolor="#eeeeee", color="blue"),
                                Text("Determinate ProgressBProgressBar"),
                                ProgressRing(bgcolor="#eeeeee", color="blue", value=0.4, tooltip="Withdrawal progress", ),
                                Text("Indeterminate Progress Ring"),
                                ProgressRing(bgcolor="#eeeeee", color="blue")


                            ]
                        )
                ),
                text = "Make a Withdrawal",
                
            )
        ]
    )

    
    page.update()
    page.add(tabs)


app(target=main, view=AppView.FLET_APP_WEB, assets_dir="assets")



