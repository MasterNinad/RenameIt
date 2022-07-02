from msilib.schema import RadioButton
import os
import pathlib

from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import filedialog

MainWindow = Tk()
MainWindow.geometry("320x210")
MainWindow.title("Rename It")

brackets = BooleanVar()
brackets.set(False)

openFolder = BooleanVar()
openFolder.set(True)

confirmRename = BooleanVar()
confirmRename.set(True)

folderPath = StringVar()
folderPath.set("")

def getFolder():
	folderPath.set(filedialog.askdirectory(title = "Select your folder"))
	FolderNameLabel["text"] = folderPath.get()

def startRename():
	if (confirmRename):
		result = messagebox.askyesno('Confirm Rename', 'Are you sure you want to rename the files?', parent = MainWindow)
		if (result):
			rename()
	else:
		rename()
		
def rename():
	fileNumber = 1
	for filename in os.listdir(folderPath.get()):
		fileExt = pathlib.Path(filename).suffix
		filePath = folderPath.get() + '/' + filename
		if (brackets.get()):
			os.rename(filePath, folderPath.get() + "/" + str(fileNumber) + ')' + fileExt)
		else:
			os.rename(filePath, folderPath.get() + "/" + str(fileNumber) + fileExt)
		if (openFolder.get()):
			os.startfile(folderPath.get()) 
		fileNumber += 1

MainFrame = Frame()
MainFrame.pack()

LabelFont = tkFont.Font(family="Calibri", size=20, weight="bold")
WelcomeLabel = Label(MainFrame, text = "Welcome to Rename It!", font = LabelFont)
WelcomeLabel.grid(row = 0, column = 0, columnspan = 2, pady = 3)

OpenFolderBtn = Button(MainFrame, text = "Open Folder", command = getFolder)
OpenFolderBtn.grid(row = 1, column = 0, pady = 3)

RenameBtn = Button(MainFrame, text = "Rename", command = startRename)
RenameBtn.grid(row = 1, column = 1, pady = 3)

FolderNameLabel = Label(MainFrame, text = "Select Folder")
FolderNameLabel.grid(row = 2, column = 0, columnspan = 2, pady = 3)

BracketsBtn = Checkbutton(MainFrame, text = "Add brackets, e.g. - 1), 2), ...", variable = brackets)
BracketsBtn.grid(row = 3, column = 0, columnspan = 2, pady = 3)

ConfirmBtn = Checkbutton(MainFrame, text = "Show a confirmation before renaming", variable = confirmRename)
ConfirmBtn.grid(row = 4, column = 0, columnspan = 2, pady = 3)

FolderBtn = Checkbutton(MainFrame, text = "Open folder after renameing is complete", variable = openFolder)
FolderBtn.grid(row = 5, column = 0, columnspan = 2, pady = 3)

MainWindow.mainloop();