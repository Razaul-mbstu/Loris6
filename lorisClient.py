import pygame
from card import Card
from table import Table
from button import Button
from lorisGame import Game
from lorisNetwork import Network


pygame.font.init()
width = 1300
height = int(width*0.54)
win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Loris Player')

cardW = int(width*5.4/100)
cardH = int(height*15.6/100)

card8x,card8y = int(width*26.9/100),int(height*65/100)

all_cards = {} #Dictionary for all the cards .
call_btns = [Button('Pass',int(width*45.4/100),int(height*44.2/100),int(width*7.7/100),int(height*6.5/100),(0,150,110)),Button('UP',int(width*45.4/100),int(height*26/100),int(width*7.7/100),int(height*6.5/100),(255,0,0))]
trump_btns = [Button('Club',int(width*63/100),int(height*1.3/100),int(width*6.2/100),int(height*6.5/100),(148,0,211)),Button('Dice',int(width*69.6/100),int(height*1.3/100),int(width*6.2/100),int(height*6.5/100),(148,0,211)),Button('Spade',int(width*76.2/100),int(height*1.3/100),int(width*6.2/100),int(height*6.5/100),(148,0,211)),Button('Heart',int(width*82.7/100),int(height*1.3/100),int(width*6.2/100),int(height*6.5/100),(148,0,211)),Button('NoTrump',int(width*89.2/100),int(height*1.3/100),int(width*7.7/100),int(height*6.5/100),(148,0,211))]
power = Button('Power',int(width*57.7/100),int(height*77.9/100),int(width*11.5/100),int(height*6.5/100),(255,0,0))


def load_cards():
    for i in range(3,15):
        im = pygame.image.load('C{}.png'.format(i))
        id = 'C{}'.format(i)
        all_cards[id] = pygame.transform.scale(im,(cardW,cardH))
    for i in range(3,15):
        im = pygame.image.load('D{}.png'.format(i))
        id = 'D{}'.format(i)
        all_cards[id] = pygame.transform.scale(im,(cardW,cardH))
    for i in range(3,15):
        im = pygame.image.load('H{}.png'.format(i))
        id = 'H{}'.format(i)
        all_cards[id] = pygame.transform.scale(im,(cardW,cardH))
    for i in range(3,15):
        im = pygame.image.load('S{}.png'.format(i))
        id = 'S{}'.format(i)
        all_cards[id] = pygame.transform.scale(im,(cardW,cardH))

    im = pygame.image.load('joker.png')
    id = 'Joker'
    all_cards[id] = pygame.transform.scale(im,(cardW,cardH))

def sort_cards(cards):
    c = []
    # Getting The Hearts
    for i in range(8):
        id = cards[i][0]
        if id == 'H':
            c.append(cards[i])
    #Sorting The cards with the nubers...
    l1 = len(c)
    for i in range(l1):
        for j in range(l1):
            a = int(c[i][1:])
            b = int(c[j][1:])
            if a>b:
                dump = c[i]
                c[i] = c[j]
                c[j] = dump
    # Getting The Clubs
    for i in range(8):
        id = cards[i][0]
        if id == 'C':
            c.append(cards[i])
    # Sorting Again
    l2 = len(c)
    for i in range(l1,l2):
        for j in range(l1,l2):
            a = int(c[i][1:])
            b = int(c[j][1:])
            if a>b:
                dump = c[i]
                c[i] = c[j]
                c[j] = dump
    l1 = l2
    # Getting The Dices
    for i in range(8):
        id = cards[i][0]
        if id == 'D':
            c.append(cards[i])
    l2 = len(c)
    for i in range(l1,l2):
        for j in range(l1,l2):
            a = int(c[i][1:])
            b = int(c[j][1:])
            if a>b:
                dump = c[i]
                c[i] = c[j]
                c[j] = dump
    l1 = l2
    # Getting The Spades..
    for i in range(8):
        id = cards[i][0]
        if id == 'S':
            c.append(cards[i])
    l2 = len(c)
    for i in range(l1,l2):
        for j in range(l1,l2):
            a = int(c[i][1:])
            b = int(c[j][1:])
            if a>b:
                dump = c[i]
                c[i] = c[j]
                c[j] = dump
    l1 = l2
    for i in range(8):
        id = cards[i][0]
        if id == 'J':
            c.append(cards[i])


    return c

def draw_player(game,table,p):
    text = ''
    if p == 0:
        if 0 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[0]],0)
        if 1 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[1]],1)
        if 2 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[2]],2)
        if 3 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[3]],3)
        if 4 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[4]],4)
        if 5 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[5]],5)

        text = 'Player-0'
        table.draw_player(win,0,text)
        text = 'Player-1'
        table.draw_player(win,1,text)
        text = 'Player-2'
        table.draw_player(win,2,text)
        text = 'Player-3'
        table.draw_player(win,3,text)
        text = 'Player-4'
        table.draw_player(win,4,text)
        text = 'Player-5'
        table.draw_player(win,5,text)

    elif p == 1:
        if 0 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[0]],5)
        if 1 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[1]],0)
        if 2 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[2]],1)
        if 3 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[3]],2)
        if 4 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[4]],3)
        if 5 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[5]],4)

        text = 'Player-1'
        table.draw_player(win,0,text)
        text = 'Player-2'
        table.draw_player(win,1,text)
        text = 'Player-3'
        table.draw_player(win,2,text)
        text = 'Player-4'
        table.draw_player(win,3,text)
        text = 'Player-5'
        table.draw_player(win,4,text)
        text = 'Player-0'
        table.draw_player(win,5,text)

    elif p == 2:
        if 0 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[0]],4)
        if 1 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[1]],5)
        if 2 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[2]],0)
        if 3 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[3]],1)
        if 4 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[4]],2)
        if 5 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[5]],3)

        text = 'Player-2'
        table.draw_player(win,0,text)
        text = 'Player-3'
        table.draw_player(win,1,text)
        text = 'Player-4'
        table.draw_player(win,2,text)
        text = 'Player-5'
        table.draw_player(win,3,text)
        text = 'Player-0'
        table.draw_player(win,4,text)
        text = 'Player-1'
        table.draw_player(win,5,text)

    elif p == 3:
        if 0 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[0]],3)
        if 1 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[1]],4)
        if 2 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[2]],5)
        if 3 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[3]],0)
        if 4 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[4]],1)
        if 5 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[5]],2)

        text = 'Player-3'
        table.draw_player(win,0,text)
        text = 'Player-4'
        table.draw_player(win,1,text)
        text = 'Player-5'
        table.draw_player(win,2,text)
        text = 'Player-0'
        table.draw_player(win,3,text)
        text = 'Player-1'
        table.draw_player(win,4,text)
        text = 'Player-2'
        table.draw_player(win,5,text)

    elif p == 4:
        if 0 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[0]],2)
        if 1 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[1]],3)
        if 2 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[2]],4)
        if 3 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[3]],5)
        if 4 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[4]],0)
        if 5 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[5]],1)

        text = 'Player-4'
        table.draw_player(win,0,text)
        text = 'Player-5'
        table.draw_player(win,1,text)
        text = 'Player-0'
        table.draw_player(win,2,text)
        text = 'Player-1'
        table.draw_player(win,3,text)
        text = 'Player-2'
        table.draw_player(win,4,text)
        text = 'Player-3'
        table.draw_player(win,5,text)

    elif p == 5:
        if 0 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[0]],1)
        if 1 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[1]],2)
        if 2 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[2]],3)
        if 3 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[3]],4)
        if 4 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[4]],5)
        if 5 in game.cards_on_table:
            table.draw(win,all_cards[game.cards_on_table[5]],0)

        text = 'Player-5'
        table.draw_player(win,0,text)
        text = 'Player-0'
        table.draw_player(win,1,text)
        text = 'Player-1'
        table.draw_player(win,2,text)
        text = 'Player-2'
        table.draw_player(win,3,text)
        text = 'Player-3'
        table.draw_player(win,4,text)
        text = 'Player-4'
        table.draw_player(win,5,text)

def getTaker(starter,passed):
    return starter+passed

def no_running_card(cards,game):
    decision = True
    for c in cards:
        if game.running_card[0] == c.id[0] and c.show:
            decision = False
            break
    return decision

def have_trump(cards,game):
    decision = False
    for c in cards:
        if c.id[0] == game.trump_card[0] and c.show:
            decision = True
            break
    return decision

def no_of_player(game):
    p = 0
    for i in range(6):
        if game.player_ready[i] == False:
            p += 1
    return p

wait = False
def redrawWindow(win,game,cards,player):
    global wait
    win.fill((255,255,255))
    table = Table(win,width,height)

    draw_player(game,table,player)

    if not game.connected():

        font = pygame.font.SysFont('comicsans',int(width*3.1/100))
        text = font.render('Waiting for {} more Players ...'.format(no_of_player(game)),1,(255,0,0))
        win.blit(text,(int(width*0.77/100),int(height*3.9/100)))
    else:
        if not game.called:
            if game.chance_to_call == player: #While all the players still calling ...
                bt1 = call_btns[0]
                if bt1.show:
                    bt1.draw(win)
                bt2 = call_btns[1]
                if bt2.show:
                    bt2.draw(win)
            else:
                font = pygame.font.SysFont('comicsans',int(width*5.4/100))
                text = font.render('Please Wait',1,(255,0,0))
                win.blit(text,(int(width*40.8),int(height*23.4/100)))

            if game.passed != 6:
                font = pygame.font.SysFont('comicsans',int(width*6.2/100))
                text = font.render('P-{}= '.format(game.high_call_taker)+str(game.min_call),1,(0,0,0))
                win.blit(text,(int(width*42.7/100),int(height*35.1/100)))

            if player == game.chance_to_call:
                font = pygame.font.SysFont('comicsans',int(width*3.1/100))
                text = font.render('Your Call ...',1,(0,0,0))
                win.blit(text,(int(width*0.77/100),int(height*6.5/100)))
            else:
                font = pygame.font.SysFont('comicsans',int(width*3.1/100))
                text = font.render('Player-{} Taking the calls'.format(game.chance_to_call),1,(0,0,0))
                win.blit(text,(int(width*0.77/100),int(height*6.5/100)))

        elif not game.trump_taken:
            #Selecting Trump Card ...

            if player == game.high_call_taker:
                font = pygame.font.SysFont('comicsans',int(width*3.1/100))
                text = font.render('Please Select The Trump Card',1,(0,0,0))
                win.blit(text,(int(width*61.5/100),int(height*9.1/100)))
                for t in trump_btns:
                    t.draw(win)
            else:
                font = pygame.font.SysFont('comicsans',int(width*3.1/100))
                text = font.render('Player-{} selecting the Trump'.format(game.high_call_taker),1,(0,0,0))
                win.blit(text,(int(width*61.5/100),int(height*9.1/100)))

        elif not game.all_player_turned(): #After selecting The Trump card, Game began...
            wait = True # For waiting when trick will be completed
            font = pygame.font.SysFont('comicsans',int(width*3.1/100))
            text = font.render('Trump is - {}'.format(game.trump_card),1,(0,0,0))
            win.blit(text,(int(width*69.2/100),int(height*9.1/100)))
            font = pygame.font.SysFont('comicsans',int(width*2.3/100))
            text = font.render('Call is Taken by player-{}'.format(game.high_call_taker),1,(0,0,0))
            win.blit(text,(int(width*69.2/100),int(height*15.6/100)))
            font = pygame.font.SysFont('comicsans',int(width*2.3/100))
            text = font.render('High Call is -{}'.format(game.min_call),1,(0,0,0))
            win.blit(text,(int(width*69.2/100),int(height*20.8/100)))

            if player == game.chance_to_turn:
                font = pygame.font.SysFont('comicsans',int(width*3.1/100))
                text = font.render('Your Turn ...',1,(0,0,0))
                win.blit(text,(int(width*0.77/100),int(height*3.9/100)))
                power.draw(win)
            else:
                font = pygame.font.SysFont('comicsans',int(width*3.1/100))
                text = font.render('Player-{} is turning..'.format(game.chance_to_turn),1,(0,0,0))
                win.blit(text,(int(width*0.77/100),int(height*3.9/100)))

            if game.power:
                font = pygame.font.SysFont('comicsans',int(width*3.1/100))
                text = font.render('Player-{} is giving Power..'.format(game.chance_to_turn),1,(0,0,0))
                win.blit(text,(int(width*40/100),int(height*2/100)))

        elif game.trick_done:
            if game.trickTaker == player:
                font = pygame.font.SysFont('comicsans',int(width*3.1/100))
                text = font.render('You Took The Trick',1,(0,0,0))
                win.blit(text,(int(width*0.77/100),int(height*3.9/100)))
            else:
                font = pygame.font.SysFont('comicsans',int(width*3.1/100))
                text = font.render('Player-{} Took The Trick..'.format(game.trickTaker),1,(0,0,0))
                win.blit(text,(int(width*0.77/100),int(height*3.9)))

        if game.prev_trick:
            font = pygame.font.SysFont('comicsans',int(width*3.1/100))
            text = font.render('Previous Trick - Player-{}'.format(game.prev_taker),1,(0,0,0))
            win.blit(text,(int(width*0.77/100),int(height*13/100)))

        font = pygame.font.SysFont('comicsans',int(width*3.1/100))
        text = font.render('Trick Taken',1,(0,0,0))
        win.blit(text,(int(width*0.77/100),int(height*22/100)))
        font = pygame.font.SysFont('comicsans',int(width*3.1/100))
        text = font.render('Team-0,2,4',1,(0,0,0))
        win.blit(text,(int(width*0.77/100),int(height*28.6/100)))
        font = pygame.font.SysFont('comicsans',int(width*3.1/100))
        text = font.render('{}'.format(game.trick_taken[0]),1,(0,0,0))
        win.blit(text,(int(width*0.77/100),int(height*35.1/100)))
        font = pygame.font.SysFont('comicsans',int(width*3.1/100))
        text = font.render('Team-1,3,5',1,(0,0,0))
        win.blit(text,(int(width*0.77/100),int(height*41.6/100)))
        font = pygame.font.SysFont('comicsans',int(width*3.1/100))
        text = font.render('{}'.format(game.trick_taken[1]),1,(0,0,0))
        win.blit(text,(int(width*0.77/100),int(height*48.1/100)))

        font = pygame.font.SysFont('comicsans',int(width*3.1/100))
        text = font.render('Point Table',1,(0,0,0))
        win.blit(text,(int(width*84.62/100),int(height*28.6/100)))
        font = pygame.font.SysFont('comicsans',int(width*3.1/100))
        text = font.render('Team-0,2,4',1,(0,0,0))
        win.blit(text,(int(width*84.62/100),int(height*35.1/100)))
        font = pygame.font.SysFont('comicsans',int(width*3.1/100))
        text = font.render('{}'.format(game.points[0]),1,(0,0,0))
        win.blit(text,(int(width*84.62/100),int(height*43.3/100)))
        font = pygame.font.SysFont('comicsans',int(width*3.1/100))
        text = font.render('Team-1,3,5',1,(0,0,0))
        win.blit(text,(int(width*84.62/100),int(height*48.1/100)))
        font = pygame.font.SysFont('comicsans',int(width*3.1/100))
        text = font.render('{}'.format(game.points[1]),1,(0,0,0))
        win.blit(text,(int(width*84.62/100),int(height*53.2/100)))

    ### Drawing the eight cards ... for the current player...
    for c in cards:
        if c.show:
            c.draw(win)

    pygame.display.update()

    if game.connected() and game.all_player_turned() and wait:
        pygame.time.delay(1500)
        wait = False


def main():
    global call_btns
    load_cards()
    run = True
    net = Network() #creating network
    cards = []
    trick_done = False
    player = int(net.getP())
#    print('You Are Player: ',player)

    #game = Game(1,1)
    #cards_on_table = {} ##Dictionari for the cards on table
    create_card_btn = True
    while run:
        try:
            game = net.send('get')
#            print('Game Recieved ...')
            if game.art_card[player]:
                ownCards = sort_cards(game.get_cards(player))
#                print('Cards recieved ...')
                net.send('art_card')
                x = card8x
                cards = []
                for c in ownCards:
                    c1 = Card(c,x,card8y,cardW,cardH)
                    c1.setImage(all_cards[c])
                    x = x+int(width*0.4/100)+cardW
                    cards.append(c1)
#               print('cards btn created ...')

        except Exception as e:
            run = False
#            print(e)
#            print('Could not get The Game')
            break

        if game.trick_taken[0]+game.trick_taken[1] == 8: #One round Finished
            net.send('reDistribute')

        if game.trick_done:
            redrawWindow(win,game,cards,player)
            if game.trickTaker == player:
                try:
                    net.send('reTurn')
                except Exception as e:
                    pass
#                   print(e)
#                   print('Could not get The Game')
        if game.all_player_turned() and not game.trick_done:
            net.send('taker')


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if power.click(pos) and game.chance_to_turn == player:
                    net.send('power')

                for c in cards:
                    if c.click(pos) and game.connected() and not game.turn[player] and player == game.chance_to_turn:
                        if player == game.starter:
                            net.send(c.id)
                            c.show = False
                        else:

                            if game.running_card[0] == c.id[0]:
                                net.send(c.id)
                                c.show = False
                            elif c.id[0] == 'J':
                                net.send(c.id)
                                c.show = False
                            elif game.running_card[0] == 'J':
                                if c.id[0] == game.trump_card[0]:
                                    net.send(c.id)
                                    c.show = False
                                elif not have_trump(cards,game):
                                    net.send(c.id)
                                    c.show = False
                            elif no_running_card(cards,game):
                                net.send(c.id)
                                c.show = False

                for b in call_btns:
                    if b.click(pos) and b.show and game.connected() and not game.called and game.chance_to_call == player:
                        net.send(b.text)


                if game.high_call_taker == player and game.called and not game.trump_taken and game.connected():
                    for t in trump_btns:
                        if t.click(pos) and t.show:
                            net.send('T'+t.text)

        redrawWindow(win,game,cards,player)


def menu_screen():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        win.fill((128,128,128))
        font = pygame.font.SysFont('comicsans',int(width*4.7/100))
        text = font.render('Click To Play...',1,(255,0,0))
        win.blit(text,(int(width*7.7/100),int(height*26/100)))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()


menu_screen()
