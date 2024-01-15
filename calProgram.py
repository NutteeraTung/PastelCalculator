from tkinter import *
root =Tk()
root.title("Calculator Program")
root.iconbitmap(r'D:\Tkinker Kongsaksayam\Calculator Asset\cal-logo.ico')
root.config(bg="#ffd3fc")
root.geometry("300x400+500+200")
root.resizable(1,1)

font = ('Bookman Old Style',12)
#test 
Label(root,text="Click me",font=font,bg="#ffd3fc").pack(pady=5)

#frame
displayFrame = LabelFrame(root,bg="#D4F6FF")
displayFrame.pack(padx=2,pady=2)  
buttonFrame = LabelFrame(root,bg="#C9CFFF")
buttonFrame.pack(ipadx=4,ipady=4) 

#variable
# inputNum = IntVar()

def showNum(number):
    dis.insert(END,number)
    if "." in dis.get(): #ไม่ให้มี . มากกว่า 1จุด
        decBut.config(state=DISABLED)

def operation(value):
    global firstNumber #ทุกฟังก์ชันสามารถเรียกใช้งานได้
    global operator
    operator = value
    firstNumber = dis.get()

    #reset state
    decBut.config(state=NORMAL)
    dis.delete(0,END)
    #dsiplay operator button
    addBut.config(state=DISABLED)
    subBut.config(state=DISABLED)
    mulBut.config(state=DISABLED)
    divBut.config(state=DISABLED)
    expBut.config(state=DISABLED)
    inverseBut.config(state=DISABLED)
    sqBut.config(state=DISABLED)
        
def equal():
    if operator == "add":
        result = float(firstNumber) + float(dis.get())
    elif operator == "subtract":
        result = float(firstNumber) - float(dis.get())
    elif operator == "multiply":
        result = float(firstNumber) * float(dis.get())
    elif operator == "divide":
        if dis.get() == "0":
            result = "Error"
        else:
            result = float(firstNumber) / float(dis.get())
    elif operator == "exponent":
        result = float(firstNumber) ** float(dis.get())
        
    dis.delete(0,END)
    dis.insert(0,result)
    enableOperator()
    
def inverse():
    if dis.get() == 0:
        result = "Error"
    else:
        result = 1/float(dis.get())
    dis.delete(0,END)
    dis.insert(0,result)
    
def sqrt():
    result = float(dis.get()) **2
    dis.delete(0,END)
    dis.insert(0,result)
    
def negate():
    result = (-1)*float(dis.get())
    dis.delete(0,END)    
    dis.insert(0,result)
    
def enableOperator():
    addBut.config(state=NORMAL)
    subBut.config(state=NORMAL)
    mulBut.config(state=NORMAL)
    divBut.config(state=NORMAL)
    expBut.config(state=NORMAL)
    inverseBut.config(state=NORMAL)
    sqBut.config(state=NORMAL)
    
def clearDis():
    dis.delete(0,END)    
    enableOperator()

#display frame
dis = Entry(displayFrame,width=30,font=font,bg="#EEEEA6",border=5,justify=LEFT) #,textvariable=inputNum
dis.pack(padx=5,pady=5)

#create button
clearBut= Button(buttonFrame,text="Clear",font=font,bg="#bc90dd",command=clearDis)
clearBut.grid(row=0,column=0,ipadx=10,ipady=4,padx=2,sticky="WE")
quitBut = Button(buttonFrame,text="Quit",font=font,command=root.destroy,bg="#bc90dd")
quitBut.grid(row=0,column=3,ipadx=10,ipady=4,padx=2,sticky="WE")

#operator button
inverseBut = Button(buttonFrame,text="1/x",font=font,bg="#C7E2BD",command=inverse)
inverseBut.grid(row=1,column=0,pady=1,ipadx=10,sticky="WE")
sqBut = Button(buttonFrame,text="x^2",font=font,bg="#C7E2BD",command=sqrt)
sqBut.grid(row=1,column=1,pady=1,ipadx=10,sticky="WE")
expBut = Button(buttonFrame,text="x^n",font=font,bg="#C7E2BD",command=lambda:operation("exponent"))
expBut.grid(row=1,column=2,pady=1,ipadx=10,sticky="WE")
divBut = Button(buttonFrame,text="/",font=font,bg="#C7E2BD",command=lambda:operation("divide"))
divBut.grid(row=1,column=3,pady=1,ipadx=10,sticky="WE")
mulBut = Button(buttonFrame,text="x",font=font,bg="#C7E2BD",command=lambda:operation("multiply"))
mulBut.grid(row=2,column=3,pady=1,ipadx=10,sticky="WE")
subBut = Button(buttonFrame,text="-",font=font,bg="#C7E2BD",command=lambda:operation("subtract"))
subBut.grid(row=3,column=3,pady=1,ipadx=10,sticky="WE")
addBut = Button(buttonFrame,text="+",font=font,bg="#C7E2BD",command=lambda:operation("add"))
addBut.grid(row=4,column=3,pady=1,ipadx=10,sticky="WE")
equalBut = Button(buttonFrame,text="=",font=font,bg="#C7E2BD",command=equal)
equalBut.grid(row=5,column=3,pady=1,ipadx=10,sticky="WE")
decBut = Button(buttonFrame,text=".",font=font,bg="#C7E2BD",command=lambda:showNum("."))
decBut.grid(row=5,column=2,pady=2,ipadx=10,sticky="WE")
negBut = Button(buttonFrame,text="+/-",font=font,bg="#C7E2BD",command=negate)
negBut.grid(row=5,column=0,pady=1,ipadx=10,sticky="WE")

#number button
but9 = Button(buttonFrame,text="9",font=font,bg="#A3D092",command=lambda:showNum(9))
but9.grid(row=2,column=2,pady=1,ipadx=10,sticky="WE")
but8 = Button(buttonFrame,text="8",font=font,bg="#A3D092",command=lambda:showNum(8))
but8.grid(row=2,column=1,pady=1,ipadx=10,sticky="WE")
but7 = Button(buttonFrame,text="7",font=font,bg="#A3D092",command=lambda:showNum(7))
but7.grid(row=2,column=0,pady=1,ipadx=10,sticky="WE")
but6 = Button(buttonFrame,text="6",font=font,bg="#A3D092",command=lambda:showNum(6))
but6.grid(row=3,column=2,pady=1,ipadx=10,sticky="WE")
but5 = Button(buttonFrame,text="5",font=font,bg="#A3D092",command=lambda:showNum(5))
but5.grid(row=3,column=1,pady=1,ipadx=10,sticky="WE")
but4 = Button(buttonFrame,text="4",font=font,bg="#A3D092",command=lambda:showNum(4))
but4.grid(row=3,column=0,pady=1,ipadx=10,sticky="WE")
but3 = Button(buttonFrame,text="3",font=font,bg="#A3D092",command=lambda:showNum(3))
but3.grid(row=4,column=2,pady=1,ipadx=10,sticky="WE")
but2 = Button(buttonFrame,text="2",font=font,bg="#A3D092",command=lambda:showNum(2))
but2.grid(row=4,column=1,pady=1,ipadx=10,sticky="WE")
but1 = Button(buttonFrame,text="1",font=font,bg="#A3D092",command=lambda:showNum(1))
but1.grid(row=4,column=0,pady=1,ipadx=10,sticky="WE")
but0 = Button(buttonFrame,text="0",font=font,bg="#A3D092",command=lambda:showNum(0))
but0.grid(row=5,column=1,pady=1,ipadx=10,sticky="WE")

root.mainloop()