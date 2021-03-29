import random 

def gameWin (comp, you):
    if comp == you:
        return None 
    elif comp =='s':
        if you=='w':
            return False
        elif you =='g':
            return True 
    elif comp =='w':
        if you=='g':
            return False
        elif you =='s':
            return True
    elif comp =='w':
        if you=='g':
            return False
        elif you =='s':
            return True
    
print ("Comp Turn: Snake(s) Water(w) Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp= 's'
elif randNo == 3:
    comp= 'g'
elif randNo == 2:
    comp= 'w'
you = input("your turn : Snake(s) Water(w) Gun(g)?")
gameWin(comp, you)

print ( f" Computer chose {comp}")
print (f" you chose {you}")

a = gameWin(comp, you)

if a == None: 
    print ("THE GAME IS TIE! ")
elif a: 
   print ("YOU WIN !")
else: 
   print ("YOU LOSE!")