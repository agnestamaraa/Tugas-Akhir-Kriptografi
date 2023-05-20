from pathlib import Path
from tkinter import DISABLED, FLAT, LEFT, NORMAL, RIGHT, Label, LabelFrame, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox, scrolledtext
import tkinter as Tk
from hashlib import sha3_256
import PilihKandidat

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class PanitiaPage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Panitia()
    
    def Panitia(self):
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
            file=relative_to_assets("decrypt_button.png"))
        self.decrypt_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.dekrip(),
            relief="flat"
        )
        self.decrypt_button.place(
            x=515.0,
            y=510.0,
            width=250.58250427246094,
            height=55.0
        )

        self.fileMasukan = StringVar()
        self.entry_image1 = PhotoImage(
            file=relative_to_assets("masukan_file.png"))
        self.masukan_file = Entry(
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.fileMasukan
        )
        self.masukan_file.place(
            x=459.0,
            y=270.0,
            width=365.0,
            height=103.0
        )

        self.b2 = Button(
            self.canvas,
            text="Pilih File",
            command=lambda: self.uploadEncryptedFile(),  # ini diganti buat pilih file
            bg='#FA8072'
        )
        self.b2.place(x=800, y=232)

        privatekey_d = LabelFrame(
            self.canvas,
            relief=FLAT, 
            background="#FFFFFF"
        )
        privatekey_d.place(x=570, y=435)

        self.d = Text(
            privatekey_d, 
            width=41, 
            height=1, 
            font=("Times New Roman", 10), 
            background="#FFFFFF"
        )
        self.d.pack(side = LEFT)
        self.d.config(state = DISABLED)

        privatekey_n2 = LabelFrame(
            self.canvas,
            relief=FLAT, 
            background="#FFFFFF"
        )
        privatekey_n2.place(x=570, y=462)

        self.n2 = Text(
            privatekey_n2, 
            width=41, 
            height=1, 
            font=("Times New Roman", 10), 
            background="#FFFFFF"
        )
        self.n2.pack(side = LEFT)
        self.n2.config(state = DISABLED)

        self.output = scrolledtext.ScrolledText(
            self.canvas, 
            wrap=Tk.WORD,
            width=56, 
            height=8, 
            font=("Times New Roman", 10)
        )
        self.output.place(x=459, y=590)

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("pilih_Kunci.png"))
        self.pilih_Kunci = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.GetPrivateKey(),
            relief="flat"
        )
        self.pilih_Kunci.place(
            x=459.0,
            y=435.0,
            width=75.0,
            height=48.0
        )

        self.saveButton = Button(
            self.canvas,
            text="Save File", 
            command=lambda: self.saveDecrypted(
                self.output.get("1.0", Tk.END).strip()
            ), 
            bg='#FA8072'
        )
        self.saveButton.place(x=860, y=640)

        self.canvas.create_text(
            545.0,
            435.0, # 180 semua
            anchor="nw",
            text="d:",
            fill="#000000",
            font=("Inter Regular", 20 * -1)
        )

        self.canvas.create_text(
            542.0,
            461.0,
            anchor="nw",
            text="n2:",
            fill="#000000",
            font=("Inter Regular", 20 * -1)
        )

        self.canvas.create_text(
            459.0,
            400.0,
            anchor="nw",
            text="Kunci privat:",
            fill="#000000",
            font=("Inter Regular", 20 * -1)
        )

        self.canvas.create_text(
            459.0,
            232.0,
            anchor="nw",
            text="Masukkan file enkripsi suara pemilih:",
            fill="#000000",
            font=("Inter Regular", 20 * -1)
        )

        self.canvas.create_text(
            350.0,
            97.0,
            anchor="nw",
            text="Perhitungan Suara",
            fill="#000000",
            font=("Inter Bold", 64 * -1)
        )

    # start page
    def startPage(self):
        self.mainloop()

    # Buka file pri
    def GetPrivateKey(self):
        try:
            self.filename_key = filedialog.askopenfilename(
                title='Open a file',
                initialdir='Key/',
                filetypes =[('Private key files', '*.pri')]
                )
            with open(self.filename_key, 'rb') as f:
                self.fileinput = f.read().decode("latin-1")
            f.close()
            key = self.fileinput[1:-1]
            E,N = str(key).split(", ")
            self.d.config(state = NORMAL)
            self.d.delete('0.0', Tk.END)
            self.d.insert(Tk.END, f'{int(E)}')
            self.d.config(state = DISABLED)
            self.n2.config(state = NORMAL)
            self.n2.delete('0.0', Tk.END)
            self.n2.insert(Tk.END, f'{int(N)}')
            self.n2.config(state = DISABLED)
        except:
            False

    # upload file txt of plaintext
    def uploadEncryptedFile(self):
        file = filedialog.askopenfile(mode='rb', filetypes =[('Text files', 'txt')])
        if file != None:
            read_filetxt = bytearray(file.read())
            text = read_filetxt.decode("latin-1")
            self.fileMasukan.set(text)

    # Dekripsi
    def dekrip(self):
        encrypted_message = self.masukan_file.get()
        d = int(self.d.get()) 
        n2 = int(self.n2.get())
        encrypted_list = [int(char) for char in encrypted_message.split()]
        # plain = [chr((char ** d) % n2) for char in encrypted_message]
        plain = [chr(pow(char, d, n2)) for char in encrypted_list]
        decrypted_message = ''.join(plain)
        self.output.insert(Tk.END, decrypted_message)
        messagebox.showinfo("Decryption Successful", "Message decrypted successfully.")

    # Save file hasil enkripsi
    def saveDecrypted(self, decrypted_message):
        try:
            file_path = filedialog.asksaveasfilename(
                initialdir=OUTPUT_PATH,
                title="Save Decrypted File",
                defaultextension=".txt",
                filetypes=[("Text files", "*.dec")]
            )
            with open(file_path, 'w') as f:
                f.write(str(decrypted_message))
            messagebox.showinfo("Save Decrypted File", "Decrypted message saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the encrypted file: {str(e)}")
        self.origin.Home()