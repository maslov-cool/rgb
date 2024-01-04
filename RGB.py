import tkinter


def color(r, g, b):
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, bg='#' + ''.join([r, g, b]), height=300, width=600)
    canvas.grid()
    window.mainloop()


r1, g1, b1 = int(input()), int(input()), int(input())
r1, g1, b1 = [hex(int(i))[2:] if i != '0' else '00' for i in [r1, g1, b1]]
color(r1, g1, b1)
