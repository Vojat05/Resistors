from tkinter import Tk, StringVar, IntVar, Canvas, Label, ttk
from PIL import Image, ImageTk
from functions import resource_path

# Variables for buttons and answer data
x = IntVar()
y = IntVar()
z = IntVar()
n = IntVar()
t = IntVar()
h = IntVar()
getVal = StringVar()

# The main window and canvas (the main panel)
window = Tk()
canvas = Canvas(window, width=900, height=710)

# Variables for the answer and the toleration answer
p_hotovo = 0
toler = 0

# Images for the background and the background resistor shape.
imgbck = Image.open(resource_path('../Pics/bg.jpg'))
imgbckk = ImageTk.PhotoImage(image=imgbck)
image = Image.open(resource_path('../Pics/normal2.png'))
img1 = ImageTk.PhotoImage(image=image)

# labels for the column names
label = Label(canvas, text="1. Line", font=("Arial", 12, "bold"), fg='#10bbbb', bg="#3e3e42")
label1 = Label(canvas, text="2. Line", font=("Arial", 12, "bold"), fg='#10bbbb', bg="#3e3e42")
label2 = Label(canvas, text="3. Line", font=("Arial", 12, "bold"), fg='#10bbbb', bg="#3e3e42")
label3 = Label(canvas, text="Multiplicator", font=("Arial", 12, "bold"), fg='#10bbbb', bg="#3e3e42")
label4 = Label(canvas, text="Toleration", font=("Arial", 12, "bold"), fg='#10bbbb', bg="#3e3e42")
label7 = Label(canvas, text="Prefix", font=("Arial", 12, "bold"), fg='#10bbbb', bg="#3e3e42")
err = Label(canvas, text='', font=('Arial', 14), bg='#3e3e42', fg='#e80707')

labelr = Label(canvas, text=f"R: {p_hotovo} Ω", font=("Arial", 20, "bold"), bg='#3e3e42', fg='#10bbbb')
labelt = Label(canvas, text=f"T: {toler} %", font=("Arial", 20, "bold"), bg='#3e3e42', fg='#10bbbb')
entry = ttk.Entry(canvas, width=20, font=('Arial', 13, 'bold'), textvariable=getVal)