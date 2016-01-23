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
    exists = os.path.isfile("PH/" + user + ".ph");
    #If I do
    if exists is True:
        #Load the entry
        Respo = open("PH/" + user + ".ph", "r");
        respo = file.read(Respo);
        Respo.close();
        #reply
        Input = raw_input(respo);
        
    #If I don't
    if exists is False:
        #Choose a random entry:
        DB = os.listdir("DB/");
        One = random.choice(DB);
        Respo = open("DB/" + One, "r");
        respo = file.read(Respo);
        Respo.close();
        Input = raw_input(respo);
    DBup = open("DB/" + Input + ".ph", "w");
    DBup.write(Input);
    file.close(DBup);
    PHup = open("PH/" + respo + ".ph", "w");
    PHup.write(Input);
    file.close(PHup);
    Initiate(Input)
#Begin our engine, saying "I am Brian, a Bot..." etc.
Initiate("Who are you?");
