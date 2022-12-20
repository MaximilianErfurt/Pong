

import tkinter
fenster = tkinter.Tk()
width = fenster.winfo_screenwidth()
height = fenster.winfo_screenheight()
fenster.state('zoomed')

label = tkinter.Label(text='Hallo, Leute', font='Arial 24')
label.pack()
fenster.mainloop()



