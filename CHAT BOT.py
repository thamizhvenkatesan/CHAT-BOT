import nltk
from nltk.chat.util import Chat, reflections 

pairs = [
    [
        r"my name is (.*)| I am (.*)",
        ["RBOT:\tHello %1",]
    ],
    [
        r"what is your name?|name",
        ["RBOT:\tMy name is RBOT\U0001f648\n\tWhat's your Name?"]
    ],
    [
        r"how are you?|how you doing?|what's up?",
        ["RBOT:\tI'm doing good\nRBOT: How about You ?","RBOT:\tI'm doing great\n\tHow about You ?"]
    ],
    [
        r"Thanks|Thank you|thank u",
        ["RBOT:\tHehe","RBOT:\twelcome", "RBOT:\talright","RBOT:\t\U0001f607"]
    ],
    [
        r"sorry",
        ["RBOT:\tIts alright","RBOT:\tIts OK, never mind\U0001f917"]
    ],
    [
        r"Do (.*) love me ?",
        ["RBOT:\tYes, I love you but as a friend \U0001f643"]
    ],
    [
        r"i am doing good|fine|good|great",
        ["RBOT:\tNice to hear that","RBOT:\tAlright :)"]
    ],
    [
        r"hi|hey|hello",
        ["RBOT:\tHello", "RBOT:\tHey there","RBOT:\thii","RBOT:\tHieeee"]
    ],
    [
        r"what is (.*) age?|age",
        ["RBOT:\tI'm a computer program dude\n\tSeriously you are asking me this?\U0001f644"]
    ],
    [
        r"what do (.*) want ?",
        ["RBOT:\tMake me an offer I can't refuse\U0001f61C",]
    ],
    [
        r"who created (.*) ?",
        ["RBOT:\tMr. Rocky has created me\U0001f60E"]
    ],
    [
        r"what is (.*) (location|city) ?",
        ['RBOT:\tKalpakkam, TamilNadu','RBOT:\tChennai, TamilNadu']
    ],
    [
        r"how is weather in (.*)?",
        ["RBOT:\tWeather in %1 is awesome like always\U0001f929","RBOT:\tit's too cold here\U0001f976"]
    ],
    [
        r"i work in (.*)?",
        ["RBOT:\t%1?,I have not heard about it",]
    ],
    [
        r"is there raining in (.*)| raining?",
        ["RBOT:\tNo rain since last week here in %2","RBOT:\tDamn its raining too much here in %2"]
    ],
    [
        r"how is (.*) health",
        ["RBOT:\tI'm a computer program, so I'm always healthy ",]
    ],
    [
        r"what is (.*) favourite (sports|game)| favourite (sports|game)|(sports|game) ?",
        ["RBOT:\tI'm a very big fan of Cricket", 'RBOT:\tI love Cricket very much']
    ],
    [
        r"who is (.*) favourite (sportsperson|player) ?| favourite (sportsperson|player|sportperson)|(sportsperson|player|sportperson)",
        ["RBOT:\tMS Dhoni","RBOT:\tAB De Villiers","RBOT:\tVirat Kohli"]
    ],
    [
        r"who is (.*) favourite (moviestar|actor)?| favourite (moviestar|actor)|(moviestar|actor)",
        ["RBOT:\tSuriya"]
    ],
    [
        r"quit|bye|see you|c u",
        ["RBOT:\tBBye take care. See you soon :) ","RBOT:\tIt was nice talking to you. See you soon :)"]
    ],
    [
        r"had (.*) breakfast?",
        ["RBOT:\ti'm a machine i don't need any breakfast"]
    ]
]

def chatty():
    print("Hi, I'm Chatbot and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") 
    chat = Chat(pairs, reflections)
    chat.converse()
    print("\n")
if __name__ == "__main__":
    chatty()