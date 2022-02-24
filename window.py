import tkinter as tk
from tkinter import ttk
import src.inapp_text.inapp_text as text
import src.inapp_ressources.inapp_ressources as ressources

# premiere fenetre
win = tk.Tk()

# Textes variable
qst1_text = tk.StringVar()
qst1_text.set("Valide ton choix")

# Constantes
bg = '#DFDFDF'
font = "Rajdhani"

# Radio
RadioVar = tk.IntVar()
RadioVar.set(None)

# creer un frame
frame1 = tk.Frame(win, bg=bg, border=1, relief=tk.SUNKEN)
frame2 = tk.Frame(win, bg=bg, border=1, relief=tk.SUNKEN)

# canvas
canvas = tk.Canvas(frame2)

# scroll bar
yscrollbar = ttk.Scrollbar(frame1, orient="vertical", command=canvas.yview)
yscrollbar.pack(side="right", fill="y")
frame = tk.Frame(canvas)

# personalisation de la fenetre
win.title("Learn HTML !")
win.minsize(1080, 500)
win.iconbitmap("src/pic/logo.ico")
win.config(background=bg)

# texte
txt_1 = tk.Label(win, text=text.head_title, font=(font, 35), bg=bg)
txt_2 = tk.Label(win, text="avec notre superbe application !", font=(font, 20), bg=bg)
txt_3 = tk.Label(frame1, text=text.qst_1, font=(font, 15), bg=bg)
qst1 = tk.Label(frame1, textvariable=qst1_text, font=(font, 15), bg=bg)

# Cases à cocher
radio1 = tk.Radiobutton(frame1, text="Vrai", variable=RadioVar, value=1, bg=bg, font=(font, 15))
radio2 = tk.Radiobutton(frame1, text="Faux", variable=RadioVar, value=0, bg=bg, font=(font, 15))

# bouton
btn = tk.Button(frame1, text="Vérification", font=(font, 15), command=lambda :ressources.react_qst1(RadioVar.get(), qst1_text))

# pack()
txt_1.pack()
txt_2.pack()
txt_3.pack(pady=(20, 0))
radio1.pack()
radio2.pack()
btn.pack(pady=15, fill=tk.X)
qst1.pack()
frame1.pack(fill="x", pady=10, padx=10)

# afficher
win.mainloop()