from tkinter import *
expression = ""


def addToExpression(number):
    '''
    Function that adds inputs from calculator buttons to global variable expression
    Concatenates strings and transforms into sets
    Returns expression as set
    '''
    global expression
    expression = expression + str(number)
    settedExpression.set(expression)
    return expression

def evaluateExpression():
    '''
    Evaluates expression upon click '=' on calculator
    Returns evaluated expression as str
    '''
    try:
        global expression
        expression = str(eval(expression))
        settedExpression.set(expression)
        return expression
    except ZeroDivisionError:
        settedExpression.set("You can't divide by 0!")
        expression = ""
        return expression
    except:
        settedExpression.set("Error! Terminating!")
        expression = ""
        return expression



        

def clearExpression():
    '''
    Clears expression upon click of clear button
    Returns empty expression string
    '''
    global expression
    expression = ""
    settedExpression.set("")
    return expression



#Creating tkinter display with function-calling buttons
root = Tk() 
root.title("Calculator program Y1") 
root.geometry("300x200") 

settedExpression = StringVar() #Instantiating settedExpression, the StringVar() object that is displayed on screen

expression_field = Entry(root, textvariable=settedExpression) 

# grid method is used for placing 
# the widgets at respective positions 
# in table like structure . 
expression_field.grid(columnspan=4, ipadx=70) 

settedExpression.set('enter your expression') 

# create a Buttons and place at a particular 
# location inside the root window . 
# when user press the button, the command or 
# function affiliated to that button is executed . 
button1 = Button(root, text=' 1 ', command=lambda: addToExpression(1), height=1, width=7) 
button1.grid(row=2, column=0) 

button2 = Button(root, text=' 2  ', command=lambda: addToExpression(2), height=1, width=7) 
button2.grid(row=2, column=1) 

button3 = Button(root, text=' 3 ', command=lambda: addToExpression(3), height=1, width=7) 
button3.grid(row=2, column=2) 

button4 = Button(root, text=' 4 ', command=lambda: addToExpression(4), height=1, width=7) 
button4.grid(row=3, column=0) 

button5 = Button(root, text=' 5 ', command=lambda: addToExpression(5), height=1, width=7) 
button5.grid(row=3, column=1) 

button6 = Button(root, text=' 6 ', command=lambda: addToExpression(6), height=1, width=7) 
button6.grid(row=3, column=2) 

button7 = Button(root, text=' 7 ', command=lambda: addToExpression(7), height=1, width=7) 
button7.grid(row=4, column=0) 

button8 = Button(root, text=' 8 ', command=lambda: addToExpression(8), height=1, width=7) 
button8.grid(row=4, column=1) 

button9 = Button(root, text=' 9 ', command=lambda: addToExpression(9), height=1, width=7) 
button9.grid(row=4, column=2) 

button0 = Button(root, text=' 0 ', command=lambda: addToExpression(0), height=1, width=7) 
button0.grid(row=5, column=0) 

plus = Button(root, text=' + ', command=lambda: addToExpression("+"), height=1, width=7) 
plus.grid(row=2, column=3) 

minus = Button(root, text=' - ', command=lambda: addToExpression("-"), height=1, width=7) 
minus.grid(row=3, column=3) 

multiply = Button(root, text=' * ', command=lambda: addToExpression("*"), height=1, width=7) 
multiply.grid(row=4, column=3) 

divide = Button(root, text=' / ', command=lambda: addToExpression("/"), height=1, width=7) 
divide.grid(row=5, column=3)

openParen = Button(root, text = ' ( ', command=lambda: addToExpression("("), height = 1, width = 7)
openParen.grid(row = 5, column = 1)

closeParen = Button(root, text = ' ) ', command=lambda: addToExpression(")"), height = 1, width = 7)
closeParen.grid(row = 5, column = 2)

equal = Button(root, text=' = ', command=evaluateExpression, height=1, width=7) 
equal.grid(row=6, column=2) 

clear = Button(root, text=' AC ', command=clearExpression, height=1, width=7) 
clear.grid(row=6, column=1) 

Decimal= Button(root, text='.', command=lambda: addToExpression('.'), height=1, width=7) 
Decimal.grid(row=6, column=0) 
# start the GUI 
root.mainloop() 
