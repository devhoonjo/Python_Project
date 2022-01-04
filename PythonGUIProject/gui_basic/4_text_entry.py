from tkinter import *

root = Tk()

root.title("Hoon GUI")
root.geometry("640x480+500+150") #가로 X 세로


txt = Text(root, width=30, height=5) #여러줄에 걸쳐 입력
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) #한줄만 입력 가능로그인 아이디 닉네임 같은거
e.pack()
e.insert(0, "한줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1: 첫번쨰라인, 0: 0번쨰 컬럼 위치
    print(e.get())
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않W도록
