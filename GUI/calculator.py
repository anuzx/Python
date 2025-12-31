import tkinter as tk

def add_func():
    n1 = float(num1.get())
    n2 = float(num2.get())
    ans = n1+n2
    label.config(text=f"Answer is:  {ans}")

def sub_func():
    n1 = float(num1.get())
    n2 = float(num2.get())
    ans = n1-n2
    label.config(text=f"Answer is:  {ans}") 

def multi_func():
    n1 = float(num1.get())
    n2 = float(num2.get())
    ans = n1*n2
    label.config(text=f"Answer is:  {ans}") 

def div_func():
    n1 = float(num1.get())
    n2 = float(num2.get())
    if n2 == 0 :
        label.config(text="Cannot divide by zero")
    else:      
      ans = n1/n2
      label.config(text=f"Answer is:  {ans}")          

def clear_func():
    num1.delete(0, tk.END)
    num2.delete(0, tk.END)
    label.config(text="Enter two numbers")

    


#creating main window
root = tk.Tk()
root.title("CALCULATOR")
root.geometry("500x500")


#creating label and packing it 
label = tk.Label(root , text="Enter two numbers")  
label.pack(pady=5)  

#creating input box and packing it
num1 = tk.Entry(root)
num1.pack(pady=5)
num2 = tk.Entry(root)
num2.pack(pady=5)

#creating buttons and packing it
add_button = tk.Button(root , text="+" , command=add_func)
add_button.pack(pady=5)
sub_button = tk.Button(root , text="-" , command=sub_func)
sub_button.pack(pady=5)
multi_button= tk.Button(root , text="*" , command = multi_func)
multi_button.pack(pady=5)
div_button = tk.Button(root , text="/" , command=div_func)
div_button.pack(pady=5)
clear_button = tk.Button(root, text="Clear", command=clear_func)
clear_button.pack(pady=5)


#run
root.mainloop()