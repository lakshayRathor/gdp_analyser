from intro import *
from filedata import *
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from sklearn.model_selection import train_test_split
def final():
    filename = 'DataFinal.csv'                                          
    intro()                                                         
    get_code(filename)                                              
    #key=input("\n Please select a Country of your choice:") 
    #key=91
    if keys:
      key=int(keys.get())
    else:
      key=91
    if key in range(1,212):                                         
        fd=file_data(filename,key)                                  
        X,Y,year = fd.get_data(key)   
        print(X)
        print(Y)
        train_X, test_X = train_test_split(X, test_size=0.2)
        train_Y, test_Y = train_test_split(Y, test_size=0.2)
        #print("X is"+str(X.length()))
        #print("Y is"+str(length(Y)))
        om=OLSModel(filename,X, Y, key)                             
        res=om.olsm()                                               
        print(res.summary())
        #print(res.score(X,Y)*100)                                        
        data2=plotlib(filename,key)
       	data2.shape
        regressor=LinearRegression().fit(X,Y)
        gdp=Y
        plt.scatter(year,gdp)
        #print(regressor.score([x],predictedgdp[0])*100)
        #plt.plot(year,regressor.predict(Ys),color='red')
        #con=int(input("1.Consumption"))
        #imp=int(input("2.Govt. Budget "))
        #exp=int(input("3.Market capExport"))
        #govt=int(input("4.Import"))
        #cap= int(input("5.Export"))
        acc=regressor.score(X,Y)*100
        print(acc)
        cons=int(con.get())
        govtb=int(govt.get())
        cape=int(cap.get())
        impt=int(imp.get())
        expt=int(exp.get())
         
        x = [cons,govtb,cape,impt,expt]
        #x=[367203.44,64100.07,163231.96,93564.02,89341.83]
        predictedgdp1=regressor.predict([x])
        print(acc)
        #print(regressor.score([x],predictedgdp[0])*100)
        return predictedgdp1[0] 
    else:
        print(" \n Wrong country code , Check again")
def predict():
	ttk.Label(root, text='1.Consumption').grid(row=0)
	ttk.Label(root, text='2.Government Budget').grid(row=1)
	ttk.Label(root, text='3.Market CAP').grid(row=2)
	ttk.Label(root, text='4.Import').grid(row=3)
	ttk.Label(root, text='5.Export').grid(row=4)
	e1 = ttk.Entry(root,textvariable = con)
	e2 = ttk.Entry(root,textvariable = govt)
	e3 = ttk.Entry(root,textvariable = cap)
	e4 = ttk.Entry(root,textvariable = imp)
	e5 = ttk.Entry(root,textvariable = exp)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	e4.grid(row=3, column=1)
	e5.grid(row=4, column=1)
	lcc.grid(row=5,column=0)
	ecc.grid(row=5,column=1)
	#messageVar.pack()
	#btn = ttk.Button(root, text="Predict",command=clicked('''con.get(),govt.get(),cap.get(),imp.get(),exp.get()''' 545452,123123,123123,123123,123131))
	btn = ttk.Button(root, text="Predict",command=clicked)
	btn.grid(column=1, row=6)
	messageVar.grid(row=7,column=5)
def clicked():
     '''con=int(con.get())
     govt=int(govt.get())
     cap=int(cap.get())
     imp=int(imp.get())
     exp=int(exp.get())'''
     #predictedgdp=final(con,govt,cap,imp,exp)
     predictedgdp=final()
     messagebox.showinfo('Prediction',str(predictedgdp))

def op():
      
      lcc.grid(row=6)
      ecc.grid(row=6, column=1)


root = Tk() 
root.title("Welcome to GDPPREDICT toolkit")
root.geometry('1350x1200')
menu = Menu(root) 
root.config(menu=menu) 
#filemenu = Menu(menu)
#menu.add_cascade(label='File', menu=filemenu)
#filemenu.add_command(label='Country Code', command=op)
#filemenu.add_command(label='Open...',command=op)
#filemenu.add_separator()
#filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Predict', menu=helpmenu)
helpmenu.add_command(label='GDPPREDICT', command=predict)
con = StringVar()
govt = StringVar()
cap = StringVar()
imp = StringVar()
exp = StringVar()
keys = StringVar()
e1 = ttk.Entry(root,textvariable = con)
e2 = ttk.Entry(root,textvariable = govt)
e3 = ttk.Entry(root,textvariable = cap)
e4 = ttk.Entry(root,textvariable = imp)
e5 = ttk.Entry(root,textvariable = exp)
lcc = ttk.Label(root, text='country code')
ecc = ttk.Entry(root,textvariable = keys)
data2 = pd.read_csv('DataFinal.csv', encoding = "ISO-8859-1")
d=list(data2['CID'].unique())
e=list(data2['Country'].unique())
f=list(zip(d,e))
ourMessage = f
messageVar = Message(root, text = ourMessage) 
messageVar.config(bg='lightgreen') 
root.mainloop()