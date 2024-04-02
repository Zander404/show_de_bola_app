import flet as ft


class View(ft.View):
    def __init__(self, page:ft.Page):
        super(View, self).__init__(
            route="/stock/new",
            vertical_alignment="",
            horizontal_alignment="",
        )
        self.initialize()



    def initialize(self):
        self.view_Stock = ft.Container(
            ft.Row(
                [
                    ft.Text("VIEW DE STOCK")

                ],
            ))
        self.controls = [
            self.view_Stock
         ]