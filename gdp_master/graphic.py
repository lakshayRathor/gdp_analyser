from tkinter import *
from tkinter import messagebox
from intro import *



def predict():
	Label(root, text='1.Consumption').grid(row=0)
	Label(root, text='2.Government Budget').grid(row=1)
	Label(root, text='3.Market CAP').grid(row=2)
	Label(root, text='4.Import').grid(row=3)
	Label(root, text='5.Export').grid(row=4)
	e1 = Entry(root)
	e2 = Entry(root)
	e3 = Entry(root)
	e4 = Entry(root)
	e5 = Entry(root)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2, column=1)
	e4.grid(row=3, column=1)
	e5.grid(row=4, column=1)
	btn = Button(root, text="Predict",command=clicked)
	btn.grid(column=0, row=5)
def clicked():
     messagebox.showinfo('Prediction','yet to calculate')


def op():
      data2 = pd.read_csv('DataFinal.csv', encoding = "ISO-8859-1")
      d=list(data2['CID'].unique())
      e=list(data2['Country'].unique())
      f=list(zip(d,e))
      ourMessage = f
      messageVar = Message(root, text = ourMessage) 
      messageVar.config(bg='lightgreen') 
      messageVar.pack() 


root = Tk() 
root.title("Welcome to GDPPREDICT toolkit")
root.geometry('1350x1200')
menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...',command=op)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Tools', menu=helpmenu)
helpmenu.add_command(label='GDPPREDICT', command=predict)


mainloop()

