import tkinter as tk

from tkinter.ttk import *
from tkinter import X, Tk, simpledialog, messagebox
from matplotlib.pyplot import pie

import pandas as pd
import numpy as np
from io import BytesIO

import requests
import os
from io import BytesIO
from food import cal_calcurater,dayoftime

from PIL import ImageTk, Image  
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import datetime


def createnew(food,Calories,Protien,Carbohydrate,Fat,Day,Month,Year):
    
    asking = pd.read_csv('extention/collection.csv')
    asking.loc[len(asking.index)] =[food.title(),Calories,Protien,Carbohydrate,Fat,Day,Month,Year]   
    asking.to_csv('extention/collection.csv',index = False)
def delete():
    toolbar.destroy()
    connection()
def Exit():
    root.destroy()
def connection():
    
    barh_t.place(x=470333,y=420333)
   
    try:   
        
        r = requests.get('https://docs.google.com/spreadsheet/ccc?key=1TZQ7C9gXkZaXQbBAglAkYriqfX2KW8rHVzmdLgZ7wi4&output=csv')
    except:
        
        panel.config(image=img_reconnect,width=550,height=479)
        panel.place(x=350,y=230, anchor="center")
        head_letter.config(text='Connection Lost!!!')
        head_letter.place(x=350,y=400, anchor="center")
        weight.place(x=470333,y=420333)
        Sub.config(text='Exit',command=Exit)
        Sub.place(x=350,y=450,anchor="center")
        head_letter2.place(x=470333,y=420333)
        checking.place(x=470333,y=420333)
        head_letter3.place(x=470333,y=420333)   
    else:
        data = r.content
        df_f = pd.read_csv(BytesIO(data))
        cm =list(set(df_f['Ingredient']))
        cm.sort()
        h= pd.read_csv('extention/collection.csv')
        combo['values'] =cm
        
        combo.current(0)
        combo.config(font=('Comic Sans MS',20))

        ny=list(set(h['Year']))
        ny.sort()
        ny.insert(0,'Every Year')
        histo_year['values'] =ny
        histo_year.current(0)
        histo_year.config(font=('Comic Sans MS',13),width=10)
        

       
        nm=list(set(h['Month']))
        nm.sort()
        nm.insert(0,'Every Month')
        histo_month['values'] =nm
        histo_month.current(0)
        histo_month.config(font=('Comic Sans MS',13),width=10)
        

      
        nd=list(set(h['Day']))
        nd.sort()
        nd.insert(0,'Every Day')
        histo_day['values'] =nd
        histo_day.current(0)
        histo_day.config(font=('Comic Sans MS',13),width=10)
       
        

        
        main()

def  clicked_choose():
    global toolbar
   
    try:
        if float(weight.get()) <= 0:
                int('hello')
    except:
        messagebox.showerror('error','Weight must more than zero')
    else:
        try:
            cal=cal_calcurater(combo.get().title(),weight.get())
        except:
            messagebox.showerror('error',combo.get()+' is not defined')
        else:
                d = datetime.datetime.now()
                createnew(combo.get().title(),str(round(cal['cal'], 2)),str(round(cal['protein'], 2)),str(round(cal['carbohydrate'], 2)),str(round(cal['fat'], 2)),d.day,d.month,d.year)
                head_letter.config(text='')
                
                head_letter2.config(text='')
            
                
                head_letter3.config(text='')

                checking.place(relx=0.5,rely=0.5,anchor="center")
                histo_day.place(relx=0.5,rely=0.5,anchor="center")
                histo_month.place(relx=0.5,rely=0.5, anchor="center")
                histo_year.place(relx=0.5,rely=0.5, anchor="center")


                d = datetime.datetime.now()
                createnew(combo.get().title(),str(round(cal['cal'], 2)),str(round(cal['protein'], 2)),str(round(cal['carbohydrate'], 2)),str(round(cal['fat'], 2)),d.day,d.month,d.year)
                
                c=combo.get()


                v = list(cal.values())
                l = list(cal.keys())
                l.append('Other')
                r=float(cal['cal']) - (float(cal['protein'])+float(cal['carbohydrate'])+float(cal['fat']))
                print(r)
                if r >= 0:
                    v.append(round(r,2))
                else:
                    v.append(0)
                v.remove(v[3])
                l.remove('cal')
                varr =np.array(v)

                def absolute_value(val):
                    a  = np.round(val/100.*varr.sum(), 2)
                    return a
                plot1.clear()
            
                plot1.set_title(c.title()+' '+str(round(cal['cal'], 2))+' calories')
                


                plot1.set_facecolor("#121212")
                myexplode = [0.1, 0.1, 0.1, 0.1]
                plot1.pie(varr,labels =l ,autopct=absolute_value,shadow=True,explode=myexplode)
            

                toolbar = NavigationToolbar2Tk(barh,
                                            root)
                toolbar.config(background='#b6c471')
                toolbar._message_label.config(background='#b6c471')
                toolbar.winfo_children()[-2].config(background='#b6c471')
                toolbar.place(relx=0.3,rely=0.9, anchor="center")  
                toolbar.update()
                
            
                barh_t =barh.get_tk_widget()
                barh_t.place(x=350,y=210, anchor="center")
            
                Sub.config(text='back',command=delete)
                Sub.place_configure(relx=0.8,rely=0.9, anchor="center")

def history():
    global toolbar
    Y=histo_year.get()
    M=histo_month.get()
    D=histo_day.get()
    ti = dayoftime(Y,M,D)

    v = list(ti.values())
    l = list(ti.keys())
    l.append('Other')
    r=ti['cal'] - (ti['protein']+ti['carbohydrate']+ti['fat'])
    allc= ti['cal']
    print(r)
    if r >= 0:
        v.append(round(r,2))
    else:
        v.append(0)
    v.remove(v[3])
    l.remove('cal')
    varr =np.array(v)

    def absolute_value(val):
        a  = np.round(val/100.*varr.sum(), 2)
        return a
    plot1.clear()
            
   
    



    plot1.set_facecolor("#121212")
    myexplode = [0.1, 0.1, 0.1, 0.1]
    try:
        
        plot1.pie(varr,labels =l ,autopct=absolute_value,shadow=True,explode=myexplode)
    except:
         messagebox.showerror('error','Either your date '+D+'/'+M+'/'+Y+' isn\'t defined\nor you don\'t have any consumption history yet' ) 
    
    else:
        plot1.set_title('Calories you gained in '+D+'/'+M+'/'+Y+'\n is about '+str(round(allc,2))+' calories')
        head_letter.config(text='')
                
        head_letter2.config(text='')
    
        
        head_letter3.config(text='')

        checking.place(relx=0.5,rely=0.5,anchor="center")
        histo_day.place(relx=0.5,rely=0.5,anchor="center")
        histo_month.place(relx=0.5,rely=0.5, anchor="center")
        histo_year.place(relx=0.5,rely=0.5, anchor="center")

        toolbar = NavigationToolbar2Tk(barh,
                                    root)
        toolbar.config(background='#b6c471')
        toolbar._message_label.config(background='#b6c471')
        toolbar.winfo_children()[-2].config(background='#b6c471')
        toolbar.place(relx=0.3,rely=0.9, anchor="center")  
        toolbar.update()
        

        barh_t =barh.get_tk_widget()
        barh_t.place(x=350,y=210, anchor="center")

        Sub.config(text='back',command=delete)
        Sub.place_configure(relx=0.8,rely=0.9, anchor="center")
def main():
    weight.delete(0, 'end')
    weight.insert(0, "")
    head_letter.config(text='Choose your Ingredient')
    head_letter.place(relx=0.5,rely=0.1, anchor="center")

    
    combo.place(relx=0.5,rely=0.25, anchor="center")
    
    head_letter2.config(text='Enter the weight')
    head_letter2.place(relx=0.5,rely=0.4, anchor="center")
    weight.config(font=('Comic Sans MS',18),width=17)
    weight.place(relx=0.5,rely=0.53, anchor="center",relwidth=0.5)

    Sub.config(text='Ok',command=clicked_choose)
    Sub.place(relx=0.5,rely=0.63, anchor="center",relwidth=0.1)

    head_letter3.config(text='Calories Summation')
    head_letter3.place(relx=0.5,rely=0.73, anchor="center",relwidth=0.5)

    histo_year.place(relx=0.3,rely=0.8, anchor="center")
    histo_day.place(relx=0.7,rely=0.8, anchor="center")
    histo_month.place(relx=0.5,rely=0.8, anchor="center")
    checking.place(relx=0.5,rely=0.9, anchor="center")
    

    

root =tk.Tk()
root.geometry('700x500')
root.resizable(False,False)
root['background']='#b6c471'
root.title("Smart Scale Calories Calculator")
root.iconbitmap('extention/food.ico')

img= (Image.open("extention/internet_lost.png"))
resized_image= img.resize((350,300), Image.ANTIALIAS)
img_reconnect= ImageTk.PhotoImage(resized_image)
panel = tk.Label(root, image = '',background='#b6c471')

head_letter =tk.Label(root,text = ' ',font =('Comic Sans MS',30,'bold'),background='#b6c471')

combo = Combobox(root)

head_letter2 =tk.Label(root,text = ' ',font =('Comic Sans MS',30,'bold'),background='#b6c471')
weight =tk.Entry(root, borderwidth=5)

Sub=tk.Button(root,text="Ok",font=('Comic Sans MS',10,'bold'),
                    width=10,
                    height=1,command=clicked_choose,
                    background='#9AF4BB', borderwidth=5,)
head_letter3 =tk.Label(root,text = ' ',font =('Comic Sans MS',20,'bold'),background='#b6c471')

histo_year = Combobox(root)
histo_month = Combobox(root)
histo_day = Combobox(root)

checking = tk.Button(root,text='Check',command=history,
        font=('Comic Sans MS',10,'bold'),
                    width=10,
                    height=1,#command=ok# 
                    background='#9AF4BB', borderwidth=5)

fig = Figure(figsize = (6, 4),
            dpi = 100)
fig.patch.set_facecolor('#b6c471')

plot1 = fig.add_subplot(111)

plot1.tick_params(axis='y', colors='white')
plot1.tick_params(axis='x', colors='white')

# plotting the graph


# creating the Tkinter canvas
# containing the Matplotlib figure
barh = FigureCanvasTkAgg(fig,
                        master = root,)  
barh.get_tk_widget().configure(bg="#b6c471")

barh.draw()



barh_t =barh.get_tk_widget()


connection()
root.mainloop()
