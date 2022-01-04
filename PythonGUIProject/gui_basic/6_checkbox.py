from tkinter import *

root = Tk()

root.title("Hoon GUI")
root.geometry("640x480+500+150") #가로 X 세로

chkvar = IntVar()
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.select() #자동 선택
chkbox.deselect() #선택해제
chkbox.pack()


chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get()) # 0 : 체크가 안된상태, 1: 체크가 된 상태
    print(chkvar2.get()) # 0 : 체크가 안된상태, 1: 체크가 된 상태


btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않W도록
