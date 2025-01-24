from tkinter import *

root = Tk()
root.title("Счетчик кликов")
root.geometry("500x500")
root.resizable(height=False, width= False)

count1 = 0
count2 = 0
def clickedplus():
    global count1
    count1 += 1
    Click.configure(text= count1)

def clickedminus():
    global count2
    count2 -= 1
    Click.configure(text= count2)

def clearplus():
    global count1
    count1 = 0
    Click.configure(text = count1)

def clearminus():
    global count2
    count2 = 0
    Click.configure(text = count2)


Click = Label(root, text = "0", font = "Arial 30")
Click.pack()

btn1 = Button(root, text= "Кликни меня" , padx= '20', pady= '-30', command = clickedplus)
btn2 = Button(root, text= "Обнулить" , padx= '20', pady= '-30', command = clearplus)
btn3 = Button(root, text= "Уйди в минус" , padx= '20', pady= '20', command = clickedminus)
btn4 = Button(root, text= "Обнулить" , padx= '20', pady= '20', command = clearminus)


btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()


root.mainloop()
