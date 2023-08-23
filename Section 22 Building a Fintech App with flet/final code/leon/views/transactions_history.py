from flet import *
from datetime import datetime
from helper import generate_initial, user_info, user_info_name

class TransactionHistory(UserControl):

    def __init__(self, page:Page):
        self.page = page
        super().__init__()
    
    def dashboard(self, event):
        self.page.go("/dashboard")

    def transaction_history(self, event):
        self.page.go("/stats/transaction-history")

    def did_mount(self):
        users_data = self.page.client_storage.get('users')
        active_user = self.page.client_storage.get('active_user')
        account_numbers = self.page.client_storage.get('account_numbers')

        active_user_dict = user_info(users_data, active_user)
        transactions = active_user_dict['transactions']

        for transaction in transactions:
            if transaction['transaction_type'] == "debit":
                receiver_full_name = transaction['receiver']
                self.history_list.controls.append(
                    Row(
                    alignment= MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                            CircleAvatar(
                                content = Text(generate_initial(transaction['receiver']), color=colors.GREY_500)
                            ),
                            Text(receiver_full_name,
                                color=colors.WHITE,
                                weight = FontWeight.BOLD,
                                spans = [
                                    TextSpan(
                                        text= f"\n{transaction['time']}",
                                        style= TextStyle(
                                            color= colors.WHITE,
                                            weight= FontWeight.W_400
                                        )
                                    )
                                ]
                            ),
                            Text(f"-{transaction['amount']}", color=colors.RED)
                        ]
                    )
                )
            else:
                sender_full_name = transaction['sender']
                self.history_list.controls.append(
                    Row(
                    alignment= MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                            CircleAvatar(
                                content = Text(generate_initial(sender_full_name), color=colors.GREY_500)
                            ),
                            Text(
                                sender_full_name,
                                color=colors.WHITE,
                                weight = FontWeight.BOLD,
                                spans = [
                                    TextSpan(
                                        text= f"\n{transaction['time']}",
                                        style= TextStyle(
                                            color= colors.WHITE,
                                            weight= FontWeight.W_400
                                        )
                                    )
                                ]
                            ),
                            Text(f"+{transaction['amount']}", color=colors.GREEN)
                        ]
                    )
                )
        self.update()

    def build(self):
        self.date = datetime.now().date()
        self.history_list = ListView(height=610, width=400, spacing=10)

        self.history = Container(
            padding= 20,
            margin= margin.only(top=10),
            height=600,
            border_radius= border_radius.only(top_left=30, top_right=30),
            bgcolor= colors.GREY_900,
            content= Column(
                controls=[
                    Row(
                        alignment = MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            Text(self.date, weight=FontWeight.BOLD, size=20, color=colors.WHITE),
                            Container(
                                alignment= alignment.center,
                                border_radius= 10,
                                bgcolor= colors.GREY_700,
                                content= IconButton(
                                    icon= icons.CALENDAR_TODAY_SHARP,
                                    icon_color= colors.WHITE 
                                )
                            )
                        ]
                    ),
                    self.history_list
                ]
            )
        )

        self.nav_bar = Container(
            bgcolor= colors.GREY_900,
            alignment= alignment.top_center,
            padding= padding.symmetric(horizontal= 30, vertical= 20),
            content= Row(
                spacing= 90,
                controls= [
                    Container(
                            col={"xs": 4},
                            width = 90,
                            border_radius= 10,
                            content= IconButton(
                            icon= icons.ACCOUNT_BALANCE,
                            icon_color= colors.WHITE,
                            on_click = self.dashboard
                            )
                    ),
                    Container(
                            col={"xs": 4},
                            width = 90,
                            border_radius= 10,
                            gradient = LinearGradient(
                                colors = [colors.YELLOW, colors.PINK],
                                begin = alignment.top_right,
                                end = alignment.top_left,
                            ),
                            content= IconButton(
                            icon= icons.BAR_CHART,
                            icon_color= colors.WHITE,
                            on_click = self.transaction_history
                            )
                    ),
                ]
            )
        )

        self.page_controls = Column(
            alignment= MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
            spacing= 0,
            controls= [
                self.history,
                self.nav_bar,
            ]
        )

        return self.page_controls