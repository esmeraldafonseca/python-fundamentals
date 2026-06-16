from tkinter import PhotoImage
from customtkinter import * 

def main():
    
    tela = CTk()
    tela.geometry("400x500")
    tela.title("Meu primeiro app")
    tela.config(background="white")
    tela.resizable(False, False)

    frame = CTkFrame(tela, width=360, height=460, fg_color="blue", bg_color="white")
    frame.place(x=20, y=20)

    frame1 = CTkFrame(frame, width=340, height=40, fg_color="red", bg_color="blue")
    frame1.place(x=10, y=20)

    label1 = CTkLabel(frame1, text="Curso de customTkinder", font=("Arial", 20))
    label1.place(relx=0.50, rely=0.50, anchor=CENTER)

    frame2 =CTkFrame(frame, width=200, height=380, fg_color="yellow", bg_color="blue")
    frame2.place(x=10, y=70)

    frame3 = CTkFrame(frame, width=140, height=200, corner_radius=100, bg_color="blue", fg_color="orange")
    frame3.place(x=215, y=70)

    tela.mainloop()

if __name__ == "__main__":
    main()