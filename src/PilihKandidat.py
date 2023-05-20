from pathlib import Path
from tkinter import DISABLED, FLAT, LEFT, NORMAL, RIGHT, LabelFrame, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox, scrolledtext
import tkinter as Tk
from PIL import ImageTk, Image
from hashlib import sha3_256
import Pemilih

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class PilihKandidatPage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.PilihKandidat()
    
    def PilihKandidat(self):
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
            file=relative_to_assets("encrypt_button.png"))
        self.encrypt_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.enkrip(
                self.pilih_nomor.get("1.0", Tk.END).strip(), 
                int(self.e.get("1.0", Tk.END)), 
                int(self.n.get("1.0", Tk.END))
            ),
            relief="flat"
        )
        self.encrypt_button.place(
            x=515.0,
            y=620.0,
            width=250.58250427246094,
            height=55.0
        )

        self.pilih_nomor = Text(
            self.canvas, 
            width=60, 
            height=1, 
            font=("Times New Roman", 10)
        )
        self.pilih_nomor.place(
            x=458.0,
            y=270.0
        )

        publickey_e = LabelFrame(
            self.canvas,
            relief=FLAT, 
            background="#FFFFFF"
        )
        publickey_e.place(x=570, y=355)

        self.e = Text(
            publickey_e, 
            width=41, 
            height=1, 
            font=("Times New Roman", 10), 
            background="#FFFFFF"
        )
        self.e.pack(side = LEFT)
        self.e.config(state = DISABLED)

        publickey_n = LabelFrame(
            self.canvas,
            relief=FLAT, 
            background="#FFFFFF"
        )
        publickey_n.place(x=570, y=382)

        self.n = Text(
            publickey_n, 
            width=41, 
            height=1, 
            font=("Times New Roman", 10), 
            background="#FFFFFF"
        )
        self.n.pack(side = LEFT)
        self.n.config(state = DISABLED)

        self.input = scrolledtext.ScrolledText(
            self.canvas, 
            wrap=Tk.WORD,
            width=56, 
            height=8, 
            font=("Times New Roman", 10)
        )
        self.input.place(x=458, y=450)

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("pilih_Kunci.png"))
        self.pilih_Kunci = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.GetPublicKey(),
            relief="flat"
        )
        self.pilih_Kunci.place(
            x=459.0,
            y=355.0,
            width=75.0,
            height=48.0
        )

        self.saveButton = Button(
            self.canvas,
            text="Save File", 
            command=lambda: self.saveEncrypted(
                self.input.get("1.0", Tk.END).strip()
            ), 
            bg='#FA8072'
        )
        self.saveButton.place(x=615, y=680)

        self.canvas.create_text(
            545.0,
            355.0,
            anchor="nw",
            text="e:",
            fill="#000000",
            font=("Inter Regular", 20 * -1)
        )

        self.canvas.create_text(
            546.0,
            381.0,
            anchor="nw",
            text="n:",
            fill="#000000",
            font=("Inter Regular", 20 * -1)
        )

        self.canvas.create_text(
            975.0,
            547.0,
            anchor="nw",
            text="2. Daniel",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.canvas.create_text(
            236.0,
            547.0,
            anchor="nw",
            text="1. Abel",
            fill="#000000",
            font=("Inter Bold", 20 * -1)
        )

        self.canvas.create_text(
            459.0,
            320.0,
            anchor="nw",
            text="Kunci publik:",
            fill="#000000",
            font=("Inter Regular", 20 * -1)
        )

        self.canvas.create_text(
            459.0,
            232.0,
            anchor="nw",
            text="Masukkan nama kandidat:",
            fill="#000000",
            font=("Inter Regular", 20 * -1)
        )

        self.canvas.create_text(
            498.0,
            97.0,
            anchor="nw",
            text="Kandidat",
            fill="#000000",
            font=("Inter Bold", 64 * -1)
        )

        self.abel_kandidat = Image.open(relative_to_assets("abel_kandidat.png"))
        self.abel_kandidat = self.abel_kandidat.resize((222, 305), Image.ANTIALIAS)
        self.abel_kandidat = ImageTk.PhotoImage(self.abel_kandidat)
        self.canvas.create_image(
            270.0,
            380.0,
            image=self.abel_kandidat
        )

        self.daniel_kandidat = Image.open(relative_to_assets("daniel_kandidat.png"))
        self.daniel_kandidat = self.daniel_kandidat.resize((222, 305), Image.ANTIALIAS)
        self.daniel_kandidat = ImageTk.PhotoImage(self.daniel_kandidat)
        self.canvas.create_image(
            1015.0,
            380.0,
            image=self.daniel_kandidat
        )

    # start page
    def startPage(self):
        self.mainloop()

    # Buka file pub
    def GetPublicKey(self):
        try:
            self.filename_key = filedialog.askopenfilename(
                title='Open a file',
                initialdir='Key/',
                filetypes =[('Public key files', '*.pub')]
                )
            with open(self.filename_key, 'rb') as f:
                self.fileinput = f.read().decode("latin-1")
            f.close()
            key = self.fileinput[1:-1]
            D,N = str(key).split(", ")
            self.e.config(state = NORMAL)
            self.e.delete('0.0', Tk.END)
            self.e.insert(Tk.END, f'{int(D)}')
            self.e.config(state = DISABLED)
            self.n.config(state = NORMAL)
            self.n.delete('0.0', Tk.END)
            self.n.insert(Tk.END, f'{int(N)}')
            self.n.config(state = DISABLED)
        except:
            False

    # Enkripsi
    def enkrip(self, message, e, n):
        cipher = [(ord(char) ** e) % n for char in message]
        self.input.insert(Tk.END, cipher)
        messagebox.showinfo("Encryption Successful",f"Message encrypted successfully.")
    
    # Save file hasil enkripsi
    def saveEncrypted(self, encrypted_message):
        try:
            file_path = filedialog.asksaveasfilename(
                initialdir=OUTPUT_PATH,
                title="Save Encrypted File",
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt")]
            )
            with open(file_path, 'w') as f:
                f.write(str(encrypted_message.split(': ')[-1]))
            messagebox.showinfo("Save Encrypted File", "Encrypted message saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the encrypted file: {str(e)}")
        self.origin.Home()