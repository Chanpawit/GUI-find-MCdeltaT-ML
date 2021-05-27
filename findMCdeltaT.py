from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.geometry('800x500')
root.title('Program Find MC▲T And ML')

style = ttk.Style()

style.configure('W.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'red')

#################################

TAB = ttk.Notebook(root)
MainT = Frame(TAB)
T1 = Frame(TAB)
T2 = Frame(TAB)
TAB.pack(fill=BOTH, expand=1)

TAB.add(MainT, text=f'{"Main Page":^{30}}', compound='top')

#################################

############--Main Tab--###########

def start():
	TAB.hide(0)
	TAB.add(T1, text=f'{"Find MC▲T":^{30}}', compound='top')
	TAB.add(T2, text=f'{"Find ML":^{30}}', compound='top')

MainB = ttk.Button(MainT, text='Start!', style='W.TButton', width=20, command=start)
MainB.pack(pady=10)

MainL = ttk.Label(MainT, text='<Press F1 for more information!>', font=(None, 20), foreground='#EBA70A')
MainL.pack(pady=20)

###################################

###########--Tab 1--###############

def mainFind(event=None):
	try:
		e1, e2, e3, e4 = v_e1.get(), v_e2.get(), v_e3.get(), v_e4.get()
		String = v_String1.get()

		Minimal = int(e3) - int(e4)
		result = int(e1) * int(e2) * Minimal

		messagebox.showinfo('System', f'The Value is {result}')

		#print(result)

		v_e1.set('')
		v_e2.set('')
		v_e3.set('')
		v_e4.set('')
		v_String1.set(f'The value is {result}')
	except Exception as e:
		messagebox.showerror('System', 'Please Enter the Completed Number or Enter Number not Letters')
		v_e1.set('')
		v_e2.set('')
		v_e3.set('')
		v_e4.set('')
		v_String1.set('')

def showinformation(event=None):
	messagebox.showinfo('System', 'This Program develop By Ryu\nThis program is for find MC▲T And ML in science subject, hope you will enjoy this program.')

L1 = ttk.Label(T1, text='Enter M down here', font=(None, 20), foreground='coral2')
L1.place(x=2, y=0)

v_e1 = StringVar()
E1 = ttk.Entry(T1, textvariable=v_e1, font=(None, 20))
E1.place(x=2, y=35)

L2 = ttk.Label(T1, text='Enter C down here', font=(None, 20), foreground='#13E0D7')
L2.place(x=2, y=80)

v_e2 = StringVar()
E2 = ttk.Entry(T1, textvariable=v_e2, font=(None, 20))
E2.place(x=2, y=115)

L3 = ttk.Label(T1, text='Enter The largest value ▲T down here', font=(None, 20), foreground='#1395E0')
L3.place(x=2, y=160)

v_e3 = StringVar()
E3 = ttk.Entry(T1, textvariable=v_e3, font=(None, 20))
E3.place(x=2, y=195)

L4 = ttk.Label(T1, text='Enter The Minimal value ▲T down here', font=(None, 20), foreground='#4E0AEB')
L4.place(x=2, y=240)

v_e4 = StringVar()
E4 = ttk.Entry(T1, textvariable=v_e4, font=(None, 20))
E4.place(x=2, y=275)

B1 = ttk.Button(T1, text='Enter', style='W.TButton', width=20, command=mainFind)
B1.place(x=2, y=335)

v_String1 = StringVar()
LString = ttk.Label(T1, textvariable=v_String1, font=(None, 20), foreground='#0A99EB')
LString.place(x=2, y=380)

#T1.bind('<Return>', mainFind)
root.bind('<F1>', showinformation)

###################################

############--Tab2--###############
def viceRun():
	try:
		e5, e6 = v_e5.get(), v_e6.get()
		LString2 = v_String2.get()
		result = int(e5) * int(e6)
		messagebox.showinfo('System', f'The value is {result}')

		v_e5.set('')
		v_e6.set('')
		v_String2.set(f'The value is {result}')

	except:
		messagebox.showerror('System', 'Please Enter the Completed Number or Enter Number not Letters')
		v_e5.set('')
		v_e6.set('')
		v_String2.set('')


L6 = ttk.Label(T2, text='Enter M down here', font=(None, 20), foreground='coral2')
L6.place(x=2, y=0)

v_e5 = StringVar()
E5 = ttk.Entry(T2, textvariable=v_e5, font=(None, 20))
E5.place(x=2, y=35)

L8 = ttk.Label(T2, text='Enter L down here', font=(None, 20), foreground='#13E0D7')
L8.place(x=2, y=80)

v_e6 = StringVar()
E6 = ttk.Entry(T2, textvariable=v_e6, font=(None, 20))
E6.place(x=2, y=115)

B2 = ttk.Button(T2, text='Enter',style='W.TButton', width=20, command=viceRun)
B2.place(x=2, y=170)

v_String2 = StringVar()
L9 = ttk.Label(T2, textvariable=v_String2, font=(None, 20), foreground='#0A99EB')
L9.place(x=2, y=220)

#v_String
###################################
root.mainloop()