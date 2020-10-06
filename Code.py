from Tkinter import *
import random
import time
import datetime
import tkMessageBox

root=Tk()
root.geometry("1280x800+0+0")
root.title("Restaurent Management Syatem")
root.configure(background='black')
#Total main frame
Tops=Frame(root,width=1350,height=100,bd=14,relief="raise")
Tops.pack(side=TOP)
#Total main frame

#main left frame
f1=Frame(root,width=900,height=650,bd=8,relief="raise")
f1.pack(side=LEFT)
#left top frame
f1a=Frame(f1,width=900,height=330,bd=8,relief="raise")
f1a.pack(side=TOP)
#left top left frame
f1aa=Frame(f1a,width=450,height=330,bd=16,relief="raise")
f1aa.pack(side=LEFT)
#left top right frame
f1ab=Frame(f1a,width=450,height=320,bd=16,relief="raise")
f1ab.pack(side=RIGHT)
#left bottom frame
f2a=Frame(f1,width=900,height=320,bd=6,relief="raise")
f2a.pack(side=BOTTOM)
#left bottom left frame
f2aa=Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2aa.pack(side=LEFT)
#left bottom right frame
f2ab=Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2ab.pack(side=RIGHT)

#main right frame
f2=Frame(root,width=440,height=650,bd=8,relief="raise")
f2.pack(side=RIGHT)
#right top frame
ft2=Frame(f2,width=440,height=450,bd=12,relief="raise")
ft2.pack(side=TOP)
#right bottom frame
fb2=Frame(f2,width=440,height=300,bd=16,relief="raise")
fb2.pack(side=BOTTOM)

Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')

#main header name
lblInfo=Label(Tops,font=('arial',60,'bold'),text="   Restaurent Management System    ", bd=10)
lblInfo.grid(row=0,column=0)

#exit function
def qExit():
        qExit=tkMessageBox.askyesno("Quit System","Do you want to exit?")
        if(qExit>0):
            root.destroy()
            return

#reset function
def qReset():
        PaidTax.set("")
        SubTotal.set("")
        TotalCost.set("")
        CostOfBeverages.set("")
        CostOfFoods.set("")
        ServiceCharge.set("")
        txtReceipt.delete("1.0",END)

        E_Burger.set("0")   
        E_Pizza.set("0")
        E_Sandwich.set("0")
        E_Pasta.set("0")
        E_Fries.set("0")
        E_Nachos.set("0")
        E_Soup.set("0")
        E_Salad.set("0")
        E_Coffee.set("0")
        E_Tea.set("0")
        E_Mojito.set("0")
        E_Shake.set("0")
        E_Lemondae.set("0")
        E_Coke.set("0")
        E_Soda.set("0")
        E_Juice.set("0")

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)

        txtBurger.configure(state="disabled")
        txtPizza.configure(state="disabled")   
        txtSandwich.configure(state="disabled")
        txtPasta.configure(state="disabled")
        txtFries.configure(state="disabled")
        txtNachos.configure(state="disabled")
        txtSoup.configure(state="disabled")
        txtSalad.configure(state="disabled")
        txtCoffee.configure(state="disabled")
        txtTea.configure(state="disabled")   
        txtMojito.configure(state="disabled")
        txtShake.configure(state="disabled")
        txtLemondae.configure(state="disabled")
        txtCoke.configure(state="disabled")
        txtSoda.configure(state="disabled")
        txtJuice.configure(state="disabled")

#check function
def chkButton():
        if(var1.get()==1):
            txtBurger.configure(state="normal")
        elif(var1.get()==0):
            txtBurger.configure(state="disabled")
            E_Burger.set("0")

        if(var2.get()==1):
            txtPizza.configure(state="normal")
        elif(var2.get()==0):
            txtPizza.configure(state="disabled")
            E_Pizza.set("0")

        if(var3.get()==1):
            txtSandwich.configure(state="normal")
        elif(var3.get()==0):
            txtSandwich.configure(state="disabled")
            E_Sandwich.set("0")

        if(var4.get()==1):
            txtPasta.configure(state="normal")
        elif(var4.get()==0):
            txtPasta.configure(state="disabled")
            E_Pasta.set("0")

        if(var5.get()==1):
            txtFries.configure(state="normal")
        elif(var5.get()==0):
            txtFries.configure(state="disabled")
            E_Fries.set("0")

        if(var6.get()==1):
            txtNachos.configure(state="normal")
        elif(var6.get()==0):
            txtNachos.configure(state="disabled")
            E_Nachos.set("0")

        if(var7.get()==1):
            txtSoup.configure(state="normal")
        elif(var6.get()==0):
            txtSoup.configure(state="disabled")
            E_Soup.set("0")

        if(var8.get()==1):
            txtSalad.configure(state="normal")
        elif(var6.get()==0):
            txtSalad.configure(state="disabled")
            E_Salad.set("0")

        if(var9.get()==1):
            txtCoffee.configure(state="normal")
        elif(var6.get()==0):
            txtCoffee.configure(state="disabled")
            E_Coffee.set("0")

        if(var10.get()==1):
            txtTea.configure(state="normal")
        elif(var6.get()==0):
            txtTea.configure(state="disabled")
            E_Tea.set("0")

        if(var11.get()==1):
            txtMojito.configure(state="normal")
        elif(var6.get()==0):
            txtMojito.configure(state="disabled")
            E_Mojito.set("0")

        if(var12.get()==1):
            txtShake.configure(state="normal")
        elif(var6.get()==0):
            txtShake.configure(state="disabled")
            E_Shake.set("0")

        if(var13.get()==1):
            txtLemondae.configure(state="normal")
        elif(var6.get()==0):
            txtLemondae.configure(state="disabled")
            E_Lemondae.set("0")

        if(var14.get()==1):
            txtCoke.configure(state="normal")
        elif(var6.get()==0):
            txtCoke.configure(state="disabled")
            E_Coke.set("0")

        if(var15.get()==1):
            txtSoda.configure(state="normal")
        elif(var6.get()==0):
            txtSoda.configure(state="disabled")
            E_Soda.set("0")

        if(var16.get()==1):
            txtJuice.configure(state="normal")
        elif(var6.get()==0):
            txtJuice.configure(state="disabled")
        E_Juice.set("0") 

#calculate function
def CostOfItem():
    Item1=float(E_Burger.get())
    Item2=float(E_Pizza.get())
    Item3=float(E_Sandwich.get())
    Item4=float(E_Pasta.get())
    Item5=float(E_Fries.get())  
    Item6=float(E_Nachos.get())
    Item7=float(E_Soup.get())
    Item8=float(E_Salad.get())
    Item9=float(E_Coffee.get())
    Item10=float(E_Tea.get())   
    Item11=float(E_Mojito.get())
    Item12=float(E_Shake.get())
    Item13=float(E_Lemondae.get())
    Item14=float(E_Coke.get())
    Item15=float(E_Soda.get())
    Item16=float(E_Juice.get())

    PriceOfBeverages=(Item1*2)+(Item2*2)+(Item3*2)+(Item4*2)+(Item5*2)+(Item6*2)+(Item7*2)+(Item8*2)
    PriceOfFoods=(Item9*2)+(Item10*2)+(Item11*2)+(Item12*2)+(Item13*2)+(Item14*2)+(Item15*2)+(Item16*2)        

    BeveragesPrice="$"+str('%.2f'%(PriceOfBeverages))
    FoodsPrice="$"+str('%.2f'%(PriceOfFoods))

    CostOfBeverages.set(BeveragesPrice)
    CostOfFoods.set(FoodsPrice)

    SC="$"+str('%.2f'%(1.59))
    ServiceCharge.set(SC)

    #mention calculation of tax
    subTotal1="$"+str('%.2f'%(PriceOfBeverages+PriceOfFoods+1.59))
    SubTotal.set(subTotal1)

    Tax="$"+str('%.2f'%((PriceOfBeverages+PriceOfFoods+1.59)*0.15))
    PaidTax.set(Tax);     

    TT=((PriceOfBeverages+PriceOfFoods+1.59)*0.15)

    TC="$"+str('%.2f'%(PriceOfBeverages+PriceOfFoods+1.59+TT))
    TotalCost.set(TC)

def receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(100898,6812789)
    randomRef=str(x)
    Receipt_Ref.set("Bill"+randomRef)
    txtReceipt.insert(END,'Burger\t\t\t'+str(E_Burger.get()) +"\n")
    txtReceipt.insert(END,'Pizza\t\t\t'+str(E_Pizza.get()) +"\n")
    txtReceipt.insert(END,'Sandwich\t\t\t'+str(E_Sandwich.get()) +"\n")
    txtReceipt.insert(END,'Pasta\t\t\t'+str(E_Pasta.get()) +"\n")
    txtReceipt.insert(END,'Fries\t\t\t'+str(E_Fries.get()) +"\n")
    txtReceipt.insert(END,'Nachos\t\t\t'+str(E_Nachos.get()) +"\n")
    txtReceipt.insert(END,'Soup\t\t\t'+str(E_Soup.get()) +"\n")
    txtReceipt.insert(END,'Salad\t\t\t'+str(E_Salad.get()) +"\n")
    txtReceipt.insert(END,'Coffee\t\t\t'+str(E_Coffee.get()) +"\n")
    txtReceipt.insert(END,'Tea\t\t\t'+str(E_Tea.get()) +"\n")
    txtReceipt.insert(END,'Mojito\t\t\t'+str(E_Mojito.get()) +"\n")
    txtReceipt.insert(END,'Shake\t\t\t'+str(E_Shake.get()) +"\n")
    txtReceipt.insert(END,'Lemondae\t\t\t'+str(E_Lemondae.get()) +"\n")
    txtReceipt.insert(END,'Coke\t\t\t'+str(E_Coke.get()) +"\n")
    txtReceipt.insert(END,'Soda\t\t\t'+str(E_Soda.get()) +"\n")
    txtReceipt.insert(END,'Juice\t\t\t'+str(E_Juice.get()) +"\n")
    txtReceipt.insert(END,'Cost Of Foods\t\t\t'+str(CostOfFoods.get()) +"\n")
    txtReceipt.insert(END,'Cost Of Beverages\t\t\t'+str(CostOfBeverages.get()) +"\n")
    txtReceipt.insert(END,'Tax Paid:\t\t\t'+PaidTax.get() +"\n")
    txtReceipt.insert(END,'Service Charge:\t\t\t'+ServiceCharge.get() +"\n")
    txtReceipt.insert(END,'Total Cost:\t\t\t'+TotalCost.get() +"\n")

var1=IntVar()   
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar() 

DateofOrder=StringVar()
DateofOrder.set(time.strftime("%d/%m/%y"))
Receipt=StringVar()
PaidTax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostOfBeverages=StringVar()
CostOfFoods=StringVar()
ServiceCharge=StringVar()
Receipt_Ref=StringVar()

#food input
E_Burger=IntVar()
E_Pizza=IntVar()
E_Sandwich=IntVar()
E_Pasta=IntVar()
E_Fries=IntVar()
E_Nachos=IntVar()
E_Soup=IntVar()
E_Salad=IntVar()
E_Burger.set("0")
E_Pizza.set("0")
E_Sandwich.set("0")
E_Pasta.set("0")
E_Fries.set("0")
E_Nachos.set("0")
E_Soup.set("0")
E_Salad.set("0")

#beverage input
E_Coffee=IntVar()
E_Tea=IntVar()
E_Mojito=IntVar()
E_Shake=IntVar()
E_Lemondae=IntVar()
E_Coke=IntVar()
E_Soda=IntVar()
E_Juice=IntVar()
E_Coffee.set("0")
E_Tea.set("0")
E_Mojito.set("0")
E_Shake.set("0")
E_Lemondae.set("0")
E_Coke.set("0")
E_Soda.set("0")
E_Juice.set("0")

#left foods side
Burger=Checkbutton(f1aa,text="Burger\t",variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=0,sticky=W)
Pizza=Checkbutton(f1aa,text="Pizza\t",variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=1,sticky=W)
Sandwich=Checkbutton(f1aa,text="Sandwich\t",variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=2,sticky=W)
Pasta=Checkbutton(f1aa,text="Pasta\t",variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=3,sticky=W)
Fries=Checkbutton(f1aa,text="Fries\t",variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=4,sticky=W)
Nachos=Checkbutton(f1aa,text="Nachos\t",variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=5,sticky=W)
Soup=Checkbutton(f1aa,text="Soup\t",variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=6,sticky=W)
Salad=Checkbutton(f1aa,text="Salad\t",variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=7,sticky=W)  
#left food enter side
txtBurger=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Burger,justify='left',state='disabled')  
txtBurger.grid(row=0,column=1)
txtPizza=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Pizza,justify='left',state='disabled')  
txtPizza.grid(row=1,column=1)
txtSandwich=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Sandwich,justify='left',state='disabled')  
txtSandwich.grid(row=2,column=1)
txtPasta=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Pasta,justify='left',state='disabled')  
txtPasta.grid(row=3,column=1)
txtFries=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Fries,justify='left',state='disabled')  
txtFries.grid(row=4,column=1)
txtNachos=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Nachos,justify='left',state='disabled')  
txtNachos.grid(row=5,column=1)
txtSoup=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Soup,justify='left',state='disabled')  
txtSoup.grid(row=6,column=1)
txtSalad=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Salad,justify='left',state='disabled')  
txtSalad.grid(row=7,column=1)
#right beverage side
Coffee=Checkbutton(f1ab,text="Coffee\t",variable=var9,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=0,sticky=W)
Tea=Checkbutton(f1ab,text="Tea\t",variable=var10,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=1,sticky=W)
Mojito=Checkbutton(f1ab,text="Mojito\t",variable=var11,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=2,sticky=W)
Shake=Checkbutton(f1ab,text="Shake\t",variable=var12,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=3,sticky=W)
Lemondae=Checkbutton(f1ab,text="Lemondae\t",variable=var13,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=4,sticky=W)
Coke=Checkbutton(f1ab,text="Coke\t",variable=var14,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=5,sticky=W)
Soda=Checkbutton(f1ab,text="Soda\t",variable=var15,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=6,sticky=W)
Juice=Checkbutton(f1ab,text="Juice\t",variable=var16,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=chkButton).grid(row=7,sticky=W)  
#right beverage enter side
txtCoffee=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Coffee,justify='left',state='disabled')  
txtCoffee.grid(row=0,column=1)
txtTea=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Tea,justify='left',state='disabled')  
txtTea.grid(row=1,column=1)
txtMojito=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Mojito,justify='left',state='disabled')  
txtMojito.grid(row=2,column=1)
txtShake=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Shake,justify='left',state='disabled')  
txtShake.grid(row=3,column=1)
txtLemondae=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Lemondae,justify='left',state='disabled')  
txtLemondae.grid(row=4,column=1)
txtCoke=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Coke,justify='left',state='disabled')  
txtCoke.grid(row=5,column=1)
txtSoda=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Soda,justify='left',state='disabled')  
txtSoda.grid(row=6,column=1)
txtJuice=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=15,textvariable=E_Juice,justify='left',state='disabled')  
txtJuice.grid(row=7,column=1)
#for Receipt Frame
lblReceipt=Label(ft2,font=('arial',12,'bold'),text="Restaurant Receipt",bd=2)
lblReceipt.grid(row=0,column=0,sticky=W)
txtReceipt=Text(ft2,font=('arial',11,'bold'),bd=8,width=40)
txtReceipt.grid(row=1,column=0)
#cost of item information
lblCostOfFoods=Label(f2aa,font=('arial',16,'bold'),text="Enter the Amount Per Cost of Foods:",bd=8)
lblCostOfFoods.grid(row=0,column=0,sticky=W)
txtCostOfFoods=Entry(f2aa,font=('arial',16,'bold'),bd=6,width=12,justify='left',textvariable=CostOfFoods)
txtCostOfFoods.grid(row=0,column=1,sticky=W)
lblCostOfBeverages=Label(f2aa,font=('arial',16,'bold'),text="Enter the Amount Per Cost of Beverages:",bd=8)
lblCostOfBeverages.grid(row=1,column=0,sticky=W)
txtCostOfBeverages=Entry(f2aa,font=('arial',16,'bold'),bd=7,width=12,justify='left',textvariable=CostOfBeverages)
txtCostOfBeverages.grid(row=1,column=1,sticky=W)
lblCostofserviceCharge=Label(f2aa,font=('arial',16,'bold'),text="Service Charge",bd=8)
lblCostofserviceCharge.grid(row=2,column=0,sticky=W)
txtCostofserviceCharge=Entry(f2aa,font=('arial',16,'bold'),bd=6,width=12,justify='left',textvariable=ServiceCharge)
txtCostofserviceCharge.grid(row=2,column=1,sticky=W)
#payment Information
lblCostofTax=Label(f2ab,font=('arial',16,'bold'),text="Enter tax Percentage:",bd=8)
lblCostofTax.grid(row=0,column=0,sticky=W)
txtCostofTax=Entry(f2ab,font=('arial',16,'bold'),bd=6,width=12,justify='left',textvariable=PaidTax)
txtCostofTax.grid(row=0,column=1,sticky=W)
lblCostofSubTotal=Label(f2ab,font=('arial',16,'bold'),text="Sub Total:",bd=8)
lblCostofSubTotal.grid(row=1,column=0,sticky=W)
txtCostofSubTotal=Entry(f2ab,font=('arial',16,'bold'),bd=7,width=12,justify='left',textvariable=SubTotal)
txtCostofSubTotal.grid(row=1,column=1,sticky=W)
lblCostofTotal=Label(f2ab,font=('arial',16,'bold'),text="Total",bd=8)
lblCostofTotal.grid(row=2,column=0,sticky=W)
txtCostofTotal=Entry(f2ab,font=('arial',16,'bold'),bd=6,width=12,justify='left',textvariable=TotalCost)
txtCostofTotal.grid(row=2,column=1,sticky=W)
#Bottom Total payment right corner down frame
btnTotal=Button(fb2,padx=25,pady=25,bd=2,fg="black",font=('arial',10,'bold'),width=1,text="Total",command=CostOfItem).grid(row=0,column=0)
btnReceipt=Button(fb2,padx=25,pady=25,bd=2,fg="black",font=('arial',10,'bold'),width=1,text="Receipt",command=receipt).grid(row=0,column=1)
btnReset=Button(fb2,padx=25,pady=25,bd=2,fg="black",font=('arial',10,'bold'),width=1,text="Reset",command=qReset).grid(row=0,column=2)
btnExit=Button(fb2,padx=25,pady=25,bd=2,fg="black",font=('arial',10,'bold'),width=1,text="Exit",command=qExit).grid(row=0,column=3)

root.mainloop()
