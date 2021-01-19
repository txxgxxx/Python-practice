import tkinter as tk
window = tk.Tk()
class First_Frame:
    import tkinter as tk
    def __init__ (self):
        from main_module import switch_frame
        self.original_frame = tk.Frame(window)
        self.original_frame.pack()

        self.tk.Label(self.original_frame, text='Welcome', font=('Helvetica', 18, 'bold')).pack()
        self.tk.Button(self.original_frame, text='Go to order', font=('Helvetica', 18, 'bold'),
                       command=lambda: switch_frame(Frame2.order_frame, self.original_frame)).pack()


class Second_Frame:
    def __init__(self):
        self.order_frame = tk.Frame(window)
        self.order_frame.pack()
    def object(self):
        from main_module import switch_frame
        self.tk.Label(self.order_frame, text='Order', font=('Helvetica', 18, 'bold')).pack(side='top')



Frame1 = First_Frame()
Frame2 = Second_Frame()































window.title("Cafe")
window.geometry("640x400+100+100")
window.resizable(False, False)
window.mainloop()


#main_module

def switch_frame(open_frame, close_frame):
    close_frame.destroy()
    open_frame.pack()
