from tkinter import *

root = Tk()

root.title("Hoon GUI")
root.geometry("640x480") #가로 X 세로
# root.geometry("640x480+300+100") #가로 X 세로 x좌표  y좌표

root.resizable(False, False) #x(너비), y(높이) 값 변경 불가 (창 크기)


root.mainloop() #창이 닫히지 않W도록
