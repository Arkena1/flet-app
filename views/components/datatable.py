import flet as ft

class MyDataRow(ft.UserControl):

    def updateHandle(self, e):
        self.data.get("page").go(f"/pipeinfo/{self.id}")
    def deleteHandle(self, e):
        self.data.get("page").db.crud.delete_pipeinfo(self.data.get("page").db.db_session, self.id)
        self.data.get("page").tableFill(self.data.get("pipe_id"))
    def build(self):
        self.id =  self.data.get("id")
        return ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(self.data.get("nitro_total"), width=75)),
                        ft.DataCell(ft.Text(self.data.get("nitro_a"), width=50)),
                        ft.DataCell(ft.Text(self.data.get("nitro_b"), width=50)),
                        ft.DataCell(ft.Text(self.data.get("nitro_percent"), width=75)),
                        ft.DataCell(ft.Text(self.data.get("platelets"), width=75)),
                        ft.DataCell(ft.Text(self.data.get("hydrogen"), width=75)),
                        ft.DataCell(ft.Text(self.data.get("source_name"), width=255)),
                        ft.DataCell(ft.IconButton(icon = ft.icons.UPDATE_SHARP, on_click=self.updateHandle)),
                        ft.DataCell(ft.IconButton(icon = ft.icons.DELETE, icon_color= "red", on_click= self.deleteHandle)),
                    ],
        )


class MyDataTable(ft.UserControl):
    
    def build(self): # (id, [])
        self.table_data = self.data.get("row_data") #self.controls.models.get("table_data")
        self.rows_list = []
        def fillRows():
            if len(self.table_data)>0:
                [self.rows_list.append(row) for row in self.table_data]
        fillRows()
        return ft.Container(
            ft.DataTable(
                vertical_lines=ft.border.BorderSide(2, ft.colors.BLUE_GREY_100),
                columns=[
                    ft.DataColumn(ft.Text("Азот общее")),
                    ft.DataColumn(ft.Text("Азот А")),
                    ft.DataColumn(ft.Text("Азот B")),
                    ft.DataColumn(ft.Text("Азот процент")),
                    ft.DataColumn(ft.Text("Плейтлетс")),
                    ft.DataColumn(ft.Text("Водород")),
                    ft.DataColumn(ft.Text("Источник данных")),
                    ft.DataColumn(ft.Text("")),
                    ft.DataColumn(ft.Text(""))
                ],

                rows= self.rows_list

            )
        )