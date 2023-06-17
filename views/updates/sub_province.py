import flet as ft
from flet import Page, View, TextField, ElevatedButton
from flet_route import Params, Basket
from views.components.combobox import Combobox

class UpdateSubprovincePage:
    def view(self, page: Page, params: Params, basket: Basket):
        tt  =  ft.Ref[TextField]()
        id = params.get("id")
        combo = ft.Ref[Combobox]()  
        province_data = page.models.get("province_data")    
        sub_province_data = page.db.crud.get_sub_province(page.db.db_session, id)
        def back_handler(self):
            page.go("/")
        def save_handler(self):
            sub_province_data["name"] =  tt.current.value
            sub_province_data["province_id"] =  combo.current.controls[0].controls[0].value
            page.db.crud.update_sub_province(page.db.db_session, data = sub_province_data)
            page.update_datas()
            page.update()
            page.go("/")    
        return View(
            "/sub_province/:id",
            controls=[
                TextField(ref=tt, value= sub_province_data.get("name")),
                Combobox(ref=combo,data={"label":"Поле","value": sub_province_data.get("province_id"),"options":province_data,
                                                        "popup_visible": False
                                                        }),
                ElevatedButton("Назад", on_click= back_handler),
                ElevatedButton("Сохранить", on_click= save_handler)
            ]
        )