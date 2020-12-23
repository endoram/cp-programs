from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('CyberPatriot Editor')
#root.iconbitmap('/home/ken/Documents/git/cpedit/squadronlogo2.ico')
#root.iconphoto(True, PhotoImage(file="/home/ken/Documents/git/cpedit/squadronlogo2.ico"))
#root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='squadronlogo2.ico'))
root.geometry("1200x660")

# Create New File Fuction
def new_file():
    my_text.delete("1.0", END)
    status_bar.config(text="New File   ")

def open_file():
    # Delete prvious text
    my_text.delete("1.0", END)

    # Grab Filename
    text_file = filedialog.askopenfilename(initialdir = "/home/ken/Documents/git/cpedit", title = "Open File", filetypes = (("text files", ".txt"), ("all Files", "*.*")))
    # Update Status Bar
    name = text_file
    status_bar.config(f'{name}        ')
    name = name.replace("/home/ken/Documents/git/cpedit", "")
    root.title(f'{name} - CyberPatriot Editor')

    # Open the File
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # Add file to textbox
    my_text.insert(END, stuff)
    # Close the opened file
    text_file.close()

# Create Main Frame
my_frame = Frame(root)
my_frame.pack(fill=X)

# Create Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
my_text = Text(my_frame, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
#width=97, height=25,
my_text.pack(side=LEFT, fill=BOTH, expand=YES)

# Configure Scroolbar
text_scroll.config(command=my_text.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_separator()
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add Status Bar to the bottom of main window
status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)



root.mainloop()
