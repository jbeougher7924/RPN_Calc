import operator
from Tkinter import *

def rpn_method(rpn_string):
    # use a char operator symbal to do an operator method by passing the two value
    ops_list = { "+": operator.add,"-": operator.sub,"*": operator.mul,"/": operator.div}

    #  this holds the test value for running this method

    rpn_list = rpn_string.split(".")

    # define that rpn_stack is a list and to empty the list
    rpn_stack = [0]
    rpn_stack.pop()

    # cycle through all of the value in rpn_list and either add them to the stack or do the operator method
    for value in rpn_list:
        if value in ops_list:
            # top value is alway the second value only important for subtract and divide
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

    def buttonValue(self,value):
        if value in RPN_GUI.ops_char_list:
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

        self.place(x=0, y=0)
        self.createWidgets()

root =Tk()
app = RPN_GUI(master=root)
app.master.title("RPN Calculator")
app.mainloop()
root.destroy()