import flet as ft
from flet import Page, View, TextField, ElevatedButton
from flet_route import Params, Basket
from views.components.combobox import Combobox

class CreateAreaPage:
    def view(self, page: Page, params: Params, basket: Basket):
        tt  =  ft.Ref[TextField]()
        combo = ft.Ref[Combobox]()
        def back_handler(self):
            page.go("/")
        def save_handler(self):
            page.go("/")    
        return View(
            "/area",
            controls=[
                ft.Text("Добавить район",size=30, text_align=ft.TextAlign.CENTER),
                TextField(ref=tt),
                Combobox(ref=combo,data={"label":"район","options":[(1, "район 1"),
                                                                        (2, "район 2")
                                                                        ],
                                                                        "popup_visible": False
                                                                        }),
                ElevatedButton("Назад", on_click= back_handler),
                ElevatedButton("Сохранить", on_click= save_handler)
            ]
        )
