from flet import *
from data import *

class SignUpSuccess(UserControl):
    def __init__(self, page: Page):
        self.page = page
        super().__init__()

    def login(self, event):
        self.page.go("/login")

    def home(self, event):
        self.page.go("/")
        
    def build(self):
        self.close_btn = Container(
            alignment= alignment.top_left,
            content = IconButton(
                icon = icons.CLOSE_SHARP,
                icon_color= colors.WHITE,
                on_click= self.home,
            )
        )
        self.check_mark = Container(
            padding= 5,
            bgcolor= GREEN_COLOR,
            border_radius= 35,
            height= 70,
            width = 70,
            margin= 70,
            content = Icon(
                icons.CHECK_SHARP,
                color = colors.WHITE,
                size= 30
            )
        )

        self.success = Container(
            margin= 10,
            content= Text(
                "Success!",
                color = colors.WHITE,
                size = 30,
                weight = FontWeight.BOLD,
                text_align= TextAlign.CENTER
            )
        )
        self.hint = Container(
            margin = margin.only(bottom=150),
            content= Text(
                value="You have successfully signup proceed to ",
                size= 14,
                weight= FontWeight.W_400,
                color = colors.WHITE,
                text_align = TextAlign.CENTER,
                spans=[
                    TextSpan(
                        text="Login Page",
                        style= TextStyle(
                            color= GREEN_COLOR
                        ),
                        on_click = self.login
                    )
                ]
            )
        )
    
        self.chat = Container(
            margin= 10,
            content= Text(
                "Chat with us",
                color = GREEN_COLOR,
                size = 14,
                weight = FontWeight.W_500,
                text_align= TextAlign.CENTER
            )
        )
        self.page_controls = Column(
            alignment = MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.CENTER,
            controls= [
                self.close_btn,
                self.check_mark,
                self.success,
                self.hint,
                self.chat
            ]
        )

        return self.page_controls