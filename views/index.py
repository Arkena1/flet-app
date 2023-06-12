import flet as ft
from flet import Page, View, Text, TextButton, ElevatedButton
from flet_route import Params, Basket 
from views.components.combobox import Combobox

class MyDataRow(ft.UserControl):    
    def build(self):
        row = self.data.get("cel")
        return ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(row[0])),
                        ft.DataCell(ft.Text(row[1])),
                        ft.DataCell(ft.Text(row[2])),
                        ft.DataCell(ft.Text(row[3])),
                        ft.DataCell(ft.Text(row[4])),
                        ft.DataCell(ft.Text(row[5])),
                        ft.DataCell(ft.Text(row[6])),
                        ft.DataCell(ft.Text(row[7])),
                        ft.DataCell(ft.IconButton(icon = ft.icons.UPDATE_SHARP)),
                        ft.DataCell(ft.IconButton(icon = ft.icons.DELETE, icon_color= "red")),
                    ],
        )


class DataTable(ft.UserControl):
    def build(self):
        return ft.DataTable(
            
            columns=[
                ft.DataColumn(ft.Text("Трубка")),
                ft.DataColumn(ft.Text("N tot")),
                ft.DataColumn(ft.Text("N A")),
                ft.DataColumn(ft.Text("N B")),
                ft.DataColumn(ft.Text("N B%")),
                ft.DataColumn(ft.Text("Плейтлетс")),
                ft.DataColumn(ft.Text("Водород")),
                ft.DataColumn(ft.Text("Источник данных")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text(""))
            ],
            rows=[
                MyDataRow(data  = {"cel": ["Первая ячейка", 
                                           "Вторая", 
                                           "Третья", 
                                           "четвертая", 
                                           "5", 
                                           "6", 
                                           "7", 
                                           "8"]}).build(),
                MyDataRow(data  = {"cel": ["Первая ячейка", 
                                           "Вторая", 
                                           "Третья", 
                                           "четвертая", 
                                           "5", 
                                           "6", 
                                           "7", 
                                           "8"]}).build(),
                MyDataRow(data  = {"cel": ["Первая ячейка", 
                                           "Вторая", 
                                           "Третья", 
                                           "четвертая", 
                                           "5", 
                                           "6", 
                                           "7", 
                                           "8"]}).build(),
                MyDataRow(data  = {"cel": ["Первая ячейка", 
                                           "Вторая", 
                                           "Третья", 
                                           "четвертая", 
                                           "5", 
                                           "6", 
                                           "7", 
                                           "8"]}).build(),
                MyDataRow(data  = {"cel": ["Первая ячейка", 
                                           "Вторая", 
                                           "Третья", 
                                           "четвертая", 
                                           "5", 
                                           "6", 
                                           "7", 
                                           "8"]}).build(),                                                      
            ],
        )

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
    def view(self, page: ft.Page, params:Params, basket: Basket):
        page.data_list = {
                        0: {"id":1, "value":"Трубка Удачная"},
                        1: {"id":2, "value":"Трубка Зарница"},
                        2: {"id":3, "value":"Трубка Айхал"},
                        3: {"id":4, "value":"Трубка Юбилейная"},
                        4: {"id":5, "value":"Трубка Удачная"},
                        5: {"id":6, "value":"Трубка Зарница"},
                        6: {"id":7, "value":"Трубка Айхал"},
                        7: {"id":8, "value":"Трубка Юбилейная"},
                        8: {"id":9, "value":"Трубка Комсомольская"}

                    }
        data_list = [
                        ListItem(key = 0,data= page.data_list[0]),
                        ListItem(key = 1,data= page.data_list[1]),
                        ListItem(key = 2,data= page.data_list[2]),
                        ListItem(key = 3,data= page.data_list[3]),
                        ListItem(key = 4,data= page.data_list[4]),
                        ListItem(key = 0,data= page.data_list[5]),
                        ListItem(key = 1,data= page.data_list[6]),
                        ListItem(key = 2,data= page.data_list[7]),
                        ListItem(key = 3,data= page.data_list[8]),
                    ]

        return ft.View(
            "/",
            controls=[
                
        ft.Row(key = "top_row",controls=[
            ft.Container(
            expand = 1,
            content =ft.Column(controls=[
                Combobox(data={"label":"Провинция", "add":"/province", "options": 
                               [(1,"Якутская алмазоносная провинция"), 
                                (2,"Архангельская алмазоносная провинция"), 
                                (3, "Уральская алмазоносная провинция")]}),

                Combobox(data={"label":"Субпровинция", "add":"/sub_province" , "options": 
                               [(1,"Центральносибирская субпровинция"), 
                                (2,"Лено-Анабарская субпровинция"), 
                                (3,"Тунгусская субпровинция"), 
                                (4,"Алданская субпровинция"), 
                                (5,"Архангельская субпровинция"), 
                                (6,"Уральская субпровинция")]}),

                Combobox(data={"label":"Район", "add":"/area", "options": 
                               [(1,"Верхнемунский район"), 
                                (2,"Далдыно-Алакитский район"), 
                                (3,"Среднемархинский район"), 
                                (4,"Малоботуобинский район"), 
                                (5,"Куонапский район"),
                                (6,"Среднеоленекский район"),
                                (7,"Нижнеоленекский район"),
                                (8,"Котуй-Меймечинский район район"),
                                (9,"Моркокинский район"),
                                (10,"Анабарский  район"),
                                (11,"Архангельский район"),
                                (12,"Уральский район")]}),

                Combobox(data={"label":"Поле", "add":"/field", "options": 
                               [(1,"Верхнемунское поле"), 
                                (2,"Далдынское поле"), 
                                (3,"Алакит-мархинское поле"), 
                                (4,"Накынское поле"), 
                                (5,"Мирнинское поле"),
                                (6,"Орто-Ыаргинское поле"),
                                (7,"Ары-мастахское поле"),
                                (8,"Старореченское поле"),
                                (9,"Дьюкенское поле"),
                                (10,"Лучаканское поле"),
                                (11,"Куранахское поле"),
                                (12,"Чомурдахское поле"), 
                                (13,"Огонер-Юряхское поле"), 
                                (14,"Западно-Укукитское поле"), 
                                (15,"Восточно-Укукисткое поле"),
                                (16,"Верхнемоторчунское поле"),
                                (17,"Мерчимденское поле"),
                                (18,"Верхнемолодинское поле"),
                                (19,"Куойкское поле"),
                                (20,"Котуй-Меймечинское поле"),
                                (21,"Чадобецкое поле"),
                                (22,"Ингашинское поле"), 
                                (23,"Верхнеалданское поле"), 
                                (24,"Ингилийское поле "), 
                                (25,"Золотицкое поле"),
                                (26,"Верхотинское поле"),
                                (27,"Кепинское поле"),
                                (28,"Уральское поле")]})
                ])),
        ft.Container(
            height = 300,
            expand = 2,
                content =ft.ListView(
                    key= "list",
                    spacing=10, 
                    divider_thickness= 1,
                    data = {"on_update": False},
                    controls=data_list
                    )),
                ]
            ),
     
        ft.Container(
            DataTable()
        )
            ]
        )
