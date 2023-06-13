import flet as ft

class MyDataRow(ft.UserControl):
    def selectHandle(self, e):
        print(f"selected {self.id}")
    def updateHandle(self, e):
        pass
    def deleteHandle(self, e):
        pass    
    def build(self):
        row = self.data.get("cel")
        self.id =  self.data.get("id")
        return ft.DataRow(selected=True,
                    on_select_changed=self.selectHandle,
                    cells=[
                        ft.DataCell(ft.Text(row[0])),
                        ft.DataCell(ft.Text(row[1])),
                        ft.DataCell(ft.Text(row[2])),
                        ft.DataCell(ft.Text(row[3])),
                        ft.DataCell(ft.Text(row[4])),
                        ft.DataCell(ft.Text(row[5])),
                        ft.DataCell(ft.Text(row[6])),
                        ft.DataCell(ft.Text(row[7])),
                        ft.DataCell(ft.IconButton(icon = ft.icons.UPDATE_SHARP, on_click=self.updateHandle)),
                        ft.DataCell(ft.IconButton(icon = ft.icons.DELETE, icon_color= "red", on_click= self.deleteHandle)),
                    ],
        )


class MyDataTable(ft.UserControl):
    def build(self): # (id, [])
        table_data = self.controls.models.get("table")
        print(table_data)
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

            rows=[MyDataRow(data = {"cel": row, "id": id}).build() for id, row in table_data]

        )
