import tkinter as tk
root = tk.Tk()
root.title("Lesson04")

#関数定義
def show_message():
    print("ボタンがクリックされました")

def hello_msg():
    print("こんにちは")

def end_msg():
    print("さようなら")

#オブジェクト定義
button = tk.Button(root, text="クリック", command=show_message)
button_hello = tk.Button(root, text="挨拶", command=hello_msg)
button_end = tk.Button(root, text="終了", command=end_msg)


#配置

button.pack()
button_hello.pack()
button_end.pack()


#表示

root.mainloop()