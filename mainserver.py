import threading
import  socket


host = '127.0.0.1'
port =  55555

server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))

server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client  in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message  =  client.recv(1024)
            broadcast(message)
        except:
            index =  clients.index(client)
            clients.remove(client)
            client.close()
            nickname  = nicknames[index]
            broadcast(f"{nickname} Left The Chat!".encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():


    while True:
        client , address =  server.accept()
        print(f"Connected With {address}")

        client.send("NAME".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname Of Client  Is {nickname}")
        broadcast(f'{nickname} Joined The Chat!'.encode('ascii'))
        client.send("Connected To Server".encode('ascii'))

        thread =threading.Thread(target=handle, args=(client, ))
        thread.start()







print(f"Server Started...")


receive()



