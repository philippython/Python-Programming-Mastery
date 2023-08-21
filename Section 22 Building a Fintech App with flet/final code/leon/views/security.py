from flet import *
from data import *

class Security(UserControl):

    def __init__(self, page: Page):
        self.page = page
        super().__init__()

    def dashboard(self, event):
        self.page.go("/dashboard")

    def build(self):
        self.top = Container(
            margin= 20 ,
            content= Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Container(
                            alignment= alignment.top_left,
                            content = IconButton(
                                icon = icons.ARROW_BACK,
                                icon_color=colors.WHITE,
                                on_click = self.dashboard
                                ),
                            ),
                            Text("Account Password", weight=FontWeight.W_500, size=15, color=colors.WHITE),  
                            Container(
                                alignment= alignment.center,
                                border_radius = 10,
                                bgcolor = GREEN_COLOR,
                                padding = 5,
                                on_click = self.dashboard,
                                content = Text("update", color= colors.WHITE, size=15, weight=FontWeight.W_400)
                            ),
                        ]
            )
        )

        self.old_password_label = Text("Old Password", size = 14, color= colors.GREY_500, weight= FontWeight.W_300)
        self.new_password_label = Text("New Password", size = 14, color= colors.GREY_500, weight= FontWeight.W_300)
        self.confirm_password_label = Text("Confirm New Password", size = 14, color= colors.GREY_500, weight= FontWeight.W_300)

        self.old_password = Container(
            margin = margin.only(left=20, right=20),
            bgcolor= colors.GREY_900,
            border_radius= 10,
            content= TextField(
                border= InputBorder.NONE,
                cursor_color= colors.BLACK,
                text_style = TextStyle(
                color = colors.BLACK
                ),
                password= True,
            )
        )

        self.new_password = Container(
            margin = margin.only(left=20, right=20),
            bgcolor= colors.GREY_900,
            border_radius= 10,
            content= TextField(
                border= InputBorder.NONE,
                cursor_color= colors.BLACK,
                text_style = TextStyle(
                color = colors.BLACK
                ),
                password= True,
            )
        )

        self.confirm_password = Container(
            margin = margin.only(left=20, right=20),
            bgcolor= colors.GREY_900,
            border_radius= 10,
            content= TextField(
                border= InputBorder.NONE,
                cursor_color= colors.BLACK,
                text_style = TextStyle(
                color = colors.BLACK
                ),
                password= True,
            )
        )

        self.security_controls = Column(
            alignment= MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.CENTER,
            controls= [
                self.top,
                self.old_password_label,
                self.old_password,
                self.new_password_label,
                self.new_password,
                self.confirm_password_label,
                self.confirm_password
            ]
        )

        return self.security_controls