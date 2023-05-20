from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as Tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class HomePage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Home()

    def Home(self):
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
            file=relative_to_assets("pemilih_button.png"))
        self.pemilih_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.click_Pemilih(), # ini nanti diganti sama tombol ke page home
            relief="flat"
        )
        self.pemilih_button.place(
            x=488.0,
            y=302.0,
            width=303.0,
            height=105.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("panitia_button.png"))
        self.panitia_button = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.click_Panitia(),  # ini nanti diganti ke page yang buat pemilih dekripsi
            relief="flat"
        )
        self.panitia_button.place(
            x=488.0,
            y=425.0,
            width=303.0,
            height=105.0
        )

        self.canvas.create_text(
            230.0,
            97.0,
            anchor="nw",
            text="E-Voting Pemilihan Umum",
            fill="#000000",
            font=("Inter Bold", 64 * -1)
        )

    # start page
    def startPage(self):
        self.mainloop()

    # jika pemilih
    def click_Pemilih(self):
        self.origin.Pemilih()

    # jika panitia
    def click_Panitia(self):
        self.origin.Panitia()