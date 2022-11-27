import os
from valuedata import *
from tkinter import END


def resource_path(relative):
    return os.path.join(os.environ.get("_MEIPASS2", os.path.abspath(".")), relative)


def find(err, x, y, z, n):
    value = getVal.get()
    if value.isdigit() is False:
        err.config(text='Value must be a whole numbers.')
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
            err.config(text='Resistor with this value doesn\'t exist')


def clear():
    entry.delete(0, END)
    err.config(text='')


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