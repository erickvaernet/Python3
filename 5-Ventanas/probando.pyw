from Tkinter import *


def main():
    window = Tk()
    window.title("TexComp")
    window.geometry("500x500")
    window.resizable(height=FALSE, width=FALSE)

    windowBackground = '#E3DCA8'

    window.configure(bg=windowBackground)

    instruction = Label(
        text="Type or paste your text into one box,\nthen paste the text you want to compare it too\ninto the other one.", bg=windowBackground)
    instruction.place(x=115, y=10)

    text1 = Text(width=25)
    text1.pack(side=LEFT)
    text2 = Text(width=25)
    text2.pack(side=RIGHT)

    scroll1y = Scrollbar(window, command=text1.yview)
    scroll1y.pack(side=LEFT, fill=Y, pady=65)
    scroll2y = Scrollbar(window, command=text2.yview)
    scroll2y.pack(side=RIGHT, fill=Y, pady=65)

    mainloop()


if __name__ == '__main__':
    main()
