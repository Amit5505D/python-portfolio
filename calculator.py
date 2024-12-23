from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, header):
        header.title("Calculator")
        header.geometry('320x480+0+0')
        header.config(bg='grey')
        header.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        # Entry widget for display
        Entry(header, bg='#fff', font=('Arial bold', 22), textvariable=self.equation, justify='right').place(x=0, y=0, width=320, height=50)

        # Buttons
        Button(header, widt=11, height=4, relief='flat', text='(', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
        Button(header, width=11, height=4, relief='flat', text=')', bg='white', command=lambda: self.show(')')).place(x=80, y=50)
        Button(header, width=11, height=4, relief='flat', text='%', bg='white', command=lambda: self.show('%')).place(x=160, y=50)
        Button(header, width=11, height=4, relief='flat', text='C', bg='white', command=self.clear).place(x=240, y=50)

        Button(header, width=11, height=4, relief='flat', text='7', bg='white', command=lambda: self.show('7')).place(x=0, y=120)
        Button(header, width=11, height=4, relief='flat', text='8', bg='white', command=lambda: self.show('8')).place(x=80, y=120)
        Button(header, width=11, height=4, relief='flat', text='9', bg='white', command=lambda: self.show('9')).place(x=160, y=120)
        Button(header, width=11, height=4, relief='flat', text='/', bg='white', command=lambda: self.show('/')).place(x=240, y=120)

        Button(header, width=11, height=4, relief='flat', text='4', bg='white', command=lambda: self.show('4')).place(x=0, y=190)
        Button(header, width=11, height=4, relief='flat', text='5', bg='white', command=lambda: self.show('5')).place(x=80, y=190)
        Button(header, width=11, height=4, relief='flat', text='6', bg='white', command=lambda: self.show('6')).place(x=160, y=190)
        Button(header, width=11, height=4, relief='flat', text='*', bg='white', command=lambda: self.show('*')).place(x=240, y=190)

        Button(header, width=11, height=4, relief='flat', text='1', bg='white', command=lambda: self.show('1')).place(x=0, y=260)
        Button(header, width=11, height=4, relief='flat', text='2', bg='white', command=lambda: self.show('2')).place(x=80, y=260)
        Button(header, width=11, height=4, relief='flat', text='3', bg='white', command=lambda: self.show('3')).place(x=160, y=260)
        Button(header, width=11, height=4, relief='flat', text='-', bg='white', command=lambda: self.show('-')).place(x=240, y=260)

        Button(header, width=11, height=4, relief='flat', text='0', bg='white', command=lambda: self.show('0')).place(x=0, y=330)
        Button(header, width=11, height=4, relief='flat', text='.', bg='white', command=lambda: self.show('.')).place(x=80, y=330)
        Button(header, width=11, height=4, relief='flat', text='=', bg='white', command=self.solve).place(x=160, y=330)
        Button(header, width=11, height=4, relief='flat', text='+', bg='white', command=lambda: self.show('+')).place(x=240, y=330)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception:
            self.equation.set("Error")

# Main Program
root = Tk()
calculator = Calculator(root)
root.mainloop()

























