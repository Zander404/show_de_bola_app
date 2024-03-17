import flet as ft

from models.model import Model


class Product(ft.View):
    def __init__(self, page: ft.Page) -> None:
        super(Product, self).__init__(
            route="/products"
        )
        self.page = page
        self.initilize()

    def initilize(self):
        self.products = ft.Row(expand=True, scroll="auto", spacing=30)
        self.create_poducts()

        self.controls = [
            self.display_product_page_header(),
            ft.Text("Shop",size=32),
            ft.Text("Select items form the list bellow"),
            self.products,
            # self.display_product_page_footer(),
        ]

    def display_product_page_header(self):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon("settings", size=18),
                    ft.IconButton(
                        "shopping_cart_outlined",
                        on_click=lambda e: self.page.go("/cart"),
                        icon_size=18
                    )

                ], alignment="spaceBetween"
            )

        )
    
    def display_product_page_footer(self):
        ...

    def create_poducts(self, products: dict = Model.get_products()) -> None:
        for _, values in products.items():
            for key, value in values.items():

                if key == "img_src":
                    img_src: ft.Container = self.create_product_image(img_path=values["img_src"])

                elif key == "name":
                    name = values["name"]
                    
                elif key == "description":
                    description = values["description"]

                elif key == "id":
                    idd = values['id']
                    
                elif key == "price":
                    price = self.create_product_price(values["price"], idd)

            texts  = self.create_product_text(name, description)

            self.create_full_item_view(img_src, texts, price)

    

    def create_full_item_view(self, img_src, texts, price) -> None:
        item = ft.Column()
        item.controls.append(self.create_product_container(4, img_src))
        item.controls.append(self.create_product_container(4, texts))
        item.controls.append(self.create_product_container(4, price))
        
        self.products.controls.append(
            self.create_item_wrapper(item)
        )



    def create_item_wrapper(self, item: ft.Column):
        return ft.Container( width=250, height=450, content=item, padding=8,
                            border_radius=6)

    def create_product_image(self, img_path: str) -> ft.Container:
        return ft.Container(image_src=img_path, image_fit="fill",
                            border_radius=6, padding=10)
    
    def create_product_text(self, name: str, description: str) -> ft.Column:
        return ft.Column([ft.Text(name, size=18), ft.Text(description, size=11)])

    def create_product_price(self, price: str, idd: str):
        return ft.Row(
            [
                ft.Text(price, size=14),
                ft.IconButton("add", data=idd, 
                              on_click=self.add_to_cart
                              )
            ]
        )
    
    def create_product_container(self, expand: bool, control: ft.control) -> ft.Container: 
        return ft.Container(content=control, expand=expand, padding=5)

    def add_to_cart(self, e: ft.TapEvent):
        Model.add_item_to_cart(e.control.data)