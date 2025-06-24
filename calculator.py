import tkinter as tk

window = tk.Tk()
window.title("calculator")
window.geometry("300x400")

display = tk.Entry(window, font=("Ariel", 20), borderwidth = "2", relief = "ridge", justify = "right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady = 10, sticky = "we")

def press(value):
    display.insert(tk.END, value)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0,tk.END)
        display.insert(0, result)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")    

def clear():
    display.delete(0, tk.END)        
    
def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0,current[:-1])

button = [
    ('c', 1, 0, clear), ('⌫', 1, 2, backspace), ('%', 1, 2, lambda: press("%")), ('/', 1, 3, lambda: press("/")),
    ('7', 2, 0, lambda: press("7")), ('8', 2, 1, lambda: press('8')), ('9', 2, 2, lambda: press('9')), ('*', 2, 3, lambda: press('*')),
    ('4', 3, 0, lambda: press('4')), ('5', 3, 1, lambda: press('5')), ('6', 3, 2, lambda: press('6')), ('-', 3, 3, lambda: press('-')),
    ('1', 4, 0, lambda: press('1')), ('2', 4, 1, lambda: press('2')), ('3', 4, 2, lambda: press('3')), ('+', 4, 3, lambda: press('+')),
    ('0', 5, 0, lambda: press('0')), ('.', 5, 1, lambda: press('.')), ('=', 5, 2, calculate)
]

for(text, row, col, cmd)in button:
    if text == '=':
        tk.Button(window, text = text, width = 10, height = 2, command = cmd) .grid(row = row, column = col, columnspan = 2, sticky="nsew", padx=2,pady=2 )
    else:
        tk.Button(window, text = text, width=5, height=2, command = cmd) .grid(row = row, column = col, padx=2, pady=2)

for i in range(6):
    window.grid_rowconfigure(i, weight = 1)

for i in range(4):
    window.grid_columnconfigure(i, weight=1)


window.mainloop()