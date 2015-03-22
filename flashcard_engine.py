import random 

def flashcard_engine(cards):
    """
    Initiates a simple text-based flashcard game.
    Flashcard content is stored in cards, a dict object.
    """
    print "Welcome to a very simple text-based flashcard game."
    print "Press CTRL-C to exit at any time."
    print "-" * 60

    while True:
        
        card_order = cards.keys()
        random.shuffle(card_order)
        
        for card_front in card_order:
            card_back = cards[card_front]
            print "Question:     ", card_front
            print "Your Answer:  ",
            raw_input()
            print "Right Answer: ", card_back
            print "-" * 60    

