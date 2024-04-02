import flet as ft


class Home(ft.View):
    def __init__(self, page:ft.Page):
        super(Home, self).__init__(
            route="/product/new",
            vertical_alignment="",
            horizontal_alignment="",
        )
        self.initialize()



    def initialize(self):
        self.new_Product = ft.Container(
            ft.Row(
                [
                    ft.Text("HOME DE PRODUTO")

                ],
            ))
        self.controls = [
            self.new_Product
         ]