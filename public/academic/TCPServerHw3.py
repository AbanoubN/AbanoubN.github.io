import socket
import sys
class Server():
    def __init__(self):
        self.acc_balance = float(100)  
        self.Starting_balance = self.acc_balance
        self.depo = float(0) 
        self.withdraw_amount = float(0) 

    def withdrawal(self, amount, conn):
        temp = self.acc_balance
        self.acc_balance -= amount
        self.withdraw_amount += amount

        if self.acc_balance < 0:
            self.acc_balance = temp 
            print("Not enough funds")
            data = "Invalid operation, not enough funds."   
        else:
            print("Withdrawal was $%.2f, current balance is $%.2f" % (amount, self.acc_balance))
            data = "Withdrawal was $%.2f, current balance is $%.2f" % (amount, self.acc_balance)
        conn.send(data.encode())

    def print_balance(self, conn):
        print("Your current balance: $%.2f" % self.acc_balance)
        data = "Your current balance: $%.2f" % self.acc_balance
        conn.send(data.encode())

    def deposit(self, entered_amount, conn):
        self.acc_balance += entered_amount
        self.depo += entered_amount
        print("Deposit was $%.2f, current balance is $%.2f" % (entered_amount, self.acc_balance))
        data = "Deposit was $%.2f, current balance is $%.2f" % (entered_amount, self.acc_balance)
        conn.send(data.encode())  
    def clear_account(self):
        self.acc_balance  = 0 


def main():

    host = socket.gethostname()  
    port = 25045  
    s = socket.socket()  
    s.bind((host, port))  

    s.listen(5)  
    c, addr = s.accept()  
    print('connected to', addr)
    account = Server() 
    while True:
        userchoice = c.recv(1024).decode()
        if userchoice =='1':        
            c.send("please enter deposit amount".encode())
            amount = float(c.recv(1024).decode())
            account.deposit(amount, c)
        elif userchoice =='2':
            c.send("please enter amount".encode())
            amount = float(c.recv(1024).decode())
            account.withdrawal(amount, c)
        elif userchoice == '3':
            account.print_balance(c)
        elif userchoice == '4':
            account.clear_account()
            c.send("cleared".encode())
        else:
            print("Wrong Choice!")
            c.send("Wrong Choice!".encode())
    c.close() 

main()