from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import Combobox
import canlı_algılama

window = Tk()
photo = PhotoImage(file="dosyalar/fotograflar/ilk_ekran_deneme2.png")
w = Label(window, image=photo)
window.iconbitmap("dosyalar/fotograflar/ilk_ekran_deneme2.ico")
photo_basla=PhotoImage(file="dosyalar/fotograflar/basla.png")
photo_info=PhotoImage(file="dosyalar/fotograflar/info.png")
photo_ayarlar=PhotoImage(file="dosyalar/fotograflar/ayarlar.png")


w.pack()

window.title("Hoşgeldiniz")


def basla():
    window.destroy()
    canlı_algılama.canlı_algılama()

def ayarlar():
    with open("dosyalar/ayarlar/font.txt", "r") as dosya:
        font=dosya.readline()

    window2 = Tk()
    window2.iconbitmap("dosyalar/fotograflar/ayarlar.ico")
    window2.title("Ayarlar")
    photo2 = PhotoImage(file="dosyalar/fotograflar/ayarlar_secim.png", master=window2)
    w2= Label(window2, image=photo2)
    w2.pack()

    secenekler=["Calibri","Arial","Verdana"]
    secenekler2 = ["Sarı","Kırmızı","Yesil","Mavi","Siyah"]

    combo1 = Combobox(window2, values=secenekler ,font=font)
    combo1.place(x=185, y=190)
    combo1.current(0)

    combo2 = Combobox(window2, values=secenekler2, font=font)
    combo2.place(x=185, y=295)
    combo2.current(0)
    def uygula():
        with open("dosyalar/ayarlar/font.txt", "w") as dosya:
            dosya.write(combo1.get())
        with open("dosyalar/ayarlar/renk.txt", "w") as dosya:
            dosya.write(combo2.get())

        window2.destroy()
    font_uygula=tkFont.Font(family='Arial',size=8)
    btn_uygula = Button(window2,bg='black', fg='#5881cc',text='Uygula', command=uygula,height=2, relief=FLAT,font=font_uygula)
    btn_uygula.place(x=220,y=400)


    window2.mainloop()



def info():
    window2 = Tk()
    window2.iconbitmap("dosyalar/fotograflar/info.ico")
    window2.title("Info")
    photo2 = PhotoImage(file="dosyalar/fotograflar/info_window.png", master=window2)
    w2 = Label(window2, image=photo2)
    w2.pack()

    def geri():
        window2.destroy()

    font_uygula = tkFont.Font(family='Arial', size=8)
    btn_uygula = Button(window2, bg='black', fg='#5881cc', text='Geri', command=geri, height=2, relief=FLAT,
                        font=font_uygula)
    btn_uygula.place(x=220, y=400)
    window2.mainloop()


btn_basla = Button(bg='black',fg='black', image=photo_basla,command=basla,relief=FLAT)
btn_basla.place(relx=0.5, rely=0.5, anchor=CENTER)

btn_info = Button(bg='black',fg='black', image=photo_info,command=info,relief=FLAT)
btn_info.place(relx=0.05, rely=0.95, anchor=CENTER)

btn_ayarlar = Button(bg='black',fg='black', image=photo_ayarlar,command=ayarlar,relief=FLAT)
btn_ayarlar.place(relx=0.95, rely=0.05, anchor=CENTER)

window.mainloop()

