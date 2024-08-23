from tkinter import *

value = ""

def enter(num):
    global value
    value = value + str(num)
    equation.set(value)

def enterequal():
    try:
        global value
        total = str(eval(value))
        equation.set(total)
        value = ""
    except:
        equation.set(" error ")
        value = ""

def clear_entry():
    global value
    value = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.title("GUI Calculator")
    
    equation = StringVar()
    value_space = Entry(gui, textvariable=equation)
    value_space.grid(columnspan=7, ipadx=70, ipady=30)
    
    button1 = Button(gui, text=' 7 ', fg='black', bg='pink',
                    command=lambda: enter(7), height=5, width=10)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 8 ', fg='black', bg='pink',
                    command=lambda: enter(8), height=5, width=10)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 9 ', fg='black', bg='pink',
                    command=lambda: enter(9), height=5, width=10)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='pink',
                    command=lambda: enter(4), height=5, width=10)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black',bg='pink',
                    command=lambda: enter(5), height=5, width=10)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black',bg='pink',
                    command=lambda: enter(6), height=5, width=10)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 1 ', fg='black',bg='pink',
                    command=lambda: enter(1), height=5, width=10)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 2 ', fg='black',bg='pink',
                    command=lambda: enter(2), height=5, width=10)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 3 ', fg='black', bg='pink',
                    command=lambda: enter(3), height=5, width=10)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='pink',
                    command=lambda: enter(0), height=5, width=10)
    button0.grid(row=5, column=1)

    button_1 = Button(gui, text=' . ', fg='black', bg='pink',
                    command=lambda: enter('.'), height=5, width=10)
    button_1.grid(row=6, column=0)

    add = Button(gui, text=' Add', fg='black',bg='pink',
                command=lambda: enter("+"), height=5, width=10)
    add.grid(row=2, column=3)

    subt = Button(gui, text=' Subtract', fg='black',bg='pink',
                command=lambda: enter("-"), height=5, width=10)
    subt.grid(row=3, column=3)

    multiply = Button(gui, text=' Multiply', fg='black', bg='pink',
                    command=lambda: enter("*"), height=5, width=10)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' Divide', fg='black',bg='pink',
                    command=lambda: enter("/"), height=5, width=10)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' Answer', fg='black', bg='pink',
                   command=enterequal, height=5, width=10)
    equal.grid(row=6, column=2)

    pink2 = Button(gui, text=' ', fg='black',bg='pink',
                 height=5, width=10)
    pink2.grid(row=6, column=3)

    clear = Button(gui, text='Clear', fg='black',bg='pink',
                command=clear_entry, height=5, width=10)
    clear.grid(row=6, column=1)

    pink = Button(gui, text='', bg='pink',
                  height=5, width=10)
    pink.grid(row=5, column=0)

    pink_1 = Button(gui, text='', bg='pink',
                    height=5, width=10)
    pink_1.grid(row=5, column=2)

    gui.mainloop()
