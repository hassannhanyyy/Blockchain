# Blockchain CW HCoin Transaction

import hashlib
import datetime

class HCoin:
    
    def __init__(self, previoushash, transaction):
        self.previoushash = previoushash
        self.transaction = transaction
        
        self.contents = "\n".join(transaction) + "\n" + previoushash
        self.hashing = hashlib.sha256(self.contents.encode()).hexdigest()

a = input("Would you like to borrow or send money?  ")
k = input("Enter the amount:  ")
b = input("Would you like to borrow or send money?  ")
l = input("Enter the amount:  ")
c = input("Would you like to borrow or send money?  ")
m = input("Enter the amount:  ")
d = input("Would you like to borrow or send money?  ")
n = input("Enter the amount:  ")
e = input("Would you like to borrow or send money?  ")
o  = input("Enter the amount:  ")
f = input("Would you like to borrow or send money?  ")
p  = input("Enter the amount:  ")
g = input("Would you like to borrow or send money?  ")
q  = input("Enter the amount:  ")
h = input("Would you like to borrow or send money?  ")
r  = input("Enter the amount:  ")
i= input("Would you like to borrow or send money?  ")
s  = input("Enter the amount:  ")
j = input("Would you like to borrow or send money?  ")
t  = input("Enter the amount:  ")



firstb = HCoin("\nBlock Hashing: ", [k])
print("---"*50, "\nGenesis Block\n")
print("Transaction Information: \n$", firstb.contents)
print(firstb.hashing , "\nDate & Time: ", str(datetime.datetime.now()))


nextb = HCoin("\nBlock #2 Hashing: ", [l])
print("---"*50, "\nTransaction Information: \nSent  $", nextb.contents)
print(nextb.hashing , "\n", "\nPrevious Block Hashing: ", firstb.hashing, "\nDate & Time: ", str(datetime.datetime.now()))


nextb2 = HCoin("\nBlock #3 Hashing: ", [m])
print("---"*50, "\nTransaction Information: \nSent  $", nextb2.contents)
print(nextb2.hashing , "\n", "\nPrevious Block Hashing: ", nextb.hashing,  "\nDate & Time: ", str(datetime.datetime.now()))


nextb3 = HCoin("\nBlock #4 Hashing: ", [n])
print("---"*50, "\nTransaction Information: \nSent  $", nextb3.contents)
print(nextb3.hashing , "\n", "\nPrevious Block Hashing: ", nextb2.hashing,  "\nDate & Time: ", str(datetime.datetime.now()))


nextb4 = HCoin("\nBlock #5 Hashing: ", [o])
print("---"*50, "\nTransaction Information: \nSent  $", nextb4.contents)
print(nextb4.hashing , "\n", "\nPrevious Block Hashing: ", nextb3.hashing,  "\nDate & Time: ", str(datetime.datetime.now()))


nextb5 = HCoin("\nBlock #6 Hashing: ", [p])
print("---"*50, "\nTransaction Information: \nSent  $", nextb5.contents)
print(nextb5.hashing , "\n", "\nPrevious Block Hashing: ", nextb4.hashing,  "\nDate & Time: ", str(datetime.datetime.now()))

nextb6 = HCoin("\nBlock #7 Hashing: ", [q])
print("---"*50, "\nTransaction Information: \nSent  $", nextb6.contents)
print(nextb6.hashing , "\n", "\nPrevious Block Hashing: ", nextb5.hashing,  "\nDate & Time: ", str(datetime.datetime.now()))

nextb7 = HCoin("\nBlock #8 Hashing: ", [r])
print("---"*50, "\nTransaction Information: \nSent  $", nextb7.contents)
print(nextb7.hashing , "\n", "\nPrevious Block Hashing: ", nextb6.hashing,  "\nDate & Time: ", str(datetime.datetime.now()))

nextb8 = HCoin("\nBlock #9 Hashing: ", [s])
print("---"*50, "\nTransaction Information: \nSent  $", nextb8.contents)
print(nextb8.hashing , "\n", "\nPrevious Block Hashing: ", nextb7.hashing,  "\nDate & Time: ", str(datetime.datetime.now()))

nextb9 = HCoin("\nBlock #10 Hashing: ", [t])
print("---"*50, "\nTransaction Information: \nSent  $", nextb9.contents)
print(nextb8.hashing , "\n", "\nPrevious Block Hashing: ", nextb8.hashing,  "\nDate & Time: ", str(datetime.datetime.now()), "\n---"*50)

