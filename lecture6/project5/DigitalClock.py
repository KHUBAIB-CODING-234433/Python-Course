import tkinter as st
from time import strftime
root = st.Tk()
root.title("digitalCloack")
def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)

label = st.Label(root,font=('calibri ',50,'bold'),background='yellow',foreground='black')
label.pack(anchor='center')
time()
root.mainloop()
