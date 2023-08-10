from flet import *
from counter import Counter

def main(page: Page):
    page.title = "Counter App"
    page.bgcolor = "white"
    page.padding = 10
    page.scroll = ScrollMode.ALWAYS

    counter = Counter(3)
    counter_2 = Counter(5)
    page.add(counter, counter_2)

app(target=main, view=AppView.FLET_APP_WEB)