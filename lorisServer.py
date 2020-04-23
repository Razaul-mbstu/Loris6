import socket
from _thread import *
import pickle
from lorisGame import Game

# Server Adrs and Port Number..
server = "192.168.43.230"    ### IP ADRES is given here
port = 5555    ### Port Number to connect

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Trying to bind the server and the Port.
try:
    sock.bind((server,port))
except socket.error as e:
    str(e)

# Listening for client request...
sock.listen()
print('Server Started, Waiting for connection....')

### Will be started when a client will be connected ..
def threaded_client(conn,p,gameId):

    conn.send(str.encode(str(p))) # Sending the number of player as identity
    reply = ''

    while True:
        try:
            #print('Into the Try Catch ..')
            data = conn.recv(4096).decode() #trying to recieve data from Client
            #print(data,' is recieved')
            if gameId in games:
                game = games[gameId] #getting the game from the dictionary
                if not data:
                    break
                else:
                    if data == 'reset':
                        game.reset()
                    elif data == 'UP':
                        game.call_up(p)
                    elif data == 'Pass':
                        game.call_pass(p)
                    elif data[0] == 'T':
                        game.trump_selected(data)
                    elif data == 'taker':
                        game.trick_taker()
                    elif data == 'reTurn':
                        game.reTurn()
                    elif data == 'reDistribute':
                        game.reDistibrute()
                    elif data == 'art_card':
                        game.artCard(p)
                    elif data == 'power':
                        game.raisePower()
                    elif data != 'get':
                        game.play(p,data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except Exception as e:
            print(e)
            break
    print('Lost Connection ... ... ...')

    try:
        games[gameId].playerGone(p)
        if games[gameId].all_gone():
            del games[gameId]
            print('Closing Game :',gameId)
        print('Player-{} has gone'.format(p))
    except:
        pass

    conn.close()


#### Main Server Handling....

#essential storage ...
connected = set()
games = {} #For Listing The current Running Games
clientCount = 0 # For Tracking The Clients
gameId = 0
current_player = 0 #Initially no client connceted..
while True:
    conn,adrs = sock.accept()  # Accepts The Connection
    print('Connected to : ',adrs)

    new_game = True
    for key in games.keys():
        check = False
        for i in range(6):
            if games[key].player_ready[i] == False:
                new_game = False
                current_player = i
                gameId = key
                check = True
                break
        if check:
            break

    if new_game:
        games[gameId] = Game(gameId,current_player)
        games[gameId].playerReady(current_player)
        start_new_thread(threaded_client,(conn,current_player,gameId))
        print('Thread Started ...')
    else:
        games[gameId].playerReady(current_player)
        check = 0
        if games[gameId].all_ready():
            games[gameId].readyGame()
            gameId += 1
            check = 1

        start_new_thread(threaded_client,(conn,current_player,gameId-check))
        print('Thread Started ...')
    ## Starting Thread for the current Player or Client..









