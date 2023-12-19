import tkinter as tk

win = tk.Tk()

win.geometry("325x350")

win.title(" Simple Calculator")

input_value = ""

display_text = tk.StringVar()

def click_button_action(item):
    global input_value
    input_value = input_value + str(item)
    display_text.set(input_value)

def clear_button_action():
    global input_value
    input_value = ""
    display_text.set("")

def equal_button_action():
    global input_value
    result = str(eval(input_value))
    display_text.set(result)
    input_value = ""

input_frame = tk.Frame(win, width=325, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                       highlightthickness=2)

input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=display_text, width=50, bg="#eee", bd=0,
                       justify=tk.RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)
buttons_frame = tk.Frame(win, width=300, height=270, bg="grey")

buttons_frame.pack()

clear_button = tk.Button(buttons_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
                      command=lambda: clear_button_action()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide_button = tk.Button(buttons_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                       command=lambda: click_button_action("/")).grid(row=0, column=3, padx=1, pady=1)

button_7 = tk.Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: click_button_action(7)).grid(row=1, column=0, padx=1, pady=1)

button_8 = tk.Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: click_button_action(8)).grid(row=1, column=1, padx=1, pady=1)

button_9 = tk.Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: click_button_action(9)).grid(row=1, column=2, padx=1, pady=1)

multiply_button = tk.Button(buttons_frame, text="X", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                         command=lambda: click_button_action("*")).grid(row=1, column=3, padx=1, pady=1)


button_4 = tk.Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: click_button_action(4)).grid(row=2, column=0, padx=1, pady=1)

button_5 = tk.Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: click_button_action(5)).grid(row=2, column=1, padx=1, pady=1)

button_6 = tk.Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: click_button_action(6)).grid(row=2, column=2, padx=1, pady=1)

subtraction_button = tk.Button(buttons_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                      command=lambda: click_button_action("-")).grid(row=2, column=3, padx=1, pady=1)

button_1 = tk.Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: click_button_action(1)).grid(row=3, column=0, padx=1, pady=1)

button_2 = tk.Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: click_button_action(2)).grid(row=3, column=1, padx=1, pady=1)

button_3 = tk.Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: click_button_action(3)).grid(row=3, column=2, padx=1, pady=1)

Additon_button = tk.Button(buttons_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                     command=lambda: click_button_action("+")).grid(row=3, column=3, padx=1, pady=1)

button_0 = tk.Button(buttons_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: click_button_action(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point_button = tk.Button(buttons_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                      command=lambda: click_button_action(".")).grid(row=4, column=2, padx=1, pady=1)

equals_button = tk.Button(buttons_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                       command=lambda: equal_button_action()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()