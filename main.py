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
                on_click=lambda x: page.go("/cashier")
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
                    ft.TextButton(icon=ft.icons.ARROW_BACK_OUTLINED,  text=("Voltar"), on_click=lambda x: page.go("/")),
                    ft.TextButton(icon=ft.icons.BACKPACK,  text=("Adicionar Produto"), on_click=lambda x: page.go("/product/new"))
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
            ft.TextButton(icon=ft.icons.ARROW_BACK_OUTLINED, text="Voltar", on_click=lambda x: page.go("/teste"))
        ]
    )





@app.page("/cashier")
def cashier(data: fs.Datasy):
    page = data.page
    place = ft.DataTable(
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
    
   

    for index, i in enumerate(users):
        cod = ft.Text(i["cod"])
        nome = ft.Text(i["nome"])
        email = ft.Text(i["email"])

        row =  ft.DataRow(
                cells=[
                    ft.DataCell(cod),
                    ft.DataCell(nome),
                    ft.DataCell(email),
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
                    ft.TextButton(icon=ft.icons.ARROW_BACK_OUTLINED,  text=("Voltar"), on_click=lambda x: page.go("/")),
                    ft.TextButton(icon=ft.icons.ACCOUNT_CIRCLE_SHARP,  text=("Adicionar Caixar"), on_click=lambda x: page.go("/cashier/new"))
                ],
                alignment="spaceAround"
                
            )

        ]
    )


app.run()
