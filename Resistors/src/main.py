from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os


def resource_path(relative):
    return os.path.join(os.environ.get("_MEIPASS2", os.path.abspath(".")), relative)


def find(err, x, y, z, n):
    value = getVal.get()
    if value.isdigit() is False:
        err.config(text='Hodnota musí obsahovat pouze celá čísla')
    else:
        if int(value) < 10:
            err.config(text='')
            x.set(0)
            y.set(0)
            z.set(value[0])
            n.set(0)
            print(f"{value[0]} method 1")
            pruh1Draw(x.get())
            pruh2Draw(y.get())
            pruh3Draw(z.get())
            pruhnDraw(n.get())
        if 9 < int(value) < 100:
            err.config(text='')
            x.set(0)
            y.set(value[0])
            z.set(value[1])
            n.set(0)
            print(f"{value[0]} {value[1]} method 2")
            pruh1Draw(x.get())
            pruh2Draw(y.get())
            pruh3Draw(z.get())
            pruhnDraw(n.get())
        if 99 < int(value) < 1000:
            err.config(text='')
            x.set(value[0])
            y.set(value[1])
            z.set(value[2])
            n.set(0)
            print(f"{value[0]} {value[1]} {value[2]} method 3")
            pruh1Draw(x.get())
            pruh2Draw(y.get())
            pruh3Draw(z.get())
            pruhnDraw(n.get())
        if 10000000000 > int(value) > 999:
            err.config(text='')
            x.set(value[0])
            y.set(value[1])
            z.set(value[2])
            n.set(len(value)-3)
            print(f"{value} method 4")
            pruh1Draw(x.get())
            pruh2Draw(y.get())
            pruh3Draw(z.get())
            pruhnDraw(n.get())
        if int(value) >= 10000000000:
            err.config(text='Rezistor s touto hodnotou neexistuje')

# Hlavní GUI
window = Tk()
window.geometry("900x710")
window.title("Výpočet Rezistorů")
#window.resizable(False, False)
imgbck = Image.open(resource_path('../Pics/bg.jpg'))
imgbckk = ImageTk.PhotoImage(image=imgbck)
Label(window, image=imgbckk).place(x=0, y=0)
canvas = Canvas(window, width=900, height=710)
canvas.configure(bg='#3e3e42', highlightthickness=4, highlightbackground='#646464')
canvas.pack(side='left', expand=True)

# Obrázek rezistoru.
image = Image.open(resource_path('../Pics/normal2.png'))
image = image.resize((480, 270), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(image=image)
canvas.create_image(450, 100, image=img1)

# Označení sekcí výběru.
label = Label(canvas, text="1. Pruh", font=("Arial", 12, "bold"), fg='#10bbbb', bg="#3e3e42")
label.place(x=112, y=297)
label1 = Label(canvas, text="2. Pruh", font=("Arial", 12, "bold"), fg='#10bbbb', bg="#3e3e42")
label1.place(x=268, y=297)
label2 = Label(canvas, text="3. Pruh", font=("Arial", 12, "bold"), fg='#10bbbb', bg="#3e3e42")
label2.place(x=423, y=297)
label3 = Label(canvas, text="Násobek", font=("Arial", 12, "bold"), fg='#10bbbb', bg="#3e3e42")
label3.place(x=570, y=297)
label4 = Label(canvas, text="Tolerance", font=("Arial", 12, "bold"), fg='#10bbbb', bg="#3e3e42")
label4.place(x=717, y=297)
label7 = Label(canvas, text="Předpony", font=("Arial", 12, "bold"), fg='#10bbbb', bg="#3e3e42")
label7.place(x=42, y=58)
err = Label(canvas, text='', font=('Arial', 14), bg='#3e3e42', fg='#e80707')
err.place(x=290, y=677)

# Výsledkové pole
p_hotovo = 0
toler = 0
labelr = Label(canvas, text=f"R: {p_hotovo} Ω", font=("Arial", 20, "bold"), bg='#3e3e42', fg='#10bbbb')
labelr.place(x=350, y=160)
labelt = Label(canvas, text=f"T: {toler} %", font=("Arial", 20, "bold"), bg='#3e3e42', fg='#10bbbb')
labelt.place(x=350, y=200)

pruh_1 = ["Černá", "Hnědá", "Červená", "Oranžová", "Žlutá", "Zelená", "Modrá", "Fialová", "Šedá", "Bílá"]
pruh_2 = ["Černá", "Hnědá", "Červená", "Oranžová", "Žlutá", "Zelená", "Modrá", "Fialová", "Šedá", "Bílá"]
pruh_3 = ["Černá", "Hnědá", "Červená", "Oranžová", "Žlutá", "Zelená", "Modrá", "Fialová", "Šedá", "Bílá"]
nasobek = ["Černá", "Hnědá", "Červená", "Oranžová", "Žlutá", "Zelená", "Modrá", "Fialová", "Zlatá", "Stříbrná"]
tolerance = ["Hnědá", "Červená", "Zelená", "Modrá", "Fialová", "Šedá", "Zlatá", "Stříbrná", "Žádná"]
hodnoty = ["Ω", "kΩ", "MΩ"]
x = IntVar()
y = IntVar()
z = IntVar()
n = IntVar()
t = IntVar()
h = IntVar()
getVal = StringVar()

# Zadávací pole pro hledání rezistoru
canvas.create_rectangle(0, 620, 905, 625, fill='#292929')

entry = ttk.Entry(canvas, width=20, font=('Arial', 13, 'bold'), textvariable=getVal)
entry.place(x=370, y=645)
Label(canvas, text='Najít rezistor', font=('Arial', 15, 'bold'), bg='#3e3e42', fg='#10bbbb').place(x=190, y=640)
Label(canvas, text='Ω', bg='#fff', font=('Arial', 9, 'bold')).place(x=535, y=647)
ttk.Button(canvas, text='Najít', command=lambda: find(err, x, y, z, n)).place(x=615, y=645)


def clear():
    entry.delete(0, END)
    err.config(text='')

Button(canvas, text='❌', font=('Arial', 9), command=clear, bd=1).place(x=558, y=646)

# Segment funkcí.
def label_polyoval(width, height, locx, locy):
    points = [locx-width/2+height/4, locy-height/2,
              locx+width/2-height/4, locy-height/2,
              locx+width/2, locy-height/4,
              locx+width/2, locy+height/4,
              locx+width/2-height/4, locy+height/2,
              locx-width/2+height/4, locy+height/2,
              locx-width/2, locy+height/4,
              locx-width/2, locy-height/4,
              ]
    canvas.create_polygon(points, outline='#10bbbb', fill='#3e3e42')
label_polyoval(width=80, height=32, locx=143, locy=309)
label_polyoval(width=80, height=32, locx=298, locy=309)
label_polyoval(width=80, height=32, locx=453, locy=309)
label_polyoval(width=100, height=32, locx=606, locy=309)
label_polyoval(width=110, height=32, locx=758, locy=309)
label_polyoval(width=100, height=32, locx=81, locy=70)
label_polyoval(width=170, height=32, locx=253, locy=655)


def drawBlock(x1, y1, x2, y2, x12, y12, x21, y21, x121, y121, x212, y212, x11, y11, x22, y22, x111, y111, x222, y222):
    canvas.create_rectangle(x1, y1, x2, y2, fill='black')
    canvas.create_rectangle(x1, y1+25, x2, y2+25, fill='#7f3c05')
    canvas.create_rectangle(x1, y1+50, x2, y2+50, fill='#eb0000')
    canvas.create_rectangle(x1, y1+75, x2, y2+75, fill='#f48500')
    canvas.create_rectangle(x1, y1+100, x2, y2+100, fill='#f4da00')
    canvas.create_rectangle(x1, y1+125, x2, y2+125, fill='#37d509')
    canvas.create_rectangle(x1, y1+150, x2, y2+150, fill='#0953d5')
    canvas.create_rectangle(x1, y1+175, x2, y2+175, fill='#6c09d5')
    canvas.create_rectangle(x1, y1+200, x2, y2+200, fill='#8a8a8a')
    canvas.create_rectangle(x1, y1+225, x2, y2+225, fill='#fff')

    canvas.create_rectangle(x12, y12, x21, y21, fill='black')
    canvas.create_rectangle(x12, y12+25, x21, y21+25, fill='#7f3c05')
    canvas.create_rectangle(x12, y12+50, x21, y21+50, fill='#eb0000')
    canvas.create_rectangle(x12, y12+75, x21, y21+75, fill='#f48500')
    canvas.create_rectangle(x12, y12+100, x21, y21+100, fill='#f4da00')
    canvas.create_rectangle(x12, y12+125, x21, y21+125, fill='#37d509')
    canvas.create_rectangle(x12, y12+150, x21, y21+150, fill='#0953d5')
    canvas.create_rectangle(x12, y12+175, x21, y21+175, fill='#6c09d5')
    canvas.create_rectangle(x12, y12+200, x21, y21+200, fill='#8a8a8a')
    canvas.create_rectangle(x12, y12+225, x21, y21+225, fill='#fff')

    canvas.create_rectangle(x121, y121, x212, y212, fill='black')
    canvas.create_rectangle(x121, y121+25, x212, y212+25, fill='#7f3c05')
    canvas.create_rectangle(x121, y121+50, x212, y212+50, fill='#eb0000')
    canvas.create_rectangle(x121, y121+75, x212, y212+75, fill='#f48500')
    canvas.create_rectangle(x121, y121+100, x212, y212+100, fill='#f4da00')
    canvas.create_rectangle(x121, y121+125, x212, y212+125, fill='#37d509')
    canvas.create_rectangle(x121, y121+150, x212, y212+150, fill='#0953d5')
    canvas.create_rectangle(x121, y121+175, x212, y212+175, fill='#6c09d5')
    canvas.create_rectangle(x121, y121+200, x212, y212+200, fill='#8a8a8a')
    canvas.create_rectangle(x121, y121+225, x212, y212+225, fill='#fff')

    canvas.create_rectangle(x11, y11, x22, y22, fill='black')
    canvas.create_rectangle(x11, y11 + 25, x22, y22 + 25, fill='#7f3c05')
    canvas.create_rectangle(x11, y11 + 50, x22, y22 + 50, fill='#eb0000')
    canvas.create_rectangle(x11, y11 + 75, x22, y22 + 75, fill='#f48500')
    canvas.create_rectangle(x11, y11 + 100, x22, y22 + 100, fill='#f4da00')
    canvas.create_rectangle(x11, y11 + 125, x22, y22 + 125, fill='#37d509')
    canvas.create_rectangle(x11, y11 + 150, x22, y22 + 150, fill='#0953d5')
    canvas.create_rectangle(x11, y11 + 175, x22, y22 + 175, fill='#6c09d5')
    canvas.create_rectangle(x11, y11 + 210, x22, y22 + 210, fill='#FFD700')
    canvas.create_rectangle(x11, y11 + 235, x22, y22 + 235, fill='#C0C0C0')

    canvas.create_rectangle(x111, y111, x222, y222, fill='#7f3c05')
    canvas.create_rectangle(x111, y111 + 25, x222, y222 + 25, fill='#eb0000')
    canvas.create_rectangle(x111, y111 + 60, x222, y222 + 60, fill='#37d509')
    canvas.create_rectangle(x111, y111 + 85, x222, y222 + 85, fill='#0953d5')
    canvas.create_rectangle(x111, y111 + 110, x222, y222 + 110, fill='#6c09d5')
    canvas.create_rectangle(x111, y111 + 135, x222, y222 + 135, fill='#8a8a8a')
    canvas.create_rectangle(x111, y111 + 170, x222, y222 + 170, fill='#FFD700')
    canvas.create_rectangle(x111, y111 + 195, x222, y222 + 195, fill='#C0C0C0')
    canvas.create_rectangle(x111, y111 + 240, x222, y222 + 240, fill='#fff')


def pruh_x():
    global pruhy_1
    pruhy_1 = int(x.get() * 100)


def pruh_y():
    global pruhy_2
    pruhy_2 = int(y.get() * 10)


def pruh_z():
    global pruhy_3
    pruhy_3 = int(z.get())


def nasobek_f():
    global nasob
    if n.get() == 0:
        nasob = 1
    elif 1 <= n.get() <= 7:
        nasob = 10 ** n.get()
    elif n.get() > 7:
        nasob = 10000000 / 10 ** n.get()


def tolerance_f():
    global toler
    if 0 <= t.get() <= 1:
        toler = t.get() + 1
    elif t.get() == 2:
        toler = 0.5
    elif t.get() == 3:
        toler = 0.25
    elif t.get() == 4:
        toler = 0.1
    elif t.get() == 5:
        toler = 0.05
    elif t.get() == 6:
        toler = 5
    elif t.get() == 7:
        toler = 10
    else:
        toler = 20


def jedna(p_hotovo):
    if h.get() == 0:
        labelr.config(text=f"R: {round(p_hotovo, 6)} Ω")
        labelr.update()
    elif h.get() == 1:
        p_hotovo /= 1000
        labelr.config(text=f"R: {round(p_hotovo, 6)} kΩ")
        labelr.update()
    else:
        p_hotovo /= 1000000
        labelr.config(text=f"R: {round(p_hotovo, 6)} MΩ")
        labelr.update()


def click():
    global p_hotovo
    pruh_x()
    pruh_y()
    pruh_z()
    tolerance_f()
    nasobek_f()
    p_hotovo = (pruhy_1 + pruhy_2 + pruhy_3) * nasob
    labelr.config(text=f"R: {p_hotovo} Ω")
    labelr.update()
    labelt.config(text=f"T: {toler} %")
    labelt.update()
    jedna(p_hotovo)


def pruh1Draw(x):
    global ima
    global img2
    if 1 == x:
        ima = Image.open(resource_path('../Pics/hneda.png'))

    elif 2 == x:
        ima = Image.open(resource_path('../Pics/cervena.png'))

    elif 3 == x:
        ima = Image.open(resource_path('../Pics/oranzova.png'))

    elif 4 == x:
        ima = Image.open(resource_path('../Pics/zluta.png'))

    elif 5 == x:
        ima = Image.open(resource_path('../Pics/zelena.png'))

    elif 6 == x:
        ima = Image.open(resource_path('../Pics/modra.png'))

    elif 7 == x:
        ima = Image.open(resource_path('../Pics/fialova.png'))

    elif 8 == x:
        ima = Image.open(resource_path('../Pics/seda.png'))

    elif 9 == x:
        ima = Image.open(resource_path('../Pics/bila.png'))

    else:
        ima = Image.open(resource_path('../Pics/cerna.png'))

    ima = ima.resize((480, 270), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(image=ima)
    canvas.create_image(390, 100, image=img2)
    click()
pruh1Draw(0)


def pruh2Draw(y):
    global imay
    global img2y
    if 1 == y:
        imay = Image.open(resource_path('../Pics/hneda.png'))

    elif 2 == y:
        imay = Image.open(resource_path('../Pics/cervena.png'))

    elif 3 == y:
        imay = Image.open(resource_path('../Pics/oranzova.png'))

    elif 4 == y:
        imay = Image.open(resource_path('../Pics/zluta.png'))

    elif 5 == y:
        imay = Image.open(resource_path('../Pics/zelena.png'))

    elif 6 == y:
        imay = Image.open(resource_path('../Pics/modra.png'))

    elif 7 == y:
        imay = Image.open(resource_path('../Pics/fialova.png'))

    elif 8 == y:
        imay = Image.open(resource_path('../Pics/seda.png'))

    elif 9 == y:
        imay = Image.open(resource_path('../Pics/bila.png'))

    else:
        imay = Image.open(resource_path('../Pics/cerna.png'))

    imay = imay.resize((480, 270), Image.ANTIALIAS)
    img2y = ImageTk.PhotoImage(image=imay)
    canvas.create_image(420, 100, image=img2y)
    click()
pruh2Draw(0)


def pruh3Draw(z):
    global imaz
    global img2z
    if 1 == z:
        imaz = Image.open(resource_path('../Pics/hneda.png'))

    elif 2 == z:
        imaz = Image.open(resource_path('../Pics/cervena.png'))

    elif 3 == z:
        imaz = Image.open(resource_path('../Pics/oranzova.png'))

    elif 4 == z:
        imaz = Image.open(resource_path('../Pics/zluta.png'))

    elif 5 == z:
        imaz = Image.open(resource_path('../Pics/zelena.png'))

    elif 6 == z:
        imaz = Image.open(resource_path('../Pics/modra.png'))

    elif 7 == z:
        imaz = Image.open(resource_path('../Pics/fialova.png'))

    elif 8 == z:
        imaz = Image.open(resource_path('../Pics/seda.png'))

    elif 9 == z:
        imaz = Image.open(resource_path('../Pics/bila.png'))

    else:
        imaz = Image.open(resource_path('../Pics/cerna.png'))

    imaz = imaz.resize((480, 270), Image.ANTIALIAS)
    img2z = ImageTk.PhotoImage(image=imaz)
    canvas.create_image(450, 100, image=img2z)
    click()
pruh3Draw(0)


def pruhnDraw(n):
    global iman
    global img2n
    if 1 == n:
        iman = Image.open(resource_path('../Pics/hneda.png'))

    elif 2 == n:
        iman = Image.open(resource_path('../Pics/cervena.png'))

    elif 3 == n:
        iman = Image.open(resource_path('../Pics/oranzova.png'))

    elif 4 == n:
        iman = Image.open(resource_path('../Pics/zluta.png'))

    elif 5 == n:
        iman = Image.open(resource_path('../Pics/zelena.png'))

    elif 6 == n:
        iman = Image.open(resource_path('../Pics/modra.png'))

    elif 7 == n:
        iman = Image.open(resource_path('../Pics/fialova.png'))

    elif 8 == n:
        iman = Image.open(resource_path('../Pics/zlata.png'))

    elif 9 == n:
        iman = Image.open(resource_path('../Pics/stribrna.png'))

    else:
        iman = Image.open(resource_path('../Pics/cerna.png'))

    iman = iman.resize((480, 270), Image.ANTIALIAS)
    img2n = ImageTk.PhotoImage(image=iman)
    canvas.create_image(500, 100, image=img2n)
    click()
pruhnDraw(0)


def pruhtDraw(t):
    global imat
    global img2t
    if 1 == t:
        imat = Image.open(resource_path('../Pics/cervena.png'))

    elif 2 == t:
        imat = Image.open(resource_path('../Pics/zelena.png'))

    elif 3 == t:
        imat = Image.open(resource_path('../Pics/modra.png'))

    elif 4 == t:
        imat = Image.open(resource_path('../Pics/fialova.png'))

    elif 5 == t:
        imat = Image.open(resource_path('../Pics/seda.png'))

    elif 6 == t:
        imat = Image.open(resource_path('../Pics/zlata.png'))

    elif 7 == t:
        imat = Image.open(resource_path('../Pics/stribrna.png'))

    elif 8 == t:
        imat = Image.open(resource_path('../Pics/default.png'))

    else:
        imat = Image.open(resource_path('../Pics/hneda.png'))

    imat = imat.resize((480, 270), Image.ANTIALIAS)
    img2t = ImageTk.PhotoImage(image=imat)
    canvas.create_image(530, 100, image=img2t)
    click()
pruhtDraw(0)

# Výběrová tlačítka pro 1. pruh.
for index in range(len(pruh_1)):
    radiobutton1 = Radiobutton(canvas, text=pruh_1[index], variable=x, value=index, indicatoron=0, width=10,
                               bg="#c4c4c4", command=lambda: pruh1Draw(x.get()))
    if index == 0:
        radiobutton1.place(x=105, y=340)
    elif index == 1:
        radiobutton1.place(x=105, y=365)
    elif index == 2:
        radiobutton1.place(x=105, y=390)
    elif index == 3:
        radiobutton1.place(x=105, y=415)
    elif index == 4:
        radiobutton1.place(x=105, y=440)
    elif index == 5:
        radiobutton1.place(x=105, y=465)
    elif index == 6:
        radiobutton1.place(x=105, y=490)
    elif index == 7:
        radiobutton1.place(x=105, y=515)
    elif index == 8:
        radiobutton1.place(x=105, y=540)
    else:
        radiobutton1.place(x=105, y=565)

# Výběrová tlačítka pro 2. pruh.
for index in range(len(pruh_2)):
    radiobutton2 = Radiobutton(canvas, text=pruh_2[index], variable=y, value=index, indicatoron=0, width=10,
                               bg="#c4c4c4", command=lambda: pruh2Draw(y.get()))
    if index == 0:
        radiobutton2.place(x=260, y=340)
    elif index == 1:
        radiobutton2.place(x=260, y=365)
    elif index == 2:
        radiobutton2.place(x=260, y=390)
    elif index == 3:
        radiobutton2.place(x=260, y=415)
    elif index == 4:
        radiobutton2.place(x=260, y=440)
    elif index == 5:
        radiobutton2.place(x=260, y=465)
    elif index == 6:
        radiobutton2.place(x=260, y=490)
    elif index == 7:
        radiobutton2.place(x=260, y=515)
    elif index == 8:
        radiobutton2.place(x=260, y=540)
    else:
        radiobutton2.place(x=260, y=565)

# Výběrová tlačítka pro 3. pruh.
for index in range(len(pruh_3)):
    radiobutton3 = Radiobutton(canvas, text=pruh_3[index], variable=z, value=index, indicatoron=0, width=10,
                               bg="#c4c4c4", command=lambda: pruh3Draw(z.get()))
    if index == 0:
        radiobutton3.place(x=415, y=340)
    elif index == 1:
        radiobutton3.place(x=415, y=365)
    elif index == 2:
        radiobutton3.place(x=415, y=390)
    elif index == 3:
        radiobutton3.place(x=415, y=415)
    elif index == 4:
        radiobutton3.place(x=415, y=440)
    elif index == 5:
        radiobutton3.place(x=415, y=465)
    elif index == 6:
        radiobutton3.place(x=415, y=490)
    elif index == 7:
        radiobutton3.place(x=415, y=515)
    elif index == 8:
        radiobutton3.place(x=415, y=540)
    else:
        radiobutton3.place(x=415, y=565)

# Výběrová tlačítka pro násobek.
for index in range(len(nasobek)):
    radiobutton4 = Radiobutton(canvas, text=nasobek[index], variable=n, indicatoron=0, width=10, value=index,
                               bg="#c4c4c4", command=lambda: pruhnDraw(n.get()))
    if index == 0:
        radiobutton4.place(x=570, y=340)
    elif index == 1:
        radiobutton4.place(x=570, y=365)
    elif index == 2:
        radiobutton4.place(x=570, y=390)
    elif index == 3:
        radiobutton4.place(x=570, y=415)
    elif index == 4:
        radiobutton4.place(x=570, y=440)
    elif index == 5:
        radiobutton4.place(x=570, y=465)
    elif index == 6:
        radiobutton4.place(x=570, y=490)
    elif index == 7:
        radiobutton4.place(x=570, y=515)
    elif index == 8:
        radiobutton4.place(x=570, y=550)
    else:
        radiobutton4.place(x=570, y=575)

# Výběrová tlačítka pro toleranci.
for index in range(len(tolerance)):
    radiobutton5 = Radiobutton(canvas, text=tolerance[index], variable=t, indicatoron=0, width=10, value=index,
                               bg="#c4c4c4", command=lambda: pruhtDraw(t.get()))
    if index == 0:
        radiobutton5.place(x=725, y=340)
    elif index == 1:
        radiobutton5.place(x=725, y=365)
    elif index == 2:
        radiobutton5.place(x=725, y=400)
    elif index == 3:
        radiobutton5.place(x=725, y=425)
    elif index == 4:
        radiobutton5.place(x=725, y=450)
    elif index == 5:
        radiobutton5.place(x=725, y=475)
    elif index == 6:
        radiobutton5.place(x=725, y=510)
    elif index == 7:
        radiobutton5.place(x=725, y=535)
    else:
        radiobutton5.place(x=725, y=580)

# Výběrová tlačítka pro hodnoty.
for index in range(len(hodnoty)):
    radiobutton6 = Radiobutton(canvas, text=hodnoty[index], variable=h, indicatoron=0, width=5, value=index,
                               command=lambda: jedna(p_hotovo), bg="#c4c4c4")
    if index == 0:
        radiobutton6.place(x=60, y=100)
    elif index == 1:
        radiobutton6.place(x=60, y=125)
    else:
        radiobutton6.place(x=60, y=150)

# Kreslení barevných kostiček
drawBlock(90, 340, 100, 360, 245, 340, 255, 360, 400, 340, 410, 360, 555, 340, 565, 360, 710, 340, 720, 360)

window.mainloop()
