"""
File Name   :  chats.py
Author      :  [Me]
Date        :  MM/DD/YYYY
Description :  This script is meant to generate a read-only text message ui. 

Usage:
- Ensure that the required libraries are installed by running 'pip install pyperclip'.
- Update any custom modules.
- Run the script to perform the desired tasks.
"""

#%%%# Import Statements #%%%#

import pyperclip            # Allows for copying to clipboard


#%%%# Chat Log Class #%%%#


class chatLog(list):
    """
    Class stores data for a record of chats
    Attributes:
        self (list) : List of chat data
        pName (str) : Name of the profile
        rName (str) : Name of the person
    Methods:
        printOut    : Copys the variable to the clipboard
        newChat     : Appends a new chat to self
    """
        
    def __init__(self, PN=None, RN=None, L=None):
        super().__init__()


        if PN == None:
            PN=str(input("Profile Name: "))

        if RN == None:
            RN=str(input("Real Name: "))

        self.pName = PN
        # print(self.pName)
        self.rName = RN
        # print(self.rName)

        if L==None :
            self.append({  'Type': 'D',
                        'Text': str(input("First Date: "))  })
        else:
            self.append(L)
        


    def printOut(self):
        string = str(self).replace("}, {", "\n}\n,\n{\n").replace("[{", "[\n{\n",1).replace("',", "',\n").replace('",','",\n')
        # .replace("{", "{\n").replace("}","\n}\n").replace(", ",",\n")
        string = "".join(([str(self.pName), " = chatLog('",self.pName, "','",  self.rName, 
                           "',", str(string), "\n) # End list"]))
        print(string)
        pyperclip.copy(string)

    def newChat(self):
        self.append({
        "Type": input("Type: "),
        "Text": input("Text: "),
        "Time": input("Time: "),
        "Number": 0
        })
    
    def multiAdd(self):
        valid = 1
        while valid:
            self.newChat()
            valid = (input("Keep going?")=="")

        self.printOut()


#%%%# Custom Functions #%%%#


#%%%# Storage Variables #%%%#

ray = [
{
'Type': "N",
'Text': "HMU",
'Label': "Ray"
},
{
'Type': 'D',
'Text': 'Sep 3, 2023'
}
,
{
'Type': 'S',
 'Text': "Hey what's up",
 'Time': '6:08 PM',
 'Number': 1
}
,
{
'Type': 'R',
 'Text': 'Going good hbu',
 'Time': '6:09 PM',
 'Number': 2
}
,
{
'Type': 'S',
 'Text': "Not too bad, how's classes?",
 'Time': '2:30 PM',
 'Number': 3
}
,
{
'Type': 'R',
 'Text': 'Not bad yet, but im procrastinating a lot of hw lol?',
 'Time': '2:35 PM',
 'Number': 4
}
,
{
'Type': 'S',
 'Text': 'Honestly same, a lot of small stuff but still',
 'Time': '2:30 PM',
 'Number': 5
}
,
{
'Type': 'R',
 'Text': 'Exactly, it all just piles up lol',
 'Time': '2:35 PM',
 'Number': 6
}
,
{
'Type': 'R',
 'Text': "What's ur major",
 'Time': '2:35 PM',
 'Number': 7
}
,
{
'Type': 'S',
 'Text': 'Mechanical Engineering hbu?',
 'Time': '2:30 PM',
 'Number': 8
}
,
{
'Type': 'R',
 'Text': 'Oh nice, im an illustration major',
 'Time': '2:35 PM',
 'Number': 9
}
,
{
'Type': 'S',
 'Text': 'Cool, what year r u?',
 'Time': '6:11 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': '3rd, hbu?',
 'Time': '6:11 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'Im 2nd',
 'Time': '6:11',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'Oh nice',
 'Time': '6:12 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': "So i see you're looking for fun with other RIT students",
 'Time': '6:15 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'Yeah, hbu?',
 'Time': '6:15 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'Definitely',
 'Time': '6:16 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'What r u into?',
 'Time': '6:16 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'Mainly giving head, some sub stuff, other stuff too hbu?',
 'Time': '6:17 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'Vers, open to mostly anything',
 'Time': '6:17 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'Cool',
 'Time': '6:17 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'Do you live on campus?',
 'Time': '6:17 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'Nah, province, so campus adjacent',
 'Time': '6:18 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'Oh nice i had a friend that lived there last year.',
 'Time': '6:18 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'Ye kinda a vibe lmao, hbu?',
 'Time': '6:18 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'Im at UC lol',
 'Time': '6:18 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'How many guys have u been with?',
 'Time': '6:19 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'I mean I typically like a fwb situation, but not a lot of guys are into that, so like maybe 15 over the past couple years',
 'Time': '6:20 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'I could be down for that, im at 5?',
 'Time': '6:20 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'Do you have a car?',
 'Time': '6:21 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'Nah, i use the shuttle hbu?',
 'Time': '6:21 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': "I don't have a car and dont use the shuttle, but i can host.",
 'Time': '6:22 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': "Cool, kinda can't meet up today, but we can see what works when the time cums",
 'Time': '6:22 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'lol love the pun',
 'Time': '6:23PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'Caught that huh lol',
 'Time': '6:23 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': "Maybe we could try for between classes, what's ur schedule?",
 'Time': '6:23',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'M-Th im free 1-4:30 then all night after 8, F im free after 1, and all day weekends ',
 'Time': '6:24 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'Cool i got 12-3 MF, end at 4 MWF, also after 5 on Tuesday, and most weekends.',
 'Time': '6:24 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'Figure throughout the week would work well, we can just head over to ur place then.',
 'Time': '6:25 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'Ooh sounds like we got plenty of matching times',
 'Time': '6:25 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': "That'll be sick, fuckin after classes",
 'Time': '6:26 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'Fuck yeah',
 'Time': '6:26 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': "How often do you think you'll be lookin for?",
 'Time': '6:26 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'Not sure, have to see how to goes, but proabably a good bit.',
 'Time': '6:26 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'lol nice honestly im horny like every single day so im always down',
 'Time': '6:27 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'Same and good to know...',
 'Time': '6:27 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'Yeah lol, wanna add on snap?',
 'Time': '6:40 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'It would be helpful to know what u look like and yeah sure',
 'Time': '6:40 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'Oh my bad lmao',
 'Time': '6:41 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'Img_R_001;Img_R_002;Img_R_003',
 'Time': '6:41 PM',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'My snap is ***snap***',
 'Time': '6:41 PM',
 'Number': 0
}
,
{
'Type': 'S',
 'Text': 'Just added ya',
 'Time': '6:41 PM',
 'Number': 0
 }
 ,
 {
'Type': 'D',
'Text': 'Sep 4, 2023'
}
,
{
'Type': 'S',
 'Text': "How's ya night going",
 'Time': '12:25 AM',
 'Number': 0
 }

]


dawson = []

rawleigh = []

Young_8 = chatLog('Young_8','Idk',[
{
'Type': 'D',
 'Text': 'Sep 8, 2023'
}
,
{
'Type': 'S',
 'Text': "Hey how's it going?",
 'Time': '---',
 'Number': 0
}
,
{
'Type': 'R',
 'Text': 'Good hbu?',
 'Time': '---',
 'Number': 0}]
) # End list



#%%%# CODE #%%%#


# print(ray)
# ray.append(newChat("R","yooo yoo yoo ", "03:23 AM", 7))
# print(ray)
# (dictionPrint(ray, "ray"))

if __name__ == '__main__':
    


    varis = dict(locals())
    print(" ")
    for var_name, var_value in varis.items():
        # print(f"{var_name}: {var_value}")
        if isinstance(var_value, (list)):
            print(var_name)
    print(" ")


    (chatLog().multiAdd())


#%%%# End of File #%%%# 