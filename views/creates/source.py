import flet as ft
from flet import Page, View, TextField, ElevatedButton
from flet_route import Params, Basket

class CreateSoursPage:
    def view(self, page: Page, params: Params, basket: Basket):
        tt  =  ft.Ref[TextField]()   
        def save_handler(self):
            page.db.crud.create_source(page.db.db_session, {"name":tt.current.value})
            page.update_datas()
            page.update()
            page.go("/")
        def back_handler(self):
            page.go("/")    
        return View(
            "/source",
            controls=[
                ft.AppBar(
                title=ft.Text("Источник"),
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
                TextField(ref=tt)
            ]
        )
