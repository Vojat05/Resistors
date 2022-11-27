from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from functions import *


# Main GUI setup
window.geometry("1920x1080")
window.title("Resistor Calculator")
Label(window, image=imgbckk).place(x=0, y=0)
canvas.configure(bg='#3e3e42', highlightthickness=2, highlightbackground='#646464')
canvas.pack(side='left', expand=True)

# Basic resistor picture resize and apply
image = image.resize((480, 270), Image.ANTIALIAS)
canvas.create_image(450, 100, image=img1)

# Labeling the sections.
label.place(x=112, y=297)
label1.place(x=268, y=297)
label2.place(x=423, y=297)
label3.place(x=560, y=297)
label4.place(x=717, y=297)
label7.place(x=56, y=58)
err.place(x=310, y=677)

# Answer label.
labelr.place(x=350, y=160)
labelt.place(x=350, y=200)

pruh_1 = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Grey", "White"]
pruh_2 = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Grey", "White"]
pruh_3 = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Grey", "White"]
nasobek = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Gold", "Silver"]
tolerance = ["Brown", "Red", "Green", "Blue", "Purple", "Gray", "Gold", "Silver", "None"]
hodnoty = ["Ω", "kΩ", "MΩ"]

# Resistor search part.
canvas.create_rectangle(0, 620, 905, 625, fill='#292929')

entry.place(x=370, y=645)
Label(canvas, text='Find value', font=('Arial', 15, 'bold'), bg='#3e3e42', fg='#10bbbb').place(x=200, y=640)
Label(canvas, text='Ω', bg='#fff', font=('Arial', 9, 'bold')).place(x=535, y=647)
ttk.Button(canvas, text='Find', command=lambda: find(err, x, y, z, n)).place(x=615, y=645)

Button(canvas, text='❌', font=('Arial', 9), command=clear, bd=1).place(x=558, y=646)

# Drawing the wide hexagon border around the column names
label_polyoval(width=80, height=32, locx=143, locy=309)
label_polyoval(width=80, height=32, locx=298, locy=309)
label_polyoval(width=80, height=32, locx=453, locy=309)
label_polyoval(width=120, height=32, locx=610, locy=309)
label_polyoval(width=110, height=32, locx=758, locy=309)
label_polyoval(width=100, height=32, locx=81, locy=70)
label_polyoval(width=170, height=32, locx=253, locy=655)

# Calling the functions to draw the default color stripes for the resistor on startup
# First stripe
pruh1Draw(0)
# Second stripe
pruh2Draw(0)
# Third stripe
pruh3Draw(0)
# Multiplicator stripe
pruhnDraw(0)
# Toleration field stripe
pruhtDraw(0)

# Buttons.
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

for index in range(len(hodnoty)):
    radiobutton6 = Radiobutton(canvas, text=hodnoty[index], variable=h, indicatoron=0, width=5, value=index,
                               command=lambda: jedna(p_hotovo), bg="#c4c4c4")
    if index == 0:
        radiobutton6.place(x=60, y=100)
    elif index == 1:
        radiobutton6.place(x=60, y=125)
    else:
        radiobutton6.place(x=60, y=150)

# Color blocks before each radiobutton.
drawBlock(90, 340, 100, 360, 245, 340, 255, 360, 400, 340, 410, 360, 555, 340, 565, 360, 710, 340, 720, 360)

window.mainloop()
