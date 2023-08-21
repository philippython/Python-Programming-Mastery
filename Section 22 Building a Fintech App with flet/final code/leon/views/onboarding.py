from flet import *
from data import *

class OnBoarding(UserControl):
    
    def __init__(self, page: Page):
        self.page = page
        super().__init__()

    def start(self, event):
        self.back_arrow.content.visible = True
        self.eclipse.visible = False
        self.welcome_text.visible = False
        self.start_btn.visible = False
        self.sign_in.visible = False
        self.terms_privacy.visible = True
        self.continue_btn.visible = True
        self.terms_check.visible = True

        self.update()

    def back_home(self, event):
        
        self.back_arrow.content.visible = False
        self.eclipse.visible = True
        self.welcome_text.visible = True
        self.start_btn.visible = True
        self.sign_in.visible = True
        self.terms_privacy.visible = False
        self.continue_btn.visible = False
        self.terms_check.visible = False

        self.update()

    def sign_up(self, event):
        self.page.go("/signup")

    def login(self, event):
       self.page.go("/login")
       
    def build(self):

        self.eclipse = Container(
            margin= margin.only(top= 20, bottom=20),
            content= Image(
                src = "assets/images/Ellipse 45.png"
            )
        )
        self.welcome_text = Text(
            "Welcome to your freedom.",
            color= colors.WHITE,
            size = 25,
            weight= FontWeight.W_900,
            text_align= TextAlign.CENTER
        )

        self.start_btn = Container(
            margin= margin.only(top=40, bottom=20),
            content= ElevatedButton(
                on_click = self.start, 
                style= ButtonStyle(
                    color= colors.WHITE,
                    bgcolor= GREEN_COLOR,
                    shape=RoundedRectangleBorder(radius=10),
                ),
                content= Container(
                    alignment= alignment.center,
                    padding= 20,
                    content= Text("Start",
                                  size=16,
                                  weight= FontWeight.W_700
                                  )
                )
            )
        )
        self.sign_in = Container(
            content= Text("Have an account? ",
                        color= colors.WHITE,
                        spans = [
                            TextSpan (
                                text= "sign in",
                                style= TextStyle(
                                    color= GREEN_COLOR
                                ),
                                on_click= self.login
                            )
                        ]
                    )
            )
        self.back_arrow = Container(
            alignment= alignment.top_left,
            content = IconButton(
                icon = icons.ARROW_BACK,
                visible=False, 
                icon_color=colors.WHITE,
                on_click = self.back_home
            ),
        )
        self.terms_privacy = Container(
            visible= False,
            bgcolor= colors.WHITE,
            border_radius= 10,
            height= 50, 
            width= 300,
            margin= margin.only(bottom=150),
            content= Row(
                alignment= MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Container(
                        bgcolor = GREEN_COLOR,
                        height = 50,
                        width = 150,
                        padding = 5,
                        border_radius = 10,
                        alignment = alignment.center,
                        content= Text(
                            "Terms",
                            color = colors.WHITE,
                            size=14,
                            weight= FontWeight.W_700
                        ),
                    ),
                    Container(
                        bgcolor = colors.WHITE,
                        padding = padding.only(right=25),
                        height = 50,
                        alignment = alignment.center,
                        content= Text(
                            "Privacy",
                            color = colors.BLACK,
                            size=14,
                            weight= FontWeight.W_700
                        )
                    )
                ]
            )
        )

        self.terms_check = Container(
            visible= False,
            content= Column(
                [
                Container(
                    bgcolor = colors.GREEN_400,
                    border_radius = 10,
                    height = 50,
                    padding = 5,
                    content=Row(
                        controls= [
                            Container(
                            border_radius = 20,
                            bgcolor= colors.WHITE,
                            content= Icon(icons.CHECK_SHARP, color=GREEN_COLOR)
                            ),
                            Text("I accept the terms of this service", 
                                color = colors.WHITE,
                                size=13,
                                weight= FontWeight.W_700 
                            )
                        ] 
                    )
                ),
                Container(
                    bgcolor = colors.GREEN_400,
                    border_radius = 10,
                    padding = 5,
                    height = 50,
                    content=Row(
                        controls= [
                            Container(
                            border_radius = 20,
                            bgcolor= colors.WHITE,
                            content= Icon(icons.CHECK_SHARP, color=GREEN_COLOR)
                            ),
                            Text("I consent to the privacy of policy",
                                color = colors.WHITE,
                                size=13,
                                weight= FontWeight.W_700
                                )
                        ] 
                    )
                ),
                ]
            )
        )
        self.continue_btn = Container(
            visible= False,
            on_click= self.sign_up,
            margin= margin.only(top=100, bottom=20),
            content= ElevatedButton(
                on_click = self.start, 
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
                    content= Text("continue",
                                  size=16,
                                  weight= FontWeight.W_700
                                  )
                )
            )
        )
        self.welcome_page = Column(
            alignment= MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            controls= [
                self.back_arrow,
                self.eclipse,
                self.welcome_text,
                self.start_btn,
                self.sign_in,
                self.terms_privacy,
                self.terms_check,
                self.continue_btn
            ]
        )
        
        return self.welcome_page