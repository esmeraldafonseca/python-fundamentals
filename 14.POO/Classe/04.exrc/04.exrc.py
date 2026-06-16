import time
class Livro:

    def __init__(self, titulo, numero_de_paginas):
        self.total_paginas = numero_de_paginas
        self.titulo = titulo
        self.pagina_actual = 1
        print(f"""Acabaste de abrir o livro {self.titulo}, que tem {self.total_paginas} paginas. Estas na paginas {self.pagina_actual}""")
        
    def __str__(self):
        return 

    def avancar_pagina(self, quantidade =1):
        contador = 0
        print(f"Avançaste {contador}.",  end=" ")
        for paginas in range(0, quantidade, 1):
            if not self.fim_do_livro():
                self.pagina_actual += 1                
                print(f"{self.pagina_actual} =>", end="")
                time.sleep(0.3)
                contador+=1
        print(f"Agora estás na pagina {self.pagina_actual}")

        if self.fim_do_livro():
            print("Chegaste ao final do livro")
    
    def fim_do_livro(self) -> bool:
        return True if self.pagina_actual == self.total_paginas else False



livro1 = Livro("Flores são não mortos", 29)
livro1.avancar_pagina(12)
livro1.avancar_pagina(4)
livro1.avancar_pagina(1)
#o while quebra com maior facilidade
#é sobre saber ler codigo 