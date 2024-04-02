import flet as ft


class New(ft.View):
    def __init__(self, page: ft.Page):
        super(New, self).__init__(
            route="/cashier/new",
            vertical_alignment="",
            horizontal_alignment="",
        )
        self.initialize()

    def initialize(self):
        self.view_Cashier = ft.Container(
            ft.Row(
                [
                    ft.Text("VIEW DE CASHIER")

                ],
            ))
        self.controls = [
            self.view_Cashier
        ]
