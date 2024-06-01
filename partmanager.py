from tkinter import *
from db import Database
from tkinter import messagebox

db = Database('data_store.db')


def populate():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


def select_items(event):
    try:

        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])

        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])

        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])

        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def add_items():
    if part_text.get == '' or customer_text.get() == '' or retailer_text.get() == '':
        messagebox.showerror('Required Field', 'Fill in the Blank space!')
        return

    db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))

    clear_items()
    populate()


def update_items():
    db.update(selected_item[0], part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    clear_items()
    populate()


def remove_items():
    db.remove(selected_item[0])
    clear_items()
    populate()


def clear_items():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)


# to create a window
window = Tk()

# part
part_text = StringVar()
part_label = Label(window, text='Part Name', font=('bold', 12))
part_label.grid(row=0, column=0, pady=20, sticky=W)

part_entry = Entry(window, textvariable=part_text)
part_entry.grid(row=0, column=1, )

# Customer
customer_text = StringVar()
customer_label = Label(window, text='Custome', font=('bold', 12))
customer_label.grid(row=0, column=2, sticky=W)

customer_entry = Entry(window, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# Retailer
retailer_text = StringVar()
retailer_label = Label(window, text='Retailer', font=('bold', 12))
retailer_label.grid(row=1, column=0, sticky=W)

retailer_entry = Entry(window, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

# price
price_text = IntVar()
price_label = Label(window, text='Price', font=('bold', 12))
price_label.grid(row=1, column=2, sticky=W)

price_entry = Entry(window, textvariable=price_text)
price_entry.grid(row=1, column=3)

# create a parts_list (Listbox)
parts_list = Listbox(window, height=10, width=70, border=0)
parts_list.grid(row=3, column=0, sticky=W, rowspan=6, columnspan=3, pady=20, padx=20)

# to create scrollbar
scrollbar = Scrollbar(window)
scrollbar.grid(row=3, column=3)

# to set a scrollbar
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# to bind Listbox with select_items()
parts_list.bind('<<ListboxSelect>>', select_items)

# to create buttons
add_btn = Button(window, text='Add', width=10, command=add_items)
add_btn.grid(row=2, column=0, pady=20)

update_btn = Button(window, text='Update', width=10, command=update_items)
update_btn.grid(row=2, column=1)

remove_btn = Button(window, text='Remove', width=10, command=remove_items)
remove_btn.grid(row=2, column=2)

clear_btn = Button(window, text='Clear', width=10, command=clear_items)
clear_btn.grid(row=2, column=3)
# to set the size of the windowclearndow.geometry('720x350')

# to create title
window.title('Part Manager Application')

# to populate the Listbox
populate()

# to start a program
window.mainloop()
