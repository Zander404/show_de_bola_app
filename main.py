import flet as ft
from screens.Landing import Landing
from screens.Product import Product
from screens.Cart import Cart
from screens.Login import Login


def main(page: ft.Page) -> None:

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
    page.go("/login")


ft.app(target=main, assets_dir="assets", upload_dir="screens")
