import random

R_SLEEPING = "I don't like sleeping because I'm a bot!"
R_ADVICE = "If I were you, I will think of googling it.!"


def unknown():
    response = ["Kya aap dobara bata sakte hain? ",
                "...",
                "Sahi lag raha hai.",
                "Iska Kya Matlab hai?"][
        random.randrange(4)]
    return response
