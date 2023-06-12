import flet as ft
from views.index import MainPage
from views.update import UpdatePage
from flet_route import Routing, path
from views.creates.province import CreateProvincePage
from views.creates.sub_province import CreateSubProvincePage
from views.creates.area import CreateAreaPage
from views.creates.field import CreateFieldPage
from views.creates.pipe import CreatePipePage
from views.creates.sours import CreateSoursPage
from views.creates.pipeinfo import CreatePipeinfoPage
from views.components.combobox import Combobox


def main(page: ft.Page):
    page.title = "Main"
    app_routes = [
        path(url="/", clear=True, view=MainPage().view),
        path(url="/update/:id", clear=True, view=UpdatePage().view),
        path(url="/province", clear=True, view=CreateProvincePage().view),
        path(url="/sub_province", clear=True, view=CreateSubProvincePage().view),
        path(url="/area", clear=True, view=CreateAreaPage().view),
        path(url="/field", clear=True, view=CreateFieldPage().view),
        path(url="/pipe", clear=True, view=CreatePipePage().view),
        path(url="/sours", clear=True, view=CreateSoursPage().view),
        path(url="/pipeinfo", clear=True, view=CreatePipeinfoPage().view),
        
    ]
    Routing(
        page=page, # Here you have to pass the page. Which will be found as a parameter in all your views
        app_routes=app_routes, # Here a list has to be passed in which we have defined app routing like app_routes
        )
    page.go(page.route)
    
if __name__ == "__main__":
    ft.app(target= main)