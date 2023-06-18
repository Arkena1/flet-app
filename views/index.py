import flet as ft
from flet import Page, View, Text, TextButton, ElevatedButton
from flet_route import Params, Basket 
from views.components.combobox import Combobox
from views.components.datatable import MyDataRow , MyDataTable

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
        e.data = self.data.get("id")
        self.data.get("change")(e)
    def listViewDeleteHandle(self,e):
        self.page.db.crud.delete_pipe(self.page.db.db_session, self.data.get("id"))
        self.page.update_datas()
        e.data = self.data
        self.data.get("update")(e)
        self.update()
    def listViewUpdateHandle(self,e):
        self.page.go(f"/pipe/{self.data.get('id')}")

    def build(self):
        return ft.ListTile(key=str(self.data.get("id")), 
                                title=ft.Text(key =self.data.get("id"), 
                                value =self.data.get("name"), disabled = True),
                                on_click = self.listViewClickHandle,trailing=ft.PopupMenuButton(
                                icon=ft.icons.MORE_VERT,
                                items=[
                                    ft.PopupMenuItem(icon=ft.icons.DELETE_SHARP, text= "Удалить", on_click= self.listViewDeleteHandle),
                                    ft.PopupMenuItem(icon=ft.icons.UPDATE_SHARP, text= "Изменить", on_click= self.listViewUpdateHandle),
                                ],
                            ),)  
    
class MainPage:
    def __init__(self) -> None:
        ...
    def view(self, page: ft.Page, params:Params, basket: Basket):
        self.comboBoxBlock = []
        self.listBlock = []
        self.table = []
        self.textBlock = []
        def pageUpdate(e):
            comboboxFill()
            page.update()
        def removeProvice(e):
            print(e.data)
            #self.province_data_current.remove(e.data)
        def provChange(e):
            self.subprovince_data_current  =  [i for i in self.subprovince_data if i.get("province_id") == int(e.data)]
            self.area_data_current =  [i for i in self.area_data if i.get("sub_province_id") in [i.get("id") for i in self.subprovince_data_current] ]
            self.field_data_current =  [i for i in self.field_data if i.get("area_id") in [i.get("id") for i in self.area_data_current] ]
            self.list_data_current =  [i for i in self.list_datas if i.get("field_id") in [i.get("id") for i in self.field_data_current ] ]
            listFill()
            comboFill(3)
        def subprovChange(e):
            self.area_data_current =  [i for i in self.area_data if i.get("sub_province_id") == int(e.data)]
            self.field_data_current =  [i for i in self.field_data if i.get("area_id") in [i.get("id") for i in self.area_data_current] ]
            self.list_data_current =  [i for i in self.list_datas if i.get("field_id") in [i.get("id") for i in self.field_data_current ] ]
            listFill()
            comboFill(2)
        def areaChange(e):
            self.field_data_current =  [i for i in self.field_data if i.get("area_id") == int(e.data)]
            self.list_data_current =  [i for i in self.list_datas if i.get("field_id") in [i.get("id") for i in self.field_data_current ] ]
            listFill()
            comboFill(1)
        def fieldChange(e):
            self.list_data_current =  [i for i in self.list_datas if i.get("field_id") == int(e.data)] 
            listFill()   
            page.update()
        def listChange(e):
            tableFill(e.data)
            page.update()
        def updateData():
            self.list_datas = page.models.get("data_list")
            self.province_data = page.models.get("province_data")
            self.subprovince_data = page.models.get("subprovince_data")
            self.area_data = page.models.get("area_data")
            self.field_data = page.models.get("field_data")
            #self.table_data = page.models.get("table_data")
            self.list_data_current = self.list_datas
            self.province_data_current =  self.province_data
            self.subprovince_data_current = self.subprovince_data 
            self.area_data_current = self.area_data
            self.field_data_current = self.field_data 
        def comboboxFill():
            self.comboBoxBlock.clear()
            self.comboBoxBlock.append(Combobox( data={"label":"Провинция", "add":"/province", "delete": page.db.crud.delete_province, "change": provChange, "update_page": pageUpdate, "options": self.province_data_current }))
            self.comboBoxBlock.append(Combobox( data={"label":"Субпровинция", "add":"/sub_province" ,  "delete": page.db.crud.delete_sub_province,"change": subprovChange, "update_page": pageUpdate,"options": self.subprovince_data_current}))
            self.comboBoxBlock.append(Combobox(data={"label":"Район", "add":"/area",  "delete": page.db.crud.delete_area,"change": areaChange, "update_page": pageUpdate, "options": self.area_data_current}))
            self.comboBoxBlock.append(Combobox( data={"label":"Поле", "add":"/field",  "delete": page.db.crud.delete_field,"change":fieldChange, "update_page": pageUpdate, "options": self.field_data_current}))



        def comboFill(count):
            for _ in range(count):
                self.comboBoxBlock.pop()
            match count:
                case 1:
                    self.comboBoxBlock.append(Combobox( data={"label":"Поле", "add":"/field",  "delete": page.db.crud.delete_field, "options": self.field_data_current}))
                case 2:
                    self.comboBoxBlock.append(Combobox(data={"label":"Район", "add":"/area",  "delete": page.db.crud.delete_area,"change": areaChange, "options": self.area_data_current}))
                    self.comboBoxBlock.append(Combobox( data={"label":"Поле", "add":"/field",  "delete": page.db.crud.delete_field, "options": self.field_data_current}))
                case 3:
                    self.comboBoxBlock.append(Combobox( data={"label":"Субпровинция", "add":"/sub_province" ,  "delete": page.db.crud.delete_sub_province,"change": subprovChange,"options": self.subprovince_data_current}))
                    self.comboBoxBlock.append(Combobox(data={"label":"Район", "add":"/area",  "delete": page.db.crud.delete_area,"change": areaChange, "options": self.area_data_current}))
                    self.comboBoxBlock.append(Combobox( data={"label":"Поле", "add":"/field",  "delete": page.db.crud.delete_field, "options": self.field_data_current}))
            page.update()
        def tableFill(id):
            self.table.clear()
            self.table.append(MyDataTable(data={"row_data": [MyDataRow(data = row | {"page":page}).build() for row in page.db.crud.get_pipeinfos(page.db.db_session, id)]}))
            self.textBlock.clear()
            try:
                tfid =  page.db.crud.get_pipe(page.db.db_session, id).get("name")
            except:
                tfid = ""
            self.textBlock.append(ft.Text(f"Информация по "  +  tfid, text_align= ft.TextAlign.CENTER, width= page.width, size= 24))
            page.update()
        def delListItem(e):
            del e.data["change"], e.data["update"]
            self.list_data_current.remove(e.data)
            listFill()
            page.update()
        def listFill():
            self.listBlock.clear()
            [self.listBlock.append(ListItem(data= row_data | {"change": listChange,"update": delListItem}  )) for indx, row_data in enumerate(self.list_data_current) if indx < 20]
        page.tableFill =  tableFill
        updateData()

        comboboxFill()
        listFill()
        # tableFill(1)
        return ft.View(
            "/",
            controls=[
         ft.AppBar(
                leading_width=40,
                title=ft.Text("Главная"), 
                center_title=True,
                actions=[
                    ft.PopupMenuButton(
                                icon=ft.icons.MORE_VERT,
                                items=[
                                    ft.PopupMenuItem(icon=ft.icons.ADD, text= "Источник", on_click= lambda _: page.go("/source")),
                                    ft.PopupMenuItem(icon=ft.icons.ADD, text= "Трубка", on_click= lambda _: page.go("/pipe")),
                                    ft.PopupMenuItem(icon=ft.icons.ADD, text= "Информация", on_click= lambda _: page.go("/pipeinfo")),
                                ],
                            ),
                ],
            ),  
        ft.Container( content= 
        ft.Row(key = "top_row",controls=[
            ft.Container(   height = 270,
            content =ft.Column(controls= self.comboBoxBlock)),
        ft.Container(
            expand = 1, border= ft.border.symmetric(horizontal=ft.border.BorderSide(1, ft.colors.BLUE_GREY_100)),border_radius =ft.border_radius.all(5),
            alignment= ft.alignment.top_center,
            height = 270,
            content =ft.ListView(
                key= "list",
                spacing=10, 
                divider_thickness= 1,
                controls=self.listBlock
                )),
                ]
            ),
        ),
        ft.Container(height=50,  alignment= ft.alignment.center_right, content=ft.Row(self.textBlock)),
        ft.Container( height =255,  border= ft.border.all(1, ft.colors.BLUE_GREY_100),border_radius =ft.border_radius.all(5),  alignment= ft.alignment.top_center, 
            content = ft.Column( scroll=ft.ScrollMode.ADAPTIVE , controls=self.table )

            )
        ]
        )
