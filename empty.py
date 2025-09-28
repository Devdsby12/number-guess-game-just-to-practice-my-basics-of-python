import time
import random
def intelwon():
    ryzen = random.randint(0,33)
    intel = random.randint(0,33)
    return ryzen == intel
def ryzenwon ():
    intel = random.randint(0,33)
    ryzen = random.randint(0,33)
    return intel == ryzen 

def userinput():
    limit = 1
    ryzenwonnn = 0
    intelwonnn = 0
    userinputt = input("enter any button to start guess game  :  q for exit proggram ")
    if userinputt == "q":
        return
    while limit < 100:
        time.sleep(0)
        intelwonn = intelwon()
        ryzenwonn = ryzenwon()
        
        if intelwonn :
            intelwonnn += 1
            print("intel won first")
        if ryzenwonn:
            ryzenwonnn += 1
            print("ryzen won first")
        print(limit)            
        limit += 1
    print(f" ryzen won {ryzenwonnn} times AND  intelwon {intelwonnn} times ")
    if ryzenwonnn > intelwonnn:
        print(f"so ryzen is winner and won by {ryzenwonnn - intelwonnn} points")
    elif ryzenwonnn < intelwonnn:
        print(f"so intel is winner and won {intelwonnn - ryzenwonnn} points")
    else:
        print("bot got equal points so rematching in 6 seconds again") 
        time.sleep(6)  
        userinput() 

userinput()
