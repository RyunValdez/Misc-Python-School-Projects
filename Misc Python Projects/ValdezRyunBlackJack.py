###########################################################################
#                    Playing Card Game Black Jack                         #
#                                                                         #
#   Programmed by Dean Zeller (03-08-2015)                                #
#   Modified by Ryun Valdez   (4-10-2015)                                 #
#                                                                         #
#   Description:  The file contains Dean Zeller's original card           #
#   objects and uses them to create a game of blackjack.                  #
#                                                                         #
#   All code contained within is copyright (c) 2015 Dean Zeller.          #
#   Permission to use code is given, provided is it for educational       #
#   purposes only.  Any commercial use of this code must obtain           #
#   permission from the authors.                                          #
#                                                                         #
###########################################################################
import math
import random
import PIL.Image
import PIL.ImageTk
from tkinter import *

Gui = Tk()
Gui.geometry('500x485+25+150')
Gui.wm_title("Black Jack")

c = Canvas(width=500, height=400, bg='green')
c.grid(row=0, column=1, columnspan=3, rowspan= 25)

Deck = ["1c","1s","1h","1d","2c","2s","2h","2d",
        "3c","3s","3h","3d","4c","4s","4h","4d",
        "5c","5s","5h","5d","6c","6s","6h","6d",
        "7c","7s","7h","7d","8c","8s","8h","8d",
        "9c","9s","9h","9d","tc","ts","th","td",
        "jc","js","jh","jd","qc","qs","qh","qd",
        "kc","ks","kh","kd"]

def shuffle(array):
    random.shuffle(array)

def newShoe():
    global Deck
    Deck = ["1c","1s","1h","1d","2c","2s","2h","2d",
        "3c","3s","3h","3d","4c","4s","4h","4d",
        "5c","5s","5h","5d","6c","6s","6h","6d",
        "7c","7s","7h","7d","8c","8s","8h","8d",
        "9c","9s","9h","9d","tc","ts","th","td",
        "jc","js","jh","jd","qc","qs","qh","qd",
        "kc","ks","kh","kd"]
    random.shuffle(Deck)
    c.after(300)
    action_text = c.create_text(250, 50, text="Adding new deck...",
                               justify=CENTER, fill="white")
    c.update()
    c.after(300)
    c.itemconfig(action_text, text="")
    c.update()
    c.after(300)
    c.itemconfig(action_text, text="Adding new deck...")
    c.update()
    c.after(300)
    c.itemconfig(action_text, text="")
    c.update()
    c.after(300)
    c.itemconfig(action_text, text="Adding new deck...")
    c.update()
    c.after(300)
    c.delete(action_text)
    c.update()

###########################################################################
#  Suit -- Enumerated data type for the card suit.                        #
###########################################################################
class Suit:
    CLUBS    = 0
    SPADES   = 1
    HEARTS   = 2
    DIAMONDS = 3

    #######################################################################
    #  num2Suit -- Convert an integer to a suit.                          #
    #######################################################################
    def num2Suit(self,n):
        if n==0:
            return "Clubs"
        elif n==1:
            return "Spades"
        elif n==2:
            return "Hearts"
        elif n==3:
            return "Diamonds"
        else:
            return "Unknown suit"

###########################################################################
#  Rank -- Ranking of each card, from low ace to high ace.                #
###########################################################################
class Rank:
    NONE   =  0
    LOWACE =  1
    _2     =  2
    _3     =  3
    _4     =  4
    _5     =  5
    _6     =  6
    _7     =  7
    _8     =  8
    _9     =  9
    _10    = 10
    JACK   = 11
    QUEEN  = 12
    KING   = 13
    ACE    = 14

    #######################################################################
    #  num2Rank -- Converts a number to a character card rank.            #
    #######################################################################
    def num2Rank(n):
        if n==0:
            return "None"
        elif n==1:
            return "Low Ace"
        elif n==2:
            return "2"
        elif n==3:
            return "3"
        elif n==4:
            return "4"
        elif n==5:
            return "5"
        elif n==6:
            return "6"
        elif n==7:
            return "7"
        elif n==8:
            return "8"
        elif n==9:
            return "9"
        elif n==10:
            return "10"
        elif n==11:
            return "Jack"
        elif n==12:
            return "Queen"
        elif n==13:
            return "King"
        elif n==14:
            return "Ace"
        else:
            return "Unknown suit"


###########################################################################
#  Card -- A single card in a standard deck.                              #
###########################################################################
class Card:
    
    def __init__ (self, abrev="2c"):
        self.abrev = abrev
        a0 = self.abrev[0]
        a1 = self.abrev[1]
        self.flipped = False
        self.x = 0
        self.y = 0


        if a0 == '1':
            self.rank = Rank.LOWACE
        elif '1' <= a0 <= '9':
            self.rank = int(a0)
        elif a0 == 'T' or a0 == 't':
            self.rank = Rank._10
        elif a0 == 'J' or a0 == 'j':
            self.rank = Rank.JACK
        elif a0 == 'Q' or a0 == 'q':
            self.rank = Rank.QUEEN
        elif a0 == 'K' or a0 == 'k':
            self.rank = Rank.KING
        elif a0 == 'A' or a0 == 'a':
            self.rank = Rank.ACE
        else:
            print("Unknown rank:",a0)

        if a1 == 'C' or a1 == 'c':
            self.suit = Suit.CLUBS
        elif a1 == 'D' or a1 == 'd':
            self.suit = Suit.DIAMONDS
        elif a1 == 'H' or a1 == 'h':
            self.suit = Suit.HEARTS
        elif a1 == 'S' or a1 == 's':
            self.suit = Suit.SPADES
        else:
            print("Unknown suit:",a1)

        if self.rank == 1:
            self.value = 11
        elif 1< self.rank <= 10:
            self.value = self.rank
        elif 11 <= self.rank <=13:
            self.value = 10
            

        self.imgSheet = PIL.Image.open('classic-playing-cards.png')
        self.cardImg = PIL.ImageTk.PhotoImage(self.imgSheet.crop(
            ((self.rank-1)*72,self.suit*98,(self.rank)*72,(self.suit+1)*98)))

    #######################################################################
    #  getRank -- Returns the card rank, in integer form.                  #
    #######################################################################
    def getRank(self):
        return self.rank

    #######################################################################
    #  getRankChar -- Returns the card rank, in character form.           #
    #######################################################################
    def getRankChar(self):
        return self.abrev[0]

    #######################################################################
    #  getSuit -- Returns the card suit, in integer form.                 #
    #######################################################################
    def getSuit(self):
        return self.suit

    #######################################################################
    #  getSuitChar -- Returns the card suit, in character form.           #
    #######################################################################
    def getSuitChar(self):
        return self.abrev[1]

    #######################################################################
    #  getAbrev -- Returns the two-character abreviation of the card.     #
    #######################################################################
    def getAbrev(self):
        return self.abrev


    ###############
    def drawCard(self, x=0, y=0, flip=False):
        c.after(200)
        self.x = x
        self.y = y
        if flip == False:
            c.create_image(38+x,50+y,image=self.cardImg)
        else:
            self.flipped = True
            c.create_rectangle(x,y,x+72,y+98, fill="blue", tag="dCard")
        c.update()
        
    def flip(self):
        if self.flipped == True:
            c.delete("dCard")
            c.create_image(38+self.x,50+self.y,image=self.cardImg)
        else:
            c.create_rectangle(self.x,self.y,self.x+72,self.y+98,
                               fill="blue", tag="dCard")

class Chip:

    objectName = "chip"
    objectNum = 0
    
    def __init__ (self, amount=0,x=0, y=0):
        self.x = x
        self.y = y
        self.amount = amount
        self.chipImg = PIL.ImageTk.PhotoImage(PIL.Image.open('Chip.png'))
        self.text = 0

        self.tag = Chip.objectName + str(Chip.objectNum)
        Chip.objectNum += 1

    def drawChip(self):
        c.create_image(38+self.x,50+self.y,image=self.chipImg, tag=self.tag)
        self.text = c.create_text(self.x+38, self.y+49, text=str(self.amount),tag=self.tag)
        c.update()

    def moveTo(self, x=0, y=0):
        deltaX = x - self.x
        deltaY = y - self.y
        c.move(self.tag, deltaX,deltaY)
        c.update()
        
    def chipVal(self, amount=0):
        self.amount = amount
        c.itemconfig(self.text, text=str(self.amount))
        c.update()

    def erase(self):
        c.delete(self.tag)
        c.update()
        

class Player:

    def __init__ (self):
        self.card1 = 0
        self.card2 = 0
        self.value = self.card1+self.card2
        self.valueLow = 0
        self.hand = []
        self.handSize = len(self.hand)
        self.chips = 1000
        self.bet = 0
        self.bets = []

#def newGame(player, dealer):

def deal(player, dealer):
    global bet_scale
    player.bet = bet_scale.get()
    bet_scale.grid_forget()
    player.chips -= player.bet
    player.bets.append(Chip(player.bet,382,210))
    player.bets[0].drawChip()
    c.itemconfig(player_chips, text="Cash:")
    player_chip.chipVal(player.chips)
    player.hand = []
    dealer.hand = []
    c.delete("dCard")
    c.itemconfig(player_display, text="")
    c.itemconfig(dealer_display, text="")
    c.itemconfig(winner_display, text="")
    c.update()
    global Deck
    if len(Deck)<= 4:
        newShoe()

    #Player Card 1
    c.after(200)    
    cardType = Deck.pop(-1)
    player.hand.append(Card(cardType))
    player.card1 = player.hand[0].value
    player.hand[0].drawCard(200,220)

    #Player Card 2
    c.after(200)
    cardType = Deck.pop(-1)
    player.hand.append(Card(cardType))
    player.card2 = player.hand[1].value 
    player.hand[1].drawCard(220,220)

    #Calculate Hand Value
    player.value = player.card1+player.card2
    if player.card1 == 11 or player.card2 == 11:
        player.valueLow = player.value - 10
    if player.card1 == 11 and player.card2 == 11:
        player.value = 12
        player.valueLow = 2

    #Dealer Card 1
    c.after(200)
    cardType = Deck.pop(-1)
    dealer.hand.append(Card(cardType))
    dealer.card1 = dealer.hand[0].value
    dealer.hand[0].drawCard(200,80)

    #Dealer Card 2
    c.after(200)
    cardType = Deck.pop(-1)
    dealer.hand.append(Card(cardType))
    dealer.card2 = dealer.hand[1].value
    dealer.hand[1].drawCard(220,80, flip=True)

    #Calculate Dealer Hand
    dealer.value = dealer.card1+dealer.card2
    if dealer.card1 == 11 or dealer.card2 == 11:
        dealer.valueLow = dealer.value-10
    if dealer.card1 == 11 and dealer.card2 == 11:
        dealer.value = 12
        dealer.valueLow = 2

    c.after(200)
    Deal_button.config(state=DISABLED)
    Hit_button.config(state=NORMAL)
    Stand_button.config(state=NORMAL)
    Double_button.config(state=NORMAL)

    if player.value == 21:
        Hit_button.config(state=DISABLED)
        Stand_button.config(state=DISABLED)
        Double_button.config(state=DISABLED)
        c.itemconfig(player_display, text="21\nBLACKJACK!")
        c.itemconfig(winner_display, text="YOU WIN!!!")
        dealer.hand[1].flip()
        c.itemconfig(dealer_display, text=dealer.value)
        player.chips += player.bet*3
        player_chip.chipVal(player.chips)
        if player.chips < 5:
            c.itemconfig(winner_display, text="YOU'VE GONE BROKE!")
            c.update()
            c.after(2000)
            Gui.destroy()
        else:
            Deal_button.config(state=NORMAL)
            bet_scale = Scale(Gui, from_=5, to=player.chips, label='Bet Amount', orient=HORIZONTAL, bg='green',
                          relief=FLAT, fg="white", resolution=5)
            bet_scale.grid(row=24, column=2, sticky=W+E)
            #remove chips from table, add loop later, especially when adding split
            i=len(player.bets)-1
            while i >= 0:
                player.bets[i].erase()
                del player.bets[i]
                i = i-1
            #
            player.valueLow = 0
            dealer.valueLow = 0
            c.update()
        c.update()
    elif player.valueLow != 0:
        c.itemconfig(player_display, text=str(player.value)+" or "+str(player.valueLow))
        c.itemconfig(dealer_display, text=str(dealer.card1)+" + ???")
        c.update()
    else:
        c.itemconfig(player_display, text=player.value)
        c.itemconfig(dealer_display, text=str(dealer.card1)+" + ???")
        c.update()
    
def hit(player,dealer):
    global bet_scale
    Double_button.config(state=DISABLED)
    global Deck
    if len(Deck)== 0:
        newShoe()
    #Pull Card
    cardType = Deck.pop(-1)
    player.hand.append(Card(cardType))
    #Update Handsize
    player.handSize = len(player.hand)
    #If an Ace, low value + 1
    if player.hand[player.handSize-1].value == 11:
        player.valueLow = player.value + 1
    #If an Ace already exists and the new card is not and Ace, add full value to low
    if player.valueLow != 0 and player.hand[player.handSize-1].value != 11:
        player.valueLow = player.valueLow + player.hand[player.handSize-1].value
    #Add value to hi
    player.value = player.value + player.hand[player.handSize-1].value
    #Draw card
    player.hand[(player.handSize-1)].drawCard(200+20*(player.handSize-1),220)
    
    if player.valueLow != 0:
        if player.value == 21:
            c.itemconfig(player_display, text=player.value)
            c.update()
        elif player.value > 21:
            player.value = player.valueLow
            player.valueLow = 0
            c.itemconfig(player_display, text=player.value)
            c.update()
        else:
            c.itemconfig(player_display, text=str(player.value)+" or "+str(player.valueLow))
            c.update()
    else:
        c.itemconfig(player_display, text=player.value)
        c.update()

    if player.value > 21:
        Hit_button.config(state=DISABLED)
        Stand_button.config(state=DISABLED)
        Double_button.config(state=DISABLED)
        c.after(1000)
        c.itemconfig(player_display, text="BUST!")
        c.itemconfig(winner_display, text="HOUSE WINS")
        dealer.hand[1].flip()
        c.itemconfig(dealer_display, text=dealer.value)
        if player.chips < 5:
            c.itemconfig(winner_display, text="YOU'VE GONE BROKE!")
            c.update()
            c.after(2000)
            Gui.destroy()
        else:
            Deal_button.config(state=NORMAL)
            bet_scale = Scale(Gui, from_=5, to=player.chips, label='Bet Amount', orient=HORIZONTAL, bg='green',
                          relief=FLAT, fg="white", resolution=5)
            bet_scale.grid(row=24, column=2, sticky=W+E)
            #remove chips from table
            i=len(player.bets)-1
            while i >= 0:
                player.bets[i].erase()
                del player.bets[i]
                i = i-1
            player.valueLow = 0
            dealer.valueLow = 0
            c.update()

    if player.value == 21 or player.valueLow == 21:
        stand(player, dealer)
    
def stand(player, dealer):

    global Deck
    global bet_scale

    Hit_button.config(state=DISABLED)
    Stand_button.config(state=DISABLED)
    Double_button.config(state=DISABLED)
    
    dealer.hand[1].flip()
    c.itemconfig(dealer_display, text=dealer.value)
    c.update()

    if dealer.value > player.value:
        c.after(1000)
        c.itemconfig(winner_display, text="HOUSE WINS")
        c.update()

    else:
        #Dealer's aces are always counted as 11 unless it causes him to bust
        while dealer.value < 17:
            c.after(750)
            if len(Deck)== 0:
                newShoe() 
            cardType = Deck.pop(-1)
            dealer.hand.append(Card(cardType))
            dealer.handSize = len(dealer.hand)
            if dealer.hand[dealer.handSize-1].value == 11:
                dealer.valueLow = dealer.value + 1
            if dealer.valueLow != 0 and dealer.hand[dealer.handSize-1].value != 11:
                dealer.valueLow = dealer.valueLow + dealer.hand[dealer.handSize-1].value
            dealer.value = dealer.value + dealer.hand[dealer.handSize-1].value
            dealer.hand[(dealer.handSize-1)].drawCard(200+20*(dealer.handSize-1),80)
            
            if dealer.valueLow != 0:
                if dealer.value == 21:
                    c.itemconfig(dealer_display, text=dealer.value)
                    c.update()
                elif dealer.value > 21:
                    dealer.value = dealer.valueLow
                    dealer.valueLow = 0
                    c.itemconfig(dealer_display, text=dealer.value)
                    c.update()
                else:
                    c.itemconfig(dealer_display, text=dealer.value)
                    c.update()
            else:
                c.itemconfig(dealer_display, text=dealer.value)
                c.update()

        if dealer.value > 21:
            c.after(1000)
            c.itemconfig(dealer_display, text="BUST!")
            c.itemconfig(winner_display, text="YOU WIN!")
            player.chips += player.bet*2
            Deal_button.config(state=NORMAL)
            player_chip.chipVal(player.chips)
        elif dealer.value == player.value:
            c.after(1000)
            c.itemconfig(winner_display, text="PUSH")
            player.chips += player.bet
            player_chip.chipVal(player.chips)
        elif dealer.value > player.value:
            c.after(1000)
            c.itemconfig(winner_display, text="HOUSE WINS")
            c.update()
        elif dealer.value < player.value:
            c.after(1000)
            c.itemconfig(winner_display, text="YOU WIN!")
            player.chips += player.bet*2
            player_chip.chipVal(player.chips)

    if player.chips < 5:
        c.itemconfig(winner_display, text="YOU'VE GONE BROKE!")
        c.update()
        c.after(2000)
        Gui.destroy()
    else:
        Deal_button.config(state=NORMAL)
        bet_scale = Scale(Gui, from_=5, to=player.chips, label='Bet Amount', orient=HORIZONTAL, bg='green',
                      relief=FLAT, fg="white", resolution=5)
        bet_scale.grid(row=24, column=2, sticky=W+E)
        #remove chips from table
        i=len(player.bets)-1
        while i >= 0:
            player.bets[i].erase()
            del player.bets[i]
            i = i-1
        player.valueLow = 0
        dealer.valueLow = 0
        c.update()

def double(player,dealer):
    player.chips -= player.bet
    player.bets.append(Chip(player.bet,390,210))
    player.bets[1].drawChip()
    c.update()
    player.bet = player.bet*2
    player_chip.chipVal(player.chips)
    global Deck
    if len(Deck)== 0:
        newShoe()
    #Pull Card
    cardType = Deck.pop(-1)
    player.hand.append(Card(cardType))
    #Update Handsize
    player.handSize = len(player.hand)
    #If an Ace, low value + 1
    if player.hand[player.handSize-1].value == 11:
        player.valueLow = player.value + 1
    #If an Ace already exists and the new card is not and Ace, add full value to low
    if player.valueLow != 0 and player.hand[player.handSize-1].value != 11:
        player.valueLow = player.valueLow + player.hand[player.handSize-1].value
    #Add value to hi
    player.value = player.value + player.hand[player.handSize-1].value
    #Draw card
    player.hand[(player.handSize-1)].drawCard(200+20*(player.handSize-1),220)
    
    if player.valueLow != 0:
        if player.value == 21:
            c.itemconfig(player_display, text=player.value)
            c.update()
        elif player.value > 21:
            player.value = player.valueLow
            player.valueLow = 0
            c.itemconfig(player_display, text=player.value)
            c.update()
        else:
            c.itemconfig(player_display, text=str(player.value)+" or "+str(player.valueLow))
            c.update()
    else:
        c.itemconfig(player_display, text=player.value)
        c.update()

    if player.value > 21:
        Hit_button.config(state=DISABLED)
        Stand_button.config(state=DISABLED)
        Double_button.config(state=DISABLED)
        c.after(1000)
        c.itemconfig(player_display, text="BUST!")
        c.itemconfig(winner_display, text="HOUSE WINS")
        dealer.hand[1].flip()
        c.itemconfig(dealer_display, text=dealer.value)
        if player.chips < 5:
            c.itemconfig(winner_display, text="YOU'VE GONE BROKE!")
            c.update()
            c.after(2000)
            Gui.destroy()
        else:
            Deal_button.config(state=NORMAL)
            bet_scale = Scale(Gui, from_=5, to=player.chips, label='Bet Amount', orient=HORIZONTAL, bg='green',
                          relief=FLAT, fg="white", resolution=5)
            bet_scale.grid(row=24, column=2, sticky=W+E)
            #remove chips from table
            i=len(player.bets)-1
            while i >= 0:
                player.bets[i].erase()
                del player.bets[i]
                i = i-1
            player.valueLow = 0
            dealer.valueLow = 0
            c.update()
    else:
        stand(player,dealer)


####GAME####
plyr = Player()
dlr = Player()
shuffle(Deck)

player_chip = Chip(1000,382,310)
player_chip.drawChip()

dealer_display = c.create_text(150, 130, text="",
                               justify=CENTER, fill="white")
player_display = c.create_text(150, 270, text="",
                               justify=CENTER, fill="white")
player_chips = c.create_text(420, 320, text="Cash:",
                               justify=CENTER, fill="white")
winner_display = c.create_text(250, 200, text="",
                               justify=CENTER, fill="white")

Hit_button = Button(Gui, text="Hit", state=DISABLED, command= lambda: hit(plyr,dlr))
Hit_button.grid(row=25, column=3, rowspan=3, sticky=N+S+W+E)

Split_button = Button(Gui, text="Split", state=DISABLED, command= lambda: hit(plyr,dlr))
Split_button.grid(row=26, column=2, sticky=N+S+W+E)

Double_button = Button(Gui, text="Double down", state=DISABLED, command= lambda: double(plyr,dlr))
Double_button.grid(row=27, column=2, sticky=N+S+W+E)

Deal_button = Button(Gui, text="Deal", command= lambda: deal(plyr, dlr))
Deal_button.grid(row=25, column=1, rowspan=3, sticky=N+S+W+E)

Stand_button = Button(Gui, text="Stand", state=DISABLED, command=lambda: stand(plyr, dlr))
Stand_button.grid(row=25, column=2, sticky=N+S+W+E)

bet_scale = Scale(Gui, from_=5, to=1000, label='Bet Amount', orient=HORIZONTAL, bg='green',
                  relief=FLAT, fg="white", resolution=5)
bet_scale.grid(row=24, column=2, sticky=W+E)


