import win32print
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


def file():
    global path
    path = filedialog.askopenfiles(
        title="KodPixel-X-Printer",
        filetypes=[
            ("KodPixel-X-Printer-File", "*.kpxpf"),
            ("Jpg", "*.jpg"),
            ("Text", "*.txt"),
            ("Png", "*.png"),
            ("Webp", "*.webp"),
            ("Tif", "*.tif")
        ]
    )

button = tk.Button(win, text="Dosya Aç", command=file)
button.pack()

label = tk.Label(win, text="Hangi Yazıcıya Göndermek İstediğiniz Yazının Adını Yazınız")
label.pack()

entry = tk.Entry(win)
entry.pack()

def entry2():
    global entry3
    entry3 = entry.get()
    global printer
    printer = entry3

def yazdır():
    hprint = win32print.OpenPrinter(printer)
    win32print.StartDocPrinter(hprint, 1, ("KodPixel-X-Printer", None, "RAW"))
    win32print.StartPagePrinter(hprint)
    win32print.WritePrinter(hprint, path)
    win32print.EndPagePrinter(hprint)
    win32print.EndDocPrinter(hprint)
    win32print.ClosePrinter(hprint)

buttonyazdır = tk.Button(win, text="Yazdır", command=yazdır)
buttonyazdır.pack()

win.mainloop()