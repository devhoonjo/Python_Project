from tkinter import *


root = Tk()

root.title("Hoon GUI")
root.geometry("640x480+500+150")  # 가로 X 세로

def create_new_file():
    print("새 파일을 만듭니다.")


menu = Menu(root)


#file 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window", )
menu_file.add_separator() #구분자
menu_file.add_command(label="Open File...")
menu_file.add_separator() #구분자
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator() #구분자
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)



#edit 메뉴
menu.add_cascade(label="Edit")


#language 메뉴
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="C++")
menu_lang.add_radiobutton(label="JAVA")
menu_lang.add_radiobutton(label="JS")
menu_lang.add_radiobutton(label="PYTHON")
menu.add_cascade(label="language", menu=menu_lang)



#checkbox
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu_view.add_checkbutton(label="Show enemy")
menu_view.add_checkbutton(label="Show character")
menu_view.add_checkbutton(label="Show HP")
menu.add_cascade(label="View", menu=menu_view)







root.config(menu=menu)

root.mainloop()  # 창이 닫히지 않W도록
