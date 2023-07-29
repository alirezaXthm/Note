import os
from tkinter import *
from tkinter import colorchooser, font, filedialog
from tkinter.messagebox import *
from tkinter.filedialog import *

    # functions
def change_color():
    color = colorchooser.askcolor(title='Pick a Color')[1]
    print(color)
    text_area.config(fg = color)


def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))
    

def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)

    
def open_file():
    file = askopenfilename(defaultextension=".txt", filetypes=(("All files", "*.*"), ("Text", "*.txt")), )
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)
        file = open(file, 'r')
        text_area.insert(1.0, file.read())

    except Exception:
        print("could nont open file")
            
    finally:
        file.close()


def save_file():
    file = filedialog.asksaveasfile(initialdir='Desktop', title='Save the FUCKING file',
                                          filetypes=(('.txt', '*.txt'), ('all', '*.*')),
                                          defaultextension='.txt'
                                          )
    if file == None:
        return
    else:
        try:
            file_text = str(text_area.get(1.0, END))
            file.write(file_text)
            file.close()
    
        except Exception:
            print("could not find your fucking file ")
    
        finally:
            file.close()


def cut():
    text_area.event_generate("<<Cut>>")
    
    
def copy():
    text_area.event_generate("<<Copy>>")

    
def paste():
    text_area.event_generate("<<Paste>>")
    

def about():
    showinfo('my info', message='https://github.com/alirezaXthm')
    

def quit():
    window.destroy()
    

    # window config
window = Tk()
window.title('Note')
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int(screen_width/2 - window_width/2)
y = int(screen_height/2 - window_height/2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

file = None

font_name = StringVar(window)
font_name.set('arial')
font_size = StringVar(window)
font_size.set(25)

    # frame, text_area and font config

text_area = Text(window, font=(font_name.get(), font_size.get()))
scroll_bar = Scrollbar(text_area)
frame = Frame(window)
color_bottun = Button(frame, text='color', command= change_color)
font_box = OptionMenu(frame, font_name, *font.families(), command = change_font)
size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command= change_font)
menu_bar = Menu(window)
window.config(menu=menu_bar)

    # file menu_bar config

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="file", menu = file_menu)
file_menu.add_command(label="new", command = new_file)
file_menu.add_command(label="open", command = open_file)
file_menu.add_command(label="save", command = save_file)
file_menu.add_separator()
file_menu.add_command(label='exit', command=quit)

    # edit menu_bar config
    
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='edit', menu=edit_menu)
edit_menu.add_command(label='cut', command=cut)
edit_menu.add_command(label='copy', command=copy)
edit_menu.add_command(label='paste', command=paste)

    # about menu_bar config
    
about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='About', menu=about_menu)
about_menu.add_command(label='me', command=about)

    # packs and grids

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)
text_area.grid(sticky=N+E+S+W)
frame.grid()
color_bottun.grid(row=0, column=0)
font_box.grid(row=0, column=1)
size_box.grid(row=0, column=2)
window.mainloop()