import random

def getLifeAdvice() :
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


def getInspiration(name):
    # returns inspirational quote

    quotes = {
        "Lemony Snicket": [
            "Do the scary thing first, and get scared later.",
            "All cannot be lost when there is still so much being found.",
            "When things don\'t go right, go left.",
            "Sometimes the things you\'ve lost can be found again in unexpected places."
        ],
        "Amelia Earhart": [
            "The most difficult thing is the decision to act, the rest is merely tenacity."
        ],
        "Angela Bassett": [
            ("Don't settle for average. Bring your best to the moment. Then, whether it fails or succeeds, "
            "at least you know you gave all you had."),
        ],
        "Barbara Elaine Smith": [
            "I have stood on a mountain of no\'s for one yes."
        ],
        "Mary Anne Radmacher": [
            ("Courage doesn't always roar. Sometimes courage is a quiet voice at the end of the day saying, "
            "\"I will try again tomorrow.\"")
        ],
        "Maya Angelou": [
            ("Courage is the most important of all the virtues because without courage, "
            "you can't practice any other virtue consistently.")
        ],
        "Frederick Douglass": [
            "If there is no struggle, there is no progress."
        ]
    }

    if name in quotes.keys():
        quote = random.choice(quotes.get(name))
    elif name == "":
        someName = random.choice(list(quotes.keys()))
        quote = random.choice(quotes.get(someName))
    else:
        print("Sorry, we don\'t seem to have any quotes from anyone by that name yet!\n")
        quote = "NO SUCH AUTHOR"

    return quote
