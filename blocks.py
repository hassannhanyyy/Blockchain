# Blockchain CW HCoin Transaction

import hashlib
import datetime


class HCoin:
    def __init__(self, previoushash, transaction):
        self.previoushash = previoushash
        self.transaction = transaction
        
        self.contents = "\n".join(transaction) + "\n" + previoushash
        self.hashing = hashlib.sha256(self.contents.encode()).hexdigest()

a = input("Enter Transferred Amount: ")
b = input("Enter Transferred Amount: ")
c = input("Enter Transferred Amount: ")
d = input("Enter Transferred Amount: ")
e = input("Enter Transferred Amount: ")
f = input("Enter Transferred Amount: ")

firstb = HCoin("\nBlock Hashing: ", [a])
print("---"*50, "\n", "Genesis Block\n")
print( "Transaction Information: \n$", firstb.contents)
print(firstb.hashing , "\nDate & Time: ", str(datetime.datetime.now()))


nextb = HCoin("\nBlock #2 Hashing: ", [b])
print("---"*50, "\n", "Transaction Information: \nSent  $", nextb.contents)
print(nextb.hashing , "\n", "\nPrevious Block Hashing: ", firstb.hashing, "\nDate & Time: ", str(datetime.datetime.now()))


nextb2 = HCoin("\nBlock #3 Hashing: ", [c])
print("---"*50, "\n", "Transaction Information: \nSent  $", nextb2.contents)
print(nextb2.hashing , "\n", "\nPrevious Block Hashing: ", nextb.hashing,  "\nDate & Time: ", str(datetime.datetime.now()))


nextb3 = HCoin("\nBlock #4 Hashing: ", [d])
print("---"*50, "\n", "Transaction Information: \nSent  $", nextb3.contents)
print(nextb3.hashing , "\n", "\nPrevious Block Hashing: ", nextb2.hashing,  "\nDate & Time: ", str(datetime.datetime.now()))


nextb4 = HCoin("\nBlock #5 Hashing: ", [e])
print("---"*50, "\n", "Transaction Information: \nSent  $", nextb4.contents)
print(nextb4.hashing , "\n", "\nPrevious Block Hashing: ", nextb3.hashing,  "\nDate & Time: ", str(datetime.datetime.now()))


nextb5 = HCoin("\nBlock #6 Hashing: ", [f])
print("---"*50, "\n", "Transaction Information: \nSent  $", nextb5.contents)
print(nextb5.hashing , "\n", "\nPrevious Block Hashing: ", nextb4.hashing,  "\nDate & Time: ", str(datetime.datetime.now()),  "\n", "---"*50)

