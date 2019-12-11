import tkinter as tk
from tkinter import *
from tkinter import messagebox
main=tk.Tk()
import ml
y=0
def cal():
    y=ml.pr(preg.get(),glu.get(),blood.get(),skin.get(),ins.get(),bmi.get(),pdf.get(),age.get())
    if y==1:
        messagebox.showinfo("Prediction","Diabetes test is Positive.\n(It means that you have diabetes)")
    else:
        messagebox.showinfo("Prediction","Diabetes test is Negative.\n(It means that you don't have diabetes)")
    #print(ml.pr(preg.get(),glu.get(),blood.get(),skin.get(),ins.get(),bmi.get(),pdf.get(),age.get()))

preg=tk.IntVar()
glu=tk.IntVar()
blood=tk.IntVar()
skin=tk.IntVar()
bmi=tk.IntVar()
age=tk.IntVar()
ins=tk.IntVar()
pdf=tk.IntVar()

def diebetes():
    main.geometry("400x400")
    tk.Label(main,text="Pregnencies").pack()
    tk.Entry(main,textvariable=preg).pack()
    
    tk.Label(main,text="Glucose").pack()
    tk.Entry(main,textvariable=glu).pack()
    
    tk.Label(main,text="Blood Pressure").pack()
    tk.Entry(main,textvariable=blood).pack()
    
    tk.Label(main,text="Skin Thickness").pack()
    tk.Entry(main,textvariable=skin).pack()
    
    tk.Label(main,text="insulin").pack()
    tk.Entry(main,textvariable=ins).pack()
    
    tk.Label(main,text="BMI").pack()
    tk.Entry(main,textvariable=bmi).pack()
    
    tk.Label(main,text="Pedgree function").pack()
    tk.Entry(main,textvariable=pdf).pack()
    
    tk.Label(main,text="Age").pack()
    tk.Entry(main,textvariable=age).pack()
    
    tk.Button(main,text="Check",command=cal).pack()
    
    
    
diebetes()
main.mainloop()
