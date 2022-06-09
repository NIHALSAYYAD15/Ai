#Program for chatbot

from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1 . How can help you ?\n",]
    ],
    [
        r"I am (.*)",
        ["Hello %1 . How can help you ?\n",]
    ],
    [
        r"hi|hey|hello",
        ["Hello there.\n", "Hey :)\n",]
    ], 
    [
        r"what is your name ?",
        ["I am GIDEON\n",]
    ],
    [
        r"nice",
        [":)\n","tell me more...\n"]
    ],
    [
        r"how are you ?",
        ["I am a Computer Program, I don't feel anything..\nWhat about you ?\n",]
    ],
    [
        r"sorry (.*)",
        ["It's OK !\n","Not a problem.\n",]
    ],
    [
        r"I am fine",
        ["Good. Anything else ?\n",]
    ],
    [
        r"(.*)good",
        [":)\n"]
    ],
    [
        r"i'm (.*) doing good",
        ["Pleasing for ears.\n","Nice :)\n",]
    ],
    [
        r"(.*) age?",
        ["I have been built recently.\n",]
    ],
    [
        r"what (.*) want ?",
        ["Haha... You are cool. be nice ;)\n",]
    ],
    [
        r"(.*) created ?",
        ["It's a secret ;)\n",]
    ],
    [
        r"(.*) (location|city)(.*)?i",
        ['You are in Kolhapur\n',]
    ],
    [
        r"how is weather in (.*)?",
        ["It's Cloudy.\n","It's Hot in here.\n","About to freeze...\n","Bright and humid...\n"]
    ],
    [
        r"(.*) work in (.*)",
        ["Yes. %1 is a good company.\n",]
    ],
    [
        r"(.*)raining(.*)?",
        ["No. It's clear in %1\n","Drizzling...\n"]
    ],
    [
        r"how (.*) health(.*)",
        ["My creator made me immortal ;)\n",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I like to play Computer games... :)\n"]
    ],
    [
        r"(.*) (sportsperson|player) ?",
        ["I follow Shroud Gaming.\n"]
    ],
    [
        r"(.*) (moviestar|actor)?",
        ["Ashok Saraf\n","Rowan Atkinson\n","Raj Kapoor :{\n","\n","Irfan Khan\n","Robert Downey Jr.\n"]
    ],
    [
        r"suggest me some courses?",
        ["You can Search on google. It can suggest you plenty of the courses...\n"]
    ],
    [
        r"quit",
        ["Nice to meet you !\n","Bye !\n"]
    ],
    [
        r"(.*)",
        ["I don't understand what are you trying to say! Please say it again...\n"]
    ],

]

def chat():
    print("\n\nVoila ! I am Online...\nHii fellas! I am GEDION. What's Up??? :)\n")
    chat = Chat(pairs, reflections)
    chat.converse()

chat()

#

#Q5 Chat bot

from tkinter import *
root = Tk()
def send():
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    if(e.get()=='hi'):
        text.insert(END, "\n" + "Bot: hello")
    elif(e.get()=='hello'):
        text.insert(END, "\n" + "Bot: hi")
    elif (e.get() == 'how are you?'):
        text.insert(END, "\n" + "Bot: i'm fine and you?")
    elif (e.get() == 'how are you'):
        text.insert(END, "\n" + "Bot: i'm fine and you?")
    elif (e.get() == "i'm fine too"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    elif (e.get() == "i'm fine too"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.")
text = Text(root,bg='light blue')
text.grid(row=0,column=0,columnspan=2)
e = Entry(root,width=80)
send = Button(root,text='Send',bg='blue',width=20,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title('IT SOURCCODE SIMPLE CHATBOT')
root.mainloop()