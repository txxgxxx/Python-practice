import tkinter as tk


window = tk.Tk()
window.title("Cafe")
window.geometry("640x400+100+100")
window.resizable(False, False)


# def drive_frame(frame):
#     frame.tkraise()

welcome_frame = tk.Frame(window)
order_frame = tk.Frame(window)
total_frame = tk.Frame(window)

def switch_frame(open_frame, close_frame):
    close_frame.destroy()
    open_frame.pack()

welcome_frame.pack()
tk.Label(welcome_frame, text='Welcome', font=('Helvetica', 18, 'bold')).pack()
tk.Button(welcome_frame, text='Go to order', command=lambda: switch_frame(order_frame, welcome_frame)).pack()


tk.Label(order_frame, text='Order', font=('Helvetica', 18, 'bold')).pack()
total = {'price': 0}
americano = {'name': 'americano', 'price': 3000, 'kind': 'coffee', 'num': 0}
latte = {'name': 'latte', 'price': 3500, 'kind': 'coffee', 'num': 0}
def order_total():
    tk.Label(order_frame, text=total).pack()
def total_button():
    total_price = total['price']
    tk.Label(total_frame, text=("총 %d원"%total_price), font=('Helvetica', 18, 'bold')).pack()
    tk.Button(total_frame, text=('주문해주셔서 감사합니다.'), font=('Helvetica', 18, 'bold'), command=lambda: window.quit()).pack()


def order_order(menu):
    global total
    global total_order
    if menu == americano:
        total['price'] += americano['price']
        americano['num'] += 1
        menu_1.config(text=americano['name'] + str(americano['num']))
        total_order.config(text=total)
    elif menu == latte:
        total['price'] += latte['price']
        latte['num'] += 1
        menu_2.config(text=latte['name'] + str(latte['num']))
        total_order.config(text=total)
menu_button_1 = tk.Button(order_frame, text=americano['name'], command=lambda: order_order(americano))
menu_button_2 = tk.Button(order_frame, text=latte['name'], command=lambda: order_order(latte))
menu_button_3 = tk.Button(order_frame, text='print', command = lambda: order_total())
menu_1 = tk.Label(order_frame, text=americano['name'] + str(americano['num']))
menu_2 = tk.Label(order_frame, text=latte['name'] + str(latte['num']))
total_order = tk.Label(order_frame, text=total)
menu_button_1.pack()
menu_button_2.pack()
menu_button_3.pack()
menu_1.pack()
menu_2.pack()
total_order.pack()
tk.Button(order_frame, text='결제', command=lambda: (total_button(), switch_frame(total_frame, order_frame))).pack()




window.mainloop()