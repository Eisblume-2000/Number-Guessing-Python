import os
import tkinter as tk
import random
from os import remove
from os import path

class guesserGUI:

    def __init__(self,highestentry, lowestentry):

        self.guesserwindow =tk.Tk()
        self.guesserwindow.geometry("400x500")
        self.guesserwindow.title("Number Guesser")
        self.guesserwindow['background'] = '#202124'

        self.numberrange = tk.Label(self.guesserwindow, text="Number range : " + lowestentry + " - " + highestentry,font=("Arial"))
        self.numberrange.pack(pady=20)

        self.userguesslabel = tk.Label(self.guesserwindow, text="Your guess",font=("Arial"))
        self.userguesslabel.pack(pady=20)

        self.userguess = tk.Entry(self.guesserwindow)
        self.userguess.pack(pady=20)

        self.startprocess = tk.Button(self.guesserwindow, text="Try your luck",font=("Arial"), command=lambda: self.gameprocess(highestentry, lowestentry))
        self.startprocess.pack(pady=20)

        path1 = path.exists(r"C:\ProgramData\numberguessing\wins")
        if path1 == False:
            r = open(r"C:\ProgramData\numberguessing\wins", "w")
            r.write(str(0))
            r.close()
        else:
            pass

        path2 = path.exists(r"C:\ProgramData\numberguessing\looses")
        if path2 == False:
            r = open(r"C:\ProgramData\numberguessing\looses", "w")
            r.write(str(0))
            r.close()
        else:
            pass

        r = open(r"C:\ProgramData\numberguessing\looses", "r")
        looses = r.read()
        looses = int(looses)
        r.close()
        r = open(r"C:\ProgramData\numberguessing\wins", "r")
        wins = r.read()
        wins = int(wins)
        r.close()
        self.gamelabel2 = tk.Label(self.guesserwindow, text="You won : " + str(wins) + " times", font=("Arial"))
        self.gamelabel2.place(y=375, relx=0.5, anchor="center", width=400)
        self.gamelabel3 = tk.Label(self.guesserwindow, text="You lost : " + str(looses) + " times", font=("Arial"))
        self.gamelabel3.place(y=400, relx=0.5, anchor="center", width=400)

        self.buttonframe = tk.Frame(self.guesserwindow)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        self.buttonback = tk.Button(self.buttonframe,text="Back",font=("Arial"), command=self.back)
        self.buttonback.grid(row=0, column=1)

        self.buttonclose = tk.Button(self.buttonframe, text="Close", font=("Arial"), command=self.close)
        self.buttonclose.grid(row=0, column=0)

        self.buttonframe.place(y=450, relx=0.5, anchor="center")

        self.guesserwindow.mainloop()

    def numbergenerator(self, highestentry, lowestentry):
        numberrandom = random.randint(int(lowestentry),int(highestentry))
        return numberrandom

    def gameprocess(self,highestentry, lowestentry):
        randomnumber = self.numbergenerator(highestentry, lowestentry)
        userguess = int(self.userguess.get())

        self.gamelabel1 = tk.Label(self.guesserwindow, text="You guessed : " + str(userguess) + " The Computer guessed : " + str(randomnumber), font=("Arial"))
        self.gamelabel1.place(y=300, relx=0.5, anchor="center", width=400)

        path1 = path.exists(r"C:\ProgramData\numberguessing\wins")
        if path1 == False:
            r = open(r"C:\ProgramData\numberguessing\wins", "w")
            r.write(str(0))
            r.close()
        else:
            pass

        path2 = path.exists(r"C:\ProgramData\numberguessing\looses")
        if path2 == False:
            r = open(r"C:\ProgramData\numberguessing\looses", "w")
            r.write(str(0))
            r.close()
        else:
            pass

        if randomnumber == int(userguess):
            self.winorlosslabel = tk.Label(self.guesserwindow, text="You Win", font=("Arial"))
            self.winorlosslabel.place(y=350, relx=0.5, anchor="center", width=400)
            r = open(r"C:\ProgramData\numberguessing\wins","r")
            wins = int(r.read())
            r.close()
            wins = wins + 1
            r = open(r"C:\ProgramData\numberguessing\wins","w")
            r.write(str(wins))
            r.close()

        else:
            self.winorlosslabel = tk.Label(self.guesserwindow, text="You Loose", font=("Arial"))
            self.winorlosslabel.place(y=350, relx=0.5, anchor="center", width=400)
            r = open(r"C:\ProgramData\numberguessing\looses","r")
            looses = int(r.read())
            r.close()
            looses = looses + 1
            r = open(r"C:\ProgramData\numberguessing\looses", "w")
            r.write(str(looses))
            r.close()

        r = open(r"C:\ProgramData\numberguessing\looses", "r")
        looses = r.read()
        looses = int(looses)
        r.close()
        r = open(r"C:\ProgramData\numberguessing\wins", "r")
        wins = r.read()
        wins = int(wins)
        r.close()
        self.gamelabel2 = tk.Label(self.guesserwindow, text="You won : " + str(wins) + " times", font=("Arial"))
        self.gamelabel2.place(y=375, relx=0.5, anchor="center", width=400)
        self.gamelabel3 = tk.Label(self.guesserwindow, text="You lost : " + str(looses) + " times", font=("Arial"))
        self.gamelabel3.place(y=400, relx=0.5, anchor="center", width=400)

    def back(self):
        self.guesserwindow.destroy()
        StartGUI()
    def close(self):
        self.guesserwindow.destroy()
        exit()

class StartGUI:

    def __init__(self):
        self.startwindow = tk.Tk()
        self.startwindow.geometry("400x500")
        self.startwindow.title("Number Guesser")
        self.startwindow['background'] = '#202124'

        self.labelwelcome = tk.Label(self.startwindow, text="Number Guesser Game, by Eisblume2000#5142",font=("Arial"))
        self.labelwelcome.pack(pady=20)

        self.labelprompt = tk.Label(self.startwindow, text="Input the Range of Numbers",font=("Arial"))
        self.labelprompt.pack(pady=20)

        self.labelinfo1 = tk.Label(self.startwindow, text="Lowest Number",font=("Arial"))
        self.labelinfo1.pack()

        self.lowestentry = tk.Entry(self.startwindow)
        self.lowestentry.pack(pady=20)

        self.labelinfo1 = tk.Label(self.startwindow, text="Highest Number",font=("Arial"))
        self.labelinfo1.pack()

        self.highstentry = tk.Entry(self.startwindow)
        self.highstentry.pack(pady=20)

        self.startbutton = tk.Button(self.startwindow,text="Start",font=("Arial"), command=self.pre_check)
        self.startbutton.pack(pady=20)

        self.buttonframe = tk.Frame(self.startwindow)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        self.buttonclose = tk.Button(self.buttonframe, text="Close", font=("Arial"), command=self.close)
        self.buttonclose.grid(row=0, column=0)

        r = open(r"C:\ProgramData\numberguessing\numberguessing.txt","r")
        option = int(r.read())
        r.close()
        if option == 0:
            status = "Off"
        if option == 1:
            status = "On"

        self.buttonoption = tk.Button(self.buttonframe, text="Save : " + status, font=("Arial"), command=self.option_change)
        self.buttonoption.grid(row=0, column=1)

        self.buttonframe.place(y=450, relx=0.5, anchor="center")

        self.startwindow.mainloop()

    def option_change(self):
        r = open(r"C:\ProgramData\numberguessing\numberguessing.txt", "r")
        option = int(r.read())
        r.close()
        if option == 0:
            r = open(r"C:\ProgramData\numberguessing\numberguessing.txt", "w")
            r.write("1")
            r.close()
        if option == 1:
            r = open(r"C:\ProgramData\numberguessing\numberguessing.txt", "w")
            r.write("0")
            r.close()

        self.buttonframe = tk.Frame(self.startwindow)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        self.buttonclose = tk.Button(self.buttonframe, text="Close", font=("Arial"), command=self.close)
        self.buttonclose.grid(row=0, column=0)

        r = open(r"C:\ProgramData\numberguessing\numberguessing.txt", "r")
        option = int(r.read())
        r.close()
        if option == 0:
            status = "Off"
        if option == 1:
            status = "On"

        self.buttonoption = tk.Button(self.buttonframe, text="Save : " + status, font=("Arial"),
                                      command=self.option_change)
        self.buttonoption.grid(row=0, column=1)

        self.buttonframe.place(y=450, relx=0.5, anchor="center")

    def pre_check(self):
        if int(self.lowestentry.get()) == int(self.highstentry.get()):
            self.errorbox = tk.Label(self.startwindow, text="Lowest Number is equal to highest, pls try again",font=("Arial"))
            self.errorbox.place(y=400, relx=0.5, anchor="center", width=400)
        if int(self.lowestentry.get()) > int(self.highstentry.get()):
            self.errorbox2 = tk.Label(self.startwindow, text="Lowest Number is bigger then highest, pls try again", font=("Arial"))
            self.errorbox2.place(y=400, relx=0.5, anchor="center", width=400)
        if int(self.lowestentry.get()) < int(self.highstentry.get()):
            highestentry = str(self.highstentry.get())
            lowestentry = str(self.lowestentry.get())
            self.startwindow.destroy()
            guesserGUI(highestentry, lowestentry)

    def close(self):
        self.startwindow.destroy()
        exit()

if path.exists(r"C:\ProgramData\numberguessing\numberguessing.txt") == False:
    r = open(r"C:\ProgramData\numberguessing\numberguessing.txt","w")
    r.write("0")
    r.close()
else:
    pass

r = open(r"C:\ProgramData\numberguessing\numberguessing.txt","r")
setting = int(r.read())
r.close()

if setting == 0:
    try:
        os.remove(r"C:\ProgramData\numberguessing\looses")
        os.remove(r"C:\ProgramData\numberguessing\wins")
    except:
        pass

StartGUI()
