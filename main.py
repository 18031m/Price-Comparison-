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
    items_listbox.insert(tk.END, item)
    item_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("My Simple GUI")

# Create a label
my_label = tk.Label(root, text="Enter items:")
my_label.pack()

# Create an entry for the user to input items
item_entry = tk.Entry(root)
item_entry.pack()

# Create a button to add items to the listbox
add_button = tk.Button(root, text="Add", command=add_item)
add_button.pack()

# Create a listbox to display the items
items_listbox = tk.Listbox(root)
items_listbox.pack()

# Run the main loop
root.mainloop()