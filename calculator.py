import tkinter as tk

color_background = "gray"
color_button = "black"
color_text = "white"
color_border = "white"

window = tk.Tk()
window.title("ماشین حساب من")
window.config(bg=color_background)

experssion = ""


def press(num):
    global experssion
    experssion += str(num)
    equation.set(experssion)


def equalpress():
    try:
        global experssion
        total = str(eval(experssion))
        equation.set(total)
        experssion = total

    except:
        equation.set("خطا")
        experssion = ""


def clear():
    global experssion
    experssion = ""
    equation.set("")


equation = tk.StringVar()
equation.set("")
experssion_field = tk.Entry(
    window, textvariable=equation, font=('Arial', 20), justify='right')
experssion_field.grid(columnspan=4, ipadx=10, ipady=20, padx=10, pady=10)

bbuttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2),
    ('^', 4, 3), ('C', 5, 0), ('=', 5, 1),
    ('v', 5, 2), ('-', 5, 3), ('+', 3, 3)
]

for (text, row, col) in bbuttons:
    if text == "=":
        btn = tk.Button(window, text=text, fg=color_text,
                        bg=color_button, command=equalpress, height=2, width=7)
    elif text == "C":
        btn = tk.Button(window, text=text, fg=color_text,
                        bg=color_button, command=clear, height=2, width=7)
    elif text == "v":
        btn = tk.Button(window, text=text, fg=color_text, bg=color_button, command=lambda:
                        press("**0.5"), height=2, width=7)
    elif text == "^":
        btn = tk.Button(window, text=text, fg=color_text, bg=color_button, command=lambda:
                        press("**"), height=2, width=7)
    else:
        btn = tk.Button(window, text=text, fg=color_text, bg=color_button,
                        command=lambda t=text: press(t), height=2, width=7)
    btn.grid(row=row, column=col, padx=5, pady=5)

window.mainloop()
