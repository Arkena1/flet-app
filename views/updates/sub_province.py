import flet as ft
from flet import Page, View, TextField, ElevatedButton
from flet_route import Params, Basket
from views.components.combobox import Combobox

class UpdateSubprovincePage:
    def view(self, page: Page, params: Params, basket: Basket):
        tt  =  ft.Ref[TextField]()
        id = params.get("id")
        sub_province_data = page.db.crud.get_sub_province(page.db.db_session, id)
        def back_handler(self):
            page.go("/")
        def save_handler(self):
            sub_province_data["name"] =  tt.current.value
            page.db.crud.update_sub_province(page.db.db_session, data = sub_province_data)
            page.update_datas()
            page.update()
            page.go("/")    
        return View(
            "/sub_province/:id",
            controls=[
                TextField(ref=tt, value= sub_province_data.get("name")),
                ElevatedButton("Назад", on_click= back_handler),
                ElevatedButton("Сохранить", on_click= save_handler)
            ]
        )