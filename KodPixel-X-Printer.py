import win32print
import win32ui
from PIL import Image, ImageWin
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

win =  tk.Tk()
win.title("KodPixel-X-Printer")
win.geometry("520x530")

printer8 = win32print.EnumPrinters(
    win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS
)
for printer3 in printer8:
    print(printer3[2])


label = tk.Label(win, text="Hangi Yazıcıya Göndermek İstediğiniz Yazının Adını Yazınız")
label.pack()

entry = tk.Entry(win)
entry.pack()

def dosyaşeç():
    global path
    path = filedialog.askopenfilename(
        title="KodPixel-X-Printer",
        filetypes=[
            ("KodPixel-X-Printer-File", "*.kpxpf"),
            ("Jpg", "*.jpg"),
            ("Text", "*.txt"),
            ("Png", "*.png"),
            ("Webp", "*.webp"),
            ("Tif", "*.tif"),
            ("Pdf", "*.pdf")
        ]   
    )

buttondosyaşeç = tk.Button(win, text="DOSYA ŞEÇ", command=dosyaşeç)
buttondosyaşeç.pack()


eni = tk.Entry()
eni.pack()

labeleni = tk.Label(win, text="Eni Giriniz", font=("Arial", 10))
labeleni.pack()

yüksekliği = tk.Entry(win)
yüksekliği.pack()

yüksekliğiLabel = tk.Label(win, text="Yükseliğini  Giriniz", font=("Arial", 9))
yüksekliğiLabel.pack()

renk = tk.Entry(win)
renk.pack()

RenkLabel = tk.Label(win, text="Renk Modunu Şeçiniz 'Siyah-Beyaz', 'Renkli' ", font=("Arial", 7))
RenkLabel.pack()


def yazdır():
    messagebox.showinfo("KodPixel-X-Printer", "Yazdırma İşlemine Geçiliyor")
    entry3 = entry.get()
    printer = entry3

    Hdc = win32ui.CreateDC()
    Hdc.CreatePrinterDC(printer)
    Hdc.StartDoc("KodPixel-X-Printer")
    Hdc.StartPage()

    img = Image.open(path)

    renk2 = renk.get()
    if renk == "Siyah-Beyaz":
        img.convert('1')
    elif renk == "Renkli":
        img.convert('RGB')
    
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