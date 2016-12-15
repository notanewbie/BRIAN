import os
import random
import math
#This is BRIAN, a Bot Really Intelligent And Nice.
#
#
#This code is still undergoing Beta testing.

#Make a new function. This will be the engine.
def Initiate(user):
    #Look in the database for a match to "User" so I can respond.
    #Do I know how to respond?
    USER = user.replace("?", "")
    USER = USER.replace('"', "")
    USER = USER.replace('PH/', "")
    USER = USER.replace('\n', "")
    USER = USER.replace('<', "")
    USER = USER.replace('>', "")
    USER = USER.replace('/', "")
    exists = os.path.isfile("PH/" + USER + ".ph");
    #If I do
    if exists is True:
        #Load the entry
        Respo = open("PH/" + USER + ".ph", "r");
        respo = file.read(Respo);
        Respo.close();
        #reply
        Input = raw_input("BRIAN: " + respo + "\nYOU: ");
        
    #If I don't
    if exists is False:
        #Choose a random entry:
        DB = os.listdir("DB/");
        One = random.choice(DB);
        Respo = open("DB/" + One, "r");
        respo = file.read(Respo);
        Respo.close();
        Input = raw_input("BRIAN: " + respo + "\nYOU: ");
    INPUT = Input.replace("?", "")
    INPUT = INPUT.replace('"', "")
    INPUT = INPUT.replace('PH/', "")
    INPUT = INPUT.replace('\n', "")
    INPUT = INPUT.replace('<', "")
    INPUT = INPUT.replace('>', "")
    INPUT = INPUT.replace('/', "")
    
    RESPO = respo.replace("?", "")
    RESPO = RESPO.replace('"', "")
    RESPO = RESPO.replace('PH/', "")
    RESPO = RESPO.replace('\n', "")
    RESPO = RESPO.replace('<', "")
    RESPO = RESPO.replace('>', "")
    RESPO = RESPO.replace('/', "")
    DBup = open("DB/" + INPUT + ".ph", "w");
    DBup.write(Input);
    file.close(DBup);
    PHup = open("PH/" + RESPO + ".ph", "w");
    PHup.write(Input);
    file.close(PHup);
    Initiate(Input)
start = raw_input("YOU: ")
Initiate(start);
