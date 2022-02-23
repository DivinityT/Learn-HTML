import tkinter as tk
from tkinter import ttk
import src.inapp_text.inapp_text as text

# premiere fenetre
win = tk.Tk()
test1 = tk.IntVar()
test2 = tk.IntVar()

# Constantes
bg = '#DFDFDF'
font = "Rajdhani"

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
win.minsize(1080, 720)
win.iconbitmap("src/pic/logo.ico")
win.config(background=bg)

# texte
txt_1 = tk.Label(frame1, text=text.head_title, font=(font, 35), bg=bg)
txt_2 = tk.Label(frame1, text="avec notre superbe application !", font=(font, 20), bg=bg)
txt_3 = tk.Label(frame1, text=text.qst_1, font=(font, 15), bg=bg)

# bouton
btn = tk.Button(frame1, text="Vérification", font=(font, 15))

# cases à cochers
check = tk.Checkbutton(frame1, text="Vrai", font=(font, 25), variable=test1, bg=bg)
check2 = tk.Checkbutton(frame1, text="Faux", font=(font, 25), variable=test2, bg=bg)

# pack()
txt_1.pack()
txt_2.pack()
txt_3.pack(pady=(20, 0))
check.pack()
check2.pack()
btn.pack(pady=15, fill=tk.X)
frame1.pack(expand="yes", fill="both", pady=10, padx=10)
frame2.pack(expand="yes", fill="both", pady=10, padx=10)

# afficher
win.mainloop()
