import tkinter as tk
def click(event):
    current = display.get()
    text = event.widget.cget('text')
    if text == "=":
        result = eval(current)
        display.delete(0,tk.END)
        display.insert(tk.END,result)
    elif text=="c":
        display.delete(0,tk.END)
    else:
        display.insert(tk.END,text)

window = tk.Tk()
window.title("my calculator")
window.config(bg="#cfdba0")
window.resizable(False,False)
window.iconbitmap("./calculator.ico")
window.attributes("-topmost",1)
display=tk.Entry(window,font=("Arial",25),justify="right",bg="#7e9682")
display.pack(fill=tk.X,padx=10,pady=10,ipady=10)
btn_frame = tk.Frame(window)
btn_frame.config(bg="#838a6a")
btn_frame.pack()
button_labels = [
    "(",")","%","**",
    "7","8","9","+",
    "4","5","6","-",
    "1","2","3","*",
    "c","0","=","/"
]
i=0
for label in button_labels:
    button=tk.Button(btn_frame,text=label,font=("Arial",20),padx=20,pady=20,bg="#31de4e")
    
    button.grid(row=i//4,column=i%4,padx=10,pady=10)
    button.bind("<Button-1>",click)
    i=i+1
window.mainloop()
