from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as box
from script import insertDateTime
import tkinter.filedialog as filedialog
##################################################################3

mainW = Tk()
mainW.title("Time Stamper")
mainW.geometry("500x500")
mainW.resizable(True, True)
START_ROW = 2

FILES = ()
####################################################

def getValues():
    global gen, FILES
    #COMMENT BELOW CODE FOR DEV MODE

    try:
        date = e0.get()
        fontSize = e1.get()
        fontColor = tuple(map(int, gen.get().split(', ')))
        extraField1 = e3.get()
        extraField2 = e4.get()
        count = 0
        max_Count = len(FILES)

        #PROGRESS BAR#################################################
        progress = Progressbar(mainW, orient = HORIZONTAL,           #
                length = 100, mode = 'determinate')                  #
        progress.grid(row = 13, column = 1, sticky = W+E, pady=10)   #
        value_label = Label(mainW, text=str(progress['value'])+'%')  #
        value_label.grid(column=2, row=13, columnspan=2, padx = 5)   #
        ##############################################################

        for ele in FILES:
            insertDateTime(str(ele), date, fontSize,
                        fontColor, extraField1, extraField2)

            #PROGRESS BAR##############################
            count+=1                                  #
            prg = int((count/max_Count)*100)          #
            progress['value'] = prg                   #
            value_label['text'] = str(prg)+'%'        #
            mainW.update_idletasks()                  #
            ###########################################

        progress.destroy()
        value_label.destroy()
        box.showinfo("Success", 'Program executed Successfully!')
    except:
        box.showerror('ERR', 'Error in Operation!')

def getImages():
    global FILES
    FILES = filedialog.askopenfilenames(initialdir="test", title="Select photos", filetypes=(("all files", "*.*"), ("png files", "*.png"), ("jpeg files", "*.jpeg")))
    

####################################################

getImages()

l0 = Label(mainW, text="Custom Date")
l0.grid(row=START_ROW, column=0)

e0 = Entry(mainW)
e0.grid(row=START_ROW, column=1)
e0.focus_force()

l1 = Label(mainW, text="Font Size")
l1.grid(row=START_ROW+1, column=0)

e1 = Entry(mainW)
e1.grid(row=START_ROW+1, column=1)

#Radiobutton
l2 = Label(mainW, text="Font Color")
l2.grid(row=START_ROW+2, column=0)

gen = StringVar()
gen.set('255, 161, 7')
r1 = Radiobutton(mainW, text="Default", variable=gen, value='255, 161, 7')
r1.grid(row=START_ROW+2, column=1)

r2 = Radiobutton(mainW, text="Black", variable=gen, value='0, 0, 0')
r2.grid(row=START_ROW+2, column=2)

r2 = Radiobutton(mainW, text="White", variable=gen, value='255, 255, 255')
r2.grid(row=START_ROW+2, column=3)

l3 = Label(mainW, text="Extra Field 1")
l3.grid(row=START_ROW+3, column=0)

e3 = Entry(mainW)
e3.grid(row=START_ROW+3, column=1)

l4 = Label(mainW, text="Extra Field 2")
l4.grid(row=START_ROW+4, column=0)

e4 = Entry(mainW)
e4.grid(row=START_ROW+4, column=1)

#Button
lbr1 = Label(mainW, text="")
lbr1.grid(row=START_ROW+5, column=0)

b1 = Button(mainW, text="STAMP IT", command=getValues)
b1.grid(row=START_ROW+6, column=0)

b2 = Button(mainW, text="RESELECT IMAGES", command=getImages)
b2.grid(row=START_ROW+6, column=1)

#Settings
lbr2 = Label(mainW, text="")
lbr2.grid(row=START_ROW+7, column=0)
# lbr3 = Label(mainW, text="")
# lbr3.grid(row=START_ROW+8, column=0)


l5 = Label(mainW, text="1. DEFAULT FONT SIZE : 148")
l5.grid(row=START_ROW+9, column=0)

mainW.mainloop()
