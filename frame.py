import tkinter as tk 
from tkinter import ttk 
def _init_(self,root): 
    the_label.pack(in_=tab1, expand=True, padx=20, pady=20) 
def _init_(self,root): 
    the_label.pack(in_=tab2, expand=True, padx=20, pady=20)
root = tk.Tk() 

notebook = ttk.Notebook(root) 
toolbar = ttk.Frame(root) 

toolbar.pack(side="top", fill="x") 
notebook.pack(side="top", fill="both", expand=True) 

tab1 = ttk.Frame(notebook) 
tab2 = ttk.Frame(notebook) 
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2") 
the_label = tk.Label(notebook, text="Click a button to move me") 
b1 = tk.Button(toolbar, text="Move to tab 1", command=tab1) 
b2 = tk.Button(toolbar, text="Move to tab 2", command=tab2) 
b1.pack(side="left") 
  
b2.pack(side="left") 
# initialize it to be on the first tab moveToOne() 
root.mainloop()