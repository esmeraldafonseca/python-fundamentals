from rich import print
from rich.panel import Panel

class Comando:
    CANAL_MAX: int = 6
    CANAL_MIN: int = 1
    VOL_MAX: int = 5
    VOL_MIN: int = 1


    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def ligado_desligado(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == self.CANAL_MAX:
                self.canal_atual= self.CANAL_MIN
            else:
                self.canal_atual += 1


    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == self.CANAL_MIN:
                self.canal_atual = self.CANAL_MAX
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != self.VOL_MAX:
                self.volume_atual+=1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != self.VOL_MIN:
                self.volume_atual -= 1


    def mostrar_tv(self):
        conteudo = ""

        if not self.ligado:
            conteudo = ":prohibited: A TV está desligada..."
        else:
            conteudo = "CANAL\n"

            for canal in range(self.CANAL_MIN, self.CANAL_MAX + 1):
                if canal == self.canal_atual:
                    conteudo += f"[black on yellow] {canal} [/] "
                else:
                    conteudo += f"{canal} "

            conteudo += "\n\nVOLUME "

            for volume in range(self.VOL_MIN, self.VOL_MAX +1):
                if volume <= self.volume_atual:
                    conteudo += "[black on cyan] [/] "
                else:
                    conteudo += "[black on white] [/] "

        panel = Panel(conteudo, title="[TV]", width=50)
        print(panel)

c = Comando()

while True:
    c.mostrar_tv()
    comando =input(f"< CANAL >      - VOLUME + : ")
    match comando:
        case "<":
            c.canal_menos()
        
        case ">":
            c.canal_mais()
        
        case "+":
            c.volume_mais()
        
        case "-":
            c.volume_menos()
        
        case "@":
            c.ligado_desligado()
        
        case "0":
            break
