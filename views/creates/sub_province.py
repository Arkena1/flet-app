import flet as ft
from flet import Page, View, TextField, ElevatedButton
from flet_route import Params, Basket
from views.components.combobox import Combobox

class CreateSubProvincePage:
    def view(self, page: Page, params: Params, basket: Basket):
        tt  =  ft.Ref[TextField]()
        combo = ft.Ref[Combobox]()

        def back_handler(self):
            page.go("/")

        def save_handler(self):
            print(combo.current.controls[0].controls[0].value)
            page.go("/")  
              
        return View(
            "/sub_province",
            controls=[
                ft.Text("Добавить субпровинцию",size=30, text_align=ft.TextAlign.CENTER),
                TextField(ref=tt),
                Combobox(ref=combo,data={"label":"провинция","options":[(1, "провинция 1"),
                                                                        (2, "провинция 2")
                                                                        ],
                                                                        "popup_visible": False
                                                                        }),
                ElevatedButton("Назад", on_click= back_handler),
                ElevatedButton("Сохранить", on_click= save_handler)
            ]
        )
    
