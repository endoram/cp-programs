from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('CyberPatriot Editor')
# Tests if Windows for icon
if (sys.platform.startswith('win')):
    root.iconbitmap('squadronlogo.ico')
else:
    logo = PhotoImage(file='squadronlogo.gif')
    root.call('wm', 'iconphoto', root._w, logo)
# Use Below if you are only on Linux
#root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='squadronlogo.gif'))
root.geometry("1200x660")

# Set variable for Open Filename
global open_status_name
open_status_name = False

# Create New File Fuction
def new_file():
    my_text.delete("1.0", END)
    status_bar.config(text="New File   ")
    global open_status_name
    open_status_name = False

def open_file():
    # Delete prvious text
    my_text.delete("1.0", END)

    # Grab Filename
    text_file = filedialog.askopenfilename(initialdir = "/home/ken/Documents/git/cp-programs/cpedit/", title = "Open File", filetypes = (("all Files", "*.*"),("text files", ".txt")))
    # Check to see if there is a Filename
    if text_file:
        # Make Filename Global
        global open_status_name
        open_status_name = text_file

    # Update Status Bars
    name = text_file
    status_bar.config(text=f'{name}        ')
    name = name.replace("/home/ken/Documents/git/cp-programs/cpedit/", "")
    root.title(f'{name} CyberPatriot Editor')

    # Open the File
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # Add file to textbox
    my_text.insert(END, stuff)
    # Close the opened file
    text_file.close()


# Save As File
def save_as_file():
    text_file = filedialog.asksaveasfilename(initialdir="/home/ken/Documents/git/cp-programs/cpedit/", title="Save File", filetypes=(("all Files", ".*"),("text files", ".txt")))
    if text_file:
        # Update Status Bars
        name = text_file
        status_bar.config(text=f'Saved: {name}        ')
        name = name.replace("/home/ken/Documents/git/cp-programs/cpedit/", "")
        root.title(f'{name} - CyberPatriot Editor')
        # Save the File
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close the File
        text_file.close()

# Save File
def save_file():
    global open_status_name
    if open_status_name:
        # Save the File
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        # Close the File
        text_file.close()

        status_bar.config(text=f'Saved: {open_status_name}        ')
    else:
        # Save the already open file
        # This is different than on Windows where you can just call the save_as_file()
        global open_satus_name
        filename = filedialog.asksaveasfile(mode='w')
        file_save()


# Create Main Frame
my_frame = Frame(root)
my_frame.pack(fill=BOTH, expand=True)

# Create Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
my_text = Text(my_frame, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
#width=97, height=25,
my_text.pack( fill=BOTH, expand=YES)
#side=LEFT,

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
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
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
status_frame = Frame()
status_frame.pack(fill=BOTH, side=BOTTOM, expand=False)
status_bar = Label(status_frame, text='Ready    ', anchor=E)
status_bar.pack(fill=BOTH, side=BOTTOM, ipady=5)

#

root.mainloop()
