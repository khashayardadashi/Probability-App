import random
import tkinter 
from tkinter import *
from tkinter import Entry
from tkinter import messagebox
#probablity---------------------
def probability ():
    try :
        n = int (entery.get())
    except (TypeError) :
        messagebox.showwarning("your input must be a number")
    # n shows the number of times the program is executed
    outcomes=[]
    i=0
    for i in range(0,n+1):
        i=i+1
        #It produces a number between 0 and 1, which includes 0 and 1
        number=random.uniform(0,1)
        #Checking that the generated number is between [0,0.2] or not
        if(number>=0 and number<=0.2):
            outcomes.append(1)
        #Checking that the generated number is between (0.2,0.5] or not
        elif(number>0.2 and number<=0.5):
            outcomes.append(2)
        #Checking that the generated number is between (0.5,0.9] or not
        elif(number>0.5 and number<=0.9):
            outcomes.append(3)
        #Checking that the generated number is between (0.9,1] or not
        elif(number>0.9 and number<=1):
            outcomes.append(4)
    #Obtaining the probability of each interval as a percentage
    number1=(outcomes.count(1)/n)*100
    number2=(outcomes.count(2)/n)*100
    number3=(outcomes.count(3)/n)*100
    number4=(outcomes.count(4)/n)*100

    messagebox.showinfo('result',f' probability for [0 , 0.2] : {number1} \n probability for (0.2 , 0.5] : {number2} \n probability for (0.5 , 0.9] : {number3} \n probability for (0.9 , 1] : {number4}')
    entery.delete(0,len(entery.get()))

#window---------------------------------
window = tkinter.Tk()
window.title("probability")
window.geometry("400x150")
window.resizable(False,False)
window.eval('tk::PlaceWindow . center')

#entery----------------------------------
entery = Entry(master=window , bd=8 , font=("Arial",12 ,"bold") )
entery.pack(fill="x" , pady=5 , padx=5 )

#button-----------------------
btn1 = Button(master = window , text="1" , bd=6 , font=("Arial" ,12 , "bold") , width=4 , command=lambda : entery.insert(len(entery.get()),"1"))
btn2 = Button(master = window , text="2" , bd=6 , font=("Arial" ,12 , "bold") , width=4 , command=lambda : entery.insert(len(entery.get()),"2"))
btn3 = Button(master = window , text="3" , bd=6 , font=("Arial" ,12 , "bold") , width=4 , command=lambda : entery.insert(len(entery.get()),"3"))
btn4 = Button(master = window , text="4" , bd=6 , font=("Arial" ,12 , "bold") , width=4 , command=lambda : entery.insert(len(entery.get()),"4"))
btn5 = Button(master = window , text="5" , bd=6 , font=("Arial" ,12 , "bold") , width=4 , command=lambda : entery.insert(len(entery.get()),"5"))
btn6 = Button(master = window , text="6" , bd=6 , font=("Arial" ,12 , "bold") , width=4 , command=lambda : entery.insert(len(entery.get()),"6"))
btn7 = Button(master = window , text="7" , bd=6 , font=("Arial" ,12 , "bold") , width=4 , command=lambda : entery.insert(len(entery.get()),"7"))
btn8 = Button(master = window , text="8" , bd=6 , font=("Arial" ,12 , "bold") , width=4 , command=lambda : entery.insert(len(entery.get()),"8"))
btn9 = Button(master = window , text="9" , bd=6 , font=("Arial" ,12 , "bold") , width=4 , command=lambda : entery.insert(len(entery.get()),"9"))
btn0 = Button(master = window , text="0" , bd=6 , font=("Arial" ,12 , "bold") , width=4 , command=lambda : entery.insert(len(entery.get()),"0"))
result = Button(master = window , text="calculate" , bd=6 , font=("Arial" ,12 , "bold") , width=10 , command= probability)

#position for buttons--------
btn1.place( x=5 , y= 50)
btn2.place( x=70 , y= 50)
btn3.place(x=135 , y=50)
btn4.place(x=200 , y=50)
btn5.place(x=265 , y=50)
btn6.place(x=330 , y=50)
btn7.place(x=5 , y=100)
btn8.place(x=70 , y=100)
btn9.place(x=135 , y=100)
btn0.place(x=200 , y=100)
result.place(x=268 , y=100)

window.mainloop()