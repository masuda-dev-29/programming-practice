import tkinter as tk
root = tk.Tk()
root.title("Household GUI App")

label_title = tk.Label(root, text="家計簿アプリ")
label_title.pack()

label_amount = tk.Label(root, text="金額")
label_amount.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="追加")
button.pack()


root.mainloop()