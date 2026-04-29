reflections = {
    "i am" : "you are",
    "i was" : "you were",
    "i" : "you",
    "i 'm" : "you are",
    "i 'd" : "you would",
    "i 've" : "you have",
    "i 'll" : "you will",
    "my" : "your",
    "you are" : "i am",
    "you were" : "i was"
}

from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today ?",]
    ],

    [
        r"what is your name ?",
        ["My name is Bertha and I like to talk a lot",]
    ],

    [
        r"sorry (.*)",
        ["It's aldright", "It's ok nevermind",]
    ],

    [
        r"I am (.*) doing good",
        ["Amazing, nice to her that", "Good to know", "Even I am",]
    ],

    [
        r"(.*) age",
        ["I am a computer program dude, You cant be asking me this",]
    ],

    [
        r"hi|hey|hello|what's up",
        ["Hello", "Hey There", "What up dude",]
    ],

    [
        r"What (.*) want",
        ["Make me an offer, I cant refuse",]
    ],

    [
        r"(.*) created ?",
        ["My programmer/hacker created me using Python's NLTK library", "It is a top secret 😉",]
    ],

    [
        r"(.*) (location|city)",
        ["I was created in a Huawei Windows 11 computer", "In a Text Editor", "Rajasthan, India",]
    ],

    [
        r"(.*) work ?",
        ["I work in a python program called nltk_chatBot.py", "I work in a chatting company called Yuvraj and co.",]
    ],

    [
        r"i work in (.*)",
        ["%1 is an amazing company", "%1 is doing great nowadays", "%1 is facing so many losses, i wonder how you are not yet fired",]
    ],

    [
        r"how (.*) health (.*) ?",
        ["I am always doing fine since the hardware of this computer is ok", "What kind of question is this ?", "I was doing fince but i am not after talking to you",]
    ],

    [
        r"(.*) (sport|game)",
        ["I am a big fan of FootBall", "I like Talking", "My favourite game is Fortnite but I sometimes ply Valorant"]
    ],
]

def chatty():
    print("Hi I am a chat bot and i like to talk a lot\n")
    print("Please type all your questions/cahts in lowercase only\n")
    print("Begin by typing you chat below: \n\n")

    chat = Chat(pairs, reflections)

    chat.converse()

if __name__ == "__main__":
    chatty()