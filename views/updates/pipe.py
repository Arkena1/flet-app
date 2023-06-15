import flet as ft
from flet import Page, View, TextField, ElevatedButton
from flet_route import Params, Basket
from views.components.combobox import Combobox

class UpdatePipePage:
    def view(self, page: Page, params: Params, basket: Basket):
        tt  =  ft.Ref[TextField]()
        id = params.get("id")
        combo = ft.Ref[Combobox]()
        field_data = page.models.get("field_data")    
        pipe_data = page.db.crud.get_pipe(page.db.db_session, id)
        #combo.current.controls[0].controls[0].value = 
        print(pipe_data)
        def back_handler(self):
            page.go("/")
        def save_handler(self):
            pipe_data["name"] =  tt.current.value
            pipe_data["field_id"] =  combo.current.controls[0].controls[0].value
            page.db.crud.update_pipe(page.db.db_session, data = pipe_data)
            page.update_datas()
            page.update()
            page.go("/")    
        return View(
            "/pipe/:id",
            controls=[
                TextField(ref=tt, value= pipe_data.get("name")),
                Combobox(ref=combo,data={"label":"Поле","value": pipe_data.get("field_id"),"options":field_data,
                                                        "popup_visible": False
                                                        }),
                ElevatedButton("Назад", on_click= back_handler),
                ElevatedButton("Сохранить", on_click= save_handler)
            ]
        )