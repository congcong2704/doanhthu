import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.ttk import Button, Style, Label, Treeview
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime
from sklearn import linear_model
import numpy as np

win = tk.Tk()
win.title('CHƯƠNG TRÌNH QUẢN LÍ CHI TIÊU')
win.state("zoomed")
chi_tieu = []
chi_tieu1 = []
thu_nhap = []
thu_nhap1 = []
day = []
month = []
year = []
day2 = []
month2 = []
year2 = []
op = tk.Frame(win, bg='#808080')
op2 = tk.Frame(win, bg='#808080')

now = datetime.datetime.now()


def delete():
    for frame in ma.winfo_children():
        frame.destroy()
    for frame2 in op2.winfo_children():
        frame2.destroy()


def click1():
    delete()

    name = Label(op2, text='Nhập Tên Sản Phẩm:', font=('Arial', 13))
    name.place(x=10, y=50)

    entry = Entry(op2, width=20, font=('Arial', 13))
    entry.place(x=150, y=50)

    name1 = Label(op2, text='Nhập Giá:', font=('Arial', 13))
    name1.place(x=10, y=80)

    entry1 = Entry(op2, width=20, font=('Arial', 13))
    entry1.place(x=150, y=80)

    name0 = Label(op2, text='Ngày', font=('Arial', 13))
    name0.place(x=10, y=10)

    entry0 = Combobox(op2, width=5, font=('Arial', 13))
    entry0['value'] = ('Hiện tại')
    entry0.current(0)
    entry0.place(x=50, y=10)

    name01 = Label(op2, text='Tháng', font=('Arial', 13))
    name01.place(x=130, y=10)

    entry01 = Combobox(op2, width=5, font=('Arial', 13))
    entry01.place(x=185, y=10)
    entry01['value'] = ('Hiện tại')
    entry01.current(0)

    name02 = Label(op2, text='Năm', font=('Arial', 13))
    name02.place(x=260, y=10)

    entry02 = Combobox(op2, width=5, font=('Arial', 13))
    entry02.place(x=305, y=10)
    entry02['value'] = ('Hiện tại')
    entry02.current(0)

    def clickA():
        name2 = Label(op2, text=entry.get(), font=('Arial', 13))
        name3 = Label(op2, text=entry1.get(), font=('Arial', 13))
        name4 = Label(op2, text=entry0.get(), font=('Arial', 13))
        name5 = Label(op2, text=entry01.get(), font=('Arial', 13))
        name6 = Label(op2, text=entry02.get(), font=('Arial', 13))
        if name4.cget('text') == 'Hiện tại' and name5.cget('text') == 'Hiện tại' and name6.cget(
                'text') == 'Hiện tại' and name3.cget('text').isdigit():
            day.append(int(now.strftime("%d")))
            month.append(int(now.strftime("%m")))
            year.append(int(now.strftime("%Y")))
            chi_tieu.append(name2.cget('text'))
            chi_tieu1.append(float(name3.cget('text')))
        elif name3.cget('text').isdigit() and name4.cget('text').isdigit() and int(name4.cget('text')) < 32 and int(
                name4.cget('text')) > 0 and name5.cget('text').isdigit() and int(name5.cget('text')) < 12 and int(
                name5.cget('text')) > 0 and name6.cget('text').isdigit() and int(name6.cget('text')) < 2100 and int(
                name6.cget('text')) > 1900:
            day.append(int(name4.cget('text')))
            month.append(int(name5.cget('text')))
            year.append(int(name6.cget('text')))
            chi_tieu.append(name2.cget('text'))
            chi_tieu1.append(float(name3.cget('text')))
            else:
            messagebox.showerror("Lỗi", "Vui lòng nhập thông tin hợp lệ!")

    button2 = Button(op2, text='Thêm', style='TButton', command=clickA)
    button2.place(x=150, y=120)


def click2():
    delete()

    name = Label(op2, text='Nhập Tên Sản Phẩm:', font=('Arial', 13))
    name.place(x=10, y=50)

    entry = Entry(op2, width=20, font=('Arial', 13))
    entry.place(x=150, y=50)

    name1 = Label(op2, text='Nhập Số Tiền:', font=('Arial', 13))
    name1.place(x=10, y=80)

    entry1 = Entry(op2, width=20, font=('Arial', 13))
    entry1.place(x=150, y=80)

    name0 = Label(op2, text='Ngày', font=('Arial', 13))
    name0.place(x=10, y=10)

    entry0 = Combobox(op2, width=5, font=('Arial', 13))
    entry0['value'] = ('Hiện tại')
    entry0.current(0)
    entry0.place(x=50, y=10)

    name01 = Label(op2, text='Tháng', font=('Arial', 13))
    name01.place(x=130, y=10)

    entry01 = Combobox(op2, width=5, font=('Arial', 13))
    entry01.place(x=185, y=10)
    entry01['value'] = ('Hiện tại')
    entry01.current(0)

    name02 = Label(op2, text='Năm', font=('Arial', 13))
    name02.place(x=260, y=10)

    entry02 = Combobox(op2, width=5, font=('Arial', 13))
    entry02.place(x=305, y=10)
    entry02['value'] = ('Hiện tại')
    entry02.current(0)

    def clickB():
        name2 = Label(op2, text=entry.get(), font=('Arial', 13))
        name3 = Label(op2, text=entry1.get(), font=('Arial', 13))
        name4 = Label(op2, text=entry0.get(), font=('Arial', 13))
        name5 = Label(op2, text=entry01.get(), font=('Arial', 13))
        name6 = Label(op2, text=entry02.get(), font=('Arial', 13))
        if name4.cget('text') == 'Hiện tại' and name5.cget('text') == 'Hiện tại' and name6.cget(
                'text') == 'Hiện tại' and name3.cget('text').isdigit():
            day2.append(int(now.strftime("%d")))
            month2.append(int(now.strftime("%m")))
            year2.append(int(now.strftime("%Y")))
            thu_nhap.append(name2.cget('text'))
            thu_nhap1.append(float(name3.cget('text')))
        elif name3.cget('text').isdigit() and name4.cget('text').isdigit() and int(name4.cget('text')) < 32 and int(
                name4.cget('text')) > 0 and name5.cget('text').isdigit() and int(name5.cget('text')) < 12 and int(
                name5.cget('text')) > 0 and name6.cget('text').isdigit() and int(name6.cget('text')) < 2100 and int(
                name6.cget('text')) > 1900:
            day2.append(int(name4.cget('text')))
            month2.append(int(name5.cget('text')))
            year2.append(int(name6.cget('text')))
            thu_nhap.append(name2.cget('text'))
            thu_nhap1.append(float(name3.cget('text')))
        else:
            messagebox.showerror("Lỗi", "Vui lòng nhập thông tin hợp lệ!")

    button2 = Button(op2, text='Thêm', style='TButton', command=clickB)
    button2.place(x=150, y=120)


def click3():
    delete()

    na = Label(op2, text='Danh Sách', font=('Arial', 13))
    na.place(x=10, y=10)

    table = Treeview(op2, columns=(1, 2, 3, 4, 5), show="headings", height="10")
    table.place(x=10, y=40)

    table.heading(1, text="STT")
    table.heading(2, text="Tên Sản Phẩm")
    table.heading(3, text="Số Tiền")
    table.heading(4, text="Ngày")
    table.heading(5, text="Tháng")
    table.heading(6, text="Năm")

    for i in range(len(chi_tieu)):
        table.insert("", "end", values=(i + 1, chi_tieu[i], chi_tieu1[i], day[i], month[i], year[i]))

    def update_item(event):
        item = table.selection()[0]
        name = table.item(item, "values")[1]
        name1 = table.item(item, "values")[2]
        name2 = table.item(item, "values")[3]
        name3 = table.item(item, "values")[4]
        name4 = table.item(item, "values")[5]

        def update():
            for i in range(len(chi_tieu)):
                if chi_tieu[i] == name and chi_tieu1[i] == float(name1) and day[i] == int(
                        name2) and month[i] == int(name3) and year[i] == int(name4):
                    chi_tieu.pop(i)
                    chi_tieu1.pop(i)
                    day.pop(i)
                    month.pop(i)
                    year.pop(i)
                    break

            name22 = Label(op2, text=entry.get(), font=('Arial', 13))
            name33 = Label(op2, text=entry1.get(), font=('Arial', 13))
            name44 = Label(op2, text=entry0.get(), font=('Arial', 13))
            name55 = Label(op2, text=entry01.get(), font=('Arial', 13))
            name66 = Label(op2, text=entry02.get(), font=('Arial', 13))
            if name44.cget('text') == 'Hiện tại' and name55.cget('text') == 'Hiện tại' and name66.cget(
                    'text') == 'Hiện tại' and name33.cget('text').isdigit():
                day.append(int(now.strftime("%d")))
                month.append(int(now.strftime("%m")))
                year.append(int(now.strftime("%Y")))
                chi_tieu.append(name22.cget('text'))
                chi_tieu1.append(float(name33.cget('text')))
            elif name33.cget('text').isdigit() and name44.cget('text').isdigit() and int(name44.cget('text')) < 32 and int(
                    name44.cget('text')) > 0 and name55.cget('text').isdigit() and int(name55.cget('text')) < 12 and int(
                    name55.cget('text')) > 0 and name66.cget('text').isdigit() and int(name66.cget('text')) < 2100 and int(
                    name66.cget('text')) > 1900:
                day.append(int(name44.cget('text')))
                month.append(int(name55.cget('text')))
                year.append(int(name66.cget('text')))
                chi_tieu.append(name22.cget('text'))
                chi_tieu1.append(float(name33.cget('text')))
            else:
                messagebox.showerror("Lỗi", "Vui lòng nhập thông tin hợp lệ!")

            for frame in op2.winfo_children():
                frame.destroy()

            name22 = Label(op2, text=name22.cget('text'), font=('Arial', 13))
            name33 = Label(op2, text=name33.cget('text'), font=('Arial', 13))
            name44 = Label(op2, text=name44.cget('text'), font=('Arial', 13))
            name55 = Label(op2, text=name55.cget('text'), font=('Arial', 13))
            name66 = Label(op2, text=name66.cget('text'), font=('Arial', 13))
            name22.place(x=10, y=10)
            name33.place(x=10, y=40)
            name44.place(x=10, y=70)
            name55.place(x=10, y=100)
            name66.place(x=10, y=130)

        entry = Entry(op2, width=20, font=('Arial', 13))
        entry.place(x=150, y=10)
        entry1 = Entry(op2, width=20, font=('Arial', 13))
        entry1.place(x=150, y=40)
        entry2 = Entry(op2, width=20, font=('Arial', 13))
        entry2.place(x=150, y=70)
        entry3 = Entry(op2, width=20, font=('Arial', 13))
        entry3.place(x=150, y=100)
        entry4 = Entry(op2, width=20, font=('Arial', 13))
        entry4.place(x=150, y=130)

        entry.insert(0, name)
        entry1.insert(0, name1)
        entry2.insert(0, name2)
        entry3.insert(0, name3)
        entry4.insert(0, name4)

        button2 = Button(op2, text='Cập Nhật', style='TButton', command=update)
        button2.place(x=150, y=170)

    table.bind("<Double-1>", update_item)


def click4():
    delete()

    df = pd.DataFrame({'Ngày': day, 'Tháng': month, 'Năm': year, 'Số Tiền': chi_tieu1})
    df['Thời Gian'] = pd.to_datetime(df[['Ngày', 'Tháng', 'Năm']])
    df.set_index('Thời Gian', inplace=True)

    def visualize():
        regr = linear_model.LinearRegression()
        regr.fit(df.index.values.reshape(-1, 1), df['Số Tiền'].values.reshape(-1, 1))
        plt.scatter(df.index, df['Số Tiền'], color='blue')
        plt.plot(df.index, regr.predict(df.index.values.reshape(-1, 1)), color='red', linewidth=3)
        plt.title('Biểu Đồ Chi Tiêu Theo Thời Gian')
        plt.xlabel('Thời Gian')
        plt.ylabel('Số Tiền')
        plt.show()

    button2 = Button(op2, text='Hiển Thị Biểu Đồ', style='TButton', command=visualize)
    button2.place(x=10, y=10)


s = Style()
s.configure('TButton', font=('Arial', 13))

delete()
ma = Label(op, text='QUẢN LÍ CHI TIÊU', font=('Arial', 20), bg='black', fg='white')
ma.place(x=250, y=10)

button = Button(op, text='Thêm Chi Tiêu', style='TButton', command=click1)
button.place(x=10, y=100)

button1 = Button(op, text='Thêm Thu Nhập', style='TButton', command=click2)
button1.place(x=10, y=150)

button2 = Button(op, text='Danh Sách', style='TButton', command=click3)
button2.place(x=10, y=200)

button3 = Button(op, text='Biểu Đồ', style='TButton', command=click4)
button3.place(x=10, y=250)

op.place(x=0, y=0)
op2.place(x=200, y=50)
win.mainloop()

