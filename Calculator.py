from tkinter import Entry, Button, StringVar, Tk
from tkinter import ttk
import math 


class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('450x420+0+0')
        master.config(bg = 'gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ' '
        Entry(width=22, bg = '#262625', font = ('Anek Devanagari', 28),fg ='white', textvariable = self.equation).place(x=0, y=0)

        Button(width = 11, height = 4, text = '(', relief = 'groove', bg = '#9acbfc', command = lambda:self.show('(')).place(x=0, y=50)
        Button(width = 11, height = 4, text = ')', relief = 'groove', bg = '#9acbfc', command = lambda:self.show(')')).place(x=90, y=50)
        Button(width = 11, height = 4, text = '%', relief = 'groove', bg = '#9acbfc', command = lambda:self.show('%')).place(x=180, y=50)
        Button(width = 11, height = 4, text = '1', relief = 'groove', bg = '#a3d0d6', command = lambda:self.show('1')).place(x=0, y=125)
        Button(width = 11, height = 4, text = '2', relief = 'groove', bg = '#a3d0d6', command = lambda:self.show('2')).place(x=90, y=125)
        Button(width = 11, height = 4, text = '3', relief = 'groove', bg = '#a3d0d6', command = lambda:self.show('3')).place(x=180, y=125)
        Button(width = 11, height = 4, text = '4', relief = 'groove', bg = '#a3d0d6', command = lambda:self.show('4')).place(x=0, y=200)
        Button(width = 11, height = 4, text = '5', relief = 'groove', bg = '#a3d0d6', command = lambda:self.show('5')).place(x=90, y=200)
        Button(width = 11, height = 4, text = '6', relief = 'groove', bg = '#a3d0d6', command = lambda:self.show('6')).place(x=180, y=200)
        Button(width = 11, height = 4, text = '7', relief = 'groove', bg = '#a3d0d6', command = lambda:self.show('7')).place(x=0, y=275)
        Button(width = 11, height = 4, text = '8', relief = 'groove', bg = '#a3d0d6', command = lambda:self.show('8')).place(x=180, y=275)
        Button(width = 11, height = 4, text = '9', relief = 'groove', bg = '#a3d0d6', command = lambda:self.show('9')).place(x=90, y=275)
        Button(width = 11, height = 4, text = '0', relief = 'groove', bg = '#a3d0d6', command = lambda:self.show('0')).place(x=90, y=350)
        Button(width = 11, height = 4, text = '.', relief = 'groove', bg = '#9acbfc', command = lambda:self.show('.')).place(x=180, y=350)
        Button(width = 11, height = 4, text = '+', relief = 'groove', bg = '#9acbfc', command = lambda:self.show(' + ')).place(x=270, y=275)
        Button(width = 11, height = 4, text = '-', relief = 'groove', bg = '#9acbfc', command = lambda:self.show(' - ')).place(x=270, y=200)
        Button(width = 11, height = 4, text = '/', relief = 'groove', bg = '#9acbfc', command = lambda:self.show(' / ')).place(x=270, y=50)
        Button(width = 11, height = 4, text = 'x', relief = 'groove', bg = '#9acbfc', command = lambda:self.show(' * ')).place(x=270, y=125)

        Button(width = 11, height = 4, text = 'tan()', relief = 'groove', bg = '#9acbfc', command = self.tan).place(x=360, y=50)
        Button(width = 11, height = 4, text = 'sin()', relief = 'groove', bg = '#9acbfc', command = self.sin).place(x=360, y=125)
        Button(width = 11, height = 4, text = 'cos()', relief = 'groove', bg = '#9acbfc', command = self.cos ).place(x=360, y=200)
        Button(width = 11, height = 4, text = '^', relief = 'groove', bg = '#9acbfc', command = lambda:self.show(' ^ ')).place(x=360, y=275)

        Button(width = 11, height = 4, text = '=', relief = 'groove', bg = '#f59393', command = self.solve).place(x=270, y=350)
        Button(width = 11, height = 4, text = 'C', relief = 'groove',bg ='#fabd7f', command = self.clear).place(x=0, y=350)

    def tan(self):
        a =0
        if self.entry_value != ' ':
            a = int(self.entry_value)
        result = math.tan(a)
        self.equation.set(result)

    def sin(self):
        a =0
        if self.entry_value != ' ':
            a = int(self.entry_value)
        result = math.sin(a)
        self.equation.set(result)

    def cos(self):
        a =0
        if self.entry_value != ' ':
            a = int(self.entry_value)
        result = math.cos(a)
        self.equation.set(result)
    
    def power(self):
        a = self.entry_value.split()
        result = int(a[0]) ** int( a[2])
        self.equation.set(result)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)
    
    def clear(self):
        self.entry_value = ' '
        self.equation.set(self.entry_value)

    def solve(self):
        
        if self.entry_value.find('^') > -1:
            self.power()
        else:
            result = eval(self.entry_value)
            self.equation.set(result)
    




root = Tk()
calculator = Calculator(root)
root.mainloop()
