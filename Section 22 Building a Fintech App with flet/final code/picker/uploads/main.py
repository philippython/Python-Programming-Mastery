from flet import *
from data import PAGE_BG_COLOR
from usercontrol import fletGPT

def main(page: Page):
    page.title = "FletGPT"
    page.bgcolor = PAGE_BG_COLOR
    page.scroll = ScrollMode.HIDDEN
    page.fonts = {
        "Segoe" : "assets/fonts/SEGOEUI.TTF"
    }
    page.theme = Theme(font_family="Arial")
    page.padding = 0
    page.update()
    
    fletgpt = fletGPT(page)
    page.add(fletgpt)

app(target=main, view=AppView.FLET_APP_WEB, assets_dir="assets")
