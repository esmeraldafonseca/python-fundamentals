from customtkinter import *

def main():
    
    tela= CTk()
    tela.title("Posionamento de botao com grid")
    tela.geometry("700x400")
    tela.resizable(False, False)

    btn1= CTkButton(tela, width=150, height=35, text="Clica aqui", bg_color="white")
    btn1.grid(row=1, column=0)

    btn2= CTkButton(tela, width=150, height=35, text="Clica aqui", bg_color="white")
    btn2.grid(row=2, column=0)

    btn3= CTkButton(tela, width=150, height=35, text="Clica aqui", bg_color="white")
    btn3.grid(row=3, column=0)

    btn4= CTkButton(tela, width=150, height=35, text="Clica aqui", bg_color="white")
    btn4.grid(row=3, column=1)

    tela.mainloop()
    

if __name__ == "__main__":
    main()