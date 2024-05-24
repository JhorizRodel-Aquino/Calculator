from math import sin, cos, tan, pi, e, asin, acos, atan, log
from tkinter import *

window = Tk()
window.title("Calculator")


# Entry
display = Entry(window, width=50)
display.grid(row=0, columnspan=4, pady=10)

equals = Label(window, text="=")
equals.place(x=150, y=30)

display2 = Entry(window, width=50, justify="right")
display2.grid(row=1, columnspan=4, pady=10)


# Functions
def click(char):
    display.insert(END, str(char))


def equal():
    result_str = display.get().replace("π", "pi").replace("^", "**")
    display2.delete(0, END)

    try:
        result = eval(result_str)
    except:
        if result_str == "":
            result = ""
        else:
            result = "Syntax Error"

    display2.insert(0, result)


def delete():
    display.delete(len(display.get()) - 1)


def clear():
    display.delete(0, END)
    display2.delete(0, END)


# Buttons
wid = 5
padx = 20
pady = 10

btn_1 = Button(window, text="1", padx=padx, pady=pady, width=wid, command=lambda: click(1))
btn_2 = Button(window, text="2", padx=padx, pady=pady, width=wid, command=lambda: click(2))
btn_3 = Button(window, text="3", padx=padx, pady=pady, width=wid, command=lambda: click(3))
btn_4 = Button(window, text="4", padx=padx, pady=pady, width=wid, command=lambda: click(4))
btn_5 = Button(window, text="5", padx=padx, pady=pady, width=wid, command=lambda: click(5))
btn_6 = Button(window, text="6", padx=padx, pady=pady, width=wid, command=lambda: click(6))
btn_7 = Button(window, text="7", padx=padx, pady=pady, width=wid, command=lambda: click(7))
btn_8 = Button(window, text="8", padx=padx, pady=pady, width=wid, command=lambda: click(8))
btn_9 = Button(window, text="9", padx=padx, pady=pady, width=wid, command=lambda: click(9))
btn_0 = Button(window, text="0", padx=padx, pady=pady, width=wid, command=lambda: click(0))
btn_e = Button(window, text="e", padx=padx, pady=pady, width=wid, command=lambda: click("e"))
btn_pi = Button(window, text="π", padx=padx, pady=pady, width=wid, command=lambda: click("π"))
btn_add = Button(window, text="+", padx=padx, pady=pady, width=wid, command=lambda: click("+"))
btn_sub = Button(window, text="-", padx=padx, pady=pady, width=wid, command=lambda: click("-"))
btn_mul = Button(window, text="*", padx=padx, pady=pady, width=wid, command=lambda: click("*"))
btn_div = Button(window, text="/", padx=padx, pady=pady, width=wid, command=lambda: click("/"))
btn_pow = Button(window, text="^", padx=padx, pady=pady, width=wid, command=lambda: click("^"))
btn_dot = Button(window, text=".", padx=padx, pady=pady, width=wid, command=lambda: click("."))
btn_comma = Button(window, text=",", padx=padx, pady=pady, width=wid, command=lambda: click(","))
btn_leftP = Button(window, text="(", padx=padx, pady=pady, width=wid, command=lambda: click("("))
btn_rightP = Button(window, text=")", padx=padx, pady=pady, width=wid, command=lambda: click(")"))
btn_log = Button(window, text="log", padx=padx, pady=pady, width=wid, command=lambda: click("log("))
btn_sin = Button(window, text="sin", padx=padx, pady=pady, width=wid, command=lambda: click("sin("))
btn_cos = Button(window, text="cos", padx=padx, pady=pady, width=wid, command=lambda: click("cos("))
btn_tan = Button(window, text="tan", padx=padx, pady=pady, width=wid, command=lambda: click("tan("))
btn_asin = Button(window, text="arcsin", padx=padx, pady=pady, width=wid, command=lambda: click("asin("))
btn_acos = Button(window, text="arccos", padx=padx, pady=pady, width=wid, command=lambda: click("acos("))
btn_atan = Button(window, text="arctan", padx=padx, pady=pady, width=wid, command=lambda: click("atan("))


btn_equal = Button(window, text="=", padx=padx, pady=pady, width=wid, height=4, bg="orange", command=equal)
btn_del = Button(window, text="del", padx=padx, pady=pady, width=wid, command=delete)
btn_clear = Button(window, text="clear", padx=padx, pady=pady, width=wid, command=clear)


# Placing Buttons
buttons = [[btn_leftP, btn_rightP, btn_del, btn_clear], [btn_1, btn_2, btn_3, btn_add],
           [btn_4, btn_5, btn_6, btn_sub], [btn_7, btn_8, btn_9, btn_mul],
           [btn_e, btn_0, btn_pi, btn_div], [btn_dot, btn_comma, btn_log, btn_pow],
           [btn_sin, btn_cos, btn_tan, btn_equal], [btn_asin, btn_acos, btn_atan]]

row = 2
for grp in buttons:
    col = 0
    for btn in grp:
        if btn == btn_equal:
            btn.grid(row=row, column=col, rowspan=2)
        else:
            btn.grid(row=row, column=col)
        col += 1
    row += 1


"-----------------------------------------------------------------------------------------------------------------"

# Additional Feature

i = 0


def dark_mode():
    global i
    i += 1

    if i % 2 != 0:
        bg = "black"
        fg = "white"
    else:
        bg = "white"
        fg = "black"

    window.configure(bg=bg)
    display.configure(bg=bg, fg=fg)
    display2.configure(bg=bg, fg=fg)
    equals.configure(bg=bg, fg=fg)
    for group in buttons:
        for button in group:
            if button != btn_equal:
                button.configure(bg=bg, fg=fg)

    dark_mode.configure(bg=fg, fg=bg)


dark_mode = Button(text="dark", width=3, bg="black", fg="white", command=dark_mode)
dark_mode.place(x=288, y=9)

"-----------------------------------------------------------------------------------------------------------------"


window.mainloop()