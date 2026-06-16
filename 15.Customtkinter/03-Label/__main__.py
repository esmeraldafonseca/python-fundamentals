from customtkinter import *

def main():
    tela = CTk()
    tela.title("Label")
    tela.geometry("700x400")
    tela.resizable(False, False)

    label =CTkLabel(tela, text="Curso de custom Tkinter", text_color="black", font=("Arial", 20, "bold"))
    label.pack(pady=20)

    tela.mainloop()


if __name__ == "__main__":
    main()