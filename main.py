'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''

import tkinter as tk

# Function to add items to the listbox
def add_item():
    item = item_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    items_listbox.insert(tk.END, f"{item} ({quantity}): ${price}")
    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    add_new_item()

# Function to add a new item
def add_new_item():
    new_item = tk.messagebox.askyesno("Add New Item", "Do you want to add a new item?")
    if new_item:
        item_entry.focus()
    else:
        item_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        item_entry.focus()

# Create the main window
root = tk.Tk()
root.title("My Simple GUI")
root.geometry("400x400") # Set the width to 400 pixels and height to 300 pixels

# Create a label for budget and entry field for budget
budget_label = tk.Label(root, text="Enter your budget:")
budget_label.pack()
budget_entry = tk.Entry(root)
budget_entry.pack()

# Create a label for item name and entry field for item name
item_label = tk.Label(root, text="Enter item name:")
item_label.pack()
item_entry = tk.Entry(root)
item_entry.pack()

# Create a label for item price and entry field for item price
price_label = tk.Label(root, text="Enter item price:")
price_label.pack()
price_entry = tk.Entry(root)
price_entry.pack()

# Create a label for item quantity and entry field for item quantity
quantity_label = tk.Label(root, text="Enter item quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

# Create a button to add items to the listbox
add_button = tk.Button(root, text="Add", command=add_item)
add_button.pack()

# Create a listbox to display the items
items_listbox = tk.Listbox(root)
items_listbox.pack()

# Run the main loop
root.mainloop()