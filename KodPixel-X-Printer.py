import win32print
import win32ui
from PIL import Image, ImageWin
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

win =  tk.Tk()
win.title("KodPixel-X-Printer")
win.geometry("520x530")

def dosyaşeç():
    global path
    path = filedialog.askopenfilename(
        title="KodPixel-X-Printer",
        filetypes=[
            ("KodPixel-X-Printer-File", "*.kpxpf"),
            ("Jpg", "*.jpg"),
            ("Png", "*.png"),
            ("Webp", "*.webp"),
            ("Tif", "*.tif"),
            ("Pdf", "*.pdf")
        ]   
    )


printer8 = win32print.EnumPrinters(
    win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS
)
for printer3 in printer8:
    print(printer3[2])


entry = tk.Entry(win)
entry.pack()

label = tk.Label(win, text="Hangi Yazıcıya Göndermek İstediğiniz Yazının Adını Yazınız")
label.pack()

eni = tk.Entry()
eni.pack()

labeleni = tk.Label(win, text="Eni Giriniz", font=("Arial", 10))
labeleni.pack()

yüksekliği = tk.Entry(win)
yüksekliği.pack()

yüksekliğiLabel = tk.Label(win, text="Yükseliğini  Giriniz", font=("Arial", 9))
yüksekliğiLabel.pack()

menu = tk.Menu(win)
win.config(menu=menu)

liste = tk.Menu(menu,tearoff=0)
menu.add_cascade(label="DOSYA",menu=liste)

liste2 = tk.Menu(menu,tearoff=0)
menu.add_cascade(label="RENK",menu=liste2)


def renkli():
    img.convert('RGB')
    

def renksiz():
    img.convert('1')

liste.add_command(label="DOSYA SEÇ",command=dosyaşeç)
liste2.add_command(label="RENKLİ",command=renkli)
liste2.add_command(label="RENKSİZ",command=renksiz)

def yazdır():
    messagebox.showinfo("KodPixel-X-Printer", "Yazdırma İşlemine Geçiliyor")
    entry3 = entry.get()
    printer = entry3

    Hdc = win32ui.CreateDC()
    Hdc.CreatePrinterDC(printer)
    Hdc.StartDoc("KodPixel-X-Printer")
    Hdc.StartPage()

    global img
    img = Image.open(path)

    dib = ImageWin.Dib(img)

    eni2 = int(eni.get())
    yüksekliği2 = int(yüksekliği.get())

    dib.draw(Hdc.GetHandleOutput(), (0, 0, eni2, yüksekliği2))

    Hdc.EndPage()
    Hdc.EndDoc()
    Hdc.DeleteDC()

buttonyazdır = tk.Button(win, text="Yazdır", command=yazdır)
buttonyazdır.pack()

win.mainloop()