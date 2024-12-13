from gui1 import *

def main():
    window = Tk()
    window.title('Project 1.1')
    window.geometry('500x500')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()