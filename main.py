import time
import flet as ft
from models.model import Model
from screens.Cart import Cart
from screens.Login import Login
# from screens.Products import edit_product, home_product, new_product, view_product
import flet_easy as fs

app = fs.FletEasy(route_init="/")


dados = [
    {
        "barCode": "8154",
        "title": "tristique",
        "observation": "Lorem ipsum",
        "price": "$2.01",
        "stock": "990"
    },
    {
        "barCode": "1024",
        "title": "Morbi",
        "observation": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Curabitur sed tortor. Integer aliquam adipiscing lacus. Ut nec urna",
        "price": "$76.88",
        "stock": "396"
    },
    {
        "barCode": "1983",
        "title": "faucibus",
        "observation": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Curabitur sed tortor. Integer aliquam",
        "price": "$2.51",
        "stock": "350"
    },
    {
        "barCode": "8181",
        "title": "In",
        "observation": "Lorem ipsum dolor sit",
        "price": "$41.82",
        "stock": "627"
    },
    {
        "barCode": "9109",
        "title": "neque.",
        "observation": "Lorem",
        "price": "$2.47",
        "stock": "435"
    }
]


# LANDING PAGE

@app.page("/")
def Landing(data: fs.Datasy):
    page = data.page

    cart_logo = ft.Icon(name="SPORTS_SOCCER_ROUNDED", size=64)
    title = ft.Text("Show de Bola App".upper(), size=28, weight="bold")
    subtitle = ft.Text("Controle de Estoque", size=11)

    product_page_btn = ft.Container(content=ft.Row(
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
                on_click=lambda x: page.go("/products")
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
                on_click=lambda x: page.go("/teste")
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
                on_click=lambda x: page.go("/products")
            ),
        ], alignment="center"
    ),)

    return ft.View(
        controls=[
            cart_logo,
            ft.Divider(height=25, color="transparent"),
            title,
            subtitle,
            ft.Divider(height=25, color="transparent"),
            product_page_btn
        ],
        vertical_alignment="center",
        horizontal_alignment="center"
    )


@app.page("/products")
def Product(data: fs.Datasy):
    page = data.page

    def display_product_page_header(self):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon("settings", size=18),
                    ft.IconButton(
                        "shopping_cart_outlined",
                        on_click=lambda e: page.go("/cart"),
                        icon_size=18
                    )

                ], alignment="spaceBetween"
            )

        )

    def display_product_page_footer():
        ...

    def create_products(products: dict = Model.get_products()) -> None:
        for _, values in products.items():
            for key, value in values.items():

                if key == "img_src":
                    img_src: ft.Container = create_product_image(
                        img_path=values["img_src"])

                elif key == "name":
                    name = values["name"]

                elif key == "description":
                    description = values["description"]

                elif key == "id":
                    idd = values['id']

                elif key == "price":
                    price = create_product_price(values["price"], idd)

            texts = create_product_text(name, description)

            create_full_item_view(img_src, texts, price)

    def create_full_item_view(img_src, texts, price) -> None:
        item = ft.Column()
        item.controls.append(create_product_container(4, img_src))
        item.controls.append(create_product_container(4, texts))
        item.controls.append(create_product_container(4, price))

        products.controls.append(
            create_item_wrapper(item)
        )

    def create_item_wrapper(item: ft.Column):
        return ft.Container(width=250, height=450, content=item, padding=8,
                            border_radius=6)

    def create_product_image(self, img_path: str) -> ft.Container:
        return ft.Container(image_src=img_path, image_fit="fill",
                            border_radius=6, padding=10)

    def create_product_text(name: str, description: str) -> ft.Column:
        return ft.Column([ft.Text(name, size=18), ft.Text(description, size=11)])

    def create_product_price(price: str, idd: str):
        return ft.Row(
            [
                ft.Text(price, size=14),
                ft.IconButton("add", data=idd,
                              on_click=add_to_cart
                              )
            ]
        )

    def create_product_container(self, expand: bool, control: ft.control) -> ft.Container:
        return ft.Container(content=control, expand=expand, padding=5)

    def add_to_cart(e: ft.TapEvent):
        Model.add_item_to_cart(e.control.data)

    products = ft.Row(expand=True, scroll="auto", spacing=30)
    # create_products(products)
    return ft.View(
        controls=[
            # display_product_page_header(),
            ft.Text("Shop", size=32),
            ft.Text("Select items form the list bellow"),
            products,
            ft.FilledButton("Go to Home", on_click=lambda x: page.go("/")),

            # display_product_page_footer(),
        ],
        vertical_alignment="center",
        horizontal_alignment="center"
    )


@app.page("/teste")
def teste(data: fs.Datasy):
    page = data.page
    place = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Código"), numeric=True),
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Obervação")),
            ft.DataColumn(ft.Text("Preço")),
            ft.DataColumn(ft.Text("Estoque")),
        ],
        rows=[],
        heading_row_color="red",
        border=ft.border.all(2, ft.colors.BLACK),
        border_radius=ft.border_radius.all(20),

    )
    
   

    for index, i in enumerate(dados):
        cod = ft.Text(i["barCode"])
        nome = ft.Text(i["title"])
        obs = ft.Text(i["observation"])
        price = ft.Text(i["price"])
        stock = ft.Text(i["stock"])

        row =  ft.DataRow(
                cells=[
                    ft.DataCell(cod),
                    ft.DataCell(nome),
                    ft.DataCell(obs),
                    ft.DataCell(price),
                    ft.DataCell(stock),
                ],
                on_select_changed=lambda e: print(f"{print(e.control.cells)}"),
                color=({ft.MaterialState.HOVERED: ft.colors.BLUE_GREY_600}),
                
            )
        

        place.rows.append(
           row
        )

    return ft.View(
        horizontal_alignment="center",
        vertical_alignment="spaceBetween",

        controls=[
            ft.Container(content=place,),
            ft.Row(
                controls=[
                    ft.TextButton(icon=ft.icons.BACKPACK,  text=("Voltar"), on_click=lambda x: page.go("/")),
                    ft.TextButton(icon=ft.icons.BACKPACK,  text=("Adicionar Produto"), on_click=lambda x: page.go("/teste/new"))
                ],
                alignment="spaceAround"
                
            )

        ]
    )


@app.page("/teste/new")
def product_view(data: fs.Datasy):
    page = data.page
    return ft.View(
        controls=[
            ft.Text("teste")
        ]
    )



app.run()
