import random

def get() :
    '''
    Returns a randomized piece of life advice if the second given argument is life advice
    '''
    pieces_of_advice = [
        "Forgive and let go",
        "Whatever you do, give it 100%",
        "Never stop learning",
        "Your thinking changes your life",
        "Be kind to people; treat people as you'd like to be treated",
        "Starting is the hardest part"
    ]

    return random.choice(pieces_of_advice)

def cs(question, debug):
    #random.seed(question);
    possibleErrors = [
        "You forgot a semicolon",
        "You forgot to close a bracket",
        "You misspelled a keyword",
        "Incorrect indentation",
        "Incorrect version",
        "There is no saving this one"
    ]
    var = random.random() * 10
    #print(var);
    if var >= 8:
        if debug:
            return random.choice(possibleErrors)
        else:
            days = Random.random() * 100
            return "You are on the right track and will finish your assignment/project in" + str(days)
    else:
        return "You are screwed. Switch major. Go next."
