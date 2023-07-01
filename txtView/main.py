# made by g3ncenter
import pathlib
import os
fl_nm = ""
mt_cr = 0


def dirq():
    dirc = pathlib.Path('./txt')
    fl_tp = "*.txt"
    for files in dirc.glob(fl_tp):
        print(files)

def isEx(path):
    if os.path.exists(path):
        return
    else:
        file = open(path, 'w')
        file.write("")
        file.close()

        
t = 1
while t == 1:

    while fl_nm == "": 
        fl_nm_f = str(input("Please, enter name of file (!q to exit / !sh to show all files): "))
        if fl_nm_f == "!q":
            exit()

        elif fl_nm_f == "!sh":
            if os.path.exists("txt"):
                dirq()
            else:
                os.mkdir("txt")
                dirq()


        else:
            if os.path.exists("txt"):
                fl_nm = ("txt/" + fl_nm_f + ".txt")
                print("Path is:", fl_nm)
                file = open(fl_nm, 'w')
                file.write("")
                file.close()
            else:
                os.mkdir("txt")
                fl_nm = ("txt/" + fl_nm_f + ".txt")
                print("Path is:", fl_nm)
                file = open(fl_nm, 'w')
                file.write("")
                file.close()
                

    mode = input("Choose action. r/w/a/rm/sh/q: ")
    if mode == "r":
        isEx(fl_nm)
        file = open(fl_nm, 'r')
        print(file.read())
        file.close()

    elif mode == "w":
        isEx(fl_nm)
        file = open(fl_nm, 'w')
        print('Tip: write "!q" to save and close file')
        while True:
            text = input("")
            if text == "!q":
                break
            text_spc = (text + "\n")
            file.write(text_spc)
            text = ""


    elif mode == "a":
        isEx(fl_nm)
        file = open(fl_nm, 'a')
        print('Tip: write "!q" to save and close file')
        while True:
            text = input("")
            if text == "!q":
                file.close()
                break
            text_spc = (text + "\n")
            file.write(text_spc)
            text = ""

    elif mode == "q":
        fl_nm = ""

    elif mode == "rm":
        os.remove(fl_nm)
        fl_nm = ""
        fl_nm_f = ""

    elif mode == "sh":
        dirq()

    else:
        print("Something went wrong")
 
