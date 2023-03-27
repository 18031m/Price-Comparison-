'''
  Name: 
  James Hargest College
  Programming Internal for 2.7 & 2.8 ~ 12 credits
  Due: 6 April 2023
  
  TIP: Use assessment guide to help guide you through this Internal
'''

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My Simple GUI")

# Create a label
my_label = tk.Label(root, text="Hello, World!")
my_label.pack()

# Create a button
my_button = tk.Button(root, text="Click me!")
my_button.pack()

# Run the main loop
root.mainloop()
