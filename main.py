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

# Function to calculate the highest value item
def calculate_highest_value():
    highest_value_item = ""
    highest_value = 0
    for item in items_listbox.get(0, tk.END):
        item_info = item.split(":")
        item_price = float(item_info[1][1:])
        item_quantity = int(item_info[0].split("(")[-1][:-1])
        item_total_value = item_price * item_quantity
        if item_total_value > highest_value:
            highest_value = item_total_value
            highest_value_item = item
    highest_value_textbox.delete("1.0", tk.END)
    highest_value_textbox.insert(tk.END, f"The highest value item is {highest_value_item} with a total value of ${highest_value}")

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
root.geometry("400x400")

# Create a label for budget and entry field for budget
budget_label = tk.Label(root, text="Enter your budget:")
budget_label.pack()
budget_entry = tk.Entry(root, width=30)
budget_entry.pack()

# Create a label for item name and entry field for item name
item_label = tk.Label(root, text="Enter item name:")
item_label.pack()
item_entry = tk.Entry(root, width=30)
item_entry.pack()

# Create a label for item price and entry field for item price
price_label = tk.Label(root, text="Enter item price:")
price_label.pack()
price_entry = tk.Entry(root, width=30)
price_entry.pack()

# Create a label for item quantity and entry field for item quantity
quantity_label = tk.Label(root, text="Enter item quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(root, width=30)
quantity_entry.pack()

# Create a button to add items to the listbox
add_button = tk.Button(root, text="Add", command=add_item)
add_button.pack()

# Create a listbox to display the items
items_listbox = tk.Listbox(root, width=50)
items_listbox.pack()

# Create a button to calculate the highest value item
highest_value_button = tk.Button(root, text="Calculate Highest Value Item", command=calculate_highest_value)
highest_value_button.pack()

# Create a text box to display the highest value item
highest_value_textbox = tk.Text(root, width=50, height=3)
highest_value_textbox.pack()

# Run the main loop
root.mainloop()
