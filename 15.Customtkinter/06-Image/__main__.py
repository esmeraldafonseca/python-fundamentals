from PIL import Image
from customtkinter import * 

def main():
    
    tela = CTk()
    tela.geometry("700x400")
    tela.title("Imagens")
    tela.config(background="white")
    tela.resizable(False, False)#tranca a tela, elimina responsibilidade

    imagem = CTkImage(Image.open("icon.png"),size=(150, 150))
    label= CTkLabel(tela, image=imagem, bg_color="white", text=None)
    label.pack(pady=20)

    imagem2 = CTkImage(Image.open("icon.png"), size=(20, 20))
    btn = CTkButton(tela, image=imagem2, text="Laranja", bg_color="white")
    btn.pack()


    tela.mainloop()

if __name__ == "__main__":
    main()