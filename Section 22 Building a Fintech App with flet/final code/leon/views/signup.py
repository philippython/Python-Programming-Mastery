from flet import *
from data import *
import random

class SignUp(UserControl):

    def __init__(self, page: Page):
        self.page = page
        super().__init__()

    def to_onboarding(self, event):
        self.page.go("/")

    def confirm(self, event):
        if self.email.content.value != "" :
            if self.password.content.value == self.confirm_password.content.value and len(self.password.content.value) >= 5:
                user_instance = {
                    "full_name" : self.fullname.content.value,
                    "email" : self.email.content.value,
                    "password" : self.password.content.value,
                    "account_no" : str(random.randrange(1_000_000_000_000_000, 2_000_000_000_000_000)),
                    "balance" : 1500.00,
                    "transactions" : []
                }
                if self.page.client_storage.contains_key("users"):
                    # adding new users to "users" list
                    user_data = self.page.client_storage.get("users")
                    user_data.append(user_instance)
                    self.page.client_storage.set("users", user_data)

                    # adding new accoutnumber to "account_numbers"
                    account_details = self.page.client_storage.get("account_numbers")
                    account_details[self.fullname.content.value] = user_instance["account_no"]
                    self.page.client_storage.set("account_numbers", account_details)
                else:
                    self.page.client_storage.set("users", [user_instance])
                    self.page.client_storage.set("account_numbers", {self.fullname.content.value : user_instance["account_no"]})

                self.page.go("/signup/success")

    def build(self):
        self.back_arrow = Container(
            alignment= alignment.top_left,
            content = IconButton(
                icon= icons.ARROW_BACK,
                icon_color=colors.WHITE,
                on_click = self.to_onboarding,
            ),
        )
        self.email_passowrd = Container(
            margin= margin.only(top=0),
            content= Text(
                        "Email & Password",
                        color = colors.WHITE,
                        size =  13,
                        weight= FontWeight.BOLD,
                        spans= [
                            TextSpan(
                                "\nOpen this account with few details",
                                style = TextStyle(
                                    weight= FontWeight.W_300,
                                )
                            )
                        ]
                    )
        )
        self.email_label = Text("Email Address", size = 14, color= colors.WHITE, weight= FontWeight.W_300)
        self.password_label = Text("Enter Password", size = 14, color= colors.WHITE, weight= FontWeight.W_300)
        self.confirm_password_label = Text("Confirm Password", size = 14, color= colors.WHITE, weight= FontWeight.W_300)

        self.fullname = Container(
            bgcolor= colors.WHITE,
            border_radius= 10,
            content= TextField(
                border= InputBorder.NONE,
                cursor_color= colors.BLACK
            )
        )
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
        
        self.confirm_password = Container(
            bgcolor= colors.WHITE,
            border_radius= 10,
            content= TextField(
                border= InputBorder.NONE,
                cursor_color= colors.BLACK,
                password= True,
            )
        )
        self.signup_btn = Container(
            on_click= self.confirm,
            margin= margin.only(top=100, bottom=20, left=80),
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
                    content= Text("Sign Up",
                                  size=16,
                                  weight= FontWeight.W_700
                        )
                )
            )
        )
        return Column(
            alignment= MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.START,
            controls = [
                self.back_arrow,
                self.email_passowrd,
                self.fullname,
                self.email_label,
                self.email,
                self.password_label,
                self.password,
                self.confirm_password_label,
                self.confirm_password,
                self.signup_btn
            ]
        )

