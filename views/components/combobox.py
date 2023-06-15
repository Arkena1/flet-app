import flet as ft

class Combobox(ft.UserControl):
    
    def deleteHandle(self,e):
        self.data.get("delete")(self.page.db.db_session, self.tt.value)
        self.page.update_datas()
        self.data.get("update_page")()
        self.fill_option_data()
        self.update()
    def changeHandle(self,e):
        print("option change")
    def updateHandle(self,e):
        self.page.go(self.data.get("add")+"/"+self.tt.value)
    def addHandle(self,e):
        self.page.go(self.data.get("add"))
    def fill_option_data(self):
            self.option_data.clear()
            [ self.option_data.append(ft.dropdown.Option(option.get('id'), option.get('name'))) for option in self.data.get("options")]
    def build(self):
        self.option_data = []
        self.tt = ft.Dropdown(
                    width = 370,
                    value=self.data.get("value"),
                    label=self.data.get("label"),
                    on_change = self.data.get("change"),
                    hint_text="Выберете "+self.data.get("label"),
                    options= self.option_data,
                )    
        self.fill_option_data()
        return ft.Row(
            controls=[
                 self.tt
                ,
                ft.PopupMenuButton(
                    visible = self.data.get("popup_visible"),
                    items= [
                    ft.PopupMenuItem(icon=ft.icons.DELETE, text="Удалить", on_click=self.deleteHandle),
                    ft.PopupMenuItem(icon=ft.icons.UPDATE_SHARP, text="Изменить", on_click=self.updateHandle),
                    ft.PopupMenuItem(icon=ft.icons.ADD, text="Добавить", on_click=self.addHandle),
                    ]
                ),
            ]
        )
#"urls":{}     
#"/sub_province/id"    
# /sub_province 