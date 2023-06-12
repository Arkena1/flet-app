from flet import Page, View, TextField, ElevatedButton
from flet_route import Params, Basket

class UpdatePage:
    def view(self, page: Page, params: Params, basket: Basket):
        id = params.get("id")
        tt = TextField()
        
        def updateData(self):
            page.go("/")
            
        return View(
            "/update/:id",
            controls=[
                tt,
                ElevatedButton("get back", on_click= updateData)
            ]
        )
    
