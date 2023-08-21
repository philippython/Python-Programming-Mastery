from flet import *
from data import *

class Transfer(UserControl):
    def __init__(self, page):
        self.page = page
        super().__init__()

    def dashboard(self, event):
        self.page.go("/dashboard")
    
    def transfer(self, event):
        self.page_controls.clear()
        self.page_controls.append(self.receiver_view)
        self.update()
        self.page.go("/transfer")
    
    def account_number_update(self, event):
        if len(event.control.value) == 19:
            self.to_amount(event)
            self.update()

    def to_amount(self, event):
        self.page_controls.clear()
        self.page_controls.append(self.amount_view)
        self.update()

    def send(self, text):
        self.page.go("/transfer-successful")

    def build(self):
        self.page_description = Container(
            margin= 20 ,
            content= Row(
                        controls=[
                            Container(
                            alignment= alignment.top_left,
                            content = IconButton(
                                icon = icons.ARROW_BACK,
                                icon_color=colors.WHITE,
                                on_click = self.dashboard
                                ),
                            ),
                            Text("Transfer to friend", weight=FontWeight.W_500, size=17, color=colors.WHITE)  
                        ]
            )
        )
        self.sender = Container(
            padding= 10,
            border_radius= 10,
            width = 300,
            height= 150,
            gradient= LinearGradient(
                colors = SENDER_GRADIENT,
                begin = alignment.top_right,
                end = alignment.top_left
            ),
            content= Column(
                alignment= MainAxisAlignment.CENTER,
                horizontal_alignment= CrossAxisAlignment.START,
                controls=[
                    Text("Odulaja Philip Temitayo", weight=FontWeight.W_500, size=16, color=colors.WHITE),  
                    Text("9590 4554 3556 3355", weight=FontWeight.BOLD, size=20, color=colors.WHITE)  
                ]
            )
        )

        self.receiver_number = Container(
            border_radius= 10,
            padding = 10,
            width = 300,
            height= 100,
            bgcolor= colors.GREY_900,
            alignment= alignment.top_center,
            content = Column(
                    spacing= 0,
                    controls = [ 
                        TextField(
                            border = InputBorder.NONE,
                            cursor_color= colors.WHITE,
                            keyboard_type = KeyboardType.NUMBER,
                            on_change = self.account_number_update,
                            text_style= TextStyle(
                                color = colors.WHITE,
                                weight = FontWeight.W_800,
                            ),
                            hint_text="- - - -   - - - -   - - - -   - - - -     ",
                            hint_style= TextStyle(
                                color = colors.WHITE,
                                weight = FontWeight.W_800,
                            )
                        ),
                        Text("Enter receiver account number", weight=FontWeight.W_500, size=13, color=colors.GREY_500)  
                    ]
            )
        )

        self.beneficiary_list = ListView(height=610, width=400, controls=[Text("No Beneficiary yet :(", weight=FontWeight.W_300, size=13, color=colors.WHITE)])

        self.beneficiaries = Container(
            padding= 20,
            margin= 20,
            height= 250,
            border_radius=10 ,
            bgcolor= colors.GREY_900,
            content= Column(
                controls=[
                    Row(
                        alignment = MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            Text("My Beneficiaries", weight=FontWeight.BOLD, size=18, color=colors.WHITE),
                        ]
                    ),
                    self.beneficiary_list
                ]
            )
        )

        self.receiver_view = Column(
            alignment= MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.CENTER,
            controls= [
                self.page_description,
                self.sender,
                Text("To receiver", weight=FontWeight.W_500, size=15, color=colors.WHITE),
                self.receiver_number,
                self.beneficiaries
            ]
        )

        self.amount_text = Container(
            margin= 20 ,
            content= Row(
                        controls=[
                            Container(
                            alignment= alignment.top_left,
                            content = IconButton(
                                icon = icons.ARROW_BACK,
                                icon_color=colors.WHITE,
                                on_click = self.transfer
                                ),
                            ),
                            Text("Amount", weight=FontWeight.W_500, size=17, color=colors.WHITE)  
                        ]
            )
        )
        self.receiver_details = Container(
            margin = margin.only(left=25),
            content= Row(
                controls=[
                    Image(src=RECEIVER_IMAGE_URL, width=35, height=35),
                    Text("Maria callas",
                         weight=FontWeight.W_500,
                         size=14, 
                         color=colors.WHITE,
                         font_family = "Poppins",
                         spans= [
                            TextSpan(
                                "\n9893 3773 2949 3994",
                                style= TextStyle(
                                    size=12,
                                    color= colors.WHITE
                                )
                            )
                        ]
                    )
                ]
            )
        )

        self.payment_details = Container(
            margin = 50,
            content= Column(
                alignment= MainAxisAlignment.CENTER,
                horizontal_alignment = CrossAxisAlignment.CENTER, 
                controls=[
                    Text("Available: ",
                         color = colors.GREY_500,
                         weight= FontWeight.W_600,
                         size = 14,
                         font_family = "Poppins",
                         spans= [
                            TextSpan(
                                "£ 3,736",
                                style= TextStyle(
                                    color= colors.WHITE,
                                )
                            )
                         ]
                    ),
                    TextField(
                        cursor_color= colors.WHITE,
                        keyboard_type = KeyboardType.NUMBER,
                        max_length = 7,
                        prefix_text = "£",
                        prefix_style = TextStyle(
                            color= colors.WHITE,
                            size = 35,
                        ),
                        text_align = TextAlign.CENTER,
                        text_style = TextStyle(
                            color= colors.WHITE,
                            size = 35,
                        ),
                        border= InputBorder.NONE
                    ),
                    Text("Commission: ",
                         color = colors.GREY_500,
                         weight= FontWeight.W_600,
                         size = 14,
                         font_family = "Poppins",
                         spans= [
                            TextSpan(
                                "£ 1.80",
                                style= TextStyle(
                                    color= colors.WHITE,
                                )
                            )
                         ]
                    ),
                    Container(
                        padding = padding.symmetric(horizontal=30, vertical=10),
                        margin = margin.only(top=100),
                        border_radius = 10,
                        gradient = LinearGradient(
                            colors = [colors.YELLOW, GREEN_COLOR],
                            begin = alignment.top_left,
                            end = alignment.top_right
                        ),
                        on_click = self.send,
                        content= Row(
                            alignment = MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                Text("send money", weight= FontWeight.W_600, size=15, color = colors.WHITE),
                                Icon(icons.ARROW_FORWARD_ROUNDED, color= colors.WHITE)
                            ]
                        )
                    )
                ]
            )
        )
        self.amount_view = Column(
            alignment= MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.CENTER,
            controls= [
                self.amount_text,
                self.receiver_details,
                self.payment_details
            ]
        )
        self.page_controls = [self.receiver_view]

        return self.page_controls