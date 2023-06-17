import flet as ft
from flet import Page, View, TextField, ElevatedButton
from flet_route import Params, Basket
from views.components.combobox import Combobox

class UpdatePipeinfoPage:
    def view(self, page: Page, params: Params, basket: Basket):
        id = params.get("id")
        nitro_total  =  ft.Ref[TextField]()
        source = ft.Ref[Combobox]()
        pipes = ft.Ref[Combobox]()
        nitro_a =  ft.Ref[TextField]()
        nitro_b =  ft.Ref[TextField]()
        nitro_percent =  ft.Ref[TextField]()
        platelets =  ft.Ref[TextField]()
        hydrogen =  ft.Ref[TextField]()
        source_data = page.models.get("source_data")     
        pipes_data = page.models.get("data_list") 
        pipeinfo_data = page.db.crud.get_pipeinfo(page.db.db_session, id)    
        def back_handler(self):
            page.go("/")
        def save_handler(self):
            data  = {   
                "nitro_total": nitro_total.current.value,
                "nitro_a": nitro_a.current.value,
                "nitro_b": nitro_b.current.value,
                "nitro_percent": nitro_percent.current.value,
                "platelets": platelets.current.value,
                "hydrogen": hydrogen.current.value,
                "pipe_id": pipes.current.controls[0].controls[0].value,
                "source_id": source.current.controls[0].controls[0].value,
            }
            pipeinfo_data.update(data)
            page.db.crud.update_pipeinfo(page.db.db_session, pipeinfo_data)
            page.update_datas()
            page.update()
            page.go("/")
            
        return View(
            "/pipeinfo/:id",
            controls=[
                ft.AppBar(
                title=ft.Text("Добавить информацию трубки"),
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
                TextField(ref=nitro_total, label="Азот общее", value=pipeinfo_data.get("nitro_total")),
                TextField(ref=nitro_a, label="Азот А", value=pipeinfo_data.get("nitro_total")),
                TextField(ref=nitro_b, label="Азот B", value=pipeinfo_data.get("nitro_total")),
                TextField(ref=nitro_percent, label="Азот процент", value=pipeinfo_data.get("nitro_total")),
                TextField(ref=platelets, label="Плейтлетс", value=pipeinfo_data.get("nitro_total")),
                TextField(ref=hydrogen, label="Водород", value=pipeinfo_data.get("nitro_total")),
                Combobox(ref=source ,data={"label":"Источник", "value" : pipeinfo_data.get("source_id"),"options":source_data,
                                                                     "popup_visible": False
                                                                    }),
                Combobox(ref=pipes,data={"label":"Трубка", "value" : pipeinfo_data.get("pipe_id"),"options":pipes_data,
                                                                    "popup_visible": False
                                                                        }),
            ]
        )