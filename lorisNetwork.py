import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = "192.168.43.230"
        self.port = 5555
        self.adrs = (self.server,self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.adrs) #connecting new client
            return self.client.recv(4096).decode()
        except:
            pass


    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)

