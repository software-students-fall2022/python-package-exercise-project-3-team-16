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


def funny(name):
    '''
    Returns happy/funny quotes
    '''
    quotes = {
        "Steven Wright": "I wish the first word I ever said was the word 'quote,' so right before I die I could say 'unquote.",
        
        "Issac Asimov": "Though sleep is called our best friend, it is a friend who often keeps us waiting!",
        
        "Leo Tolstoy": "Happiness is an allegory, unhappiness a story.",
        
        "J.K Rowling": "Happiness can be found even in the darkest of times; if only one remembers to turn on the light.",
        
        "Oscar Wilde": "Some cause happiness wherever they go; others, whenever they go.",
        
        "Mark Twain": "When your friends begin to flatter you on how young you look, it's a sure sign you're getting old.",
    }
    
    if name in quotes.keys():
        return random.choice(quotes.get(name))
    elif name == "":
        return random.choice(quotes.get(random.choice(list(quotes.keys()))))
    else:
        return "The author doesn't exist"
    
    
    

