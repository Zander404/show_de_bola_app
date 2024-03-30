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


users = [
    {
        "cod": "8054",
        "nome": "Zelenia Galloway",
                "email": "risus.quis.diam@outlook.couk"
    },
    {
        "cod": "2482",
        "nome": "Scarlett Ortiz",
                "email": "luctus.ut@hotmail.edu"
    },
    {
        "cod": "1431",
        "nome": "Imogene Phelps",
                "email": "in@aol.couk"
    },
    {
        "cod": "9306",
        "nome": "Thomas Lara",
                "email": "dis@yahoo.couk"
    },
    {
        "cod": "5389",
        "nome": "Justina Francis",
                "email": "mollis.phasellus@hotmail.edu"
    }
]

orders = [
    {
        "id": "3784",
        "data": "Oct 2, 2023",
                "client": "Shana Petersen",
                "cashier": "Imogene Daugherty",
                "payment": "Crédito",
                "order": "Mexico"
    },
    {
        "id": "1547",
        "data": "Jul 14, 2024",
                "client": "Carson Kirby",
                "cashier": "Vladimir Jimenez",
                "payment": "Dinheiro",
                "order": "Australia"
    },
    {
        "id": "2192",
        "data": "Nov 3, 2023",
                "client": "David Roberson",
                "cashier": "Martina Stevens",
                "payment": "Pix",
                "order": "Germany"
    },
    {
        "id": "2091",
        "data": "Dec 14, 2023",
                "client": "Holmes Williams",
                "cashier": "Mariam Branch",
                "payment": "Dinheiro",
                "order": "New Zealand"
    },
    {
        "id": "3194",
        "data": "Feb 8, 2024",
                "client": "Garrison Sawyer",
                "cashier": "Rhoda Salas",
                "payment": "Dinheiro",
                "order": "United States"
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
                on_click=lambda x: page.go("/cashier")
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
                on_click=lambda x: page.go("/products")
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
                on_click=lambda x: page.go("/order")
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

    for x in dados:
        cod = ft.Text(x["barCode"])
        nome = ft.Text(x["title"])
        obs = ft.Text(x["observation"])
        price = ft.Text(x["price"])
        stock = ft.Text(x["stock"])

        row = ft.DataRow(
            cells=[
                ft.DataCell(cod),
                ft.DataCell(nome),
                ft.DataCell(obs),
                ft.DataCell(price),
                ft.DataCell(stock),
            ],
            on_select_changed=lambda e,i=x: print(i),
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
                    ft.TextButton(icon=ft.icons.ARROW_BACK_OUTLINED,  text=(
                        "Voltar"), on_click=lambda x: page.go("/")),
                    ft.TextButton(icon=ft.icons.BACKPACK,  text=(
                        "Adicionar Produto"), on_click=lambda x: page.go("/product/new"))
                ],
                alignment="spaceAround"

            )

        ]
    )


@app.page("/product/new")
def product_view(data: fs.Datasy):
    page = data.page
    return ft.View(
        controls=[
            ft.Text("teste"),
            ft.TextButton(icon=ft.icons.ARROW_BACK_OUTLINED,
                          text="Voltar", on_click=lambda x: page.go("/teste"))
        ]
    )


@app.page("/cashier")
def cashier(data: fs.Datasy):
    page = data.page
    df = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Cod"), numeric=True),
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("email")),
            # ft.DataColumn(ft.Text("Preço")),
            # ft.DataColumn(ft.Text("Estoque")),
        ],
        rows=[],
        heading_row_color="red",
        border=ft.border.all(2, ft.colors.BLACK),
        border_radius=ft.border_radius.all(20),

    )

    for x in users:
        cod = ft.Text(x["cod"])
        nome = ft.Text(x["nome"])
        email = ft.Text(x["email"])

        df.rows.append(ft.DataRow(
            cells=[
                ft.DataCell(cod),
                ft.DataCell(nome),
                ft.DataCell(email),
            ],
             on_select_changed=lambda e,i=x: print(i),
            color=({ft.MaterialState.HOVERED: ft.colors.BLUE_GREY_600}),

        ))


    return ft.View(
        horizontal_alignment="center",
        vertical_alignment="spaceBetween",

        controls=[
            ft.Container(content=df),
            ft.Row(
                controls=[
                    ft.TextButton(icon=ft.icons.ARROW_BACK_OUTLINED,  text=(
                        "Voltar"), on_click=lambda x: page.go("/")),
                    ft.TextButton(icon=ft.icons.ACCOUNT_CIRCLE_SHARP,  text=(
                        "Adicionar Caixar"), on_click=lambda x: page.go("/cashier/new"))
                ],
                alignment="spaceAround"

            )

        ]
    )


@app.page("/order")
def order(data: fs.Datasy):
    page = data.page
    dt = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID"), numeric=True),
            ft.DataColumn(ft.Text("Data da Compra")),
            ft.DataColumn(ft.Text("CLIENTE")),
            ft.DataColumn(ft.Text("CAIXA")),
            ft.DataColumn(ft.Text("PAGAMENTO")),
            ft.DataColumn(ft.Text("RECIBO")),
        ],
        rows=[],
        heading_row_color="red",
        border=ft.border.all(2, ft.colors.BLACK),
        border_radius=ft.border_radius.all(20),

    )

    for x in orders:

        dt.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(x["id"])),
                    ft.DataCell(ft.Text(x["data"])),
                    ft.DataCell(ft.Text(x["client"])),
                    ft.DataCell(ft.Text(x["cashier"])),
                    ft.DataCell(ft.Text(x["payment"])),
                    ft.DataCell(ft.Text(x["order"])),
                ],
                on_select_changed=lambda e,i=x: print(i),
                color=({ft.MaterialState.HOVERED: ft.colors.BLUE_GREY_600}),

            ))

    return ft.View(
        horizontal_alignment="center",
        vertical_alignment="spaceBetween",

        controls=[
            ft.Container(content=dt),
            ft.Row(
                controls=[
                    ft.TextButton(icon=ft.icons.ARROW_BACK_OUTLINED,  text=(
                        "Voltar"), on_click=lambda x: page.go("/")),
                    ft.TextButton(icon=ft.icons.LIST_ALT_OUTLINED,  text=(
                        "Adicionar Pedido"), on_click=lambda x: page.go("/cashier/new"))
                ],
                alignment="spaceAround"

            )

        ]
    )


def ler(dt: ft.DataRow, id):
    print(orders[id])


app.run()
