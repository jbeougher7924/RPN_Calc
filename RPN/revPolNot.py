import operator
from Tkinter import *

def rpn_method(rpn_string):
    # use a char operator symbol to do an operator method by passing the two value
    ops_list = { "+": operator.add,"-": operator.sub,"*": operator.mul,"/": operator.div}

    rpn_list = rpn_string.split(".")

    # define that rpn_stack is a list and to empty the list
    rpn_stack = [0]
    rpn_stack.pop()

    # cycle through all of the value in rpn_list and either add them to the stack or do the operator method
    for value in rpn_list:
        if value in ops_list:
            # top value is always the second value only important for subtract and divide
            val2 = rpn_stack.pop()
            val1 = rpn_stack.pop()
            sum_val = ops_list[value](val1,val2)
            print "{0} {1} {2} = {3}".format(val1,value,val2,sum_val)
            rpn_stack.append(sum_val)
        else:
            rpn_stack.append(int(value))

    return rpn_stack.pop()

class RPN_GUI(Frame):

    ops_char_list = ["+", "-","*","/"]
    # could have made this into a dictionary
    all_key_list = ["plus","minus","asterisk","slash","Return","equal","BackSpace","Delete","space"]
    # don't want to type 0 through 9 like had to with the words above and its easier to read
    for numName in range(10):
        all_key_list.append(str(numName))

    # need to pass the char value of + - * / not the string plus minus, etc to the RPNDisplay
    def keyInput(self,event):
        key_str = event.keysym
        if key_str == "plus":
            key_str = "+"
        elif key_str == "minus":
            key_str = "-"
        elif key_str == "asterisk":
            key_str = "*"
        elif key_str == "slash":
            key_str = "/"
        # using the period char and not the space char to separate the math char for easier viewing
        elif key_str == "space":
            key_str = "."

        # check for the types of key being used and final pass the key_str to the RPNDisplay
        if key_str == "Return" or key_str == "equal":
            self.equalPress()
        elif key_str == "BackSpace":
            self.backSpace()
        elif key_str == "Delete":
            self.clearScreen()
        else:
            self.buttonValue(key_str)

    def buttonValue(self,value):
        if value in RPN_GUI.ops_char_list:
            #all operators will have a space before them since you can do 123 but not +-* need .+.-.*
            self.RPNDisplay["text"] += "." + value
        else:
            self.RPNDisplay["text"] += value

    def clearScreen(self):
        self.RPNDisplay["text"] = ""

    def backSpace(self):
        display_len = len(self.RPNDisplay["text"]) - 1
        if(display_len < 0):
            return
        self.RPNDisplay["text"] = self.RPNDisplay["text"][:display_len]

    def equalPress(self):
        tempDisplay = self.RPNDisplay["text"]
        if(tempDisplay == ""):
            return
        self.RPNDisplay["text"] = str(rpn_method(tempDisplay))


    def createWidgets(self):

        self.RPNDisplay = Label(self)
        self.RPNDisplay["text"] = ""
        self.RPNDisplay["width"] = 20
        self.RPNDisplay["font"] = "Verdana 15 bold"
        self.RPNDisplay["bg"] = "black"
        self.RPNDisplay["fg"] = "red"
        self.RPNDisplay.place(x=10,y=10)

        self.Exit = Button(self)
        self.Exit["text"] = "OFF"
        self.Exit["font"] = "Verdana 15 bold"
        self.Exit["command"] = self.quit
        self.Exit.place(x=235, y=350)

        self.Exit = Button(self)
        self.Exit["text"] = "<-"
        self.Exit["font"] = "Verdana 15 bold"
        self.Exit["command"] = self.backSpace
        self.Exit.place(x=115, y=350)

        self.Exit = Button(self)
        self.Exit["text"] = "Clr"
        self.Exit["font"] = "Verdana 15 bold"
        self.Exit["command"] = self.clearScreen
        self.Exit.place(x=10, y=350)



        for x in range(3):
            for y in range(3):
                self.ValueButton = Button(self)
                buttonVal = y * 3 + x + 1
                self.ValueButton["text"] = buttonVal
                self.ValueButton["font"] = "Verdana 15 bold"
                self.ValueButton["command"] = lambda n = str(buttonVal): self.buttonValue(n)
                self.ValueButton.place(x=x * 60 + 30, y=y * -60 + 220)
        y = 0
        x = 3
        for opsChar in RPN_GUI.ops_char_list:
            self.ValueButton = Button(self)
            buttonVal = opsChar
            self.ValueButton["text"] = buttonVal
            self.ValueButton["font"] = "Verdana 15 bold"
            self.ValueButton["command"] = lambda n = buttonVal: self.buttonValue(n)
            self.ValueButton.place(x=x * 60 + 30, y=y * -60 + 280)
            y += 1

        self.ValueButton = Button(self)
        buttonVal = 0
        self.ValueButton["text"] = buttonVal
        self.ValueButton["font"] = "Verdana 15 bold"
        self.ValueButton["command"] = lambda n=str(buttonVal): self.buttonValue(n)
        self.ValueButton.place(x=1 * 60 + 30, y=0 * -60 + 280)

        self.ValueButton = Button(self)
        buttonVal = "="
        self.ValueButton["text"] = buttonVal
        self.ValueButton["font"] = "Verdana 15 bold"
        self.ValueButton["command"] = lambda n=buttonVal: self.buttonValue(n)
        self.ValueButton.place(x=2 * 60 + 30, y=0 * -60 + 280)

        self.ValueButton = Button(self,height=2, width=2)
        buttonVal = "."
        self.ValueButton["text"] = "Sp"
        self.ValueButton["font"] = "Verdana 10 bold"
        self.ValueButton["command"] = lambda n=buttonVal: self.buttonValue(n)
        self.ValueButton.place(x=0 * 60 + 30, y=0 * -60 + 280)

        self.ValueButton = Button(self)
        buttonVal = 0
        self.ValueButton["text"] = buttonVal
        self.ValueButton["font"] = "Verdana 15 bold"
        self.ValueButton["command"] = lambda n=str(buttonVal): self.buttonValue(n)
        self.ValueButton.place(x=1 * 60 + 30, y=0 * -60 + 280)

        self.ValueButton = Button(self)
        buttonVal = "="
        self.ValueButton["text"] = buttonVal
        self.ValueButton["font"] = "Verdana 15 bold"
        self.ValueButton["command"] = self.equalPress
        self.ValueButton.place(x=2 * 60 + 30, y=0 * -60 + 280)

    def __init__(self, master=None):
        Frame.__init__(self, master, width=305, height=400, bg="dim grey")
        self.master.minsize(width=305,height=400)
        # set where x and y beings in the frame. Which is the top left corner for 0,0
        self.place(x=0, y=0)
        self.createWidgets()

root =Tk()
app = RPN_GUI(master=root)
app.master.title("RPN Calculator")

#bind the all_key_list to keyboard inputs
for key_list in app.all_key_list:
    key_value = "<Key-" + key_list + ">"
    # need to bind here so the entire active frame is the focus to catches the keyboard input.
    # has not worked to bind the frame in the class
    app.master.bind(key_value,app.keyInput)
app.mainloop()
root.destroy()