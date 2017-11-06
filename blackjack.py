import random
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
#     loading cards
def loadimages(card_images):
    suits = ['diamonds','club']
    face_cards = ['jack','queen','king']
    extension = 'png'
#     for suit load card images
    for suit in suits:
#       first the number cards from 1 to 10
        for card in range(1,11):
            name = 'svgcards/{}_{}.{}'.format(str(card),suit,extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card,image,))
#         nest the face cards
        for card in face_cards:
            name = 'svgcards/{}_{}.{}'.format(str(card),suit,extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10,image,))

# main screen created
mainWindow = tkinter.Tk()
# set up the screen and frames for dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background="green")
result_text = tkinter.IntVar()
result = tkinter.Label(mainWindow,textvariable=result_text)
result.grid(row=0,column=0)
card_frame = tkinter.Frame(mainWindow,relief="sunken",borderwidth=1,background="green")
card_frame.grid(row=1,column=0,sticky='ew',rowspan=2,columnspan=3)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame,text="Dealer",background="green",fg='white').grid(row=0,column=0)
tkinter.Label(card_frame,textvariable=dealer_score_label,background="green",fg="white").grid(row=1,column=0)
#embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame,background="green")
dealer_card_frame.grid(row=0,column=1,sticky="ew",rowspan=2)
player_score_label = tkinter.IntVar()
tkinter.Label(card_frame,text="Player",background="green",fg="white").grid(row=2,column=0)
tkinter.Label(card_frame,textvariable=player_score_label,background="green",fg="white").grid(row=3,column=0)
player_score = 0
player_ace = False
# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame,background="green")
player_card_frame.grid(row=2,column=1,sticky="ew",rowspan=2)
# load cards
cards = []
loadimages(cards)

# create a deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)


# create the list to store dealer's and players hands
dealer_hand=[]
player_hand=[]

def deal_card(frame):
# pop the next card off the top of the deck
    next_card = deck.pop(0)
# add the image to a label and display the label
    tkinter.Label(frame,image=next_card[1],relief='raised').pack(side='left')
# now return the cards face value
    return next_card
def dealer_card():
    dealer_score  = score_hand(dealer_hand)
    while 0<dealer_score<17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    player_score = score_hand(player_hand)
    if player_score>21:
        result_text.set("Dealer Wins!")
    elif dealer_score>21 or dealer_score<player_score:
        result_text.set("Player Wins!")
    elif dealer_score>player_score:
        result_text.set("Dealer WIns!")
    else:
        result_text.set("Draw!")

def player_card():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score>21:
        result_text.set("Dealer Wins!")
    # global player_score
    # global player_ace
    # card_value=deal_card(dealer_card_frame)[0]
    # if(card_value == 1 and not player_ace):
    #     player_ace = True
    #     card_value=11
    # player_score+=card_value
    # # if bust, check for ace and subtract
    # if player_score>21 and player_ace:
    #     player_score-=10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score>21:
    #     result_text.set("Dealer Wins!")
    # print(locals())

def score_hand(hand):
    #calculate the total score of all cards in the list
    #only one ace can have a value of 11, and will set to 1 if busts
    score =0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust , check if it is an ace and subtract 11
        if score>21 and ace:
            score -= 10
            ace = False
    return score



button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3,column=0,columnspan=3,sticky="w")

dealer_button = tkinter.Button(button_frame,text="Dealer",command=dealer_card)
dealer_button.grid(row=0,column=0)

player_button = tkinter.Button(button_frame, text="Player",command=player_card)
player_button.grid(row=0, column=1)

player_card()
dealer_hand.append(deal_card(dealer_card_frame))
player_card()





mainWindow.mainloop()

