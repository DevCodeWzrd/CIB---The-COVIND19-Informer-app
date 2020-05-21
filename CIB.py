#Credits to:
#CDC for facts
#Dev.Code.Wzrd For programming
#And Itch.io for licence, and soforth
#WRITTEN IN PYTHON v8.3.3#
#Date of developing 5/13/2020 - _/__/2020
# _______    ______    ___
#/  _____\  |_    _|  |   \
#| |          |  |    |   |
#| |          |  |    |   /
#| |______   _|  |_   |    \
#\_______/  |______|  |____|
print('LOG')
print('=+--------------+=')
print('Impoting Code...')
import tkinter as tk
from time import sleep
from random import randint
print('Creating TK window...')
FactsNum = 4 #You may change this to the number of facts in the C19R.txt file
kill = 0 #Nulls killing the program
#Creating text window
def Kill():
    #Kills Code
    print('Killing in 1.5 secs...')
    sleep(1.5)
    quit()    
def Gather_Facts(Num):
    for i in range(0, Num):
        print('Loding ' + str(i + 1) + '/' + str(Num) +' COVIND19 Facts...')
        #The 3 lines below gather the COVIND19 facts from the C19R.txt file
        file = open("C19R.txt", 'r')
        Content = file.readlines()
        print(Content[i])
    #Displays How Many facts gatherd out of how many
    print('Facts Gatherd: ' + str(Num)+ '/' + str(i + 1))
file = open("C19R.txt", 'r')
Content = file.readlines()
TkRun = 0
def Create_Window():
    #Displays all facts in a Tk window.
    root= tk.Tk()
    root.title('CIB- The COVIND19 Informer App')
    canvas1 = tk.Canvas(root, width = 1400, height = 1200, bg = 'green')
    canvas1.pack()
    root.iconphoto(False, tk.PhotoImage(file='/Users/Ronan/Downloads/CIBLogo.gif'))
    COVIND19Fact1 = tk.Label(root, text= Content[0], fg='white', bg='green', font=('helvetica', 12))
    COVIND19Fact2 = tk.Label(root, text= Content[1], fg='white', bg='green', font=('helvetica', 12))
    COVIND19Fact3 = tk.Label(root, text= Content[2], fg='white', bg='green', font=('helvetica', 12))
    COVIND19Fact4 = tk.Label(root, text= Content[3], fg='white', bg='green', font=('helvetica', 12))
    canvas1.create_window(650, 100, window=COVIND19Fact1)
    canvas1.create_window(650, 200, window=COVIND19Fact2)
    canvas1.create_window(650, 300, window=COVIND19Fact3)
    canvas1.create_window(650, 400, window=COVIND19Fact4)
    root.mainloop()
def popupmsg():
    popup = tk.Tk()
    popup.title("!")
    label = tk.Label(popup, text = '''This is a test vershion, and get's updated constantly.
    Thaks to the CDC for COVIND19 Facts.
    Thanks for using!''')
    popup.iconphoto(False, tk.PhotoImage(file='/Users/Ronan/Downloads/CIBLogo.gif'))
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
print('Gathering COVIND19 facts in 1.5 secs')
print('(Gathering ' + str(FactsNum) + ' Facts)')
popupmsg()
Create_Window()
sleep(1.5)
print('==================================')
Gather_Facts(FactsNum)
if kill == 1:
    Kill = input('Would you like to kill? (y/n)')
    if Kill == 'y':
        Kill()
    elif Kill == 'n':
        while True:
            sleep(0.1)







