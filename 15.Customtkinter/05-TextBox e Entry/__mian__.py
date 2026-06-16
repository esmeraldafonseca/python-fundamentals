from tkinter import PhotoImage
from customtkinter import * 

def main():
    
    tela = CTk()
    tela.geometry("700x400")
    tela.title("Meu primeiro app")
    tela.config(background="white")
    tela.resizable(False, False)

    #texto sem enter
    entry= CTkEntry(tela, width=300, height=50, bg_color="white", placeholder_text="Digite o seu nome")
    entry.pack(pady=20)

    #texto com enter
    textbox = CTkTextbox(tela, width=300, height=300, bg_color="white", fg_color="black")
    textbox.pack()


    tela.mainloop()

if __name__ == "__main__":
    main()