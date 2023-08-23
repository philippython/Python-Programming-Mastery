from flet import *
from data import *
from helper import user_info, generate_initial , user_info_name
from datetime import datetime

class Transfer(UserControl):
    def __init__(self, page):
        self.page = page
        self.user_data = None
        super().__init__()

    def dashboard(self, event):
        self.page.go("/dashboard")
    
    def transfer(self, event):
        self.page_controls.clear()
        self.page_controls.append(self.receiver_view)
        self.update()
        self.page.go("/transfer")
    
    def account_number_update(self, event):
        users_data = self.page.client_storage.get('users')
        active_user = self.page.client_storage.get('active_user')

        active_user_dict = user_info(users_data, active_user)
        account_dict = self.page.client_storage.get('account_numbers')

        if len(event.control.value) == 16:
            for name, account_no in account_dict.items() :
                if event.control.value == account_no :
                    self.to_amount(event)
                    receiver_avatar = CircleAvatar(
                        content = Text(generate_initial(name), color=colors.GREY_500, size=14),
                    )
                    self.receiver_details.content.controls.pop(0)
                    self.receiver_details.content.controls.insert(0, receiver_avatar)
                    self.receiver_details.content.controls[1].value = name
                    self.receiver_details.content.controls[1].spans[0].text = f"\n{account_no}"
                    self.payment_details.content.controls[0].spans[0].text = f"£ {format(int(active_user_dict['balance']), ',')}"
                    self.payment_details.content.controls[0].spans[1].text = f"{str(round(active_user_dict['balance'] - int(active_user_dict['balance']), 2))[1:]}"

                    self.update()

    def on_amount_change(self, event):
        users_data = self.page.client_storage.get('users')
        active_user = self.page.client_storage.get('active_user')
        receiver_name = self.receiver_details.content.controls[1].value

        active_user_dict = user_info(users_data, active_user)
        receiver_dict = user_info_name(users_data, receiver_name)

        amount = float(event.control.value) if event.control.value != "" else 0
        commission = 0.5 / 100 * int(amount)
        
        self.payment_details.content.controls[2].spans[0].text = f"£ {round(commission, 2)}"
        
        total_deduction = amount + commission
        self.update()
        if total_deduction > active_user_dict['balance'] :
            pass
        else:
            new_balance = float(active_user_dict['balance']) - total_deduction
            debit_instance = {
                "amount" : total_deduction,
                "transaction_type" : "debit",
                "receiver" : self.receiver_details.content.controls[1].value,
                "time" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            credit_instance = {
                "amount" : amount,
                "transaction_type" : "credit",
                "sender" : active_user_dict['full_name'],
                "time" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            active_user_dict['balance'] = new_balance
            receiver_dict['balance'] = receiver_dict['balance'] + float(amount)
            active_user_dict['transactions'].append(debit_instance)
            receiver_dict['transactions'].append(credit_instance)

            sender_id = users_data.index(active_user_dict)
            receiver_id = users_data.index(receiver_dict)

            users_data[sender_id] = active_user_dict
            users_data[receiver_id] = receiver_dict
            
            self.user_data = users_data
            self.update()

        # 1044529047629792 - odulaja philip
        # 1158771141363890 - leonard

    def to_amount(self, event):
        self.page_controls.pop()
        self.page_controls.append(self.amount_view)
        self.update()

    def send(self, event):
        self.page.client_storage.set('users', self.user_data)
        self.page.go("/transfer-successful")

    def did_mount(self):
        users_data = self.page.client_storage.get('users')
        active_user = self.page.client_storage.get('active_user')
        account_numbers = self.page.client_storage.get('account_numbers')

        active_user_dict = user_info(users_data, active_user)
        transactions = active_user_dict['transactions']
        self.sender.content.controls[0].value = active_user_dict['full_name']
        self.sender.content.controls[1].value = active_user_dict['account_no']

        for transaction in transactions:
            if transaction['transaction_type'] == "debit":
                receiver_full_name = transaction['receiver']
                self.beneficiary_list.controls.append(
                    Row(
                        controls=[
                            CircleAvatar(
                                content = Text(generate_initial(transaction['receiver']), color=colors.GREY_500)
                            ),
                            Text(receiver_full_name,
                                 color=colors.WHITE,
                                 spans = [
                                    TextSpan(
                                        text= f"\n{account_numbers[receiver_full_name]}"
                                    )
                                 ]
                                )
                        ]
                    )
                )
        self.update()

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

        self.beneficiary_list = ListView(height=610, width=400, spacing=5)

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
                            ),
                            TextSpan(
                                ".78",
                                style= TextStyle(
                                    color= colors.WHITE,
                                    weight= FontWeight.W_400,
                                )
                            ),
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
                        on_change = self.on_amount_change,
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
                                "£ 0.0",
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