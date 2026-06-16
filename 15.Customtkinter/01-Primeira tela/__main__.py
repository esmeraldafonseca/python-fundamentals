from tkinter import PhotoImage
from customtkinter import * 

def main():
    
    tela = CTk()
    tela.geometry("700x400")
    tela.title("Meu primeiro app")
    tela.config(background="white")
    tela.resizable(False, False)#tranca a tela, elimina responsibilidade


    icon = PhotoImage(file="icon.ico")
    tela.iconphoto(True, icon)


    tela.mainloop()

if __name__ == "__main__":
    main()