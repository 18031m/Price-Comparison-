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
root.title("My App")

# Create the frame
frame = tk.Frame(root, width=300, height=200)
frame.pack()

# Add some widgets to the frame
label = tk.Label(frame, text="Hello, world!")
label.pack()

button = tk.Button(frame, text="Click me!")
button.pack()

# Run the main loop
root.mainloop()