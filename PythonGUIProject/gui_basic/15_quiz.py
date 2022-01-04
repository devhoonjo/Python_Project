import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")

# root.resizable(True, False)

menu = Menu(root)

file_name = "mynote.txt"

def open_file():
    if os.path.isfile(file_name):
        with open(file_name, "r", encoding="utf8") as file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용을 본문에 입력


def save_file():
    with open(file_name, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))



menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)


menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=menu_edit)


menu_seo = Menu(menu, tearoff=0)
menu.add_cascade(label="서식", menu=menu_seo)


menu_bogi = Menu(menu, tearoff=0)
menu.add_cascade(label="보기", menu=menu_bogi)


menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="도움말", menu=menu_help)


#스크롤바
scroll_bar = Scrollbar(root)
scroll_bar.pack(side="right", fill="y")



#본문 영역
txt = Text(root, yscrollcommand=scroll_bar.set)
txt.pack(side="left", fill="both", expand=True)

scroll_bar.config(command=txt.yview)

root.config(menu=menu)

root.mainloop()

