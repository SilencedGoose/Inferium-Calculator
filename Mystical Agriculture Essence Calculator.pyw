import tkinter as tk
from tkinter import Label, Spinbox, Entry, Button, END, ttk

'''
Made by @AnimatorOfSouls on GitHub.com
'''

### MODULES ###
def calculate():
    output.delete(0, END)
    insanium = int(input6.get())
    supremium = int(input5.get())
    imperium = int(input4.get())
    tertium = int(input3.get())
    prudentium = int(input2.get())
    inferium = int(input1.get())

    supremium += insanium*4
    imperium += supremium*4
    tertium += imperium*4
    prudentium += tertium*4
    inferium += prudentium*4

    items = inferium

    stacks = round((items-items%64)/64)
    items = items%64

    total = str(inferium)+" ("+str(stacks)+" stacks + "+str(items)+")"
    output.insert(END, total)


def reset():
    for input in inputs:
        input.delete(0, END)
        input.insert(END, 0)
    output.delete(0, END)



### MAIN ###
window = tk.Tk()

sep = ttk.Separator(window, orient="vertical")
sep.place(x=165, y=0, height=230)


#Input
lblEssences = Label(window, text="Essences", font=("Arial", 12, "bold"))
lblEssences.place(x=20, y=10)

lbl1 = Label(window, text="Inferium:")
lbl2 = Label(window, text="Prudentium:")
lbl3 = Label(window, text="Tertium:")
lbl4 = Label(window, text="Imperium:")
lbl5 = Label(window, text="Supremium:")
lbl6 = Label(window, text="Insanium:")
labels = [lbl1, lbl2, lbl3, lbl4, lbl5, lbl6]
for i in range(len(labels)):
    labels[i].place(x=20, y=40+30*i)

input1 = Spinbox(window, from_=0, to=500, width=4)
input2 = Spinbox(window, from_=0, to=500, width=4)
input3 = Spinbox(window, from_=0, to=500, width=4)
input4 = Spinbox(window, from_=0, to=500, width=4)
input5 = Spinbox(window, from_=0, to=500, width=4)
input6 = Spinbox(window, from_=0, to=500, width=4)
inputs = [input1, input2, input3, input4, input5, input6]
for i in range(len(inputs)):
    inputs[i].place(x=100, y=40+30*i)


#Output
lblEssences = Label(window, text="Output", font=("Arial", 12, "bold"))
lblEssences.place(x=250, y=10)

lblOut = Label(window, text="Inferium Cost")
lblOut.place(x=240, y=60)
output = Entry(justify="center")
output.place(x=220, y=80)


#Calculate and Reset button
btnCalculate = Button(window, text="Calculate", command=calculate)
btnCalculate.place(x=250, y=130)
btnCalculate = Button(window, text="   Reset    ", command=reset)
btnCalculate.place(x=250, y=160)


#Window
window.title("Essence Calculator")
window.geometry("400x230+800+400")
window.resizable(False, False)
window.mainloop()
