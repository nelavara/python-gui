from tkinter import *
from tkinter import messagebox as mb


class modifyP(): #This is the modify class which is used by Assignment7_GUI to modify the existing patients.
    def __init__(self, patients = None):
        self.top = Tk()
        if patients == None: #We create the list, and we set it equal to what the caller provides in Assignment7_GUI
            patients = list()
        else:
            self.patients = patients
        self.top.geometry = (700,700)
        self.top.title = ("Modify Patient")
        self.top.resizable = (0,0)
        self.listPosition = 0
        self.xcord = 5
        self.ycord = 0
        self.fname = ''
        self.lname = ''
        self.dob = ''
        self.savePat = ''
        self.cancel = ''
        self.entry = ''

    def __repr__ (self):#We return the entire list as a string.
        return str(self.patients)

    def modifyPatientDisp(self, parent): #This builds the display, including the buttons and entries.
        self.outerFrame = Frame(parent)
        self.outerFrame.pack(expand=True)
        self.moveList()#This gets the fname, lname, and dob to be displayed in each of the entires.
        modifyPatientArea = Canvas(self.outerFrame)
        modifyPatientArea.create_text(self.xcord, self.ycord, anchor = "nw", text = "First Name")
        self.textboxfname = Entry(self.outerFrame)
        self.textboxfname.insert(0, self.fname)
        self.textboxfname.place(x=80,y=0)
        self.ycord += 20
        modifyPatientArea.create_text (self.xcord, self.ycord, anchor = "nw", text = "Last Name")
        self.textboxlname = Entry(self.outerFrame)
        self.textboxlname.insert(0, self.lname)
        self.textboxlname.place(x=80,y=20)
        self.ycord +=20
        modifyPatientArea.create_text (self.xcord, self.ycord, anchor = "nw", text = "DOB")
        self.textboxdob = Entry (self.outerFrame)
        self.textboxdob.insert(0, self.dob)
        self.textboxdob.place (x=80,y=40)
        prevButton = Button(self.outerFrame, text = "Previous", width = "9", height = '1', command = self.prevList).place(x = 20, y = 80)
        nextButton = Button(self.outerFrame, text = "Next", width= "9", height = '1', command = self.nextList).place(x = 130, y =80)
        modifyButton = Button (self.outerFrame, text = "Update", width = "9", height = "1", command = self.modify_close).place(x = 20, y= 225)
        cancelButton = Button(self.outerFrame, text = "Cancel", width = "9", height = "1", command = self.top.destroy).place(x = 130, y = 225)
        modifyPatientArea.pack()

    def nextList (self): #When next list is clicked, we save the changes to the list and advance to the next item in the list.       
        self.updateList() #This is the function that performs the updates.
        self.lname = ''
        self.fname = ''
        self.dob = ''
        self.listPosition+=1
        if self.listPosition >= len(self.patients):#We check if we are at the end of the array bounds, and if so, start over.
            self.listPosition = 0
        self.outerFrame.pack_forget()#Then we need to forget the array
        self.ycord = 0#It is important to reset the ycord, as it is constantly changed in the caller.
        self.modifyPatientDisp(self.top)#Then we recreate the display, by calling the caller.
        

    def prevList (self): #prevList does the same thing as nextList, but in reverse so we can go backwards.    
        self.updateList()#This function performs the updates.
        self.lname = ''
        self.fname = ''
        self.dob = ''
        self.listPosition-=1
        if self.listPosition < 0:
            self.listPosition = len(self.patients)-1
        self.outerFrame.pack_forget()
        self.ycord = 0
        self.modifyPatientDisp(self.top)

    def moveList(self):#We set the fname, lname, and dob based on the position in the list specified by prevList and nextList
        commacount = 0
        for i in self.patients[self.listPosition]:
            if commacount == 0 and i != ',' and i != ' ':
                self.lname+=i
            elif commacount == 1 and i != ',' and i != ' ':
                self.fname+=i
            elif commacount == 2 and i != ',' and i != ' ':
                self.dob+=i
            elif i == ',':
                commacount+=1

    def updateList (self):#This updates the position after update or nextList or prevList is called.
        self.lname = self.textboxlname.get()
        self.entry += self.lname
        self.entry += ", "
        self.fname = self.textboxfname.get()
        self.entry += self.fname
        self.entry += ", "
        self.dob = self.textboxdob.get()
        self.entry+= self.dob
        self.patients[self.listPosition] = self.entry
        self.entry = ''



    def modify_close (self):#This is called when Updates is clicked.
        self.updateList()#It is important that the list is updated one fine time, just in case next or previous are not clicked.
        mb.showinfo("Update", "Patient List updated!")
        self.top.quit() #Now we close the Windows and return control back to the Assignment7_GUI
        self.closeWindow()
    def closeWindow(self):
        self.top.destroy()

    def showmodifyPatient(self):#This makes the main display
        newPat = self.modifyPatientDisp(self.top)
        return None
    def run(self):#This runs the program.
        self.showmodifyPatient()
        mainloop()


