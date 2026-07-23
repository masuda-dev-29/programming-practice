import tkinter as tk
root = tk.Tk()
root.title("Lesson05")

# 関数定義
def show_status():
    print("名前 : " + name_entry.get())
    print("年齢 : " + age_entry.get())

# ラベル
name_label = tk.Label(root, text="名前")
age_label = tk.Label(root, text="年齢")


# 入力欄
name_entry = tk.Entry(root)
age_entry = tk.Entry(root)

# ボタン
button = tk.Button(root, text="表示", command=show_status)


# 配置
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
age_label.grid(row=1, column=0)
age_entry.grid(row=1, column=1)
button.grid(row=2, column=1)

# 表示

root.mainloop()