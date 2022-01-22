import random

print("\n * Welcome to Your Password Generator * \n")

char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*-+0123456789"
num = input("How many Passwords u want to generates? : ")
num = int(num)
length = input("Input Your Password length : ")
length = int(length)



for p in range(num):
    passwords = ''
    for c in range(length):
        passwords += random.choice(char)
    print("\n Here are your passwords : ",passwords)