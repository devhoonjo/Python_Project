from tkinter import *


root = Tk()

root.title("Hoon GUI")
root.geometry("640x480+500+150")  # 가로 X 세로

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")


scrollbar.config(command=listbox.yview)

root.mainloop()  # 창이 닫히지 않W도록
