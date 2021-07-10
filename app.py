import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=700, height=350)
canvas.grid(columnspan=3, rowspan=3)

logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

instructions = tk.Label(root, text="Selectionnez un fichier PDF pour extraire son texte !", font="Raleway")
instructions.grid(columnspan=3, column = 0, row=1)

def open_file():
    browse_text.set("Chargement...")
    file = askopenfile(parent=root, mode='rb', title="Choisissez un fichier", filetype=[("Fichier PDF", "*.pdf")])
    if file:
        print("Le fichier a été chargé avec succès !")

browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=3, width=20)
browse_text.set("Rechercher un PDF")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=400, height=150)
canvas.grid(columnspan=3)

root.mainloop()
