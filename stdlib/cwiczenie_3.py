import tkinter

# def jakas_funkcja():
#     wartosc = entry.get()
#     label.configure(text=wartosc)
#
# root = tkinter.Tk()
# root.columnconfigure(1)
# entry = tkinter.Entry(master=root)
# entry.grid(row=0, column=0)
# label = tkinter.Label(master=root, text="napis")
# label.grid(row=0, column=1)
#
# button = tkinter.Button(master=root, text="Click me!", command=jakas_funkcja)
# button.grid(row=1, column=0)
# root.mainloop()

def oblicz_koszt():
    wartosc = float(entry1.get())*int(entry2.get())*int(entry3.get())/100

    label5.configure(text=wartosc)


root = tkinter.Tk()
root.columnconfigure(1)
entry1 = tkinter.Entry(master=root)
entry1.grid(row=0, column=0)
label1 = tkinter.Label(master=root, text="Cena paliwa zł/l")
label1.grid(row=0, column=1)

entry2 = tkinter.Entry(master=root)
entry2.grid(row=1, column=0)
label2 = tkinter.Label(master=root, text="Spalanie l/km")
label2.grid(row=1, column=1)

entry3 = tkinter.Entry(master=root)
entry3.grid(row=2, column=0)
label3 = tkinter.Label(master=root, text="Trasa km")
label3.grid(row=2, column=1)

label4 = tkinter.Label(master=root, text="Koszt przejazdu")
label4.grid(row=3, column=0)

label5 = tkinter.Label(master=root, text="")
label5.grid(row=4, column=1)

button = tkinter.Button(master=root, text="Oblicz", command = oblicz_koszt)
button.grid(row=4, column=0)







root.mainloop()

