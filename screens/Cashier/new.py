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
        self.new_Cashier = ft.Container(
            ft.Row(
                [
                    ft.Text("NEW DE CASHIER")

                ],
            ))
        self.controls = [
            self.new_Cashier
        ]
