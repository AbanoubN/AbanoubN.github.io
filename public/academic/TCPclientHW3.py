#Name: Abanoub Nabil Yousief Abdelmessieh
#ID: 010985347


import socket

def menu():
    print("for Deposit Press 1 .")
    print("Withdrawal Press 2")
    print("Account Balance Press 3")
    print("clear account 3")
    print("Press CTRL+C ")

host = socket.gethostname()  
s = socket.socket() 
s.connect((host, 25045))
while True:
    menu() 
    print("What would you like to do: ")
    userchoice = input()
    msg = str.encode(str(userchoice), 'utf-8')
    s.send(msg)
    print(s.recv(1024))
    userchoice = input()
    msg = str.encode(str(userchoice), 'utf-8')
    s.send(msg)
    print(s.recv(1024))
s.close 

#Name: Abanoub Nabil Yousief Abdelmessieh
#ID: 010985347