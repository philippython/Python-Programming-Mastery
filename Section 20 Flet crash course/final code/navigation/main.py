from flet import *


def main(page: Page):
    page.title = "Navigation"
    page.bgcolor = "white"
    page.padding = 10
    page.scroll = ScrollMode.ALWAYS
    page.navigation_bar = NavigationBar(
        label_behavior= NavigationBarLabelBehavior.ONLY_SHOW_SELECTED,
        destinations=[
            NavigationDestination(icon=icons.EXPLORE, selected_icon=icons.EXPLORE_OFF, label="Explore"),
            NavigationDestination(icon=icons.COMMUTE, label="Commute"),
            NavigationDestination(
                icon=icons.BOOKMARK_BORDER,
                selected_icon=icons.BOOKMARK,
                label="Explore",
            ),
        ]
    )

    def add_button_clicked(event):
        page.dialog = add_alert_dialog
        page.dialog.open = True
        page.update()

    def close_dlg(event):
        page.dialog.open = False
        page.update()

    add_alert_dialog = AlertDialog(
        title= Text("Add Page"),
        content= Text("Would you like to add a page?"),
        modal=False,
        title_padding=20,
        actions= [
            TextButton(text="Yes", on_click=close_dlg),
            TextButton(text="No", on_click=close_dlg)
        ],
        actions_alignment= MainAxisAlignment.CENTER
        # content_padding=100
    )


    appbar = AppBar(
        title= Text("App Bar"),
        center_title = False,
        leading= Icon(icons.PALETTE),
        leading_width= 30,
        bgcolor= colors.OUTLINE_VARIANT,
        color=colors.RED_ACCENT_700,
        toolbar_height=60,
        actions= [
            IconButton(icons.WB_SUNNY_OUTLINED),
            IconButton(icons.WALLET_GIFTCARD),
            PopupMenuButton(
                items=[
                    PopupMenuItem(icon=icons.VERIFIED, text="verfied"),
                    PopupMenuItem(icon=icons.ACCESS_ALARM, text="alarm")
                ]
            )
        ]
    )

    rail = NavigationRail(
        bgcolor=colors.SURFACE_VARIANT,
        leading= FloatingActionButton(icon=icons.ADD, on_click=add_button_clicked),
        group_alignment= 0.6,
        # min_extended_width=500,
        # extended=True,
        # selected_index=2,
        label_type = NavigationRailLabelType.ALL,
        trailing= Icon(icons.LOGOUT),
        destinations= [
            NavigationDestination(icon=icons.FAVORITE_OUTLINE, selected_icon=icons.FAVORITE, label="Favorite"),
            NavigationRailDestination(
                icon_content=Icon(icons.BOOKMARK_BORDER),
                selected_icon_content=Icon(icons.BOOKMARK),
                label="Second",
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon_content=Icon(icons.SETTINGS),
                label_content=Text("Settings"),
            ),
        ]
    )

    row = Row(
        height=650,
        expand=False,
        controls= [
            rail
        ]
    )

    def close_banner(e):
        page.banner.open = False
        page.update()

    page.banner = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(icons.WARNING_AMBER_ROUNDED, color=colors.AMBER, size=40),
        content=Text(
            "Oops, there were some errors while trying to delete the file. What would you like me to do?"
        ),
        actions=[
            TextButton("Retry", on_click=close_banner),
            TextButton("Ignore", on_click=close_banner),
            TextButton("Cancel", on_click=close_banner),
        ],
    )

    def show_banner_click(e):
        page.banner.open = True
        page.update()

    page.add(ElevatedButton("Show Banner", on_click=show_banner_click))

    page.add(appbar, row)
    page.update()

app(main, view=AppView.FLET_APP_WEB)
