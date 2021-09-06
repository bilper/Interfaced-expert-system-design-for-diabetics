import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import *
from tkinter.messagebox import *


# window
win = tk.Tk()
win.title("Sekermatik")
# win.resizable(0,0)

# modify adding label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

# button click event
# def clickMe():
#     action.configure(text='Hello ' + name.get())
   
    
    


# drop down menu
# ttk.Label(win, text="Seker Tipi:").grid(column=0, row=0)
# number = tk.StringVar()
# numberChosen = ttk.Combobox(win, width=12, textvariable=number)
# numberChosen['values'] = ("Aclik", "Tokluk")
# numberChosen.grid(column=0, row=1)
# numberChosen.current(1)

ttk.Label(win, text="Seker tipi:").grid(column=0, row=0)
number = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=number)
nameEntered.grid(column=0, row=1)


# text box entry
ttk.Label(win, text="Yas:").grid(column=1, row=0)
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=1, row=1)

# text box entry
ttk.Label(win, text="Kan sekeri:").grid(column=2, row=0)
name1 = tk.StringVar()
nameEntered1 = ttk.Entry(win, width=12, textvariable=name1)
nameEntered1.grid(column=2, row=1)

# button
# action = ttk.Button(win, text="Click Me!", command=clickMe)
# action.grid(column=0, row=2)
# action.configure(state='disabled')

# scrolled text
scr = scrolledtext.ScrolledText(win, width=80, height=4, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)



def show_answer():
    Ans = values()
    scr.insert('1.0', Ans)







Button(win, text='Sonuc', command=show_answer).grid(row=4, column=1, sticky=W, pady=4)













def values(): 
    global Age 
    Yas = float(name.get()) 
    Kan_sekeri = float(name1.get())
    Seker_tipi = str(number.get())
    
    
    sonuc=""
    if Seker_tipi=="Aclik" and 70<=Kan_sekeri<=100:
        Seker_seviyesi="Normal"
        sonuc="Eger seker tipi=aclik ve kan sekeri>70 ve kan sekeri<=100 ise o halde kan sekeri=normal "
    elif  Seker_tipi=="Aclik" and not 70<=Kan_sekeri<=100:
        Seker_seviyesi="Normal degil"
        if Seker_seviyesi=="Normal degil" and 0<=Kan_sekeri<=50:
            sonuc="Eger seker tipi=aclik ve seker seviyesi=normal degil ve Kan sekeri<=50 o halde sonuc=Acil durum"  
        elif Seker_seviyesi=="Normal degil" and 50<Kan_sekeri<70:
            durum="Hipoglisemi"
            if durum=="Hipoglisemi" and Yas<=65:
                sonuc="Eger seker tipi=aclik ve seker seviyesi=normal degil ve durum=Hipoglisemi ve Yas<=65 o halde sonuc=20 gram seker alın ve insülin kullanmayın"
            elif durum=="Hipoglisemi" and Yas>65:
                    sonuc="Eger seker tipi=aclik ve seker seviyesi=normal degil ve durum=Hipoglisemi ve Yas>65 o halde sonuc=Acil durum"       
        elif Seker_seviyesi=="Normal degil"  and 100<Kan_sekeri<=125:
            durum="Gizli seker"
            if durum=="Gizli seker" and Yas<=65:
                sonuc="Eger seker tipi=aclik ve seker seviyesi=normal degil ve durum=Gizli Seker ve Yas<=65 o halde sonuc=Günlük 180 gram karbonhidrat alın ve 1 doz insulin kullanın"
            elif durum=="Gizli seker" and Yas>65:
                sonuc="Eger seker tipi=aclik ve seker seviyesi=normal degil ve durum=Gizli Seker ve Yas<=65 o halde sonuc=Acil durum"
        if Seker_seviyesi=="Normal degil"  and Kan_sekeri>=126 :
            durum="Diyabet"
            if durum=="Diyabet" and Yas<=65:
                insulin_miktarı=(Kan_sekeri-125)/26
                insulin_miktarı=int(insulin_miktarı)
                insulin_miktarı=str(insulin_miktarı)
                a="Günlük 180 gram karbonhidrat alın ve "
                b=" doz insulin kullanın"
                sonuc1= a + insulin_miktarı + b
                sonuc="Eger seker tipi=aclik ve seker seviyesi=normal degil ve durum=Diyabet ve Yas<=65 o halde sonuc=  " + sonuc1
            elif durum=="Diyabet" and Yas>65:
                sonuc="Eger seker tipi=aclik ve seker seviyesi=normal degil ve durum=Diyabet ve Yas>65 o halde sonuc=Acil durum" 
    if Seker_tipi=="Tokluk" and  100<=Kan_sekeri<=140:
        Seker_seviyesi="Normal"
        sonuc= "Eger seker tipi=Tokluk ve kan sekeri=>100 ve kan sekeri<=140 ise o halde kan sekeri=normal"
    elif  Seker_tipi=="Tokluk" and not  100<=Kan_sekeri<=140:
        Seker_seviyesi="Normal degil"     
        if Seker_seviyesi=="Normal degil" and  Kan_sekeri>=300:
            sonuc="Eger seker tipi=tokluk ve seker seviyesi=normal degil ve kan sekeri>=300 sonuc=Acil durum"
        elif Seker_seviyesi=="Normal degil" and  140<Kan_sekeri<=199:
            durum="Gizli seker"
            if durum=="Gizli seker" and Yas<=65:
                sonuc="Eger seker tipi=tokluk ve seker seviyesi=normal degil ve durum=Gizli seker ve Yas<=65 o halde sonuc=Günlük 180 gram karbonhidrat alın ve 1 doz insulin kullanın"
            elif durum=="Gizli seker" and Yas>65:
                sonuc="Eger seker tipi=tokluk ve seker seviyesi=normal degil ve durum=Gizli seker ve Yas>65 o halde sonuc=Acil durum"    
        elif Seker_seviyesi=="Normal degil"  and Kan_sekeri>=200 :
            durum="Diyabet"
            if durum=="Diyabet" and Yas<=65:
                insulin_miktarı=(Kan_sekeri-140)/50
                insulin_miktarı=int(insulin_miktarı)
                insulin_miktarı=str(insulin_miktarı)
                a="Günlük 180 gram karbonhidrat alın ve "
                b=" doz insulin kullanın"
                sonuc1= a +  insulin_miktarı  + b
                sonuc="Eger seker tipi=tokluk ve seker seviyesi=normal degil ve durum=Diyabet ve Yas<=65 o halde sonuc=  " + sonuc1
            elif durum=="Diyabet" and Yas>65:
                sonuc="Eger seker tipi=tokluk ve seker seviyesi=normal degil ve durum=Diyabet ve Yas>65 o halde sonuc=Acil durum"          
    return(sonuc)

    # label_Discount = tk.Label(root, text= Discount, bg='yellow')
    # canvas1.create_window(270, 200, window=label_Discount)        

        
    
    # if Age >= 60:
    #    Discount = ('Discount Status: ','Senior Discount')  
    #    label_Discount = tk.Label(root, text= Discount, bg='yellow')
    #    canvas1.create_window(270, 200, window=label_Discount)
    # elif 18 <= Age < 60:
    #    Discount = ('Discount Status: ','No Discount')  
    #    label_Discount = tk.Label(root, text= Discount, bg='yellow')
    #    canvas1.create_window(270, 200, window=label_Discount)
    # else:
    #    Discount = ('Discount Status: ','Junior Discount')  
    #    label_Discount = tk.Label(root, text= Discount, bg='yellow')
    #    canvas1.create_window(270, 200, window=label_Discount)
      




# direct keyboard input to text box entry
nameEntered.focus()



win.mainloop()