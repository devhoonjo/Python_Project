from tkinter import *


root = Tk()

root.title("Hoon GUI")
root.geometry("640x480+500+150")  # 가로 X 세로

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")


frame_burger = Frame(root, relief="solid", bd=1) #릴리프 테두리 모양, bd = 테두리 외곽선 표시
frame_burger.pack(side="left", fill="both", expand=True)
Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

frame_drink = LabelFrame(root, text = "음료")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="환타").pack()
Button(frame_drink, text="사이다").pack()


root.mainloop()  # 창이 닫히지 않W도록
