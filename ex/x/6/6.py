from tkinter import *
from tkinter import messagebox
import sqlite3


connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS my_Table(id INTEGER PRIMARY KEY, nam TEXT, qfr INTEGER, qkh INTEGER, ted INTEGER)''')
            
       
connection.commit()

root = Tk()
root.title("مدیریت کتابخانه")
root.geometry("500x250")
root.resizable(0,0) 

def bastan():
    quit()

    
def ezafe():
    try:    
        nam = nam_kala.get()
        qfr = int(qeymat_frosh.get())
        qkh = int(qeymqt_kharid.get())
        ted = int(teadad.get())
        cursor.execute("INSERT INTO my_Table (nam, qfr, qkh, ted) VALUES (?, ?, ?, ?)",(nam, qfr, qkh, ted))
        connection.commit()
        
        lb_tasks.insert(END, f"{nam} {qfr} {qkh} {ted}")     
        nam_kala.delete(0, END)
        qeymat_frosh.delete(0, END)
        qeymqt_kharid.delete(0, END)
        teadad.delete(0, END)
        
    except ValueError:
        messagebox.showwarning(END, "خطا: لطفاً مقادیر صحیح معتبر را وارد کنید")
    
    
def jostojo():
    try:
        nam = nam_kala.get()
        qfr = qeymat_frosh.get()
        qkh = qeymqt_kharid.get()
        ted = teadad.get()
        cursor.execute("SELECT * FROM my_table WHERE nam=? OR qfr=? OR qkh=? OR ted=?",
                       (nam, qfr, qkh, ted))
        rows = cursor.fetchall()
        for row in rows:
            lb_tasks.insert(END, f"{row[1]}, {row[2]}, {row[3]}, {row[4]}")
    except:
        messagebox.showwarning(END, "خطا: لطفاً مقادیر صحیح معتبر را وارد کنید")
    


def hazf():
    try:
        index = lb_tasks.curselection()[0]
        task = lb_tasks.get(index)
        nam, qfr, qkh, ted= task.split() 
        lb_tasks.delete(index)
        cursor.execute("DELETE FROM my_Table WHERE nam=? OR qfr=? OR qkh=? OR ted=?",(nam, qfr, qkh, ted))
        connection.commit()
    except IndexError:
        messagebox.showwarning(END, "خطا: لطفاً یک مورد را برای حذف انتخاب کنید")
    
        
def virayesh ():
    try:
        index = lb_tasks.curselection()[0]
        item = lb_tasks.get(index)
        parts = item.split()
        if len(parts) != 4:
            messagebox.showwarning("خطا", "لطفاً یک مورد را برای ویرایش انتخاب کنید")
        nam, qfr, qkh, ted = parts
        lb_tasks.delete(index)
        nam_kala.delete(0, END)
        nam_kala.insert(0, nam)
        qeymat_frosh.delete(0,END)
        qeymat_frosh.insert(0, qfr)
        qeymqt_kharid.delete(0,END)
        qeymqt_kharid.insert(0, qkh)
        teadad.delete(0, END)
        teadad.insert(0, ted)
    except IndexError:
        messagebox.showwarning("خطا", "لطفاً یک مورد را برای ویرایش انتخاب کنید")

def listbox():
    cursor.execute("SELECT * FROM my_Table")
    rows = cursor.fetchall()
    for row in rows:
        lb_tasks.insert(END, f"{row[1]}, {row[2]}, {row[3]}, {row[4]}")
lb_tasks = Listbox(root)
lb_tasks.grid(row=2,column=1,rowspan=7)

listbox()

lbl_namKala = Label(root, text= "نام کالا:").grid(row=0, column=0, padx=10, pady=0)
nam_kala = Entry(root)
nam_kala.grid(row=0, column=1, padx=10, pady=0)

lbl_qeymatFrosh = Label(root, text = "قیمت فروش:").grid(row=1, column=0, padx=10, pady=0)
qeymat_frosh = Entry(root)
qeymat_frosh.grid(row=1, column=1, padx=10, pady=0)

lbl_qeymqtKHarid = Label(root, text = "قیمت خرید:").grid(row=0, column=2, padx=10, pady=0)
qeymqt_kharid = Entry(root)
qeymqt_kharid.grid(row=0, column=3, padx=10, pady=0)

lbl_teadad = Label(root, text = "تعداد:").grid(row=1, column=2, padx=10, pady=0)
teadad = Entry(root)
teadad.grid(row=1, column=3, padx=10, pady=0)

but_ezafe = Button(root, text = "اضافه کردن", command = ezafe)
but_ezafe.grid(row=3, column=3, padx=10, pady=0)
but_jostojo = Button(root, text = " جستجوی کالا", command = jostojo)
but_jostojo.grid(row=4, column=3, padx=10, pady=0)
but_hazf = Button(root, text = "حذف کالا", command = hazf)
but_hazf.grid(row=5, column=3, padx=10, pady=0)
but_virayesh = Button(root, text = "ویرایش", command = virayesh)
but_virayesh.grid(row=6, column=3, padx=10, pady=0)
but_bastan = Button(root, text = "بستن", command = bastan)
but_bastan.grid(row=7, column=3, padx=10, pady=0)

scrol = Scrollbar(root, command=lb_tasks.yview)
scrol.grid(row=5,column=2, padx=10, pady=0)

root.mainloop()
