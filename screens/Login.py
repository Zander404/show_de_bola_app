import flet as ft

class Login(ft.View):
    def __init__(self, page: ft.Page):
        super(Login, self).__init__(
            route="/login",
            horizontal_alignment="center",
            vertical_alignment="center",
        )

        self.page = page
        self.initialize()

    def initialize(self):

        # Componentes de Erro
        self.error_text = ft.Container(content=ft.Row(
            [
                ft.Icon("error", color="red3"),
                ft.Text("Email ou senha inválido!",
                        color="red1", weight="bold")
            ], alignment="center"),
            visible=False,
        )

        self.wait = ft.ProgressRing(visible=False)

        # Componentes Visuais

        self.email = ft.TextField(label="Email", adaptive=True,
                                  border_radius=5, border="")

        self.senha = ft.TextField(label="Senha", password=True,
                                  adaptive=True, border_radius=5, border="", can_reveal_password=True, content_padding=20, shift_enter=True)

        self.login_page = ft.Container(content=ft.Column(
            [
                self.email,
                self.senha,
                ft.Divider(),
                ft.Row(
                    [ft.TextButton(
                        "Logar", icon="login", on_click=self.fazer_login
                    ),
                    ], alignment="center",
                ),

            ],
            alignment="center",
            spacing=20,


        )
        )

        self.controls = [
            ft.Image(src="placeholder.jpeg",
                     width=400,
                     height=400,
                     fit=ft.ImageFit.CONTAIN,
                     border_radius=9),
            ft.Text("To tentando Caralho", text_align="center", weight="bold"),
            self.error_text,
            self.login_page,
            self.wait,

        ]

    def teste123(self, queue):
        self.wait.visible=True
        self.page.update()
        queue.put("Foi")
        

     
    def fazer_login(self, e):
        import threading
        import queue

        email = self.email
        senha = self.senha
        
        self.error_text.visible = False
        q = queue.Queue()

        teste1 = threading.Thread(target=self.teste123, args=(q,))

        teste1.start()
        teste1.join()

        print(q.get())
        if email.value == "admin" and senha.value == "admin":
            # print(f"Fazer Login\n email:{email.value}\nSenha: {senha.value}")        
            self.page.go("/")

            
        else:
            self.wait.visible = False
            self.error_text.visible = True
            self.email
            self.senha
            print(f"Fazer Login\n email:{email.value}\nSenha:{senha.value}")
            print("Senha Inválida!")
            self.page.update()
