import flet as ft


class Edit(ft.View):
    def __init__(self, page: ft.Page):
        super(Edit, self).__init__(
            route="/cashier/edit",
            vertical_alignment="",
            horizontal_alignment="",
        )
        self.initialize()


    def initialize(self):
        self.edit_Cashier = ft.Container(
            ft.Row(
                [
                    ft.Text("EDIT DE CASHIER")

                ],
            ))
        self.controls = [
            self.edit_Cashier
        ]
