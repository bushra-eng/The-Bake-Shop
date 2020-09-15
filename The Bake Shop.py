#BUSHRA ASHFAQUE |CS-19011 | SECTION A | OOP ASSIGNMENT 1

def showstock(handler,name,space):#this function shows stock of boutique and food, and shows hourly wage of employees.
    global dic_food
    global dic_boutique
    global dic_employee
    if name == 'food':
        dic = dic_food
    elif name == 'boutique':
        dic = dic_boutique
    else:
        dic = dic_employee
    i=0
    Label(handler, text=space, font=("Courier", 20)).grid(row=i, sticky=W)
    if type(list((dic.values()))[0]) == int:
            Label(handler, text=f"Today's total sale is {total_sale}", font=('Courier', 20)).grid(row=i,sticky=W)
            i+=1
    for key,val in dic.items():
        if type(val)==int:#this displays hourly wage of employees
            Label(handler, text=f'{key} has hourly wage of {val}.', font=("Courier", 20)).grid(row=i,sticky=W)
        else:#this displays stock of food and employee
            Label(handler,text=f'We have {val[0]},{key} of Rs {val[1]} each.',font=("Courier",20)).grid(row=i,sticky=W)
        i+=1
    return(i)# row number
def calculate_bill(handler,amounts,i,name,space):#calculate bill of food and boutique, and daily wage of employees.
    global total_sale
    global dic_food
    global dic_boutique
    global dic_employee
    if name == 'food':
        dic = dic_food
    elif name == 'boutique':
        dic = dic_boutique
    else:
        dic = dic_employee
    total=0
    Label(handler, text=space,font=('Courier', 20)).grid(row=i)
    out_of_stock=[]
    daily_wage=[]
    k=0
    try :
       amount=list(map(lambda e:int(e.get()),amounts))# getting values from list amounts which have entry values of order_format
       for key, val in dic.items():
         if type(val)==int:#daily wage calculated
            daily_wage.append(amount[k]*val)
         else:# dictionary is reset
            new_amount=val[0]-amount[k]
            if new_amount<0:
                out_of_stock.append(key)
         k+=1
       if type(val)==int:# bonus is calculated
         k = 0
         if 1000<=total_sale <1500:
            bonus = 100
         elif 1500 <= total_sale < 3000:
            bonus = 200
         else:
            bonus = 300
         for key, val in dic.items():# displaying daily wages
            Label(handler, text=f"Today's wage of {key} is {daily_wage[k]} with bonus of {bonus}", font=('Courier', 20)).grid(row=i)
            k += 1
            i += 1
       else:
         if len(out_of_stock)!=0:# out of stock elements are displayed
                      Label(handler, text=f"Sorry your {' '.join([element for element in out_of_stock])} are out of stock ", font=('Courier', 20)).grid(row=i)
         else:
            k=0
            for key, val in dic.items():# total sale calculated
                total+=(amount[k])*val[1]
                val[0]-=amount[k]
                k+=1
            total_sale += total
            if total>=10000 :
                    Label(handler, text=f"Your total bill is :{total}.Dozen Samosas will be given free.", font=('Courier', 20)).grid(row=i)
                    if dic_food['SAMOSAS'][0]-12>=0:# free samosas when having sale of 10000 in boutique
                        dic_food['SAMOSAS'][0] -= 12
                        Label(handler, text=f"Your total bill is :{total}.Dozen Samosas will be given free.",font=('Courier', 20)).grid(row=i)
                    else:# when total is greater than 10000, but dozen samosas are not available
                        Label(handler, text=f"Your total bill is :{total}.Dozen Samosas are not available, first Restock.",font=('Courier', 20)).grid(row=i)
            else:# total bill displayed of boutique and food
                Label(handler, text=f"Your total bill is :{total}.", font=('Courier', 20)).grid(row=i)
            showstock(handler,name,space)
    except:# invalid entry is given
              Label(handler, text=space, font=("Courier", 20)).grid(row=i, sticky=W)
              Label(handler, text=f"Enter Valid value.", font=('Courier', 20)).grid(row=i)
def Done(name,amounts,space,handler,i): # button done is pressed, stock is changed
   try:
    amount=list(map(lambda e:int(e.get()),amounts)) # get entry of list amounts taken in function restock
    global dic_food
    global dic_boutique
    global dic_employee
    if name == 'food':
        dic = dic_food
    elif name == 'boutique':
        dic = dic_boutique
    else:
        dic = dic_employee
    k=0
    for key,val in dic.items(): #adjusting stock
        val[0]+=amount[k]
        k+=1
    showstock(handler,name,space)# shows changed stock
    Label(handler, text=space, font=("Courier", 20)).grid(row=i, sticky=W)
    Label(handler, text=f"Menu Changed", font=('Courier', 20)).grid(row=i)
   except:# invalid entry is given
       Label(handler, text=space, font=("Courier", 20)).grid(row=i, sticky=W)
       Label(handler, text=f"Enter Valid value.", font=('Courier', 20)).grid(row=i)
def Restock(handler,i,name,space): # restocking
    global dic_food
    global dic_boutique
    global dic_employee
    if name == 'food':
        dic = dic_food
    elif name == 'boutique':
        dic = dic_boutique
    else:
        dic = dic_employee
    i+=3
    amounts=[]
    for key,val in dic.items(): # taking entries
        Label(handler, text=f"We have {val[0]} {key}", font=('Courier', 20)).grid(row=i, sticky=W)
        Label(handler, text=f"How much you want to restock?", font=('Courier', 20)).grid(row=i+1,sticky=W)
        e = Entry(handler, width=5,font=('Courier', 20))
        e.grid(row=i+1,column=0)
        amounts.append(e)
        i += 2
    Button(handler, text="Done", command=lambda:Done(name,amounts,space,handler,i),font=("Courier", 20)).grid(row=i+1 , column=0)# amounts is list of entries
def order_format(handler,i,name,space,b):# whole format is designed buttons called
     try:
       b.destroy()# when click to order button is pressed, restock button is destroyed
     except:
       pass
     global dic_food
     global dic_boutique
     global dic_employee
     if name == 'food':
         dic = dic_food
     elif name=='boutique':
         dic=dic_boutique
     else:
         dic=dic_employee
     amounts=[]
     i+=2
     for j in range(i,i+15):
         Label(handler, text=space, font=("Courier", 20)).grid(row=j, sticky=W)
     for key,val in dic.items():
         Label(handler, text=space, font=("Courier", 20)).grid(row=i, sticky=W)
         if type(val)==int:
              Label(handler, text=f"Today's working hour of {key} is :", font=('Courier', 20)).grid(row=i, sticky=W)
         else:
              Label(handler,text=f"How many {key} you want?",font=('Courier',20)).grid(row=i,sticky=W)
         e=Entry(handler,width=5,font=('Courier',20))
         e.grid(row=i)
         amounts.append(e)
         i+=1
     if type(val)==int:
        Button(handler, text="Calculate Daily Wage.", command=lambda: calculate_bill(handler, amounts, i, name, space),font=("Courier", 20)).grid(row=i + 4, column=0)
     else:
         Button(handler, text="Calculate Bill", command=lambda: calculate_bill(handler, amounts,i,name,space), font=("Courier", 20)).grid(row=i + 1, column=0)
         Button(handler, text="RESTOCK", width=0,command=lambda: Restock(handler, i, name,space), font=("Courier", 20)).grid(row=i + 2,column=0)
def food(): #new interface food is created
    f=Tk()
    f.title('FOOD')
    space='                                                                                           '
    i=showstock(f,'food',space)# food is name, to identify which global dictionary should be used
    b=Button(f, text="RESTOCK", command=lambda: Restock(f, i, 'food',space), font=("Courier", 20))# i is the position of row, f is handler, space is to overwrite a statement
    Button(f,text="Click to order",command=lambda:order_format(f,i,'food',space,b),font=("Courier",20)).grid(row=i+1,column=0)
    b.grid(row=i+2,column=0)
def boutique(): #new interface food is created
    bou=Tk()
    bou.title('BOUTIQUE')
    space='                                                                                           '
    i=showstock(bou,'boutique',space)
    i+=1
    b=Button(bou, text="RESTOCK", command=lambda: Restock(bou, i, 'boutique',space), font=("Courier", 20))
    Button(bou,text="Click to order",command=lambda:order_format(bou,i,'boutique',space,b),font=("Courier",20)).grid(row=i,column=0)
    i+=1
    b.grid(row=i,column=0)
def employee(): #new interface food is created
    emp=Tk()
    emp.title('EMPLOYEE')
    space='                                                                                             '
    i=showstock(emp,'employee',space)
    i+=1
    total = Button(emp,text="Click to Calculate daily wage",command=lambda:order_format(emp,i,'employee',space,b),font=("Courier",20)).grid(row=i,column=0)
# Main code starts
from tkinter import *
r=Tk()
r.title('My Bake Shop')
heading=Label(r,text='WELCOME TO MY BAKE SHOP',width=40,font=("Courier", 44),relief=GROOVE).grid(row=0,column=0)
choice=Label(r,text='Select your choice:',font=("Courier",22)).grid(row=1,column=0)
dic_food={'SAMOSAS':[50,20],'ROLLS':[50,25],'CUPCAKES':[50,30]}                    #
dic_boutique = {'TROUSERS': [50, 200], 'SHIRTS': [50, 500], 'SCARFS': [50, 150]}   # three dictionaries which will be globally used later
dic_employee = {'Ahmed': 200, 'Ali': 100, 'Abdullah': 300}                         #
choices={'FOOD':[food,2],'BOUTIQUE':[boutique,3],'EMPLOYEE':[employee,4]}
total_sale=0
for key,val in choices.items():
    b=Button(r,text=key,command=val[0],font=("Courier",50)).grid(row=val[1],column=0) # creating three interfaces
r.mainloop()
