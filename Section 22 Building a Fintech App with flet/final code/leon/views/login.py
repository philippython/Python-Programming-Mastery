from flet import *
from data import *

class Login(UserControl):
    def __init__(self, page: Page):
        self.page = page
        super().__init__()

    def home(self, event):
        self.page.go("/")

    def login(self, event):
        self.page.go("/dashboard")
        
    def build(self):
        self.back_arrow = Container(
            alignment= alignment.top_left,
            content = IconButton(
                icon= icons.ARROW_BACK,
                icon_color=colors.WHITE,
                on_click = self.home,
            ),
        )

        self.help = Container(
            bgcolor = colors.GREY_800,
            height= 40,
            width= 40,
            border_radius= 20,
            alignment= alignment.center,
            content= Text(
                "?",
                color= colors.WHITE,
                size = 30,
                weight= FontWeight.W_400
            )
        )

        self.image = Container(
            margin= margin.symmetric(horizontal=80, vertical=50),
            content= Image(
                src = LOGIN_IMAGE_URL
            )
        )
        self.email_label = Text("Email", size = 14, color= colors.WHITE, weight= FontWeight.W_300)
        self.password_label = Text("Enter Password", size = 14, color= colors.WHITE, weight= FontWeight.W_300)
        
        self.email = Container(
            bgcolor= colors.WHITE,
            border_radius= 10,
            content= TextField(
                border= InputBorder.NONE,
                cursor_color= colors.BLACK
            )
        )

        self.password = Container(
            bgcolor= colors.WHITE,
            border_radius= 10,
            content= TextField(
                color= colors.BLACK,
                border= InputBorder.NONE,
                cursor_color= colors.BLACK,
                password= True,
            )
        )

        self.login_btn = Container(
            on_click= self.login,
            margin= margin.only(top=120, bottom=20, left=70),
            content= ElevatedButton(
                style= ButtonStyle(
                    color= colors.WHITE,
                    bgcolor= GREEN_COLOR,
                    shape=RoundedRectangleBorder(radius=10),
                ),
                content= Container(
                    alignment= alignment.center,
                    padding= 10,
                    height= 50,
                    width= 100,
                    content= Text("Login",
                                  size=16,
                                  weight= FontWeight.W_700
                        )
                )
            )
        )
        self.page_controls = Column(
            alignment= MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.START,
            controls= [
                Row(
                    spacing= 200,
                    controls=[
                        self.back_arrow,
                        self.help,
                    ]
                ),
                self.image,
                self.email_label,
                self.email,
                self.password_label,
                self.password,
                self.login_btn
            ]
        )

        return self.page_controls