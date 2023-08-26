# print("hii i am vishesh maurya first time using laptop for programming")
#for i in range(1,11):
  #  for j in range(1,11):
  #      m = i*j
  #      print(j,"X",i,"=",m,end = "\")
#print("hii playing ascibell \a ok")
form tkinter import *
import random 
root = Tk()
root.geometry("400x240")
root.title("love calculator")
def calc_love():
    st = "0123456789"
    digit = 2
    temp = "".join(random.sample(st,digit))
    result.config(text=temp)

    heading.config(text=temp)
    heading.pack()
    slot1=Label(root,text="How much is he/she loves you")
    heading.pack()
    slot1=Label(root,text = "Enter Your Name: ")
    slot1.pack()
    name1=Entry(root,border=5)
    name1.pack()
    slot2=Label(root,text="enter your partener name")
    slot2.pack()
    name2=Entry(root,boreder = 5)
    name2.pack()
    bt = Button(root,text="calculate",height=1,width=7, command=calc_love)
    bt.pack()
    result=Label(root,text="love percentage between both of you:")
    result.pack()
    root.mainloop()
