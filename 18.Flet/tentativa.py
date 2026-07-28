import flet as ft

def main (page: ft.Page):

    PRIMARY = ft.Colors.INDIGO_400
    BACKGROUND = ft.Colors.WHITE
    ACCENT = ft.Colors.BLUE_100

    page.title = "Teste2"
    page.scroll ="auto"
    page.horizontal_alignment = "center"
    page.bgcolor = ft.Colors.WHITE

    header = ft.Container(
        content=ft.Column([
        ft.Text("Eu sou...", size=20, weight="bold", color=PRIMARY),
        ft.Text("Esmeralda Fonseca", size=20, weight="bold", color=PRIMARY),
        ft.ElevatedButton("Ver mais")])
        )
    info = ft.Row([])
    galery = ft.Row([])
    footer = ft.Row([
        ft.Text("Deselvolvido por @Esmeralda Fonseca  2026")],
        alignment="center")

    page.add(ft.Container(
        content= ft.Column([
            header,
            ft.Divider(),
            info,
            ft.Divider(),
            galery,
            ft.Divider(),
            footer
        ]), 
        alignment= ft.Alignment.CENTER, 
        width=1200
        ))

if __name__ == "__main__":
    ft.run(main)