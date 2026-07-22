class Livro:

    def __init__(self, titulo, pagina):
        self.titulo = titulo
        self.total_paginas = pagina
        self.pagina_actual=1

        print(f"Acabaste de abrir o livro {self.titulo}, que tem {self.total_paginas} paginas. Estas na paginas {self.pagina_actual}")


    def avancar_pagina(self, quantidade):
    

        while True:
            if quantidade >= self.total_paginas :
                print("Livro acabou")
                break

            if quantidade <= self.total_paginas:
                pass
            

        

livro1 = Livro("1984", 20)
livro1.avancar_pagina(10)