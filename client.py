import  threading

import  socket

import  _datetime

connected = False

client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:

    client.connect(('127.0.0.1' , 55555))
    connected  =  True
except:
    print("Connection Failed!! Check Your Network")
    print("Retrying")
    j = 0
    for i in range(0,100):
       if  j != 100:
            try:
                client.connect(('127.0.0.1', 55555))
                print("Connected!!")
                connected = True

            except:
                print("...")

       else:
           import  time
           time.sleep(5)
           break

nickname = "Bye!"
if connected == True:
    print("Connected")
    nickname = input("Please create a nickname: ")

    print(f'''
    {nickname}, Welcome To Chat! Please Make Sure You
    Are Always Positive When Talking With Others. 
    Thanks For Being Awesome!
    
    Regards:
    Server
    {_datetime.datetime.today()}
    ____________________________________________________
    ''')
def get():
    while True:
        try:
            message =  client.recv((1024)).decode('ascii')
            if message == 'NAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)

        except:
            if connected == True:
                print("Server Error: Connection Lost!!")
                client.close()
                break


def send():
    while True:
        name =  nickname[0].upper() + nickname[1:]
        message  = f'[{name}]:'+input()
        if len(message)== 0 :
            print("Your Message Can't Be Empty!")
        if f'[{name}]:     ' in message:
            print("Failed To Send, Spam Chances!")
        else:
            message = message.encode('ascii')
            client.send(message)


receive_thread = threading.Thread(target=get)
write_thread =  threading.Thread(target= send)

receive_thread.start()
write_thread.start()

