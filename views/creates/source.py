import flet as ft
from flet import Page, View, TextField, ElevatedButton
from flet_route import Params, Basket
from views.components.combobox import Combobox

class CreateSoursPage:
    def view(self, page: Page, params: Params, basket: Basket):
        tt  =  ft.Ref[TextField]()   
        combo = ft.Ref[Combobox]()   
        def back_handler(self):
            page.go("/")
        def save_handler(self):
            page.go("/")    
        return View(
            "/source",
            controls=[
                TextField(ref=tt),
                ElevatedButton("Назад", on_click= back_handler),
                ElevatedButton("Сохранить", on_click= save_handler)
            ]
        )
