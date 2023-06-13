import flet as ft

class Combobox(ft.UserControl):
    
    def deleteHandle(self,e):
        self.data.get("delete")(self.page.db.db_session, self.tt.current.value)
        self.page.update_datas()
        self.page.go(self.page.route)

    def changeHandle(self,e):
        print("option change")
    def updateHandle(self,e):
        self.page.go(self.data.get("add")+"/"+self.tt.current.value)
    def addHandle(self,e):
        print(self.tt.current.value)
        self.page.go(self.data.get("add"))
        
    def build(self):
        
        self.tt = ft.Ref[ft.Dropdown]()
        return ft.Row(
            controls=[
                ft.Dropdown(
                    ref=self.tt,
                    width = 370,
                    label=self.data.get("label"),
                    on_change = self.data.get("change"),
                    hint_text="Выберете "+self.data.get("label"),
                    options=[ ft.dropdown.Option(option.get('id'), option.get('name')) for option in self.data.get("options")],
                ),
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