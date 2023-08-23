from flet import *
from data import *
from helper import generate_initial, user_info

class UpdateProfile(UserControl):

    def __init__(self, page: Page):
        self.page = page
        super().__init__()

    def dashboard(self, event):
        self.page.go("/dashboard")

    def upload_image(Self, event):
        pass

    def did_mount(self):
        users_data = self.page.client_storage.get('users')
        active_user = self.page.client_storage.get('active_user')

        full_name = user_info(users_data, active_user)['full_name']
        self.info_row.content.controls[0].controls[1].value = full_name
        self.info_row.content.controls[1].controls[1].value = user_info(users_data, active_user)['email']
        self.info_row.content.controls[2].controls[1].value = user_info(users_data, active_user)['account_no']
        self.image_row.content.controls[0].content.value = generate_initial(full_name)

        self.update()

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
                            Text("Update Account information", weight=FontWeight.W_500, size=12, color=colors.WHITE),  
                            Stack(
                                [
                                Container(
                                    alignment= alignment.center,
                                    border_radius= 10,
                                    bgcolor= colors.GREY_900,
                                    content= 
                                        IconButton(
                                            icon= icons.NOTIFICATIONS_NONE,
                                            icon_color= colors.WHITE
                                        ),
                                ),
                                Container(
                                    margin = margin.only(left=30),
                                    alignment = alignment.top_right,
                                    content = CircleAvatar(bgcolor=GREEN_COLOR, radius=5)
                                )
                                ]
                            )
                        ]
            )
        )

        self.image_row = Container(
            margin= 10,
            bgcolor= colors.GREY_900,
            padding = 50,
            border_radius= 10,
            content= Column(
                controls = [ 
                    CircleAvatar(
                        # foreground_image_url=AVATAR_IMAGE_URL,
                        content= Text("IG", color=colors.GREY_500, size=15)
                    ),
                    IconButton(icons.UPLOAD_SHARP, icon_color= colors.GREY_400, icon_size=30, on_click=self.upload_image)
                ]
            )
        )


        self.info_row = Container(
            margin= 10,
            bgcolor= colors.GREY_900,
            padding = 10,
            border_radius= 10,
            content= Column(
                controls = [ 
                    Row(
                        [
                            Text("Full name", color=colors.GREY_400),
                            Text("Odulaja philip Temitayo", color=colors.GREY_400)
                        ]
                    ),
                    Row(
                        [
                            Text("Email", color=colors.GREY_400),
                            Text("odulajaphilip@gmail.com", color=colors.GREY_400)
                        ]
                    ),
                    Row(
                        [
                            Text("Account number", color=colors.GREY_400),
                            Text("6788 6969 4044 4456", color=colors.GREY_400)
                        ]
                    ),
                ]
            )
        )

    

        self.page_controls = Column(
            alignment= MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.CENTER,
            controls= [
                self.top,
                self.image_row,
                self.info_row
            ]
        )

        
        return self.page_controls