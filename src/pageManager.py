from tkinter import Tk
import Home, PilihKandidat, Pemilih, Panitia

class pageManager():
    def __init__(self):
        self.user = None
        self.window = Tk()
        self.window.geometry("1280x832")
        self.window.configure(bg = "#FFFFFF")
        self.window.title('Kriptografi dan Koding')
        self.window.resizable(False, False)

        self.page = Home.HomePage(master=self.window, pageManager=self)
    
    def run(self):
        self.page.startPage()
        
    def Home(self):
        self.page = Home.HomePage(master = self.window, pageManager = self)
        self.page.startPage()

    def Pemilih(self):
        self.page = Pemilih.PemilihPage(master = self.window, pageManager = self)
        self.page.startPage()

    def PilihKandidat(self):
        self.page = PilihKandidat.PilihKandidatPage(master = self.window, pageManager = self)
        self.page.startPage()

    def Panitia(self):
        self.page = Panitia.PanitiaPage(master = self.window, pageManager = self)
        self.page.startPage()