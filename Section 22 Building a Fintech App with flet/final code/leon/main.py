from flet import *
from data import *
import routes

def main(page: Page):
    page.title = "Leon"
    page.fonts = {
        "Poppins" : FONT_URL
    }
    page.theme = Theme(font_family="Poppins")
    
    def route_change(event : RouteChangeEvent):
        
        page.views.clear()
        page.views.append(
            routes.router(page)[page.route]
        )
        
    page.on_route_change = route_change
    page.go('/')
    

app(main, assets_dir="assets", view=AppView.FLET_APP_WEB)
