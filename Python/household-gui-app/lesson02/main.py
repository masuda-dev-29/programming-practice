import tkinter as tk
root = tk.Tk()
root.title("Household GUI App")
label = tk.Label(root, text="家計簿アプリ")
button = tk.Button(root, text="追加")

label.pack()
button.pack()

root.mainloop()