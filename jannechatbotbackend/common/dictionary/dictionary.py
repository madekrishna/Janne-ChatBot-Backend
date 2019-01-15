import re
import random
from bottle import response
from json import dumps

reflections = {
    "am": "r",
    "was": "were",
    "i": "u",
    "i'd": "u'd",
    "i've": "u'v",
    "ive": "u'v",
    "i'll": "u'll",
    "my": "ur",
    "are": "am",
    "you're": "im",
    "you've": "ive",
    "you'll": "i'll",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "u": "me",
    "ur": "my",
    "urs": "mine",
    "me": "u",
}

# Note: %1/2/etc are used without spaces prior as the chat bot seems
# to add a superfluous space when matching.

psychobabble = (
    (
        r'I\'m (.*)',
        (
            "ur%1?? that's so cool! kekekekeke ^_^ tell me more!",
            "ur%1? neat!! kekeke >_<",
        ),
    ),
    (
        r'(.*) (mencari|cari) (.*)',
        (
            "coba buka 99.co",
        ),
    ),
    (
        r'(.*) don\'t you (.*)',
        (
            "u think I can%2??! really?? kekeke \<_\<",
            "what do u mean%2??!",
            "i could if i wanted, don't you think!! kekeke",
        ),
    ),
    (r'ye[as] [iI] (.*)', ("u%1? cool!! how?", "how come u%1??", "u%1? so do i!!")),
    (
        r'do (you|u) (.*)\??',
        ("do i%2? only on tuesdays! kekeke *_*", "i dunno! do u%2??"),
    ),
    (
        r'(.*)\?',
        (
            "man u ask lots of questions!",
            "booooring! how old r u??",
            "boooooring!! ur not very fun",
        ),
    ),
    (
        r'(cos|because) (.*)',
        ("hee! i don't believe u! >_<", "nuh-uh! >_<", "ooooh i agree!"),
    ),
    (
        r'why can\'t [iI] (.*)',
        (
            "i dunno! y u askin me for!",
            "try harder, silly! hee! ^_^",
            "i dunno! but when i can't%1 i jump up and down!",
        ),
    ),
    (
        r'I can\'t (.*)',
        (
            "u can't what??! >_<",
            "that's ok! i can't%1 either! kekekekeke ^_^",
            "try harder, silly! hee! ^&^",
        ),
    ),
    (
        r'(.*) (like|love|watch) anime',
        (
            "omg i love anime!! do u like sailor moon??! ^&^",
            "anime yay! anime rocks sooooo much!",
            "oooh anime! i love anime more than anything!",
            "anime is the bestest evar! evangelion is the best!",
            "hee anime is the best! do you have ur fav??",
        ),
    ),
    (
        r'I (like|love|watch|play) (.*)',
        ("yay! %2 rocks!", "yay! %2 is neat!", "cool! do u like other stuff?? ^_^"),
    ),
    (
        r'anime sucks|(.*) (hate|detest) anime',
        (
            "ur a liar! i'm not gonna talk to u nemore if u h8 anime *;*",
            "no way! anime is the best ever!",
            "nuh-uh, anime is the best!",
        ),
    ),
    (
        r'(are|r) (you|u) (.*)',
        ("am i%1??! how come u ask that!", "maybe!  y shud i tell u?? kekeke >_>"),
    ),
    (
        r'what (.*)',
        ("hee u think im gonna tell u? .v.", "booooooooring! ask me somethin else!"),
    ),
    (r'how (.*)', ("not tellin!! kekekekekeke ^_^",)),
    (r'(hi|hello|hey) (.*)', ("hi!!! how r u!!",)),
    (
        r'quit',
        (
            "mom says i have to go eat dinner now :,( bye!!",
            "awww u have to go?? see u next time!!",
            "how to see u again soon! ^_^",
        ),
    ),
    (
        r'(.*)',
        (
            "I dont understand what you said",
        ),
    ),
)
