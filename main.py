from userInterface import *
       
        
def main():
    win = Tk()
    win.title("Snake and Ladder")
    win.geometry("850x600")
    img = PhotoImage( file="background.gif")
    x = Display(win, img)
    win.mainloop()


main()
