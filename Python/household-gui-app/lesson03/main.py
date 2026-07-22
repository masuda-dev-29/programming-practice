import tkinter as tk
root = tk.Tk()
root.title("Household GUI App")


#オブジェクト定義

label_name = tk.Label(root, text="名前")
entry_name = tk.Entry(root)

label_age = tk.Label(root, text="年齢")
entry_age = tk.Entry(root)

button = tk.Button(root, text="登録")


#配置

label_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_name.grid(row=0, column=1, padx=5, pady=5)
label_age.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_age.grid(row=1, column=1, padx=5, pady=5)
button.grid(row=2, column=1, padx=5, pady=10)


#表示

root.mainloop()