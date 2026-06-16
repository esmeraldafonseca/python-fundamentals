from customtkinter import *

def main():
    
    tela= CTk()
    tela.geometry("700x450")
    tela.resizable(False, False)
    tela.title("Funções")

#tela1
    pagina1 = CTkFrame(tela, bg_color="white", fg_color="#DCDCDC")
    pagina1.pack(fill="both", expand=True)

    label1_pag1 = CTkLabel(pagina1, text="Bem-vindo", font=("Arial", 30, "bold"))
    label1_pag1.place(relx=0.50, rely=0.10, anchor=CENTER)

    label2_pag1 = CTkLabel(pagina1 ,text="Clica no botão para continuar", font=("Arial", 18))
    label2_pag1.place(relx=0.50, rely=0.30, anchor=CENTER)

    def continuar():
        pagina1.forget()

#tela2
        pagina2 = CTkFrame(tela, bg_color="white", fg_color="#DCDCDC")
        pagina2.pack(fill="both", expand=True)

        label1_pag2 = CTkLabel(pagina2, text="Dados pessoais", font=("Arial", 30, "bold"))
        label1_pag2.place(relx=0.50, rely=0.10, anchor=CENTER)

        label2_pag2 = CTkLabel(pagina2 ,text="Nome: Esmeralda Fonseca\n Idade: 23\nE-mail: Esmeralda.fonseca2003@gmail.com", font=("Arial", 18))
        label2_pag2.place(relx=0.50, rely=0.30, anchor=CENTER)

        def voltar():
            pagina2.forget()
            pagina1.pack(fill="both", expand=True)

        button_voltar = CTkButton(pagina2, font=("Arial", 18), command=voltar, text="Voltar", bg_color="#DCDCDC")
        button_voltar.place(relx=0.5, rely=0.60, anchor= CENTER)

     
    button_continuar = CTkButton(pagina1,command=continuar, font=("Arial", 18), text="Continuar", bg_color="#DCDCDC")
    button_continuar.place(relx=0.5, rely=0.40, anchor= CENTER)



    tela.mainloop()

if __name__ == "__main__":
    main()