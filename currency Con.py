from tkinter import *



OPTIONS = {
    "Australian Dollar":0.018,
    "Brazilian Real":0.074,
    "British Pound":0.010,
    "Chinese Yuan":0.0858,
    "        Euro          ":0.011,
    "Japanese Yen":1.5394,
    "Pakistani Rupee":2.3545,
    "SriLankan Rupee":2.71,
    "Swiss Franc":0.01249,
    "Us Dollar             ":0.0134
        }



def convert():
    price = rupees.get()
    names = values.get()
    currency1=OPTIONS.get(names)
    converter=float(currency1)*float(price)  
    Label(root,text=names+": ",font=("arial",10,"bold"),fg="red").place(x=30, y=210)
    result.delete(0.0,END)
    result.insert(INSERT,"%.2f"%converter)
    







root= Tk()
root.title("Currency Converter")
root.geometry("600x400")

f1=Frame(root,bg="black")
f1.pack()

L1 = Label(root,text="Currency Converter",font=("arial",25,"bold","underline"),bg="black",fg="red")
L1.place(x=140, y=10)

result = Text(root,height=1.5,width=15,font=("arial",13,"bold"),bd=5)
result.place(x=155, y=200)

india = Label(root,text="INDIAN VALUE: ",font=("arial",10,"bold"),fg="red")
india.place(x=45, y=80)

rupees = Entry(root,font=("arial",20))
rupees.place(x=150, y=75)
choice = Label(root,text="SELECT CURRENCY:",font=("arial",10,"bold"),fg="red")
choice.place(x=18, y=130)

values = StringVar()
values.set(None)
option = OptionMenu(root,values,*OPTIONS)
option.place(x=150 , y=130,width=140, height=40)


button = Button(root,text="Convert",fg="red",bg="black",font=("arial",20),command=convert)
button.place(x=150, y=270,height=40,width=150)


root.mainloop()


