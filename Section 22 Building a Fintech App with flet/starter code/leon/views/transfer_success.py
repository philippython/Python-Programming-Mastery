from flet import *
from data import *

class TransferSuccess(UserControl):
    def __init__(self, page: Page):
        self.page = page
        super().__init__()
    
    def transfer(self, event):
        self.page.go("/transfer")

    def build(self):
        self.check_mark = Container(
            padding= 5,
            bgcolor= GREEN_COLOR,
            border_radius= 35,
            height= 70,
            width = 70,
            margin= 50,
            content = Icon(
                icons.CHECK_SHARP,
                color = colors.WHITE,
                size= 30
            )
        )

        self.success = Container(
            margin= 50,
            content= Text(
                "Sent!",
                color = colors.WHITE,
                size = 30,
                weight = FontWeight.BOLD,
                text_align= TextAlign.CENTER
            )
        )

        self.transaction_details = Container(
            margin= 50,
            content= Column(
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment= CrossAxisAlignment.CENTER,
                controls=[
                    Image(src=RECEIVER_IMAGE_URL, width=45, height=45),
                    Text("Maria callas", weight=FontWeight.W_600, size=16, color=colors.WHITE),
                    Text("9893 3773 2949 s3994", weight=FontWeight.W_400, size=13, color=colors.WHITE),
                    Text("You have succesfully transfer", color = colors.WHITE, size = 18, text_align = TextAlign.CENTER, weight = FontWeight.BOLD),
                ]
            )
        )

        self.transfer_again = Container(
            content= Column(
                spacing= 15,
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment= CrossAxisAlignment.CENTER,
                controls=[
                    Text("£ 1,360 to maria callas", weight=FontWeight.W_400, size=14, color=colors.WHITE),
                    Text(" ",
                        spans= [
                            TextSpan("Transfer Again", 
                            on_click = self.transfer,         
                            style= TextStyle(
                                size = 15,
                                color= colors.GREEN_800,
                                weight=FontWeight.W_500,
                                ),
                            )
                        ]
                    )
                ]
            )
        )
        self.page_controls = Column(
            alignment = MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.CENTER,
            controls= [
                self.check_mark,
                self.success,
                self.transaction_details,
                self.transfer_again
            ]
        )

        return self.page_controls