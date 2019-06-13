from tkinter import *
from tkinter import messagebox as mb
import Addfunction #We import Addfunction
import Modifyfunction #We import Modifyfunction
from string import *



class landingPage(): #This creates the first thing the user sees
    def __init__ (self): #constructor 
        self.top = Tk()
        self.top.geometry = ('700x700')
        self.top.title = ("Patients")
        self.top.resizable(0,0)
        self.exitProgram = ''
        self.populate = list() #List which holds all patients
        self.xcord = 5
        self.ycord = 0
        self.line = 0
        self.outerFrame = ''
        self.firstRun = True
    def mbr (self, parent): #This builds the menu bar and assigns buttons to functions that perform their persepective tasks.
        menubar = Menu(parent)
        filemenu = Menu (menubar, tearoff = 0)
        filemenu.add_command(label = "Load Patients", command = self.loadPatients)
        filemenu.add_command(label = "New Patient", command = self.newPatient)
        filemenu.add_command(label = "Modify Patient", command = self.modifyPatient)
        filemenu.add_command(label = "Save To File", command = self.saveToFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command = self.exitProgram)
        menubar.add_cascade(label="File", menu=filemenu)
        aboutmenu = Menu (menubar, tearoff = 0)
        aboutmenu.add_command(label = "About", command = self.about)
        menubar.add_cascade(label = "About", menu=aboutmenu)
        self.top.config(menu=menubar)
        return menubar

    def about (self): #Action when about is clicked on, displays message box
        mb.showinfo("Author Info", "Student: Evan Perry\nProfessor Frank Breitinger\nCSCI 6651 Python Script Programming")


    def saveToFile(self): #Writes screen contents out to file and saves it, name of file is hard coded.
        if len(self.populate) == 0 or self.populate[0] == 'Please load a patient file': #Error if no one to save
            mb.showinfo("ERROR!", "No Patients to write out!\nTry Entering in new patients first\nor loading patients from file.")
        elif len(self.populate) > 0:
            fn = "PatientList.txt"
            fh = open(fn, 'w+')
            for i in self.populate:
                fh.write(str(i))
                fh.write('\n')
            fh.close()

    def loadPatients(self): #load from file, which is hard coded
        fn = "PatientList.txt"
        try:
            fh = open(fn, 'r')
            fc = fh.readlines()
            for line in fc:
                line = line.rstrip()
                self.addToPatHolder(line)
            self.firstRun = False
            self.removeFrame()
            self.addFrame()
        except: #if no file, error is returned
            mb.showinfo("ERROR!", "File not found!")

    def addToPatHolder (self, addtolist = None):#Adds to patient list.
        if addtolist == None:#If nothing to add, prints this, this is only called when the program is opened.
            addtolist = "Please load a patient file"
            self.populate.append(addtolist)
        else:
            self.populate.append(addtolist)

    def removeFrame (self):#This removes the current frame, this allows changes to be printed to the screen.
        self.outerFrame.pack_forget()
        self.outerFrame = ''
        self.ycord = 0
        for i in self.populate:
            if i == "Please load a patient file":
                self.populate.remove(i)
            else:
                continue

    def addFrame (self): #Reprints the screen after changes are made.
        readd=self.patientHolder(self.top)
        readd.pack()
        return None
    
    def patientHolder (self, parent): #This is the frame that will hold all patient data.
        self.outerFrame = Frame (parent)
        patientArea = Canvas (self.outerFrame)
        if self.firstRun == True:
            self.addToPatHolder()
        for i in self.populate:
            patientArea.create_text(self.xcord,self.ycord, anchor = "nw", text =i)
            self.ycord+=15
        patientArea.pack()
        return self.outerFrame

    def newPatient(self,):#Creates a new patient, then updates the display
        if self.firstRun == True:
            self.firstRun = False
        add1 = Addfunction.addP() #Creations of Addfuction object add1
        add1.run()
        patientaddition = str(add1)#Converts to string so it can be added to the list properly.
        self.addToPatHolder(patientaddition)        
        self.removeFrame()
        self.addFrame()

    def modifyPatient(self): #This modifies the patient then updates the list properly.
        if self.firstRun == True and self.populate[0] != 'Please load a patient file':
            self.firstRun = False
        elif self.populate[0] == 'Please load a patient file': #Prevents modify in case no patients are entered yet.
            mb.showinfo("Error", "No patients, loaded!")
        else:
            modify1 = Modifyfunction.modifyP(self.populate)
            modify1.run()
            allPatients = str(modify1)
            patientEntry = ''
            counter = 0
            for c in allPatients:#List comes back from Modifyfunction as a string, so we have to convert it back to a list.
                if counter < 2 and c != "'" and c!= ' ' and c!= '[' and c!= ']':
                    patientEntry += c
                elif counter == 2 and c == "'":
                    self.addToPatHolder(patientEntry)#We repopulate our list.
                    patientEntry = ''
                else:
                    counter+=1
            self.removeFrame()
            self.addFrame()

            
    def showLanding (self):#This prepares the main function for being displayed, and packing the self.top for display.
        self.exitProgram = self.top.destroy
        menubar = self.mbr(self.top)
        self.top["menu"] = menubar
        landing = self.patientHolder(self.top)
        landing.pack()

        return None
    def run(self):#This starts the gui and allows it to run
        self.showLanding()
        mainloop()
gui = landingPage() #This creates the gui object and starts it running.
gui.run()


