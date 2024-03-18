import flet as ft


class Home(ft.View):
    def __init__(self, page:ft.Page):
        super(Home, self).__init__(
            route="/stock/home",
            vertical_alignment="",
            horizontal_alignment="",
        )
        self.initialize()



    def initialize(self):
        self.home_Stock = ft.Container(
            ft.Row(
                [
                    ft.Text("HOME DE STOCK")

                ],
            ))
        self.controls = [
            self.home_Stock
         ]