from rich import print

class Caneta:
    """
    Classe que simula o comportamento de canetas podendo tampar ou destampar elas, 
    lembrando que uma caneta tampada não escreve
    """
    def __init__(self, cor):
        cores_validas = ["vermelha", "azul", "verde"]
        self.tampa = False
        if cor.lower() in cores_validas:
            self.cor = cor.lower()
        else:
            raise Exception ("Caneta inexistente")

    def tampar(self):
        self.tampa = False
        return self.tampa

    def destampar(self):
        self.tampa = True
        return self.tampa

    def quebrar_linha(self, quantidade):
        print("\n" * quantidade, end="")


    def escrever(self, conteudo):
        if self.tampa:
            match self.cor:
                case "azul":
                    print(f"[blue]{conteudo}[/]")
                    
                case "vermelha":
                    print(f"[red]{conteudo} [/]")
                    
                case "verde":
                    print(f"[green]{conteudo}[/]")
                    
        else:
            print("Destampe primeiro.")

c1 = Caneta("AZUL")
c2 = Caneta("Vermelha")
c3 = Caneta("verde")

c3.destampar()
c1.destampar()
c2.destampar()

c3.escrever("Ola, tudo bem?")
c1.quebrar_linha(2)
c2.escrever("Entao? Como vai a vida?")
c1.escrever("Muito do mesmo")
