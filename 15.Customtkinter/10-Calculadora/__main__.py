from customtkinter import *

def main():
    
    operador =""
    tela=CTk()
    tela.title("Calculadora")
    tela.geometry("300x520")
    tela.resizable(False, False)

    frame1 = CTkFrame(tela, fg_color="gray")
    frame1.pack(fill="both", expand=True)

    titulo= CTkLabel(frame1, text="Calculadora", font=("Arial", 28, "bold"))
    titulo.pack(pady=10)


    text1 = CTkEntry(frame1, placeholder_text="Digite o 1º numero", width=250, height=50)
    text1.pack(pady=10)

    text2 = CTkEntry(frame1, placeholder_text="Digite o 2º numero", width=250, height=50)
    text2.pack()

    frame2 =CTkFrame(frame1, fg_color="gray")
    frame2.pack(fill="both", expand=True, padx=10, pady=10)

    def calcular():
        try:
            num1 = float(text1.get())
            num2 = float(text2.get())
        except:
            resultado.configure(text="Tente novamente")

        match operador:
            case "+":
                resultado_op = num1 + num2
            case "-":
                resultado_op = num1 - num2
            case "x":
                resultado_op = num1 * num2
            case "/":
                resultado_op = num1 / num2
        resultado.configure(text=f"{resultado_op:.1f}")

    def clicar (t):
        nonlocal operador
        operador=t



    botoes =[["+", "-"], ["x", "/"]]

    for linha, valores in enumerate(botoes):
        for coluna, texto in enumerate(valores):
            btn = CTkButton(frame2, text=texto, fg_color="#515860", corner_radius=20, width=130, height=80, 
                                    font=("Arial", 28, "bold"),command= lambda t = texto: clicar(t) )

            btn.grid(row=linha, column=coluna, padx=5, pady=5)

    btn_calcular= CTkButton(frame2, width= 200,text="Calcular",command=calcular, height=80, corner_radius=30)
    btn_calcular.place(y=210, x=40)

    resultado=CTkLabel(frame2, text="**", font=("Arial", 28, "bold"))
    resultado.grid(row=4, column=0, columnspan=2, pady=110)



        


    tela.mainloop()

if __name__ == "__main__":
    main()