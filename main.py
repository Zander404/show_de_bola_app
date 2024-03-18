import flet as ft
# from screens.Landing import Landing
from screens.Product import Product
from screens.Cart import Cart
from screens.Login import Login


class Landing(ft.View):
    def __init__(self, page: ft.Page) -> None:
        super(Landing, self).__init__(
            route="/", horizontal_alignment="center",
            vertical_alignment="center"
        )

        self.page = page
        self.cart_logo = ft.Icon(name="SPORTS_SOCCER_ROUNDED", size=64)
        self.title = ft.Text("Show de Bola App".upper(), size=28, weight="bold")
        self.subtitle = ft.Text("Controle de Estoque", size=11)

        self.product_page_btn = ft.Container(content=ft.Row(
            [
                ft.IconButton(
                    "ACCOUNT_CIRCLE_OUTLINED",
                    width=54,
                    height=54,
                    style=ft.ButtonStyle(
                        bgcolor={"": "#202020"},
                        shape={"": ft.RoundedRectangleBorder(radius=10)},
                        side={"": ft.BorderSide(2, "white54")}
                    ),
                    on_click=lambda x: self.page.go("/products")
                ),

                ft.IconButton(
                    "SHOPPING_BASKET_OUTLINED",
                    width=54,
                    height=54,
                    style=ft.ButtonStyle(
                        bgcolor={"": "#202020"},
                        shape={"": ft.RoundedRectangleBorder(radius=10)},
                        side={"": ft.BorderSide(2, "white54")}
                    ),
                    on_click=lambda x: self.page.go("/products")
                ),

                ft.IconButton(
                    "LIST_ALT",
                    width=54,
                    height=54,
                    style=ft.ButtonStyle(
                        bgcolor={"": "#202020"},
                        shape={"": ft.RoundedRectangleBorder(radius=10)},
                        side={"": ft.BorderSide(2, "white54")}
                    ),
                    on_click=lambda x: self.page.go("/products")
                ),
            ], alignment="center"
        ),)

        self.controls = [
            self.cart_logo,
            ft.Divider(height=25, color="transparent"),
            self.title,
            self.subtitle,
            ft.Divider(height=25, color="transparent"),
            self.product_page_btn
        ]


def main(page: ft.Page) -> None:

    theme = ft.Theme()
    theme.visual_density = ft.ThemeVisualDensity.COMPACT
    page.theme = theme
    page.theme_mode = ft.ThemeMode.LIGHT

    def router(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(Landing(page))

        if page.route == "/products":
            page.views.append(Product(page))

        if page.route == "/cart":
            page.views.append(Cart(page))

        if page.route == "/login":
            page.views.append(Login(page))

        page.update()

    page.on_route_change = router
    page.go("/")


ft.app(target=main, assets_dir="assets", upload_dir="screens")
