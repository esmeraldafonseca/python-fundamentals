from customtkinter import * 

def main():
    
    tela = CTk()
    tela.geometry("700x400")
    tela.title("Meu primeiro app")
    tela.config(background="white")
    tela.resizable(False, False)#tranca a tela, elimina responsibilidade

    radio= CTkRadioButton(tela, font=("Arial", 16), text="Clica", radiobutton_height=30, radiobutton_width=30, border_color="black", bg_color="black", text_color="blue")
    radio.pack(pady=20)

    switch = CTkSwitch(tela,  font=("Arial", 16), text="Ligar")
    switch.pack()
    


    tela.mainloop()

if __name__ == "__main__":
    main()