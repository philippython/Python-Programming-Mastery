from flet import *
from data import DEFAULT_PROMPTS, CHATGPT_IMAGE_URL , IMAGE_URL , chatgpt_response

class FletGPT(UserControl):
    def __init__(self, page):
        self.page = page
        self.appname = self.page.title
        self.prompts = []
        super().__init__()

    def new_chat(self, event):
        chat = Row(
            controls= [
                Icon(icons.MODE_COMMENT_OUTLINED, color=colors.GREY_500),
                Text("New Chat", color=colors.WHITE)
            ]
        )
        self.chat_history.controls.insert(0, chat)
        self.update()

    def prompt_hover(self, event):
        # data property ---> true as a string
        # data property ---> false as a string
        event.control.bgcolor = colors.SURFACE_VARIANT if event.data == "true" else colors.WHITE
        event.control.content.controls[-1].visible = True if event.data == "true" else False
        self.update()

    def close_sidebar(self, e):
        self.left_navbar.visible = False
        self.text_interface.col = {"lg" : 12}
        self.applogo.margin = margin.only(bottom=250, top=50, left=470)
        self.sidebar.visible = True
        self.update()

    def open_sidebar(self, e):
        self.left_navbar.visible = True
        self.text_interface.col = {"lg" : 10}
        self.applogo.margin = margin.only(bottom=250, top=50, left=350)
        self.sidebar.visible = False
        self.update()

    def send_message(self, event):
        pass

    def input_focus(self, event):
        self.send_message_btn.icon_color = colors.GREEN_400
        self.update()

    def submit(self, event):
        self.applogo.visible = False
        self.responsive_prompt.visible = False
        self.conversations.visible = True

        if isinstance(event, ContainerTapEvent):
            prompt_value = f"{event.control.content.controls[0].value} {event.control.content.controls[0].spans[0].text[1:]}"
            message = Text(value=prompt_value)

        else:
            input_value = event.control.value
            message = Text(value=input_value)

        query_prompt = Container( 
                alignment= alignment.top_left,
                padding = padding.symmetric(horizontal=50, vertical=10),
                content= Row(
                    wrap = True,
                    controls= [
                        Image(
                            src = IMAGE_URL,
                            height= 25,
                            width= 25
                        ),
                        message
                    ]
                )
            )

        self.input.value = ""
        progress_ring = ProgressBar()
        self.conversations.controls.extend([query_prompt, progress_ring])
        self.update()

        api_response = chatgpt_response(message.value)
        self.conversations.controls.pop()

        response = Container (
                bgcolor= colors.SURFACE_VARIANT,
                padding = padding.symmetric(horizontal=50, vertical=10),
                content= Row(
                    wrap = True,
                    alignment= alignment,
                    controls= [
                        Image(
                            src = CHATGPT_IMAGE_URL,
                            height= 25,
                            width= 25
                        ),
                        Text(value=api_response, size=15)
                    ]
                )
        )
        self.conversations.controls.append(response)
        self.update()

    def build(self):
        self.action_buttons = Row(
            controls=[
                Container(
                    padding = padding.only(left=5, top=5, bottom=5, right=10),
                    border = border.all(1, colors.GREY_400),
                    border_radius = 10,
                    content= TextButton(
                        text="New chat",
                        icon= icons.ADD,
                        icon_color= colors.WHITE,
                        style = ButtonStyle(
                            color= colors.WHITE
                        ),
                        on_click = self.new_chat
                    )
                ),
                Container(
                    padding = padding.symmetric(vertical=5),
                    border = border.all(1, colors.GREY_400),
                    border_radius = 10,
                    on_click = self.close_sidebar,
                    content= TextButton(
                        icon= icons.VIEW_SIDEBAR_OUTLINED,
                        icon_color= colors.WHITE,
                        style = ButtonStyle(
                            color= colors.WHITE
                        )
                    ),
                    tooltip="Close sidebar"

                )
            ]
        )
        self.chat_history = ListView(width=250,
                                    height=450,
                                    expand=True,
                                    spacing= 20,
                            )
        self.bottom_sheet = Column(
            controls=[
                Divider(thickness=1, height=1, color = colors.GREY_500),
                Row(
                    controls=[
                        Icon(icons.ACCOUNT_CIRCLE_OUTLINED, color= colors.WHITE),
                        Text("Upgrade to Plus", size=15, weight= FontWeight.W_300, color=colors.WHITE)
                    ]
                ),
                Row(
                    controls = [
                        Image(
                            src= "assets/icon.png",
                            width = 25,
                            height= 25,
                        ),
                        Text("Philip Odulaja", weight= FontWeight.W_300 ,color= colors.WHITE)
                    ]
                )
            ]
        )
        self.applogo = Container(
            margin = margin.only(bottom=250, top=50, left=350),
            content = Text(
                            "FletGPT", 
                            color=colors.GREY_400,
                            weight = FontWeight.BOLD,
                            size=40
                        )
        )

        # for loop to create prompt buttons on text interface
        for button in DEFAULT_PROMPTS:
            prompt = Container(
                alignment= alignment.top_left,
                padding= 5,
                border = border.all(1, color= colors.GREY_500),
                border_radius= 10,
                height=50,
                width=120,
                col = {"lg" : 6},
                on_click = self.submit,
                on_hover= self.prompt_hover,
                content= Row(
                    controls= [
                        Text(
                            value = button[0],
                            weight= FontWeight.BOLD,
                            style = TextThemeStyle.BODY_MEDIUM,
                            spans= [
                                TextSpan(
                                    text= button[1],
                                    style= TextStyle(
                                        size=12,
                                        weight= FontWeight.NORMAL
                                    )
                                )
                            ]
                        ),
                        Icon(icons.SEND_ROUNDED, color=colors.GREY_500, visible=False),
                    ]
                )
            )
            self.prompts.append(prompt)

        self.responsive_prompt = ResponsiveRow(
            controls= self.prompts
        )
        self.sidebar = Container(
                    border = border.all(1, colors.GREY_400),
                    border_radius = 10,
                    on_click = self.open_sidebar,
                    content= TextButton(
                        icon= icons.VIEW_SIDEBAR_OUTLINED,
                        icon_color= colors.GREY_500,
                        style = ButtonStyle(
                            color= colors.GREY_500
                        ),
                        tooltip="Open sidebar"
                    ),
                    visible= False
                )
        
        self.input = TextField(
            hint_text="Send a message", 
            border = InputBorder.NONE,
            cursor_color= colors.BLACK,
            cursor_height= 25,
            cursor_width= 1,
            shift_enter= True,
            multiline= True,
            on_focus= self.input_focus,
            on_submit= self.submit
        )

        self.send_message_btn = IconButton(
            icon= icons.SEND,
            icon_color = colors.GREY_400,
            tooltip= "Send message",
        )

        self.send_stack = Stack (
            controls= [
                Container (
                    height= 60,
                    margin = margin.only(top=5),
                    padding = padding.symmetric(horizontal=15, vertical=5),
                    bgcolor = colors.WHITE,
                    border_radius = 10,
                    content= self.input,
                    shadow= BoxShadow(
                        spread_radius= 1,
                        blur_radius= 15,
                        offset= Offset(0, 0),
                        color= colors.with_opacity(0.4, colors.BLACK)
                    )
                ),

                Container(
                    content= self.send_message_btn,
                    margin = margin.only(left=890, top=15, right=15),
                    height= 20,
                    width= 20,
                    padding= 2,
                    on_click= self.send_message
                )
            ]
        )

        self.conversations = ListView(height=600, width=1000, expand=True, visible=False, spacing = 20, auto_scroll=True)
        self.response = Container (
            content= Row(
                controls= [
                    Image(
                        src = CHATGPT_IMAGE_URL,
                        height= 25,
                        width= 25
                    ),
                ]
            )
        )

        self.left_navbar = Container(
            bgcolor= colors.GREY_900,
            padding = 5,
            width= 470,
            height= 620,
            col = {"lg": 2},
            content= Column(
                expand= True,
                alignment= MainAxisAlignment.START,
                controls= [
                    self.action_buttons,
                    self.chat_history,
                    self.bottom_sheet
                ]
            )
        )
        self.text_interface = Container(
            height= 620,
            width=1000,
            col = {"lg": 10},
            padding = padding.symmetric(vertical=30, horizontal=100),
            bgcolor= colors.WHITE,
            content= Column (
                controls= [
                    self.sidebar,
                    self.applogo,
                    self.responsive_prompt,
                    self.conversations,
                    self.send_stack
                ]
            )
        )
        self.top_row = ResponsiveRow(
            alignment = MainAxisAlignment.START,
            controls= [
                self.left_navbar,
                self.text_interface
            ]
        )

        return self.top_row