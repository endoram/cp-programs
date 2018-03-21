from tkinter import *


class beginscript:
	def __init__(self):
		print("Starting")

		title = Label(root, font=44, text="Please select all the items that you would like to be scored on your image.").pack()
#		title1 = Label(root).pack()


		var1 = IntVar()
		Checkbutton(root, text="ssh root login disabled", variable= var1).pack(side=TOP, anchor=W)

		var2 = IntVar()
		Checkbutton(root, text="ssh protocal 1 to 2", variable= var2).pack(side=TOP, anchor=W)

		var3 = IntVar()
		Checkbutton(root, text="X11 Forwarding no", variable= var3).pack(side=TOP, anchor=W)

		var4 = IntVar()
		Checkbutton(root, text="Add admin DeloorTteG", variable= var4).pack(side=TOP, anchor=W)

		var5 = IntVar()
		Checkbutton(root, text="Add program Stellarium", variable= var5).pack(side=TOP, anchor=W)

		var6 = IntVar()
		Checkbutton(root, text="Add user jams", variable= var6).pack(side=TOP, anchor=W)


		def fileoutput():
			print("Exporting...")

			output = []
			hey = str(var1.get())
			output += hey

			hey = str(var2.get())
			output += hey

			hey = str(var3.get())
			output += hey

			hey = str(var4.get())
			output += hey

			hey = str(var5.get())
			output += hey

			hey = str(var6.get())
			output += hey


			output = str(output)

			outputfile = open("output.txt", "w+")
			outputfile.write(output)

			root.quit()

		end = Button(root, text="Submit", command=fileoutput).pack(side=BOTTOM)



		mainloop()


root = Tk()
root.configure(background='white')
beginscript()
