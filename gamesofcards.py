# briscola 3

from random import shuffle

def val(card):
    'gives the value of the card as return value'
    valore = pcval[int(card[:-1])]
    return valore

def num(card):
    'gives the value of the card as return value'
    valore = int(card[:-1])
    return valore

def listcol(cards=[]):
    'returns a list of col from a list of cards'
    cardscol = []
    for i in cards:
        cardscol += [i[-1]]
    return cardscol

def goodcards(card):
    'makes list of cards to make points'
    cpnt = [str(n)+card[-1] for n in [1,3,10,9,8]]
    return cpnt

def scartine():
    colors = ['♥','♦','♣','♠']
    colors.pop(colors.index(briscola[-1]))
    from2_10 = [str(x)+cc for x in [2,4,5,6,7,8,9,10] for cc in colors]
    return from2_10

def carichi():
    colors = ['♥','♦','♣','♠']
    colors.pop(colors.index(briscola[-1])) # Erase briscola
    carichi = [str(x)+cc for x in [3,1] for cc in colors]
    return carichi

def start():
    'Create cards, shuffle them, pick pc1 (3 cards) and briscola, then choose the card to play'
    global cards,pc1,pc2,briscola,pcval
    cards = [str(num)+color for num in range(1,11) for color in ['♥','♦','♣','♠']]
    pcval = {1:11,2:0,3:10,4:0,5:0,6:0,7:0,8:2,9:3,10:4}   # dictonary for getting cards points    
    shuffle(cards)                                         # mixing cards
    briscola = cards.pop()
    pc1 = [cards.pop() for x in range(3)]
    pc2 = [cards.pop() for x in range(3)]
    
def pc1goes():
    global pc1_tbl
    print()
    print("PC1 cards",pc1,end='')

    for c in pc1_match1():
        print(">"+c,end='')
        if c in pc1:
            pc1_tbl = c
            print("*")
            if isBrisc(c):
                print("It is a briscola!")
            else:
                pass
            break

def start2():
    pc1 += pop()
    pc2 += pop()
    print(pc1,pc2)
    
            
            
def isScart(cs):
    scartine = 2,4,5,6,7
    if num(cs) in scartine:
        return True
    else:
        return False

def isCarico(cs):
    carico = 1,3
    if num(cs) in carico:
        return True
    else:
        return False

def isFig(cs):
    figure = 8,9,10
    if num(cs) in figure:
        return True
    else:
        return False

def isBrisc(cs):
    if cs[-1] == briscola[-1]:
        return True
    else:
        return False

def pc1_match1():
    'Card sequence for pc2 playing decision'
    scartine = [2,4,5,6,7,8,9,10]
    briscole = [2,4,5,6,7,8,9,10,3,1]
    carichi = [3,1]
    colori = ['♥','♦','♣','♠']
    colori.pop(colori.index(briscola[-1]))
    l_scartine = [str(x)+c for x in scartine for c in colori]
    l_briscole = [str(b)+briscola[-1] for b in briscole]
    l_carichi = [str(x)+c for x in carichi for c in colori]
    pc1_seq = l_scartine + l_briscole + l_carichi
    return pc1_seq
    
    
def pc2_match1():
    'Card sequence for pc2 playing decision'  
    listapunti = goodcards(pc1_tbl)
    listascartine = scartine()
    listabriscole = [str(x)+briscola[-1] for x in [2,4,5,6,8,7,9,10,3,1]]
    listacarichi = carichi()
    pc2_seq = listapunti + listascartine + listabriscole + listacarichi
    return pc2_seq


def pc2AI():
    'the answer of pc2'
    global pc2_tbl
    if isBrisc(pc1_tbl):
        print("I need code for this...")

    elif isScart(pc1_tbl):              # If pc1 play a 0 point card
        print("PC2 cards",pc2,end='')   # pc2 searcha a card of the same color that gives him points
        for c in pc2_match1():
            print(">"+c,end='')         # while he search we print the cards
            if c in pc2:
                print("*")              # when he finds a card in the list matching with pc2 cards... print *
                pc2_tbl=c
                print(c)
                break
            else:
                pass
        print("[PC1]",pc1_tbl,"[PC2]",pc2_tbl)
        print("Now we see who wins:")
    else:
        print("Code missing...")


def whoWins(a,b):
    'who wins between card a and b'
    print("[",a,b,"]     ",end ='')
    if a[-1]==b[-1]:
        if val(a)>=val(b):
            print("Pc1 wins with",a)
            return a
        else:
            print("Pc2 wins with",b)
            return b
    else:
        if b[-1]==briscola[-1]:
            print("[Pc2 wins with a briscola]",b)
            return b
        else:
            print("Pc1 wins with",a)
            return(a)
        
        
def main():
    start()
    pc1goes()
    pc2AI()
    whoWins(pc1_tbl, pc2_tbl)
    print("===========\nRound 2\n==========")
    pc1goes()
if __name__=='__main__':
    main()
