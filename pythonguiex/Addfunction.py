from tkinter import *
from tkinter import messagebox as mb

class addP():
    def __init__(self): #Add patient constructor, Assignment7_GUI uses this class to add patients.
        self.top = Tk()
        self.top.geometry = (700,700)
        self.top.title = ("Add Patient")
        self.top.resizable = (0,0)
        self.xcord = 5
        self.ycord = 0
        self.fname = ''
        self.lname = ''
        self.dob = ''
        self.savePat = ''
        self.cancel = ''
        self.entry = ''

    def __repr__ (self): #This returns the user entry as a string.
        return str(self.entry)
        

    def addPatientDisp(self, parent): #Here we create the display which will ask for the patient's name and date.
        outerFrame = Frame(parent)
        outerFrame.pack(expand=True)
        addPatientArea = Canvas(outerFrame)
        addPatientArea.create_text(self.xcord, self.ycord, anchor = "nw", text = "First Name")
        self.textboxfname = Entry(outerFrame)
        self.textboxfname.place(x=80,y=0)
        self.ycord += 20
        addPatientArea.create_text (self.xcord, self.ycord, anchor = "nw", text = "Last Name")
        self.textboxlname = Entry(outerFrame)
        self.textboxlname.place(x=80,y=20)
        self.ycord +=20
        addPatientArea.create_text (self.xcord, self.ycord, anchor = "nw", text = "Date of Birth")
        self.textboxdob = Entry (outerFrame)
        self.textboxdob.place (x=80,y=40)  #Creation of buttons that execute commands.
        addButton = Button (outerFrame, text = "Add Patient", width = "9", height = "1", command = self.add_close).place(x = 20, y= 80)
        cancelButton = Button(outerFrame, text = "Cancel", width = "9", height = "1", command = self.top.destroy).place(x = 130, y = 80)
        addPatientArea.pack()

    def add_close (self):#When the addbutton is clicked this function is executed.
        self.lname = self.textboxlname.get()#The program gets the entries and then appends them into one string, called self.entry.
        self.entry += self.lname
        self.entry += ", "
        self.fname = self.textboxfname.get()
        self.entry += self.fname
        self.entry += ", "
        self.dob = self.textboxdob.get()
        self.entry+= self.dob
        mb.showinfo("Notice", "Patient Added.")
        self.top.quit()  #We then close the window, and then this object is destroyed.
        self.closeWindow()
    def closeWindow(self):
        self.top.destroy()

    def showAddPatient(self): #We create the main display of add patient
        newPat = self.addPatientDisp(self.top)
        return None
    def run(self): #Here we run the gui display.
        self.showAddPatient()
        mainloop()

