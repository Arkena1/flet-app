import flet as ft
from flet import Page, View, TextField, ElevatedButton
from flet_route import Params, Basket
from views.components.combobox import Combobox

class CreateAreaPage:
    def view(self, page: Page, params: Params, basket: Basket):
        tt  =  ft.Ref[TextField]()
        combo = ft.Ref[Combobox]()
        subprovince_data = page.models.get("subprovince_data")
        def back_handler(self):
            page.go("/")
        def save_handler(self):
            page.db.crud.create_area(page.db.db_session, {"name":tt.current.value, "sub_province_id": combo.current.controls[0].controls[0].value})
            page.update_datas()
            page.update()
            page.go("/")    
        return View(
            "/area",
            controls=[
                ft.Text("Добавить район",size=30, text_align=ft.TextAlign.CENTER),
                TextField(ref=tt),
                Combobox(ref=combo,data={"label":"Субпровинция","options":subprovince_data,
                                                                        "popup_visible": False
                                                                        }),
                ElevatedButton("Назад", on_click= back_handler),
                ElevatedButton("Сохранить", on_click= save_handler)
            ]
        )
