import flet as ft


class New(ft.View):
    def __init__(self, page:ft.Page):
        super(New, self).__init__(
            route="/stock/new",
            vertical_alignment="",
            horizontal_alignment="",
        )
        self.initialize()



    def initialize(self):
        self.new_Stock = ft.Container(
            ft.Row(
                [
                    ft.Text("NEW DE STOCK")

                ],
            ))
        self.controls = [
            self.new_Stock
         ]