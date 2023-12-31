import flet as ft
from flet import Page, View, TextField, ElevatedButton
from flet_route import Params, Basket
from views.components.combobox import Combobox

class CreateProvincePage:
    def view(self, page: Page, params: Params, basket: Basket):
        tt  =  ft.Ref[TextField]()
        def back_handler(self):
            page.go("/")
        def save_handler(self):
            page.db.crud.create_province(page.db.db_session, {"name":tt.current.value})
            page.update_datas()
            page.update()
            page.go("/")    
        return View(
            "/province",
            controls=[
                TextField(ref=tt),
                ElevatedButton("Назад", on_click= back_handler),
                ElevatedButton("Сохранить", on_click= save_handler)
            ]
        )
    
