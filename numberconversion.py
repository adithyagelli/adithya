import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import random
root=tk.Tk()
global x
x="light blue"

def clear_frame():
    for widgets in root.winfo_children():
        widgets.destroy()


def color():
  if var.get()==1:
    x="light blue"
  elif var.get()==2:
    x="light green"
  elif var.get()==3:
    x="light grey"
  elif var.get()==4:
    x="light pink"  
  root.configure(background=x)
  label.configure(bg=x)
  l1.configure(bg=x)
  l2.configure(bg=x)
  l3.configure(bg=x) 
  C1.configure(bg=x)
  C2.configure(bg=x)
  C3.configure(bg=x)
  C4.configure(bg=x)
  l11.configure(bg=x)


def result_color():
  if var.get()==1:
    x="light blue"
  elif var.get()==2:
    x="light green"
  elif var.get()==3:
    x="light grey"
  elif var.get()==4:
    x="light pink"
  try:
      root.configure(background=x)
      label.configure(bg=x)
      l10.configure(bg=x)
      l4.configure(bg=x)
      l5.configure(bg=x)
      l6.configure(bg=x)
      l7.configure(bg=x)
      l8.configure(bg=x)
      l9.configure(bg=x)
  except:
      pass


def validation():
    temp=number.get()
    msg = '' 
    def bin():
        for i in temp:
            if i not in ['0','1']:
                return False
        return True
    
    def oct():
        for i in temp:
            if i not in ['0','1','2','3','4','5','6','7']:
                return False
        return True
 
    def hex():
        for i in temp:
            if i not in ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']:
                return False
        return True
    
    if selected_type.get()=="hexadecimal" and hex()==False:
            msg = 'Invalid hexadecimal number'
            messagebox.showerror("Error", msg)

    if selected_type.get()=="octal" and oct()==False:
        msg = 'Invalid Octal Number'
        messagebox.showerror('Error',msg)

    if selected_type.get()=="binary" and bin()==False:
        msg = 'Enter a valid binary number'
        messagebox.showerror('Error', msg)

    if selected_type.get() == "decimal" and temp.isdigit() == False:
            msg = 'Enter a valid decimal number'
            messagebox.showinfo('message', msg)

    if len(temp) == 0:
            msg = 'Number can\'t be empty'      
            messagebox.showinfo('message', msg)

    if selected_type.get()=="":
            msg = 'Select type'      
            messagebox.showinfo('message', msg)

    if CheckVar1.get()==0 and CheckVar2.get()==0 and CheckVar3.get()==0 and CheckVar4.get()==0:
            msg = 'Select atleast one conversion'      
            messagebox.showinfo('message', msg)

    if selected_type.get() =='binary' and CheckVar1.get()==1:
            msg = 'Binary to Binary conversion is not possible'      
            messagebox.showinfo('message', msg) 

    if selected_type.get() =='octal' and CheckVar2.get()==1:
            msg = 'Octal to Octal conversion is not possible'      
            messagebox.showinfo('message', msg)

    if selected_type.get() =='decimal' and CheckVar3.get()==1:
            msg = 'Decimal to Decimal conversion is not possible'      
            messagebox.showinfo('message', msg)

    if selected_type.get() =='hexadecimal' and CheckVar4.get()==1:
            msg = 'Hexadecimal to Hexadecimal conversion is not possible'      
            messagebox.showinfo('message', msg)
    if msg == '' :
         result() 




def home():
    
  
  global label,l1,number,l2,l3,C1,C2,C3,C4,CheckVar1,CheckVar2,CheckVar3,CheckVar4,selected_type,var,l11

  clear_frame()
  root.configure(background=x)

  label=tk.Label(root, bg=x, text="Number Conversion",font = ('Latin Modern Roman Italic bold underline',30))
  label.place(x=320,y=45)

  l1=tk.Label(root,bg=x ,text="Enter a number",font=(20))
  l1.place(x=200,y=170)
  number=tk.Entry(root,width=28,font=("Arial",13))
  number.place(x=400,y=175)

  
  l2=tk.Label(root,bg=x ,text="select type ",font=(20))
  l2.place(x=200,y=250)


  selected_type = tk.StringVar()
  num_type = ttk.Combobox(root, textvariable=selected_type, width=38, state='readonly')
  num_type['values'] = ['binary','octal','decimal','hexadecimal']
  num_type.place(x=400,y=250)
  
  
 
  l3=Label(root,bg=x ,text="Tick conversions ",font=(20))
  l3.place(x=200,y=340)

  CheckVar1 = IntVar(root)
  C1 = tk.Checkbutton(root,font=(20), text = "binary",bg=x,variable = CheckVar1,onvalue = 1, offvalue = 0,)
  C1.place(x=420,y=330)

  CheckVar2 = IntVar()
  C2 = tk.Checkbutton(root,font=(20), text = "octal",bg=x,variable = CheckVar2,onvalue = 1, offvalue = 0, )
  C2.place(x=420,y=360)
 
  CheckVar3 = IntVar() 
  C3 = tk.Checkbutton(root,font=(20), text = "decimal",bg=x,variable = CheckVar3,onvalue = 1, offvalue = 0, )
  C3.place(x=420,y=390)

  CheckVar4 = IntVar()
  C4 = tk.Checkbutton(root,font=(20), text = "hexadecimal",bg=x,variable = CheckVar4,onvalue = 1, offvalue = 0,)
  C4.place(x=420,y=420)

  

  button=Button(root,text="Result",width=10,height=2,bg="white",command=lambda:[validation()]).place(x=400,y=500)
  
  l11=tk.Label(root,bg=x ,text="select color",font=(20))
  l11.place(x=200,y=600)
  var= IntVar(root)
  blue = Radiobutton(root, text=" light blue", value=1,variable=var,command=color, padx = 1, pady = 1)
  blue.place(x=560,y=600)
  green= Radiobutton(root, text="light green",command=color,value=2, variable=var ,padx = 1, pady = 1 )
  green.place(x=660,y=600)
  grey=Radiobutton(root,text=" light grey", command=color,value=3,variable=var, padx = 1, pady = 1)  
  grey.place(x=340,y=600)
  pink=Radiobutton(root,text=" light pink", command=color,value=4,variable=var, padx = 1, pady = 1)  
  pink.place(x=450,y=600)


def result():
    global label,l4,l5,l6,l7,l8,l9,var,l10,ans,ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10,ans11,number1,st

    number1=number.get() 
    st=selected_type.get()

    clear_frame()

    label=tk.Label(root,text="RESULT PAGE",font=('Latin Modern Roman Italic bold underline',30),bg=x)
    label.place(x=300,y=40)
      

    if number1!="" and  st=="decimal":      
            if CheckVar1.get()==1:
                ans=str(bin(int(number1)))
                ans=ans[2:]
                l4=tk.Label(root,text="Decimal to binary                  :",bg=x,font=(20))
                l4.place(x=200,y=190)
                l5=tk.Label(root,text=ans,font=(20),bg=x)
                l5.place(x=500,y=190)

            if CheckVar2.get()==1:
                ans1=str(oct(int(number1)))
                ans1=ans1[2:]
                l6=tk.Label(root,text="Decimal to octal                   :",bg=x,font=(20))
                l6.place(x=200,y=270)
                l7=tk.Label(root,text=ans1,font=(20),bg=x)
                l7.place(x=500,y=270)
                        
            if CheckVar4.get()==1:
                ans2=str(hex(int(number1)))
                ans2=ans2[2:]
                l8=tk.Label(root,text="Decimal to hexadecimal        :",bg=x,font=(20))
                l8.place(x=200,y=350)
                l9=tk.Label(root,text=ans2,font=(20),bg=x)
                l9.place(x=500,y=350)

    if number1!="" and  st=="binary":
            if CheckVar2.get()==1:
                ans3=str(oct(int(number1,2)))
                ans3=ans3[2:]
                l4=tk.Label(root,text="Binary to octal                    :",font=(20),bg=x)
                l4.place(x=200,y=200)
                l5=tk.Label(root,text=ans3,font=(20),bg=x)
                l5.place(x=500,y=200)
            if CheckVar3.get()==1:
                ans4=int(number1,2)
                l6=tk.Label(root,text="Binary to decimal               :",font=(20),bg=x)
                l6.place(x=200,y=300)
                l7=tk.Label(root,text=ans4,font=(20),bg=x)
                l7.place(x=500,y=300)
            if CheckVar4.get()==1:
                ans5=str(hex(int(number1,2)))
                ans5=ans5[2:]
                l8=tk.Label(root,text="Binary to hexadecimal         :",font=(20),bg=x)
                l8.place(x=200,y=400)
                l9=tk.Label(root,text=ans5,font=(20),bg=x)
                l9.place(x=500,y=400)
                
    if number1!="" and  st=="octal":
            if CheckVar1.get()==1:
                ans6=str(bin(int(number1,8)))
                ans6=ans6[2:]
                l4=tk.Label(root,text="Octal to binary                :",font=(20),bg=x)
                l4.place(x=200,y=190)
                l5=tk.Label(root,text=ans6,font=(20),bg=x)
                l5.place(x=500,y=190)
            if CheckVar3.get()==1:
                ans7=int(number1,8)
                l6=tk.Label(root,text="Octal to decimal              :",font=(20),bg=x)
                l6.place(x=200,y=270)
                l7=tk.Label(root,text=ans7,font=(20),bg=x)
                l7.place(x=500,y=270)
            if CheckVar4.get()==1:
                ans8=str(hex(int(number1,8)))
                ans8=ans8[2:]
                l8=tk.Label(root,text="Octal to hexadecimal       :",font=(20),bg=x)
                l8.place(x=200,y=350)
                l9=tk.Label(root,text=ans8,font=(20),bg=x)
                l9.place(x=500,y=350)

    if number1!= "" and  st=="hexadecimal":
                  if CheckVar1.get()==1:
                      ans9=str(bin(int(number1,16)))
                      ans9=ans9[2:]
                      l4=tk.Label(root,text="Hexadecimal to binary      :",font=(20),bg=x)
                      l4.place(x=200,y=190)
                      l5=tk.Label(root,text=ans9,font=(20),bg=x)
                      l5.place(x=500,y=190)
                  if CheckVar2.get()==1:
                      ans10=str(oct(int(number1,16)))
                      ans10=ans10[2:]
                      l6=tk.Label(root,text="Hexadecimal to octal       :",font=(20),bg=x)
                      l6.place(x=200,y=270)
                      l7=tk.Label(root,text=ans10,font=(20),bg=x)
                      l7.place(x=500,y=270)
                  if CheckVar3.get()==1:
                      ans11=int(number1,16)
                      l8=tk.Label(root,text="Hexadecimal to decimal    :",font=(20),bg=x)
                      l8.place(x=200,y=350)
                      l9=tk.Label(root,text=ans11,font=(20),bg=x)
                      l9.place(x=500,y=350)   


    button=Button(root,text="home",width=10,height=2,command=home).place(x=240,y=480)
    button=Button(root,text="Explanation",width=10,height=2,command=explain).place(x=430,y=480)

    l10=Label(root,bg=x,text="Select Colour",font=(10))
    l10.place(x=200,y=600)
    var= IntVar(root)
    blue = Radiobutton(root, text=" light blue", value=1,variable=var,command=result_color, padx = 1, pady = 1)
    blue.place(x=560,y=600)
    green= Radiobutton(root, text="light green",command=result_color,value=2, variable=var ,padx = 1, pady = 1 )
    green.place(x=660,y=600)
    grey=Radiobutton(root,text=" light grey", command=result_color,value=3,variable=var, padx = 1, pady = 1)  
    grey.place(x=340,y=600)
    pink=Radiobutton(root,text=" light pink", command=result_color,value=4,variable=var, padx = 1, pady = 1)  
    pink.place(x=450,y=600)


def explain():
    global l20,l21,l22
    clear_frame()
    
    label=tk.Label(root,text="EXPLAINATION  PAGE",font=('Latin Modern Roman Italic bold underline',30),bg=x).place(x=225,y=35)
    
    if number1!="" and  st=="decimal" :
      if CheckVar1.get()==1:
        l20=tk.Label(root,text="Decimal to binary:",bg=x,font=(20))
        l20.place(x=25,y=140)
        l21=tk.Label(root,text="Divide the number by 2 and write the remainder in the rightmost column. Then divide the quotient by 2 and write the \nremainder in the next column to the left. Continue dividing the quotient by 2 until the quotient is 0.\n The binary number is the sequence of remainders read from right to left.",bg=x,font=("Arial", 12))
        l21.place(x=25,y=180)
        l22=tk.Label(root,text="("+number1+"/2),..."+"="+ans,bg=x,font=(20))
        l22.place(x=300,y=255)
      if CheckVar2.get()==1:
        l20=tk.Label(root,text="Decimal to octal:",bg=x,font=(20))
        l20.place(x=25,y=300)
        l21=tk.Label(root,text="Divide the number by 8 and write the remainder in the rightmost column. Then divide the quotient by 8 and write the \nremainder in the next column to the left. Continue dividing the quotient by 8 until the quotient is 0. \nThe octal number is the sequence of remainders read from right to left.",bg=x,font=("Arial", 12))
        l21.place(x=25,y=340)
        l22=tk.Label(root,text="("+number1+"/8),..."+"="+ans1,bg=x,font=(20))
        l22.place(x=300,y=400)
      if CheckVar4.get()==1:
        l20=tk.Label(root,text="Decimal to hexadecimal:",bg=x,font=(20))
        l20.place(x=25,y=440)
        l21=tk.Label(root,text="Divide the number by 16 and write the remainder in the rightmost column. Then divide the quotient by 16 and write the\n remainder in the next column to the left. Continue dividing the quotient by 16 until the quotient is 0. \nThe hexadecimal number is the sequence of remainders read from right to left.",bg=x,font=("Arial", 12))
        l21.place(x=25,y=480)
        l22=tk.Label(root,text="("+number1+"/16),..."+"="+ans2,bg=x,font=(20))
        l22.place(x=300,y=550)

    if number1!="" and  st=="binary":
        if CheckVar2.get()==1:
            l20=tk.Label(root,text="Binary to octal:",bg=x,font=(20))
            l20.place(x=25,y=140)
            l21=tk.Label(root,text="Divide the number by 8 and write the remainder in the rightmost column. Then divide the quotient by 8 and write the \nremainder in the next column to the left. Continue dividing the quotient by 8 until the quotient is 0. \nThe octal number is the sequence of remainders read from right to left.",bg=x,font=("Arial", 12))
            l21.place(x=25,y=180)
            l22=tk.Label(root,text="("+number1+"/8),..."+"="+ans3,bg=x,font=(20))
            l22.place(x=300,y=255)
        if CheckVar3.get()==1:
            l20=tk.Label(root,text="Binary to decimal:",bg=x,font=(20))
            l20.place(x=25,y=300)
            l21=tk.Label(root,text="Multiply each digit of the binary number by the corresponding power of 2. Add the products together to obtain the decimal \nnumber.This is how you convert binary to decimal",bg=x,font=("Arial", 12))
            l21.place(x=25,y=340)
            l22=tk.Label(root,text=f"({number1}*0)+({number1}*2)+({number1}*4)...={ans4}",bg=x,font=(20))     
            l22.place(x=180,y=400)  
        if CheckVar4.get()==1:
            l20=tk.Label(root,text="Binary to hexadecimal:",bg=x,font=(20))
            l20.place(x=25,y=440)
            l21=tk.Label(root,text="Divide the number by 16 and write the remainder in the rightmost column. Then divide the quotient by 16 and write the\n remainder in the next column to the left. Continue dividing the quotient by 16 until the quotient is 0. \nThe hexadecimal number is the sequence of remainders read from right to left.",bg=x,font=("Arial", 12))
            l21.place(x=25,y=480)
            l22=tk.Label(root,text="("+number1+"/16),..."+"="+ans5,bg=x,font=(20))
            l22.place(x=300,y=550)

    if number1!="" and  st=="octal":
        if CheckVar1.get()==1:
            l20=tk.Label(root,text="Octal to binary:",bg=x,font=(20))
            l20.place(x=25,y=140)
            l21=tk.Label(root,text="Divide the number by 2 and write the remainder in the rightmost column. Then divide the quotient by 2 and write the \nremainder in the next column to the left. Continue dividing the quotient by 2 until the quotient is 0.\n The binary number is the sequence of remainders read from right to left.",bg=x,font=("Arial", 12))
            l21.place(x=25,y=180)
            l22=tk.Label(root,text="("+number1+"/2),..."+"="+ans6,bg=x,font=(20))
            l22.place(x=300,y=255)
        if CheckVar3.get()==1:
            l20=tk.Label(root,text="Octal to decimal:",bg=x,font=(20))
            l20.place(x=25,y=300)
            l21=tk.Label(root,text="Multiply each digit of the octal number by the corresponding power of 8. Add the products together to obtain the decimal number.",bg=x,font=("Arial", 12))
            l21.place(x=25,y=340)
            l22=tk.Label(root,text=f"({number1}*0)+({number1}*8)+({number1}*64)...={ans7}",bg=x,font=(20))     
            l22.place(x=300,y=400)
        if CheckVar4.get()==1:
            l20=tk.Label(root,text="Octal to hexadecimal:",bg=x,font=(20))
            l20.place(x=25,y=440)
            l21=tk.Label(root,text="Divide the number by 16 and write the remainder in the rightmost column. Then divide the quotient by 16 and write the\n remainder in the next column to the left. Continue dividing the quotient by 16 until the quotient is 0. \nThe hexadecimal number is the sequence of remainders read from right to left.",bg=x,font=("Arial", 12))
            l21.place(x=25,y=480)
            l22=tk.Label(root,text="("+number1+"/16),..."+"="+ans8,bg=x,font=(20))
            l22.place(x=300,y=550)

    if number1!="" and  st=="hexadecimal":
        if CheckVar1.get()==1:
            l20=tk.Label(root,text="Hexadecimal to binary:",bg=x,font=(20))
            l20.place(x=25,y=140)
            l21=tk.Label(root,text="Divide the number by 2 and write the remainder in the rightmost column. Then divide the quotient by 2 and write the \nremainder in the next column to the left. Continue dividing the quotient by 2 until the quotient is 0.\n The binary number is the sequence of remainders read from right to left.",bg=x,font=("Arial", 12))
            l21.place(x=25,y=180)
            l22=tk.Label(root,text="("+number1+"/2),..."+"="+ans9,bg=x,font=(20))
            l22.place(x=300,y=255)
        if CheckVar2.get()==1:
            l20=tk.Label(root,text="Hexadecimal to octal:",bg=x,font=(20))
            l20.place(x=25,y=300)
            l21=tk.Label(root,text="Divide the number by 8 and write the remainder in the rightmost column. Then divide the quotient by 8 and write the \nremainder in the next column to the left. Continue dividing the quotient by 8 until the quotient is 0. \nThe octal number is the sequence of remainders read from right to left.",bg=x,font=("Arial", 12))
            l21.place(x=25,y=340)
            l22=tk.Label(root,text="("+number1+"/8),..."+"="+ans10,bg=x,font=(20))
            l22.place(x=300,y=400)
        if CheckVar3.get()==1:
            l20=tk.Label(root,text="Hexadecimal to decimal:",bg=x,font=(20))
            l20.place(x=25,y=440)
            l21=tk.Label(root,text="Multiply each digit of the hexadecimal number by the corresponding power of 16.Add the products together to obtain the decimal number.",bg=x,font=("Arial", 12))
            l21.place(x=25,y=480)
            l22=tk.Label(root,text=f"({number1}*0)+({number1}*16)+({number1}*256)...={ans11}",bg=x,font=(20))     
            l22.place(x=300,y=550)


    button=Button(root,text="home",width=10,height=2,command=home).place(x=380,y=600)


root.geometry("900x700")
root.resizable(False, False)
root.title("Home page")
home()
root.mainloop()