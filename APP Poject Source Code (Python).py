from tkinter import *
from tkinter import filedialog, messagebox
import random
import time


# Functions
def reset():
    textReceipt.delete(1.0, END)
    e_daal.set('0')
    e_roti.set('0')
    e_sabji.set('0')
    e_fish.set('0')
    e_kebab.set('0')
    e_chawal.set('0')
    e_mutton.set('0')
    e_paneer.set('0')
    e_chicken.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_roohafza.set('0')
    e_shikanji.set('0')
    e_jaljeera.set('0')
    e_masalatea.set('0')
    e_badammilk.set('0')
    e_coldrinks.set('0')

    e_kitkat.set('0')
    e_oreo.set('0')
    e_apple.set('0')
    e_vanilla.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_chocolate.set('0')
    e_blackforest.set('0')

    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textkebab.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textchawal.config(state=DISABLED)

    textlassi.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textjaljeera.config(state=DISABLED)
    textroohafza.config(state=DISABLED)
    textshikanji.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    textmasalatea.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textcolddrinks.config(state=DISABLED)

    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textblackforest.config(state=DISABLED)

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
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')


def save():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if url == None:
            pass
        else:

            bill_data = textReceipt.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information', 'Your Bill Is Succesfully Saved')


def receipt():
    global billnumber, date
    if costoffoodvar.get() != '' or costofcakesvar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0, END)
        x = random.randint(100, 10000)
        billnumber = 'BILL' + str(x)
        date = time.strftime('%d/%m/%Y')
        textReceipt.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n')
        textReceipt.insert(END, '*******\n')
        textReceipt.insert(END, 'Items:\t\t Cost Of Items(Rs)\n')
        textReceipt.insert(END, '*******\n')
        if e_roti.get() != '0':
            textReceipt.insert(END, f'Roti\t\t\t{int(e_roti.get()) * 10}\n\n')

        if e_daal.get() != '0':
            textReceipt.insert(END, f'Daal\t\t\t{int(e_daal.get()) * 60}\n\n')

        if e_fish.get() != '0':
            textReceipt.insert(END, f'Fish\t\t\t{int(e_fish.get()) * 100}\n\n')

        if e_chawal.get() != '0':
            textReceipt.insert(END, f'Chawal:\t\t\t{int(e_chawal.get()) * 30}\n\n')

        if e_sabji.get() != '0':
            textReceipt.insert(END, f'Sabji:\t\t\t{int(e_sabji.get()) * 50}\n\n')

        if e_paneer.get() != '0':
            textReceipt.insert(END, f'Paneer:\t\t\t{int(e_paneer.get()) * 100}\n\n')

        if e_kebab.get() != '0':
            textReceipt.insert(END, f'Kebab:\t\t\t{int(e_kebab.get()) * 40}\n\n')

        if e_chicken.get() != '0':
            textReceipt.insert(END, f'Chicken:\t\t\t{int(e_chicken.get()) * 120}\n\n')

        if e_mutton.get() != '0':
            textReceipt.insert(END, f'Mutton:\t\t\t{int(e_mutton.get()) * 120}\n\n')

        if e_lassi.get() != '0':
            textReceipt.insert(END, f'Lassi:\t\t\t{int(e_lassi.get()) * 50}\n\n')

        if e_coffee.get() != '0':
            textReceipt.insert(END, f'Coffee:\t\t\t{int(e_coffee.get()) * 40}\n\n')

        if e_faluda.get() != '0':
            textReceipt.insert(END, f'Faluda:\t\t\t{int(e_faluda.get()) * 80}\n\n')

        if e_shikanji.get() != '0':
            textReceipt.insert(END, f'Shikanji:\t\t\t{int(e_shikanji.get()) * 30}\n\n')

        if e_jaljeera.get() != '0':
            textReceipt.insert(END, f'Jaljeera:\t\t\t{int(e_jaljeera.get()) * 40}\n\n')

        if e_roohafza.get() != '0':
            textReceipt.insert(END, f'Roohafza:\t\t\t{int(e_roohafza.get()) * 60}\n\n')

        if e_masalatea.get() != '0':
            textReceipt.insert(END, f'Masala Chai:\t\t\t{int(e_masalatea.get()) * 20}\n\n')

        if e_badammilk.get() != '0':
            textReceipt.insert(END, f'Badam Milk:\t\t\t{int(e_badammilk.get()) * 50}\n\n')

        if e_coldrinks.get() != '0':
            textReceipt.insert(END, f'Cold Drinks:\t\t\t{int(e_coldrinks.get()) * 80}\n\n')

        if e_oreo.get() != '0':
            textReceipt.insert(END, f'Oreo:\t\t\t{int(e_oreo.get()) * 400}\n\n')

        if e_apple.get() != '0':
            textReceipt.insert(END, f'Apple:\t\t\t{int(e_apple.get()) * 300}\n\n')

        if e_kitkat.get() != '0':
            textReceipt.insert(END, f'Kitkat:\t\t\t{int(e_kitkat.get()) * 500}\n\n')

        if e_banana.get() != '0':
            textReceipt.insert(END, f'Banana:\t\t\t{int(e_banana.get()) * 450}\n\n')

        if e_brownie.get() != '0':
            textReceipt.insert(END, f'Brownie:\t\t\t{int(e_brownie.get()) * 800}\n\n')

        if e_pineapple.get() != '0':
            textReceipt.insert(END, f'Pineapple:\t\t\t{int(e_pineapple.get()) * 620}\n\n')

        if e_chocolate.get() != '0':
            textReceipt.insert(END, f'Chocolate:\t\t\t{int(e_chocolate.get()) * 700}\n\n')

        if e_blackforest.get() != '0':
            textReceipt.insert(END, f'Black Forest:\t\t\t{int(e_blackforest.get()) * 550}\n\n')

        if e_vanilla.get() != '0':
            textReceipt.insert(END, f'Vanilla:\t\t\t{int(e_vanilla.get()) * 550}\n\n')

        textReceipt.insert(END, '*******\n')
        if costoffoodvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
        if costofdrinksvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
        if costofcakesvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{10}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems + 10}Rs\n\n')
        textReceipt.insert(END, '*******\n')

    else:
        messagebox.showerror('Error', 'No Item Is selected')


def totalcost():
    global priceofFood, priceofDrinks, priceofCakes, subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
            var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
            var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
            var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
            var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
            var26.get() != 0 or var27.get() != 0:
        item1 = int(e_roti.get())
        item2 = int(e_daal.get())
        item3 = int(e_fish.get())
        item4 = int(e_sabji.get())
        item5 = int(e_kebab.get())
        item6 = int(e_chawal.get())
        item7 = int(e_mutton.get())
        item8 = int(e_paneer.get())
        item9 = int(e_chicken.get())
        item10 = int(e_lassi.get())
        item11 = int(e_coffee.get())
        item12 = int(e_faluda.get())
        item13 = int(e_shikanji.get())
        item14 = int(e_jaljeera.get())
        item15 = int(e_roohafza.get())
        item16 = int(e_masalatea.get())
        item17 = int(e_badammilk.get())
        item18 = int(e_coldrinks.get())
        item19 = int(e_oreo.get())
        item20 = int(e_apple.get())
        item21 = int(e_kitkat.get())
        item22 = int(e_vanilla.get())
        item23 = int(e_banana.get())
        item24 = int(e_brownie.get())
        item25 = int(e_pineapple.get())
        item26 = int(e_chocolate.get())
        item27 = int(e_blackforest.get())
        priceofFood = (item1 * 10) + (item2 * 60) + (item3 * 100) + (item4 * 50) + (item5 * 40) + (item6 * 30) + (
                    item7 * 120) \
                      + (item8 * 100) + (item9 * 120)
        priceofDrinks = (item10 * 50) + (item11 * 40) + (item12 * 80) + (item13 * 30) + (item14 * 40) + (item15 * 60) \
                        + (item16 * 20) + (item17 * 50) + (item18 * 80)
        priceofCakes = (item19 * 400) + (item20 * 300) + (item21 * 500) + (item22 * 550) + (item23 * 450) + (
                    item24 * 800) \
                       + (item25 * 620) + (item26 * 700) + (item27 * 550)
        costoffoodvar.set(str(priceofFood) + ' Rs')
        costofdrinksvar.set(str(priceofDrinks) + ' Rs')
        costofcakesvar.set(str(priceofCakes) + ' Rs')
        subtotalofItems = priceofFood + priceofDrinks + priceofCakes
        subtotalvar.set(str(subtotalofItems) + ' Rs')
        servicetaxvar.set('10 Rs')
        tottalcost = subtotalofItems + 10
        totalcostvar.set(str(tottalcost) + ' Rs')
    else:
        messagebox.showerror('Error', 'No Item Is selected')


def roti():
    if var1.get() == 1:
        textroti.config(state=NORMAL)
        textroti.delete(0, END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')


def daal():
    if var2.get() == 1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0, END)
        textdaal.focus()

    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')


def fish():
    if var3.get() == 1:
        textfish.config(state=NORMAL)
        textfish.delete(0, END)
        textfish.focus()

    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')


def sabji():
    if var4.get() == 1:
        textsabji.config(state=NORMAL)
        textsabji.focus()
        textsabji.delete(0, END)
    elif var4.get() == 0:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')


def kebab():
    if var5.get() == 1:
        textkebab.config(state=NORMAL)
        textkebab.focus()
        textkebab.delete(0, END)
    elif var5.get() == 0:
        textkebab.config(state=DISABLED)
        e_kebab.set('0')


def chawal():
    if var6.get() == 1:
        textchawal.config(state=NORMAL)
        textchawal.focus()
        textchawal.delete(0, END)
    elif var6.get() == 0:
        textchawal.config(state=DISABLED)
        e_chawal.set('0')


def mutton():
    if var7.get() == 1:
        textmutton.config(state=NORMAL)
        textmutton.focus()
        textmutton.delete(0, END)
    elif var7.get() == 0:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')


def paneer():
    if var8.get() == 1:
        textpaneer.config(state=NORMAL)
        textpaneer.focus()
        textpaneer.delete(0, END)
    elif var8.get() == 0:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')


def chicken():
    if var9.get() == 1:
        textchicken.config(state=NORMAL)
        textchicken.focus()
        textchicken.delete(0, END)
    elif var9.get() == 0:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')


def lassi():
    if var10.get() == 1:
        textlassi.config(state=NORMAL)
        textlassi.focus()
        textlassi.delete(0, END)
    elif var10.get() == 0:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')


def coffee():
    if var11.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.focus()
        textcoffee.delete(0, END)
    elif var11.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')


def faluda():
    if var12.get() == 1:
        textfaluda.config(state=NORMAL)
        textfaluda.focus()
        textfaluda.delete(0, END)
    elif var12.get() == 0:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')


def shikanji():
    if var13.get() == 1:
        textshikanji.config(state=NORMAL)
        textshikanji.focus()
        textshikanji.delete(0, END)
    elif var13.get() == 0:
        textshikanji.config(state=DISABLED)
        e_shikanji.set('0')


def jaljeera():
    if var14.get() == 1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.focus()
        textjaljeera.delete(0, END)
    elif var14.get() == 0:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')


def roohafza():
    if var15.get() == 1:
        textroohafza.config(state=NORMAL)
        textroohafza.focus()
        textroohafza.delete(0, END)
    elif var15.get() == 0:
        textroohafza.config(state=DISABLED)
        e_roohafza.set('0')


def masalatea():
    if var16.get() == 1:
        textmasalatea.config(state=NORMAL)
        textmasalatea.focus()
        textmasalatea.delete(0, END)
    elif var16.get() == 0:
        textmasalatea.config(state=DISABLED)
        e_masalatea.set('0')


def badammilk():
    if var17.get() == 1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.focus()
        textbadammilk.delete(0, END)
    elif var17.get() == 0:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')


def colddrinks():
    if var18.get() == 1:
        textcolddrinks.config(state=NORMAL)
        textcolddrinks.focus()
        textcolddrinks.delete(0, END)
    elif var18.get() == 0:
        textcolddrinks.config(state=DISABLED)
        e_coldrinks.set('0')


def oreo():
    if var19.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.focus()
        textoreo.delete(0, END)
    elif var19.get() == 0:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')


def apple():
    if var20.get() == 1:
        textapple.config(state=NORMAL)
        textapple.focus()
        textapple.delete(0, END)
    elif var20.get() == 0:
        textapple.config(state=DISABLED)
        e_apple.set('0')


def kitkat():
    if var21.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.focus()
        textkitkat.delete(0, END)
    elif var21.get() == 0:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')


def vanilla():
    if var22.get() == 1:
        textvanilla.config(state=NORMAL)
        textvanilla.focus()
        textvanilla.delete(0, END)
    elif var22.get() == 0:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')


def banana():
    if var23.get() == 1:
        textbanana.config(state=NORMAL)
        textbanana.focus()
        textbanana.delete(0, END)
    elif var23.get() == 0:
        textbanana.config(state=DISABLED)
        e_banana.set('0')


def brownie():
    if var24.get() == 1:
        textbrownie.config(state=NORMAL)
        textbrownie.focus()
        textbrownie.delete(0, END)
    elif var24.get() == 0:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')


def pineapple():
    if var25.get() == 1:
        textpineapple.config(state=NORMAL)
        textpineapple.focus()
        textpineapple.delete(0, END)
    elif var25.get() == 0:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')


def chocolate():
    if var26.get() == 1:
        textchocolate.config(state=NORMAL)
        textchocolate.focus()
        textchocolate.delete(0, END)
    elif var26.get() == 0:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')


def blackforest():
    if var27.get() == 1:
        textblackforest.config(state=NORMAL)
        textblackforest.focus()
        textblackforest.delete(0, END)
    elif var27.get() == 0:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')


root = Tk()
root.geometry('1270x690+0+0')
root.resizable(0, 0)
root.title('VDR DELIGHT')

root.config(bg='slateblue2')

topFrame = Frame(root, bd=10, relief=RIDGE, bg='green')
topFrame.pack(side=TOP)

labelTitle = Label(topFrame, text='VDR DELIGHT', font=('arial', 30, 'bold'), fg='lavender', bd=9,
                   bg='hotpink', width=51)
labelTitle.grid(row=0, column=0)

# frames

menuFrame = Frame(root, bd=10, relief=RIDGE, bg='blue')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame, bd=4, relief=RIDGE, bg='hotpink', pady=10)
costFrame.pack(side=BOTTOM)

foodFrame = LabelFrame(menuFrame, text='Food', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='hot pink', )
foodFrame.pack(side=LEFT)

drinksFrame = LabelFrame(menuFrame, text='Drinks', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='hotpink')
drinksFrame.pack(side=LEFT)

cakesFrame = LabelFrame(menuFrame, text='Cakes', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='hotpink')
cakesFrame.pack(side=LEFT)

rightFrame = Frame(root, bd=15, relief=RIDGE, bg='hotpink')
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame, bd=1, relief=RIDGE, bg='hotpink')
calculatorFrame.pack()

recieptFrame = Frame(rightFrame, bd=4, relief=RIDGE, bg='hotpink')
recieptFrame.pack()

buttonFrame = Frame(rightFrame, bd=3, relief=RIDGE, bg='hotpink')
buttonFrame.pack()

# Variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_roti = StringVar()
e_daal = StringVar()
e_sabji = StringVar()
e_chawal = StringVar()
e_fish = StringVar()
e_mutton = StringVar()
e_kebab = StringVar()
e_chicken = StringVar()
e_paneer = StringVar()

e_lassi = StringVar()
e_coffee = StringVar()
e_faluda = StringVar()
e_shikanji = StringVar()
e_roohafza = StringVar()
e_jaljeera = StringVar()
e_masalatea = StringVar()
e_badammilk = StringVar()
e_coldrinks = StringVar()

e_oreo = StringVar()
e_kitkat = StringVar()
e_vanilla = StringVar()
e_apple = StringVar()
e_blackforest = StringVar()
e_banana = StringVar()
e_brownie = StringVar()
e_pineapple = StringVar()
e_chocolate = StringVar()

costoffoodvar = StringVar()
costofdrinksvar = StringVar()
costofcakesvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()

e_roti.set('0')
e_daal.set('0')
e_sabji.set('0')
e_fish.set('0')
e_kebab.set('0')
e_chawal.set('0')
e_mutton.set('0')
e_chicken.set('0')
e_paneer.set('0')

e_lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_roohafza.set('0')
e_shikanji.set('0')
e_jaljeera.set('0')
e_masalatea.set('0')
e_badammilk.set('0')
e_coldrinks.set('0')

e_kitkat.set('0')
e_banana.set('0')
e_pineapple.set('0')
e_apple.set('0')
e_chocolate.set('0')
e_oreo.set('0')
e_blackforest.set('0')
e_brownie.set('0')
e_vanilla.set('0')

##FOOD

roti = Checkbutton(foodFrame, text='Roti', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var1
                   , command=roti)
roti.grid(row=0, column=0, sticky=W)

daal = Checkbutton(foodFrame, text='Daal', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var2
                   , command=daal)
daal.grid(row=1, column=0, sticky=W)

fish = Checkbutton(foodFrame, text='Fish', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var3
                   , command=fish)
fish.grid(row=2, column=0, sticky=W)

sabji = Checkbutton(foodFrame, text='Curry', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var4
                    , command=sabji)
sabji.grid(row=3, column=0, sticky=W)

kebab = Checkbutton(foodFrame, text='kebab', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var5
                    , command=kebab)
kebab.grid(row=4, column=0, sticky=W)

chawal = Checkbutton(foodFrame, text='Rice', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var6
                     , command=chawal)
chawal.grid(row=5, column=0, sticky=W)

mutton = Checkbutton(foodFrame, text='Mutton', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var7,
                     command=mutton)
mutton.grid(row=6, column=0, sticky=W)

paneer = Checkbutton(foodFrame, text='Paneer', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var8
                     , command=paneer)
paneer.grid(row=7, column=0, sticky=W)

chicken = Checkbutton(foodFrame, text='Chicken', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var9
                      , command=chicken)
chicken.grid(row=8, column=0, sticky=W)

# Entry Fields for Food Items

textroti = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_roti)
textroti.grid(row=0, column=1)

textdaal = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_daal)
textdaal.grid(row=1, column=1)

textfish = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_fish)
textfish.grid(row=2, column=1)

textsabji = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sabji)
textsabji.grid(row=3, column=1)

textkebab = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kebab)
textkebab.grid(row=4, column=1)

textchawal = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chawal)
textchawal.grid(row=5, column=1)

textmutton = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_mutton)
textmutton.grid(row=6, column=1)

textpaneer = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_paneer)
textpaneer.grid(row=7, column=1)

textchicken = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken)
textchicken.grid(row=8, column=1)

# Drinks

lassi = Checkbutton(drinksFrame, text='Lassi', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var10
                    , command=lassi)
lassi.grid(row=0, column=0, sticky=W)

coffee = Checkbutton(drinksFrame, text='Coffee', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var11
                     , command=coffee)
coffee.grid(row=1, column=0, sticky=W)

faluda = Checkbutton(drinksFrame, text='Faluda', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var12
                     , command=faluda)
faluda.grid(row=2, column=0, sticky=W)

shikanji = Checkbutton(drinksFrame, text='Shikanji', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var13
                       , command=shikanji)
shikanji.grid(row=3, column=0, sticky=W)

jaljeera = Checkbutton(drinksFrame, text='Jaljeera', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var14
                       , command=jaljeera)
jaljeera.grid(row=4, column=0, sticky=W)

roohafza = Checkbutton(drinksFrame, text='Roohafza', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var15
                       , command=roohafza)
roohafza.grid(row=5, column=0, sticky=W)

masalatea = Checkbutton(drinksFrame, text='Masala Tea', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                        variable=var16
                        , command=masalatea)
masalatea.grid(row=6, column=0, sticky=W)

badammilk = Checkbutton(drinksFrame, text='Badam Milk', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                        variable=var17
                        , command=badammilk)
badammilk.grid(row=7, column=0, sticky=W)

colddrinks = Checkbutton(drinksFrame, text='Cold Drinks', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                         variable=var18
                         , command=colddrinks)
colddrinks.grid(row=8, column=0, sticky=W)

# entry fields for drink items

textlassi = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_lassi)
textlassi.grid(row=0, column=1)

textcoffee = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=1, column=1)

textfaluda = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_faluda)
textfaluda.grid(row=2, column=1)

textshikanji = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_shikanji)
textshikanji.grid(row=3, column=1)

textjaljeera = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_jaljeera)
textjaljeera.grid(row=4, column=1)

textroohafza = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_roohafza)
textroohafza.grid(row=5, column=1)

textmasalatea = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_masalatea)
textmasalatea.grid(row=6, column=1)

textbadammilk = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_badammilk)
textbadammilk.grid(row=7, column=1)

textcolddrinks = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coldrinks)
textcolddrinks.grid(row=8, column=1)

# Cakes

oreocake = Checkbutton(cakesFrame, text='Oreo', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var19
                       , command=oreo)
oreocake.grid(row=0, column=0, sticky=W)

applecake = Checkbutton(cakesFrame, text='Apple', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var20
                        , command=apple)
applecake.grid(row=1, column=0, sticky=W)

kitkatcake = Checkbutton(cakesFrame, text='Kitkat', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var21
                         , command=kitkat)
kitkatcake.grid(row=2, column=0, sticky=W)

vanillacake = Checkbutton(cakesFrame, text='Vanilla', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var22
                          , command=vanilla)
vanillacake.grid(row=3, column=0, sticky=W)

bananacake = Checkbutton(cakesFrame, text='Banana', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var23
                         , command=banana)
bananacake.grid(row=4, column=0, sticky=W)

browniecake = Checkbutton(cakesFrame, text='Brownie', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var24
                          , command=brownie)
browniecake.grid(row=5, column=0, sticky=W)

pineapplecake = Checkbutton(cakesFrame, text='Pineapple', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                            variable=var25
                            , command=pineapple)
pineapplecake.grid(row=6, column=0, sticky=W)

chocolatecake = Checkbutton(cakesFrame, text='Chocolate', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                            variable=var26
                            , command=chocolate)
chocolatecake.grid(row=7, column=0, sticky=W)

blackforestcake = Checkbutton(cakesFrame, text='Black Forest', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                              variable=var27
                              , command=blackforest)
blackforestcake.grid(row=8, column=0, sticky=W)

# entry fields for cakes

textoreo = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_oreo)
textoreo.grid(row=0, column=1)

textapple = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_apple)
textapple.grid(row=1, column=1)

textkitkat = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kitkat)
textkitkat.grid(row=2, column=1)

textvanilla = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_vanilla)
textvanilla.grid(row=3, column=1)

textbanana = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_banana)
textbanana.grid(row=4, column=1)

textbrownie = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_brownie)
textbrownie.grid(row=5, column=1)

textpineapple = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pineapple)
textpineapple.grid(row=6, column=1)

textchocolate = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chocolate)
textchocolate.grid(row=7, column=1)

textblackforest = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,
                        textvariable=e_blackforest)
textblackforest.grid(row=8, column=1)

# costlabels & entry fields

labelCostofFood = Label(costFrame, text='Cost of Food', font=('arial', 16, 'bold'), bg='hotpink', fg='white')
labelCostofFood.grid(row=0, column=0)

textCostofFood = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                       textvariable=costoffoodvar)
textCostofFood.grid(row=0, column=1, padx=41)

labelCostofDrinks = Label(costFrame, text='Cost of Drinks', font=('arial', 16, 'bold'), bg='hotpink', fg='white')
labelCostofDrinks.grid(row=1, column=0)

textCostofDrinks = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                         textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1, column=1, padx=41)

labelCostofCakes = Label(costFrame, text='Cost of Cakes', font=('arial', 16, 'bold'), bg='hotpink', fg='white')
labelCostofCakes.grid(row=2, column=0)

textCostofCakes = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                        textvariable=costofcakesvar)
textCostofCakes.grid(row=2, column=1, padx=41)

labelSubTotal = Label(costFrame, text='Sub Total', font=('arial', 16, 'bold'), bg='hotpink', fg='white')
labelSubTotal.grid(row=0, column=2)

textSubTotal = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly', textvariable=subtotalvar)
textSubTotal.grid(row=0, column=3, padx=41)

labelServiceTax = Label(costFrame, text='Service Tax', font=('arial', 16, 'bold'), bg='hotpink', fg='white')
labelServiceTax.grid(row=1, column=2)

textServiceTax = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                       textvariable=servicetaxvar)
textServiceTax.grid(row=1, column=3, padx=41)

labelTotalCost = Label(costFrame, text='Total Cost', font=('arial', 16, 'bold'), bg='hotpink', fg='white')
labelTotalCost.grid(row=2, column=2)

textTotalCost = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                      textvariable=totalcostvar)
textTotalCost.grid(row=2, column=3, padx=41)

# Buttons

buttonTotal = Button(buttonFrame, text='Total', font=('arial', 14, 'bold'), fg='white', bg='black', bd=3, padx=5,
                     command=totalcost)
buttonTotal.grid(row=0, column=0)

buttonReceipt = Button(buttonFrame, text='Receipt', font=('arial', 14, 'bold'), fg='white', bg='black', bd=3, padx=5
                       , command=receipt)
buttonReceipt.grid(row=0, column=1)

buttonSave = Button(buttonFrame, text='Save', font=('arial', 14, 'bold'), fg='white', bg='black', bd=3, padx=5
                    , command=save)
buttonSave.grid(row=0, column=2)

buttonReset = Button(buttonFrame, text='Reset', font=('arial', 14, 'bold'), fg='white', bg='black', bd=3, padx=5,
                     command=reset)
buttonReset.grid(row=0, column=3)

# textarea for receipt

textReceipt = Text(recieptFrame, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
textReceipt.grid(row=0, column=0)

import sqlite3
from tkinter import *
from tkinter import messagebox

# Connect to database
conn = sqlite3.connect('employees.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS employees
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              position TEXT NOT NULL,
              salary REAL NOT NULL)''')

conn.commit()


# Define functions
def add_employee():
    name = name_entry.get()
    position = position_entry.get()
    salary = float(salary_entry.get())
    c.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", (name, position, salary))
    conn.commit()
    view_employees()


def view_employees():
    # Clear grid
    for widget in grid.winfo_children():
        widget.destroy()

    # Add column headers
    Label(grid, text='ID').grid(row=0, column=0)
    Label(grid, text='Name').grid(row=0, column=1)
    Label(grid, text='Position').grid(row=0, column=2, padx=20)
    Label(grid, text='Salary').grid(row=0, column=3)

    # Add data rows
    c.execute("SELECT * FROM employees")
    rows = c.fetchall()
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            if j == 1:
                Label(grid, text=value).grid(row=i + 1, column=1)
            elif j == 2:
                Label(grid, text=value).grid(row=i + 1, column=2)
            else:
                Label(grid, text=value).grid(row=i + 1, column=3)

    # Add remove buttons
    for i, row in enumerate(rows):
        remove_button = Button(grid, text='Remove', command=lambda id=row[0]: remove_employee(id))
        remove_button.grid(row=i + 1, column=4)


def remove_employee(id):
    c.execute("DELETE FROM employees WHERE id=?", (id,))
    conn.commit()
    view_employees()


# Create employee database window
employee_window = Tk()
employee_window.title('Employee Database')

# Add employee form frame
form_frame = Frame(employee_window)
form_frame.pack(side=LEFT)

Label(form_frame, text='Name').grid(row=0, column=0)
name_entry = Entry(form_frame)
name_entry.grid(row=0, column=1)

Label(form_frame, text='Position').grid(row=1, column=0)
position_entry = Entry(form_frame)
position_entry.grid(row=1, column=1)

Label(form_frame, text='Salary').grid(row=2, column=0)
salary_entry = Entry(form_frame)
salary_entry.grid(row=2, column=1)

add_button = Button(form_frame, text='Add Employee', command=add_employee)
add_button.grid(row=3, column=0)

# Add employee grid frame
grid_frame = Frame(employee_window)
grid_frame.pack(side=LEFT)

grid = Frame(grid_frame)
grid.grid(row=0, column=0)

view_employees()

employee_window.protocol('WM_DELETE_WINDOW', employee_window.withdraw)

# Create main window
root = Tk()
root.title('Main Window')


# Define password check function
def check_password():
    password = password_entry.get()
    if password == 'mypassword':
        employee_window.deiconify()
    else:
        messagebox.showerror('Error', 'Incorrect password.')


# Add employee database button
def open_employee_db():
    password_window = Toplevel(root)
    password_window.title('Password')

    password_label = Label(password_window, text='Enter password:')
    password_label.pack(side=LEFT)
    global password_entry
    password_entry = Entry(password_window, show='*')
    password_entry.pack(side=LEFT)
    submit_button = Button(password_window, text='Submit', command=check_password)
    submit_button.pack(side=LEFT)


buttonReset = Button(buttonFrame, text='EMP', font=('arial', 14, 'bold'), fg='white', bg='black', bd=3, padx=5,
                     command=open_employee_db, )
buttonReset.grid(row=0, column=4)
from tkinter import *


def book_table(table_num):
    message_label.config(text="Table {} has been booked!".format(table_num))
    button_table[table_num]["state"] = "disabled"
    button_table[table_num].config(bg="red")


def remove_table():
    table_num = int(table_num_entry.get())
    if table_num < 1 or table_num > 9:
        message_label.config(text="Invalid table number!")
    else:
        message_label.config(text="Table {} has been removed!".format(table_num))
        button_table[table_num]["state"] = "normal"
        button_table[table_num].config(bg="green")
        table_num_entry.delete(0, END)


def create_table_window():
    table_window = Tk()
    table_window.title("Table Booking System")

    # create button table
    global button_table
    button_table = {}
    for i in range(1, 10):
        button_table[i] = Button(table_window, text="Table {}".format(i), bg="green",
                                 command=lambda i=i: book_table(i))
        button_table[i].grid(row=(i - 1) // 3, column=(i - 1) % 3)

    # create remove table section
    remove_frame = Frame(table_window)
    remove_frame.grid(row=3, column=1)
    table_num_label = Label(remove_frame, text="Enter table number:")
    table_num_label.pack(side=LEFT)
    global table_num_entry
    table_num_entry = Entry(remove_frame, width=2)
    table_num_entry.pack(side=LEFT)
    remove_table_button = Button(remove_frame, text="Remove Table", command=remove_table)
    remove_table_button.pack(side=LEFT)

    # create message label
    global message_label
    message_label = Label(table_window, text="")
    message_label.grid(row=4, column=0, columnspan=3)

    table_window.mainloop()


root = Tk()
TABLE = Button(buttonFrame, text='Tab', font=('arial', 14, 'bold'), fg='white', bg='black', bd=3, padx=5,
               command=create_table_window)
TABLE.grid(row=1, column=3)


def submit_feedback():
    global feedback_entry, name_entry, feedback_listbox, message_label
    feedback = feedback_entry.get()
    name = name_entry.get()
    if feedback:
        feedback_listbox.insert(END, f"{name}: {feedback}")
        feedback_entry.delete(0, END)
        name_entry.delete(0, END)
        message_label.config(text="Feedback submitted!", fg="green")
    else:
        message_label.config(text="Please enter feedback.", fg="red")


def open_feedback_window():
    global feedback_entry, name_entry, feedback_listbox, message_label
    feedback_window = Toplevel(root)
    feedback_window.title("Feedback")
    feedback_window.geometry("400x400")
    feedback_frame = Frame(feedback_window, bg="#ececec")
    feedback_frame.pack(padx=10, pady=10)
    feedback_label = Label(feedback_frame, text="Please provide your feedback below:", bg="#ececec", fg="#333")
    feedback_label.pack()
    name_label = Label(feedback_frame, text="Your name:", bg="#ececec", fg="#333")
    name_label.pack()
    name_entry = Entry(feedback_frame, width=50)
    name_entry.pack(pady=5)
    feedback_entry = Entry(feedback_frame, width=50)
    feedback_entry.pack(pady=5)
    submit_button = Button(feedback_frame, text="Submit Feedback", bg="#333", fg="#fff", command=submit_feedback)
    submit_button.pack(pady=10)
    message_label = Label(feedback_frame, text="", bg="#ececec", fg="#333")
    message_label.pack()
    # create feedback history section
    history_frame = Frame(feedback_window, bg="#ececec")
    history_frame.pack(padx=10, pady=10)
    history_label = Label(history_frame, text="Feedback History", bg="#ececec", fg="#333")
    history_label.pack()
    feedback_listbox = Listbox(history_frame, width=50, height=10)
    feedback_listbox.pack(pady=10)


root = Tk()
feedback_button = Button(buttonFrame, text='Review', font=('arial', 14, 'bold'), fg='white', bg='black', bd=3, padx=5,
                         command=open_feedback_window)
feedback_button.grid(row=1, column=1)
root.mainloop()
root.mainloop()
conn.close