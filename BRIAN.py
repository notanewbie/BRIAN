import os
import random
import math
import time
import sys
from findtext import scour
import urllib2
import sys
#botname = "BRIAN"
ver = "18.7.13"
#update = "yes"
try:
    tempfile = open("settings.pts", "r");
    settings = file.read(tempfile);
    tempfile.close();
except IOError:
    tempfile = open("settings.pts", "w");
    tempfile.write("botname = BRIAN\nupdate = yes")
    tempfile.close();
    tempfile = open("settings.pts", "r");
    settings = file.read(tempfile);
    tempfile.close();
c = 0
while c < len(settings.split("\n")):
    if settings.split("\n")[c].split(" = ")[0] in "botname":
        botname = settings.split("\n")[0].split(" = ")[1]
    if settings.split("\n")[c].split(" = ")[0] in "autoupdate":
        update = settings.split("\n")[0].split(" = ")[1]
    c = c + 1
def autoupdate():
    l = urllib2.urlopen("https://raw.githubusercontent.com/notanewbie/BRIAN/master/latest?nocache").read().replace("\n", "")
    ldl = "https://github.com/notanewbie/BRIAN/archive/" + l + ".zip"
    if l in ver:
        #print l
        #print ver
        print botname + " is up to date."
        print "Version: " + ver;
    else:
        print "Updating to " + l + "..."
        f = open(sys.argv[0], "w")
        f.write(urllib2.urlopen("https://raw.githubusercontent.com/notanewbie/BRIAN/" + l + "/BRIAN.py").read())
        file.close(f)
        t = sys.argv[0]
        print "Update installed."
        print "Restarting..."
        #raw_input("Please restart inact changes. Press enter to continue.")
        #sys.exit(0)
        execfile(t)
if "no" in update:
    ver = ver
else:
    try:
        l = urllib2.urlopen("https://raw.githubusercontent.com/notanewbie/BRIAN/master/latest?nocache").read().replace("\n", "")
        autoupdate()
    except urllib2.URLError:
        print "Unable to reach CDN server to check for updates. Please connect to the internet. If the problem persists, please email notanewbie at admin@notanewbie.com."
        print "Version: " + ver;
#This is BRIAN, a Bot Really Intelligent And Nice.
#
#
#This code is still undergoing Beta testing.

#Function to parse harmful characters.

def parseChars(t):
    t = t.replace("?", "")
    t = t.replace('"', "")
    t = t.replace('PH/', "")
    t = t.replace('\n', "")
    t = t.replace('<', "")
    t = t.replace('>', "")
    t = t.replace('/', "")
    t = t.replace(':', "")
    t = t.replace('*', "")
    t = t.replace('\\', "")
    return t

#Log my intelligence upon startup.

#Find out how many phrases I know.
kno = os.listdir("DB/")
i = 0
for item in kno:
    i = i + 1
kno = i * 1.0
i = 0
#Find out how many phrases I understand.
und = os.listdir("PH/")
for item in und:
    i = i + 1
und = i * 1.0
i = 0
#Calculate my relative knowledge of phrases known to phrases understood.
try:
    Think = und/kno
    Think = Think * 100
    Think = str(Think) + "%"
    #Save the log.
    filename = time.strftime("%Y.%m.%d - %H-%M-%S.txt")
    Logz = open(filename, "w");
    Logz.write("Knows " + str(kno) + " phrases. \n Understands " + str(und) + " phrases. \n Knowledge level: " + Think + ".");
    file.close(Logz);
except ZeroDivisionError:
    #Save the log.
    filename = time.strftime("%Y.%m.%d - %H-%M-%S.txt")
    Logz = open(filename, "w");
    Logz.write("Is brand new. Knows nothing.");
    file.close(Logz);

#Make a new function. This will be the engine.
def Initiate(user):
    #Look in the database for a match to "User" so I can respond.
    #Do I know how to respond?
    USER = parseChars(user)
    exists = os.path.isfile("PH/" + USER + ".ph");
    #If I do
    if exists is True:
        #Load the entry
        Respo = open("PH/" + USER + ".ph", "r");
        respo = file.read(Respo);
        Respo.close();
        #reply
        Speak(respo)
        Input = raw_input(botname + ": " + respo + "\nYOU: ");
        
    #If I don't
    if exists is False:
        #Choose a similar response:
        PHDB = os.listdir("PH/");
        T = open("PH/" + scour(user, PHDB)[0], "r");
        respo = file.read(T);
        T.close();
        Input = raw_input(botname + ": " + respo + "\nYOU: ");
    INPUT = parseChars(Input)
    
    RESPO = parseChars(respo)

    DBup = open("DB/" + INPUT + ".ph", "w");
    DBup.write(Input);
    file.close(DBup);
    PHup = open("PH/" + RESPO + ".ph", "w");
    PHup.write(Input);
    file.close(PHup);
    Initiate(Input)
start = raw_input("YOU: ")
#Speak() from pySpeak
def Speak(words):
    if "win32" in sys.platform or "win64" in sys.platform:
        os.system('mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""' + parseChars(words) + '"")(window.close)")')
    if "darwin" in sys.platform:
        os.system("say " + words)
#DEMO CODE:
#
#Speak("I'm eighteen years old but I'm not done yet. I'm not Molly and I'm not Percocet.")

Initiate(start);
