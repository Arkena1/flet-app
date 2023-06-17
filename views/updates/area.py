import flet as ft
from flet import Page, View, TextField, ElevatedButton
from flet_route import Params, Basket
from views.components.combobox import Combobox

class UpdateAreaPage:
    def view(self, page: Page, params: Params, basket: Basket):
        tt  =  ft.Ref[TextField]()
        id = params.get("id")
        field_data = page.models.get("subprovince_data")
        combo = ft.Ref[Combobox]()  
        area_data = page.db.crud.get_area(page.db.db_session, id)
        def back_handler(self):
            page.go("/")
        def save_handler(self):
            area_data["name"] =  tt.current.value
            area_data["sub_province_id"] =  combo.current.controls[0].controls[0].value
            page.db.crud.update_area(page.db.db_session, data = area_data)
            page.update_datas()
            page.update()
            page.go("/")    
        return View(
            "/area/:id",
            controls=[
                TextField(ref=tt, value= area_data.get("name")),
                Combobox(ref=combo,data={"label":"Поле","value": area_data.get("sub_province_id"),"options":field_data,
                                                        "popup_visible": False
                                                        }),
                ElevatedButton("Назад", on_click= back_handler),
                ElevatedButton("Сохранить", on_click= save_handler)
            ]
        )