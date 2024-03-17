
import flet as ft

from models.model import Model

class Cart(ft.View):
    def __init__(self, page: ft.Page):
        super(Cart, self).__init__(
            route="/cart"
        )
        self.page = page
        self.initilize()


    def initilize(self):
        self.cart_items = ft.Column(spacing=20)
        self.create_cart()

        self.controls = [
            ft.Row(
                [
                    ft.IconButton(
                        "arrow_back_ios_new_outlined", 
                        on_click=lambda e: self.page.go("/products"),
                        icon_size=16,
                    ),
                ],
                alignment="spaceBetween",
            ),
            ft.Text("Cart", size=32),
            ft.Text("You Cart Items"),
            self.cart_items,
        ]

        
    def create_cart(self, cart: dict = Model.cart):
        for _, values in cart.items():
            for key, value in values.items():
                if key == "img_src":
                    img_src = self.create_item_image(values["img_src"])
                    
                elif key == "quantity":
                    quantity = self.create_item_quantity(values["quantity"])
                    
                elif key == "name":
                    name = self.create_item_name(values["name"])
                
                elif key == "price":
                    price = self.create_item_price(values["price"])
            
            self.compile_cart_item(img_src, quantity, name, price)
                    
    def create_cart_item(self):
        return ft.Row(alignment="spaceBetween")
    
    
    def compile_cart_item(self, img_src, quantity, name, price):
        row = self.create_cart_item()

        row.controls.append(img_src)
        row.controls.append(name)
        row.controls.append(quantity)
        row.controls.append(price)

        self.cart_items.controls.append(self.create_item_wrap(row))


    def create_item_wrap(self, control: ft.Control):
        return ft.Container(
            content=control,
            padding=10,
            border=ft.border.all(1, "white10"),
            border_radius=6,
        )
    def create_item_image(self, img_path: str) -> ft.Container:
        return ft.Container(image_src=img_path, image_fit="fill",
                        border_radius=6, padding=10)
    
    def create_item_quantity(self, quantity: int):
        return ft.Text(f"{quantity} X")
    
    def create_item_name(self, name: str):
        return ft.Text(name, size=16)
    
    def create_item_price(self, price: int):
        return ft.Text(price)
