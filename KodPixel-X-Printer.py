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


label = tk.Label(win, text="Hangi Yazıcıya Göndermek İstediğiniz Yazının Adını Yazınız")
label.pack()

entry = tk.Entry(win)
entry.pack()


def yazdır():
    path = filedialog.askopenfilename(
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
    
    messagebox.showinfo("KodPixel-X-Printer", "Yazdırma İşlemine Geçiliyor")
    entry3 = entry.get()
    printer = entry3
    hprint = win32print.OpenPrinter(printer)
    win32print.StartDocPrinter(hprint, 1, ("KodPixel-X-Printer", None, "RAW"))
    win32print.StartPagePrinter(hprint)
    with open(path, 'rb') as file:
        file_data = file.read()

    win32print.WritePrinter(hprint, file_data)
    win32print.EndPagePrinter(hprint)
    win32print.EndDocPrinter(hprint)
    win32print.ClosePrinter(hprint)

buttonyazdır = tk.Button(win, text="Yazdır", command=yazdır)
buttonyazdır.pack()

win.mainloop()