from tkinter import *

#improvisied


window = Tk()
window.geometry("312x324")
window.resizable(0,0)
window.title("Calculator")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    input_text.set("")

def btn_equal(inp):
    if (inp == "i"):
        global expression
        result = str(eval(expression))
        input_text.set(result)
    elif (inp == "ans"):
        return 0
    expression = ""

expression = ""
input_text = StringVar()

input_frame = Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor="black", highlightthickness="1")
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font =('arial',18, 'bold'), textvariable= input_text, width = 50, bg = "#eee", bd=0,justify="center")
input_field.grid(row=0,column=0)
input_field.pack(ipady = 10)

btns_frame = Frame(window, width=312, height=272.5, bg="grey")
btns_frame.pack()

clear = Button(btns_frame, text = "C", fg = "black", width = 10, height = 3, bd = 0, bg ="#eee", cursor ="hand2" ,command = lambda : btn_clear()).grid(row=0)
divide = Button(btns_frame, text="/", fg="black", width= 10, height=3, bd=0, bg="#eee", cursor="hand2" ,command=lambda : btn_click("/")).grid(row=0,column=1)
openparenthesis = Button(btns_frame, text="", fg="black", width= 10, height=3, bd=0, bg="#eee", cursor="hand2" ,).grid(row=0,column=2)
closeparenthesis = Button(btns_frame, text="", fg="black", width= 10, height=3, bd=0, bg="#eee", cursor="hand2" ).grid(row=0,column=3)

seven = Button(btns_frame, text="7", fg="black", width= 10, height=3, bd=0, bg="#fff", cursor="hand2" ,command=lambda : btn_click(7)).grid(row=1)
eight = Button(btns_frame, text="8", fg="black", width= 10, height=3, bd=0, bg="#fff", cursor="hand2" ,command=lambda : btn_click(8)).grid(row=1,column=1)
nine = Button(btns_frame, text="9", fg="black", width= 10, height=3, bd=0, bg="#fff", cursor="hand2" ,command=lambda : btn_click(9)).grid(row=1,column=2)
multiply = Button(btns_frame, text="*", fg="black", width= 10, height=3, bd=0, bg="#fff", cursor="hand2" ,command=lambda : btn_click("*")).grid(row=1,column=3)

four = Button(btns_frame, text="4", fg="black", width= 10, height=3, bd=0, bg="#fff", cursor="hand2" ,command=lambda : btn_click(4)).grid(row=2)
five = Button(btns_frame, text="5", fg="black", width= 10, height=3, bd=0, bg="#fff", cursor="hand2" ,command=lambda : btn_click(5)).grid(row=2,column=1)
six = Button(btns_frame, text="6", fg="black", width= 10, height=3, bd=0, bg="#fff", cursor="hand2" ,command=lambda : btn_click(6)).grid(row=2,column=2)
minus = Button(btns_frame, text="-", fg="black", width= 10, height=3, bd=0, bg="#fff", cursor="hand2" ,command=lambda : btn_click("-")).grid(row=2,column=3)

one  = Button(btns_frame, text="1", fg="black", width= 10, height=3, bd=0, bg="#fff", cursor="hand2" ,command=lambda : btn_click(1)).grid(row=3)
two = Button(btns_frame, text="2", fg="black", width= 10, height=3, bd=0, bg="#fff", cursor="hand2" ,command=lambda : btn_click(2)).grid(row=3,column=1)
three = Button(btns_frame, text="3", fg="black", width= 10, height=3, bd=0, bg="#fff", cursor="hand2" ,command=lambda : btn_click(3)).grid(row=3,column=2)
plus = Button(btns_frame, text="+", fg="black", width= 10, height=3, bd=0, bg="#fff", cursor="hand2" ,command=lambda : btn_click("+")).grid(row=3,column=3)

zero = Button(btns_frame, text="0", fg="black", width= 10, height=3, bd=0, bg="#fff", cursor="hand2" ,command=lambda : btn_click(0)).grid(row=4)
point = Button(btns_frame, text=".", fg="black", width= 10, height=3, bd=0, bg="#eee", cursor="hand2" ,command=lambda : btn_click(".")).grid(row=4,column=1)
ans = Button(btns_frame, text="ANS", fg="black", width= 10, height=3, bd=0, bg="#eee", cursor="hand2" ,command=lambda : btn_equal('ans')).grid(row=4,column=2)
equals = Button(btns_frame, text="=", fg="black", width= 10, height=3, bd=0, bg="#eee", cursor="hand2" ,command=lambda : btn_equal("i")).grid(row=4,column=3)

window.mainloop()