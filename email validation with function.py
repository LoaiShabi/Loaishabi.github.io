from tkinter import *

 

window = Tk() #creates window

window.geometry("500x400") # size of window

window.configure(bg = "pink") #colour of window

mylabel = Label(window, text = "BMI Calculator") #add titke

def validate_email():
    global email, foundAt, foundDot
    for i in range (0, len (email)):
        print(email.get [i])

    #ives each letter its own place

        if (email.get [i]=="@") :
            foundAt = i
        if (email.get[i]== "."):
            foundDot = i
 
validate_email()

welcome= Label(window, text="welcome yo the email validation")

enterE= Label(window, text="enter email")

email= Entry(window)

validation= Button(window, text = "validate email", command= validate_email)























#or x in range (2, 20) :
    
    #print(x*4)

email = input("enter email")

foundAt = -1 # declare a variable
foundDot=-1
def validate_email():
    global email, foundAt, foundDot
    for i in range (0, len (email)):
        print(email [i])

    #ives each letter its own place

        if (email [i]=="@") :
            foundAt = i
        if (email[i]== "."):
            foundDot = i
 
validate_email()
if (foundAt>=1 and foundDot> foundAt+1 and foundDot,len(email)-2):
        print("valid email")

else:
    print("invalid")


















