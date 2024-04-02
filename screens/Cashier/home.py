import flet as ft


class Home(ft.View):
    def __init__(self, page: ft.Page):
        super(Home, self).__init__(
            route="/cashier/home",
            vertical_alignment="",
            horizontal_alignment="",
        )
        self.initialize()

    def initialize(self):
        self.home_Cashier = ft.Container(
            ft.Row(
                [
                    ft.Text("HOME DE CASHIER")

                ],
            ))
        self.controls = [
            self.home_Cashier
        ]
