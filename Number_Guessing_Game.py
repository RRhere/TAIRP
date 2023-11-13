import random
def guess_number():
    n=int(input("Guess the number:"))
    return n
start,end=map(int,input("Enter the range for guessing the number seperated by a space:").split(" "))
comp_num=random.randint(start,end)
n=guess_number()
while comp_num!=n:
    print("Try Again!")
    n=guess_number()
    if n==comp_num:
        print("Awesome Guess!")
        break