import random
import time

def makerandomtwodice():
    return random.randint(1,6), random.randint(1,6)

a_cond = True
while(a_cond):
    print("Rolling the dice...")
    time.sleep(3)
    print(makerandomtwodice())
    y = input("Roll again? (y/n)")
    if y=='n':
        a_cond = False
