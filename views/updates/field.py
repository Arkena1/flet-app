import flet as ft
from flet import Page, View, TextField, ElevatedButton
from flet_route import Params, Basket
from views.components.combobox import Combobox

class UpdateFieldPage:
    def view(self, page: Page, params: Params, basket: Basket):
        tt  =  ft.Ref[TextField]()
        id = params.get("id")
        combo = ft.Ref[Combobox]()
        area_data = page.models.get("area_data")
        field_data = page.db.crud.get_field(page.db.db_session, id)
        def back_handler(self):
            page.go("/")
        def save_handler(self):
            field_data["name"] =  tt.current.value
            field_data["area_id"] =  combo.current.controls[0].controls[0].value
            page.db.crud.update_field(page.db.db_session, data = field_data)
            page.update_datas()
            page.update()
            page.go("/")    
        return View(
            "/field/:id",
            controls=[
                TextField(ref=tt, value= field_data.get("name")),
                Combobox(ref=combo,data={"label":"Поле","value": field_data.get("area_id"),"options":area_data,
                                                        "popup_visible": False
                                                        }),
                ElevatedButton("Назад", on_click= back_handler),
                ElevatedButton("Сохранить", on_click= save_handler)
            ]
        )