import time
import tkinter.ttk as ttk
from tkinter import *


root = Tk()

root.title("Hoon GUI")
root.geometry("640x480+500+150")  # 가로 X 세로

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") #indeterminate : 결정되지 않은, 
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") 
# progressbar.start(5) #5 ms 마다 움직임
# progressbar.pack()



# def btncmd():
#     progressbar.stop() #작동중지


# btn = Button(root, text="중지", command=btncmd)
# btn.pack()


P_var2 = DoubleVar() #실수값도 반영하기 위해 double
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=P_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01) # 0.01초 대기

        P_var2.set(i)
        progressbar2.update()
        print(P_var2.get())



btn = Button(root, text="시작", command=btncmd2)
btn.pack()








root.mainloop()  # 창이 닫히지 않W도록
