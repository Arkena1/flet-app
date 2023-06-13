import flet as ft
from flet import Page, View, Text, TextButton, ElevatedButton
from flet_route import Params, Basket 
from views.components.combobox import Combobox
from views.components.datatable import MyDataTable

class DialogWindow(ft.UserControl):
    def close_dlg(self,e):
        self.open = False
        self.update()

    def build(self):
        return ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirm"),
            content=ft.Text("Вы хотите удалить трубку?"),
            actions=[
                ft.TextButton("Да", on_click=self.close_dlg),
                ft.TextButton("Отмена", on_click=self.close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
            )

class ListItem(ft.UserControl):


    def listViewClickHandle(self,e):
        print(self.data.get("id"))
    def listViewDeleteHandle(self,e):
        print("Удалить "+str(self.data.get("id")))
    def listViewUpdateHandle(self,e):
        self.page.go(f"/update/{self.key}")

    def build(self):
        return ft.ListTile(key=str(self.data.get("id")), 
                                title=ft.Text(key =self.data.get("id"), 
                                value =self.data.get("value"), disabled = True),
                                on_click = self.listViewClickHandle,trailing=ft.PopupMenuButton(
                                icon=ft.icons.MORE_VERT,
                                items=[
                                    ft.PopupMenuItem(icon=ft.icons.DELETE_SHARP, text= "Удалить", on_click= self.listViewDeleteHandle),
                                    ft.PopupMenuItem(icon=ft.icons.UPDATE_SHARP, text= "Изменить", on_click= self.listViewUpdateHandle),
                                ],
                            ),)
    
class MainPage:
    def test(self,e):
        print(1)
    def view(self, page: ft.Page, params:Params, basket: Basket):

        self.list_datas = page.models.get("data_list")
        self.province_data = page.models.get("province_data")
        self.subprovince_data = page.models.get("subprovince_data")
        self.area_data = page.models.get("area_data")
        self.field_data = page.models.get("field_data")
        self.province_cb = ft.Ref[Combobox]()
        self.subprovince_cb = ft.Ref[Combobox]()
        self.area_cb = ft.Ref[Combobox]()
        self.field_cb = ft.Ref[Combobox]()
        self.tt= ft.View(
            "/",
            controls=[
                
        ft.Row(key = "top_row",controls=[
            ft.Container(
            expand = 1,
            content =ft.Column(controls=
            [
                Combobox(ref= self.province_cb, data={"label":"Провинция", "add":"/province", "delete": page.db.crud.delete_province, "change": self.test, "options": self.province_data}),

                Combobox(ref= self.subprovince_cb, data={"label":"Субпровинция", "add":"/sub_province" ,  "delete": page.db.crud.delete_sub_province,"options": self.subprovince_data}),

                Combobox(ref= self.area_cb, data={"label":"Район", "add":"/area",  "delete": page.db.crud.delete_area, "options": self.area_data}),

                Combobox(ref= self.field_cb, data={"label":"Поле", "add":"/field",  "delete": page.db.crud.delete_field, "options": self.field_data})
            ])),
        ft.Container(
            height = 300,
            expand = 2,
                content =ft.ListView(
                    key= "list",
                    spacing=10, 
                    divider_thickness= 1,
                    data = {"on_update": False},
                    controls=[ListItem(data= row_data) for row_data in self.list_datas]
                    )),
                ]
            ),
     
        ft.Container(

           MyDataTable(page).build()
        )
            ]
        )
        return self.tt
