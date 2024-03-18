import flet as ft
from screens.Landing import Landing
from screens.Product import Product
from screens.Cart import Cart
from screens.Login import Login
from screens.Products import edit_product, home_product, new_product, view_product




def main(page: ft.Page) -> None:

    theme = ft.Theme()
    theme.visual_density = ft.ThemeVisualDensity.COMPACT
    page.theme = theme
    page.theme_mode = ft.ThemeMode.LIGHT

    def router(route):
        page.views.clear()


        # ROTA DE LOGIN
        if page.route == "/login":
            page.views.append(Login(page))

        # LANDING PAGE
        elif page.route == "/":
            page.views.append(Landing(page))

        # ROTA DE PRODUTOS
        elif page.route == "/products":
            page.views.append(home_product.Home(page))

        elif page.route == "/product/add":
            page.views.append(new_product.New(page))

        elif page.route == "/product/edit":
            page.views.append(edit_product.Edit(page))

        elif page.route == "/product/view":
            page.views.append(view_product.View(page))


        # ROTA DE PEDIDOS
        elif page.route == "/stock":
            page.views.append(Cart(page))

        elif page.route == "/stock/add":
            page.views.append(Cart(page))

        elif page.route == "/stock/edit":
            page.views.append(Cart(page))

        elif page.route == "/stock/view":
            page.views.append(Cart(page))


        page.update()

    page.on_route_change = router
    page.go("/")


ft.app(target=main, assets_dir="assets")
