import tkinter as tk
root=tk.Tk()
text_box=tk.Text()
text_box.pack()
st="tera baap aaya"
text_box.insert("2.0",st)
text_box.insert("2.0","\ntu asdasd")
text_box.insert(tk.END,"\nput me in the end")
root.mainloop()