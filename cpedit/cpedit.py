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
root.geometry("1200x680")

# Global Variables
# Set variable for Open Filename
global open_status_name
open_status_name = False

global selected
selected = False



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

# Cut Text
def cut_text(e):
	global selected
	# Check if keyboard shortcut used
	if e:
		selected = root.clipboard_get()
	else:	
		if my_text.selection_get():
			# Grab selected text from textbox
			selected = my_text.selection_get()
			# Delete selected text from texbox
			my_text.delete("sel.first", "sel.last")
			# Clear the clipboard
			root.clipboard_clear()
			root.clipboard_appemnd(selected)

# Copy Text
def copy_text(e):
	global selected
	# Check if keyboard shortcut used
	if e:
		selected = root.clipboard_get()
	else:	
		if my_text.selection_get():
			# Grab selected text from textbox
			selected = my_text.selection_get()
			# Clear the clipboard
			root.clipboard_clear()
			root.clipboard_appemnd(selected)
# Paste Text
def paste_text(e):
	# Find cursor to determine where to paste
	global selected
	# Check if keyboard shortcut used
	if e:
		selected = root.clipboard_get()
	else:
		if selected:
			position = my_text.index(INSERT)
			my_text.insert(position, selected)
			# Clear the clipboard
			root.clipboard_clear()
			root.clipboard_appemnd(selected)
	
	
# Create Main Frame
my_frame = Frame(root)
my_frame.pack(fill=BOTH, expand=True)

# Create Scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Horizontal Scrollbar (Not Working)
#hor_scroll = Scrollbar(my_frame, orient='horizontal')
#hor_scroll.pack(side=RIGHT, fill=X)

# Create Text Box
my_text = Text(my_frame, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none")
#width=97, height=25,
my_text.pack( fill=BOTH, expand=YES)
#side=LEFT,

# Configure Scroolbar
text_scroll.config(command=my_text.yview)
#hor_scroll.config(command=my_text.xview)

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
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="Ctrl+C")
edit_menu.add_command(label="Paste     ", command=lambda: paste_text(False), accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="Ctrl+Y")

# Add Status Bar to the bottom of main window
#status_frame = Frame()
#status_frame.pack(fill=BOTH, side=BOTTOM, expand=False)
#status_bar = Label(status_frame, text='Ready    ', anchor=E)
#status_bar.pack(fill=BOTH, side=BOTTOM, ipady=15)

status_bar = Label(root, text='Ready    ', anchor=E)
status_bar.pack(fill=BOTH, side=BOTTOM, ipady=15)

# Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)



root.mainloop()
