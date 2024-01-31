import random
char ="abcdefghijklmnopqrstuvwxyz0123456789!@#$%&*ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
len=(int(input("Enter Lenght:")))
i=int(input("How many password to generate:"))
for a in range(i):
    # for a in range(len):
    password="".join(random.sample(char,len))
    print(password)