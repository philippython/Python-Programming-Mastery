from flet import *
from views.onboarding import OnBoarding
from views.signup import SignUp
from views.signup_success import SignUpSuccess
from views.login import Login
from views.dashboard import DashBoard
from views.transactions_history import TransactionHistory
from views.transfer import Transfer
from views.transfer_success import TransferSuccess
from views.security import Security
from views.settings import AccountInformation

def router(page: Page):

    return {
        "/" : View(
            page.route,
            [OnBoarding(page)],
            bgcolor = colors.BLACK,
            padding = 40
        ),
        "/signup" : View(
            page.route,
            [SignUp(page)],
            bgcolor = colors.BLACK,
            padding = 30
        ),
        "/signup/success" : View(
            page.route,
            [SignUpSuccess(page)],
            bgcolor = colors.BLACK,
            padding = 30
        ),
        "/login" : View(
            page.route,
            [Login(page)],
            bgcolor= colors.BLACK,
            padding= 30
        ),
        "/dashboard" : View(
            page.route,
            [DashBoard(page)],
            bgcolor= colors.BLACK,
            padding= 0
        ),
        "/stats/transaction-history" : View(
            page.route,
            [TransactionHistory(page)],
            bgcolor = colors.BLACK,
            padding = 0
        ),
        "/transfer" : View(
            page.route,
            [Transfer(page)],
            bgcolor = colors.BLACK,
            padding = 0
        ),
        "/transfer-successful": View(
            page.route,
            [TransferSuccess(page)],
            bgcolor = colors.BLACK,
            padding = 0
        ),
        "/security": View(
            page.route,
            [Security(page)],
            bgcolor = colors.BLACK,
            padding = 0
        ),
        "/account-information": View(
            page.route,
            [AccountInformation(page)],
            bgcolor = colors.BLACK,
            padding = 0
        )
    }