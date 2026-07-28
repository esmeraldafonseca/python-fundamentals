import flet as ft

def main (page: ft.Page):

    #Definição das cores principais
    PRIMARY = ft.Colors.INDIGO_400
    BACKGROUND = ft.Colors.WHITE
    ACCENT = ft.Colors.BLUE_100

    CENTRO = ft.Alignment.CENTER

    page.title = 'Meu Portfolio'
    page.scroll = 'auto'
    page.theme_mode = 'light'
    page.horizontal_alignment ="center"
    page.bgcolor = BACKGROUND

    about_us = ft.Container(
        content = ft.Column([
            ft.Text('Olá, meu nome é...', size=30, weight='bold', color= PRIMARY),
            ft.Text('Esmeralda Fonseca', size=40, weight='bold', color=PRIMARY),
            ft.ElevatedButton("Ver projectos", color= BACKGROUND, bgcolor=PRIMARY)
        ]),
        alignment= ft.Alignment.CENTER_LEFT,
        padding= ft.Padding.all(20),
        border_radius= ft.BorderRadius.all(12),
        bgcolor= ACCENT
    )

    lista_projetos = [
        {"title":"Student Task Planer", "description": "Um aplicativo desktop para criação e organizção de tarefas acadamemicas"},
        {"title":"Personal Finance Manager", "description": "Um app python"},
        {"title":"Portfolio com Python", "description": "Um app python"}
    ] 
    projects =  ft.Container(
        content= ft.Column([
            ft.Text("Projectos", size=38, color=PRIMARY),
            ft.Text("Veja aqui alguns dos meus projectos mais recentes, " \
            "clica em saber mais para navegar por todos", size=20, color=ft.Colors.BLACK_54),
            ft.Row([ft.Container(
                content=ft.Column([
                    ft.Text(project['title'], size=22, color=PRIMARY, weight='bold'),
                    ft.Text(project['description'], size=18, color=ft.Colors.BLACK_54)
                ], spacing=1),
                padding=12,
                bgcolor= ACCENT,
                border_radius= ft.BorderRadius.all(8),
                width=240,
                height=150
            )for project in lista_projetos
            ], run_spacing= 10, spacing=20
            )
        ]), padding=ft.Padding.all(40)
    )

    contact = ft.Container(
        content= ft.Column([
            ft.Text("Contatos", size=38, color=PRIMARY),
            ft.Text("Vamos conversar sobre novas oportunidades e colaborações, não hesite em contactar! ",
                     size=20, color=ft.Colors.BLACK_54), 

            ft.TextField(label="Nome", border_radius=ft.BorderRadius.all(12), width=600),
            ft.TextField(label="Email", border_radius=ft.BorderRadius.all(12), width=600),
            ft.TextField(label="Mensagem", multiline=True, border_radius=ft.BorderRadius.all(12), width=600) ,

            ft.ElevatedButton("Enviar", 
                            on_click=lambda e: page.show_dialog(ft.SnackBar(content=ft.Text("Mensagem enviada!"))),
                            color= BACKGROUND, 
                            bgcolor=PRIMARY,
                            style=ft.ButtonStyle(padding=ft.Padding.symmetric(horizontal=80, vertical=30))
                            )
        ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
          alignment= CENTRO,
          padding= ft.Padding.all(10), 
          bgcolor= ACCENT,
          border_radius= ft.BorderRadius.all(12)
    )

    footer = ft.Row([  
                ft.Text('Desenvolvido por @Esmeralda Fonseca : 2026', 
                color=ft.Colors.BLACK_54)],
                alignment = 'center')


    page.add(
        ft.Container(
            content= ft.Column([
                about_us,
                ft.Divider(),
                projects,
                ft.Divider(),
                contact,
                ft.Divider(),
                footer
            ])      ,
            alignment = CENTRO,
            width=800
        )
        
    )

if __name__ == "__main__":
    ft.run(main)