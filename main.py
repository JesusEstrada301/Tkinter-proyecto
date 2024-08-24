import tkinter as tk
import math

# Funciones de la calculadora
def click_button(item):
    current = input_text.get()
    input_text.set(current + str(item))

def clear_input():
    input_text.set("")

def calculate():
    try:
        result = str(eval(input_text.get()))
        add_to_history(input_text.get() + " = " + result)
        input_text.set(result)
    except:
        input_text.set("Error")

def sqrt():
    try:
        result = str(math.sqrt(float(input_text.get())))
        add_to_history("sqrt(" + input_text.get() + ") = " + result)
        input_text.set(result)
    except:
        input_text.set("Error")

def square():
    try:
        result = str(float(input_text.get()) ** 2)
        add_to_history(input_text.get() + "^2 = " + result)
        input_text.set(result)
    except:
        input_text.set("Error")

def power():
    try:
        base, exp = input_text.get().split('^')
        result = str(math.pow(float(base), float(exp)))
        add_to_history(input_text.get() + " = " + result)
        input_text.set(result)
    except:
        input_text.set("Error")

def sin():
    try:
        result = str(math.sin(math.radians(float(input_text.get()))))
        add_to_history("sin(" + input_text.get() + ") = " + result)
        input_text.set(result)
    except:
        input_text.set("Error")

def cos():
    try:
        result = str(math.cos(math.radians(float(input_text.get()))))
        add_to_history("cos(" + input_text.get() + ") = " + result)
        input_text.set(result)
    except:
        input_text.set("Error")

def tan():
    try:
        result = str(math.tan(math.radians(float(input_text.get()))))
        add_to_history("tan(" + input_text.get() + ") = " + result)
        input_text.set(result)
    except:
        input_text.set("Error")

def log():
    try:
        result = str(math.log10(float(input_text.get())))
        add_to_history("log(" + input_text.get() + ") = " + result)
        input_text.set(result)
    except:
        input_text.set("Error")

def ln():
    try:
        result = str(math.log(float(input_text.get())))
        add_to_history("ln(" + input_text.get() + ") = " + result)
        input_text.set(result)
    except:
        input_text.set("Error")

def exp():
    try:
        result = str(math.exp(float(input_text.get())))
        add_to_history("exp(" + input_text.get() + ") = " + result)
        input_text.set(result)
    except:
        input_text.set("Error")

def factorial():
    try:
        result = str(math.factorial(int(input_text.get())))
        add_to_history(input_text.get() + "! = " + result)
        input_text.set(result)
    except:
        input_text.set("Error")

def add_to_history(operation):
    history.insert(tk.END, operation)

# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora Científica")
window.configure(bg='#282C34')
window.geometry("480x720")

input_text = tk.StringVar()

# Crear el cuadro de historial y entrada combinados
top_frame = tk.Frame(window, bd=10, relief='raised', bg='#1E2127')
top_frame.pack(pady=20)

# Historial de operaciones
history = tk.Listbox(top_frame, height=4, bd=0, font=('Arial', 18), bg="#3B3F45", fg="white", justify='right', highlightthickness=0, selectbackground="#5A5E67", activestyle="none")
history.grid(row=0, column=0, columnspan=5, sticky="nsew")

# Campo de entrada
input_field = tk.Entry(top_frame, textvariable=input_text, font=('Arial', 18), bd=0, bg="#3B3F45", fg="white", insertbackground="white", justify='right', highlightthickness=0)
input_field.grid(row=1, column=0, columnspan=5, sticky="nsew")

# Crear los botones
buttons_frame = tk.Frame(window, bd=10, relief='raised', bg='#1E2127')
buttons_frame.pack()

# Configuración de botones
button_style = {
    "font": ('Arial', 18),
    "bd": 0,
    "bg": "#4A4F57",
    "fg": "white",
    "activebackground": "#686D75",
    "activeforeground": "white",
    "relief": "flat",
    "width": 5,
    "height": 2
}

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('x^2', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('sin', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('cos', 4, 4),
    ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('log', 5, 3), ('tan', 5, 4),
    ('ln', 6, 0), ('exp', 6, 1), ('^', 6, 2), ('!', 6, 3), ('π', 6, 4),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(buttons_frame, text=text, command=calculate, **button_style)
    elif text == 'C':
        btn = tk.Button(buttons_frame, text=text, command=clear_input, **button_style)
    elif text == 'sqrt':
        btn = tk.Button(buttons_frame, text=text, command=sqrt, **button_style)
    elif text == 'x^2':
        btn = tk.Button(buttons_frame, text=text, command=square, **button_style)
    elif text == '^':
        btn = tk.Button(buttons_frame, text=text, command=power, **button_style)
    elif text == 'sin':
        btn = tk.Button(buttons_frame, text=text, command=sin, **button_style)
    elif text == 'cos':
        btn = tk.Button(buttons_frame, text=text, command=cos, **button_style)
    elif text == 'tan':
        btn = tk.Button(buttons_frame, text=text, command=tan, **button_style)
    elif text == 'log':
        btn = tk.Button(buttons_frame, text=text, command=log, **button_style)
    elif text == 'ln':
        btn = tk.Button(buttons_frame, text=text, command=ln, **button_style)
    elif text == 'exp':
        btn = tk.Button(buttons_frame, text=text, command=exp, **button_style)
    elif text == '!':
        btn = tk.Button(buttons_frame, text=text, command=factorial, **button_style)
    elif text == 'π':
        btn = tk.Button(buttons_frame, text=text, command=lambda: click_button(math.pi), **button_style)
    else:
        btn = tk.Button(buttons_frame, text=text, command=lambda t=text: click_button(t), **button_style)
    btn.grid(row=row, column=col, padx=5, pady=5)

# Hacer que el tamaño de los widgets cambie con la ventana
for i in range(5):
    buttons_frame.grid_columnconfigure(i, weight=1)
    top_frame.grid_columnconfigure(i, weight=1)

# Ejecutar la aplicación
window.mainloop()