import os
import shutil
import turtle
import random
from pathlib import Path

PATH = "C:/!My/tmp/" 

def dir(args):
    files = os.listdir(PATH)
    for file in files:
        print(file)
    return True

def exit(args):
    return False

def delete(args):
    for file in args:
        path = os.path.join(PATH, file)
        try:
            os.remove(path)
        except Exception as e:
            print("No file ", file)
        print("File deleted")
    return True

def dupl(args):
    for file in args:
        path = os.path.join(PATH, file)
        newFile = file + ".dupl"
        newFilePath = os.path.join(PATH, newFile)
        try:
            if os.path.isfile(path):
                shutil.copy(path, newFilePath)
        except Exception as e:
            print("No file ", path)
        print("File dupled")
    return True

def deleteDups(args):    
    mask = "*.dupl"
    counter = 0
    for filename in Path(PATH).glob(mask):
        filename.unlink()
        print(filename, "deleted")
        counter += 1
    print(counter, " files has been deleted")
    return True

def draw(e):
    turtle.goto(random.randrange(0, 300), random.randrange(0, 300))
    turtle.circle(random.randrange(30,80))
    return True

def showError(e, command):
    print("There is no command like \"", command, "\"")
    return True

commands = {
    "dir" : dir,
    "del" : delete,
    "deldups" : deleteDups,
    "dupl" : dupl,
    "draw" : draw,
    "exit" : exit,
}

def doCommand(command, args):
    try:
        return commands[command] (args)
    except KeyError as e:
        return showError(e, command)


print("dir - show all files in directory")
print("del - delete file")
print("dupl - copy file")
print("deldups - delete all dupls")
print("draw - draw")

keepWorking = True
while keepWorking:
    inputPrompt = input(">")
    try:
        inputArgs = inputPrompt.split()
        inputCommand = inputArgs.pop(0)
        keepWorking = doCommand(inputCommand, inputArgs)
    except Exception as e:
        keepWorking = showError(e, inputPrompt)