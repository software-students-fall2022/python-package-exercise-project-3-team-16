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



    
    
    

