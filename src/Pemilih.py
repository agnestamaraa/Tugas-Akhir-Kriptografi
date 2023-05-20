from pathlib import Path
from tkinter import StringVar, Tk, Canvas, Entry, Button, PhotoImage, messagebox
import tkinter as Tk
import random

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class PemilihPage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Pemilih()

    def Pemilih(self):
        self.canvas = Canvas(
            self.master,
            bg = "#F4F3F9",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("genKey_button.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.GenerateKey(),
            relief="flat"
        )
        self.button_1.place(
            x=515.0,
            y=465.0,
            width=250.58250427246094,
            height=55.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("next_button.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.click_Next(), # ini nanti diganti commandnya
            relief="flat",
            state="disabled"
        )
        self.button_2.place(
            x=1101.0,
            y=685.0,
            width=141.0,
            height=55.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("back_button.png"))
        self.back_button = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.click_backHome(),
            relief="flat"
        )
        self.back_button.place(
            x=95.0,
            y=104.0,
            width=97.0,
            height=55.0
        )        

        self.name = StringVar()
        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_name.png"))
        self.entry_bg_1 = self.canvas.create_image(
            640.0,
            415.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.name
        )
        self.entry_1.place(
            x=417.0,
            y=352.0,
            width=446.0,
            height=59.0
        )

        self.canvas.create_text(
            417.0,
            320.0, #awalnya 353
            anchor="nw",
            text="Nama Pemilih:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            280.0,
            97.0,
            anchor="nw",
            text="Pemilihan Umum 2050",
            fill="#000000",
            font=("Inter Bold", 64 * -1)
        )
    
    def assignName(self):
        self.namaPemilih = str(self.name.get())

    def startPage(self):
        self.mainloop()

    def click_Next(self):
        self.origin.PilihKandidat()

    # back home
    def click_backHome(self):
        self.origin.Home()

    def isPrime(self,number):
        if(number < 2):
            return False
        else:
            for i in range(2, number):
                if((number % i)) == 0:
                    return False
            return True

    def primeNumber(self, minRange, maxRange):
        while(1):
            number = random.randint(minRange, maxRange)
            if self.isPrime(number):
                return number

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def eValue(self, totient):
        while(1):
            e = random.randint(1, totient)
            if(self.gcd(e, totient)==1):
                break
        return e

    def dValue(self, e, totient):
        d = 2
        while(1):
            if((d*e) % totient) == 1:
                break
            d += 1
        return d

    def genPubPrivKey(self):
        p = self.primeNumber(100, 500)
        q = self.primeNumber(100, 500)

        if (p != q):
            n = p*q
            totient = (p-1)*(q-1)
            e = self.eValue(totient)
            d = self.dValue(e, totient)
            # pasangan (e,n)
            publicKey = (e,n)
            # pasangan (d,n)
            privateKey = (d,n)
            return (publicKey, privateKey)

    # Generate key
    def GenerateKey(self):
        key = self.genPubPrivKey()
        priv = key[0]
        pub = key[1]
        namafile = self.name.get()
        if namafile == '':
            messagebox.showerror("Error",f"Masukkan nama pemilih")
        else:
            try:
                with open(f"key/{namafile}.pri", "w") as myfile:
                    myfile.write(f"{priv}")
                with open(f"key/{namafile}.pub", "w") as myfile:
                    myfile.write(f"{pub}")
                messagebox.showinfo("info", f"Kunci berhasil disimpan di key/{namafile}.pri dan key/{namafile}.pub")
                self.button_2.config(state="normal")
            except Exception as E:
                messagebox.showerror("Error",f"Kunci tidak dapat disimpan, {E}")