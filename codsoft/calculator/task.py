import tkinter as tk

def click(event):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + event.widget.cget("text"))

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry widget
entry = tk.Entry(root, font=("Arial", 20), borderwidth=3, relief="ridge", justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        button = tk.Button(frame, text=btn, font=("Arial", 18), borderwidth=1)
        button.pack(side="left", expand=True, fill="both")

        if btn == "=":
            button.config(command=evaluate)
        elif btn == "C":
            button.config(command=clear)
        else:
            button.bind("<Button-1>", click)

# Run the app
root.mainloop()