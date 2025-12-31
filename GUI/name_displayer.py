import tkinter as tk

#function
def update_label():
    name = entry.get()
    label.config(text=f"Hello , {name}!")

#creating main window
root = tk.Tk()
root.title("Name displayer")
root.geometery("300x300")    

#creating label and packing it

label = tk.Label(root ,text="Enter your name" )
label.pack(pady=5)

#creating input and packing it

entry = tk.Entry(root)
entry.pack(pady=5)

#creating button and packing it 

button = tk.Button(root , text= "Submit" , command = update_label)
button.pack(pady=5)

#run
root.mainloop()