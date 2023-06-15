import flet as ft
from views.index import MainPage
from views.update import UpdatePage
from flet_route import Routing, path
from views.creates.province import CreateProvincePage
from views.creates.sub_province import CreateSubProvincePage
from views.creates.area import CreateAreaPage
from views.creates.field import CreateFieldPage
from views.creates.pipe import CreatePipePage
from views.creates.source import CreateSoursPage
from views.creates.pipeinfo import CreatePipeinfoPage
from views.updates.province import UpdateProvincePage
from views.updates.pipe import UpdatePipePage
from views.components.combobox import Combobox
from data_models.test import  table_data, data_list, province_data, subprovince_data, area_data, field_data
import db_datas

models_data ={"table" : table_data
            }



def main(page: ft.Page):
    page.title = "Главная"
    page.db = db_datas
    def update_data():
        models_data["province_data"]= page.db.crud.get_provinces(page.db.db_session)
        models_data["subprovince_data"]= page.db.crud.get_sub_provinces(page.db.db_session)
        models_data["area_data"]= page.db.crud.get_areas(page.db.db_session)
        models_data["field_data"]= page.db.crud.get_fields(page.db.db_session)
        models_data["data_list"]= page.db.crud.get_pipes(page.db.db_session)
        page.models =  models_data
        page.update()
    page.update_datas = update_data
    page.update_datas()
    app_routes = [
        path(url="/", clear=True, view=MainPage().view),
        path(url="/update/:id", clear=True, view=UpdatePage().view),
        path(url="/province", clear=True, view=CreateProvincePage().view),
        path(url="/province/:id", clear=True, view=UpdateProvincePage().view),
        path(url="/sub_province", clear=True, view=CreateSubProvincePage().view),
        path(url="/area", clear=True, view=CreateAreaPage().view),
        path(url="/field", clear=True, view=CreateFieldPage().view),
        path(url="/pipe", clear=True, view=CreatePipePage().view),
        path(url="/pipe/:id", clear=True, view=UpdatePipePage().view),
        path(url="/source", clear=True, view=CreateSoursPage().view),
        path(url="/pipeinfo", clear=True, view=CreatePipeinfoPage().view),
        
    ]
    Routing(
        page=page, # Here you have to pass the page. Which will be found as a parameter in all your views
        app_routes=app_routes, # Here a list has to be passed in which we have defined app routing like app_routes
        )
    page.go(page.route)
    
if __name__ == "__main__":
    ft.app(target= main)