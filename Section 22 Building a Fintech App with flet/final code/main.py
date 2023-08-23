from datetime import datetime
# from flet import *
# import math

# def main(page: Page):
#     page.title = "routing"
#     page.bgcolor = "white"
#     page.update()

#     def go_to_john(event):
#         page.go("/john")

#     def go_to_home(event):
#         page.go("/")

#     intro = Text("Introduction to routing i am the default page", 
#                  spans=[
#                      TextSpan(
#                         "Go to john page",
#                          on_click=go_to_john,
#                          style= TextStyle(
#                             color= colors.GREEN
#                          )
#                      )
#                  ],
#                  size=35
#             )

#     john_text = Text("This page is available for all ",
#                      spans=[
#                         TextSpan(
#                             "home page",
#                             on_click=go_to_home,
#                             style= TextStyle(
#                                 color= colors.GREEN
#                             )
#                         )
#                     ],
#                     size=30,
#                     )
    
#     graident_container = Container(
#         height=200,
#         width=200,
#         gradient= LinearGradient(
#             colors= ["#F6F151", "#0A33F9"],
#             end = alignment.top_left,
#             begin= alignment.top_right,
#             # stops=[0.3, 0.1, 0.2],
#             tile_mode= GradientTileMode.MIRROR,
#             rotation = math.radians(180)   
#         )
#     )

#     radial_container = Container(
#         height=200,
#         width=200,
#         gradient= RadialGradient(
#             colors= ["#FF1B6B", "#45CAFF"],
#             center = alignment.bottom_right,
#             radius= 1.0
#             # # stops=[0.3, 0.1, 0.2],
#             # tile_mode= GradientTileMode.MIRROR,
#             # rotation = math.radians(180)   
#         )
#     )

#     sweep_container = Container(
#         gradient=SweepGradient(
#             center=alignment.top_right,
#             start_angle=0.0,
#             end_angle=math.pi * 2,
#             colors=[colors.YELLOW, colors.BLUE],
#         ),
#         width=150,
#         height=150,
#         border_radius=5,
#     )

#     def route_change(event: RouteChangeEvent):
#         if page.route == "/john":
#             page.add(john_text)
#         else:
#             page.controls.clear()
#             page.add(intro)
    
#     page.on_route_change = route_change
#     page.add( graident_container, radial_container, sweep_container)

# app(target=main, view=AppView.FLET_APP_WEB)

# names = ["Odulaja", "Philip", "Temitayo"]

# print(", ".join(names))


time = "2023-08-23 15:08:12"
print(time.split(" ")[0].split("-")[0])










