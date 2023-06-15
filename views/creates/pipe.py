import flet as ft
from flet import Page, View, TextField, ElevatedButton
from flet_route import Params, Basket
from views.components.combobox import Combobox

class CreatePipePage:
    def view(self, page: Page, params: Params, basket: Basket):
        tt  =  ft.Ref[TextField]()    
        combo = ft.Ref[Combobox]()
        field_data = page.models.get("field_data")     
        def back_handler(self):
            page.go("/")
        def save_handler(self):
            page.db.crud.create_pipe(page.db.db_session, {"name":tt.current.value, "field_id": combo.current.controls[0].controls[0].value})
            page.update_datas()
            page.update()
            page.go("/")    
        return View(
            "/pipe",
            controls=[
                ft.AppBar(
                title=ft.Text("Добавить трубку"),
                actions=[
                    ft.IconButton(
                        ft.icons.ARROW_BACK,
                        on_click= back_handler
                    ),
                    
                    ft.IconButton(
                        ft.icons.SAVE,
                        on_click= save_handler
                    ),
                ],),
                TextField(ref=tt),
                Combobox(ref=combo,data={"label":"Поле","options":field_data,
                                                                        "popup_visible": False
                                                                        }),
            ]
        )
