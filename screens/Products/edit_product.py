import flet as ft


class Edit(ft.View):
    def __init__(self, page: ft.Page):
        super(Edit, self).__init__(
            route="/product/new",
            vertical_alignment="",
            horizontal_alignment="",
        )
        self.initialize()

    def initialize(self):
        self.edit_Product = ft.Container(
            ft.Row(
                [
                    ft.Text("EDIT DE PRODUTO")

                ],
            ))
        self.controls = [
            self.edit_Product
        ]
