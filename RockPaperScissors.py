'''
Created on Jan 29, 2018

@author: Mike Noble
'''

import random


def paperScissorsRock(Player, num):
    
    if (num == 1):
        playerThrows = Player.throws("Paper")
           
    elif(num == 2):
        playerThrows = Player.throws("Scissors")
        
    else:
        playerThrows = Player.throws("Rock")
        
    return playerThrows
        


    
    
        
    
class Player:
    
    def __init__(self, name):
        self.name = name
        self.wins = False 
        
    def throws(self, throws):
        
        self.throws = throws
        print self.name+" throws "+self.throws
        return throws
    
           
def main():
    
    print "Welcome to Paper, Scissors, Rock"
    name = raw_input("What is your name? ")
    print ""
    player1 = Player(name)
    player2 = Player("Hal")
    
    print "Welcome "+name+" you are playing against The Hal 9000"
    print ""
    print "1. Paper"
    print "2. Scissors"
    print "3. Rock"
    print ""
    
    p1 = paperScissorsRock(player1, int(raw_input("Enter 1, 2 or 3: ")))
    p2 = paperScissorsRock(player2, random.randint(1,3))
    
  
    if(p1 == p2):
        print "It's a Tie!" 
    elif (p1 == "Paper"):
        if (p2 == "Scissors"):
            print "Scissors cuts Paper "+player2.name+" WINS!"
        else:
            print "Paper wraps Rock "+player1.name+" WINS!"
    elif (p1 == "Scissors"):
        if (p2 == "Paper"):
            print "Scissors cuts paper "+player1.name+" WINS!"
        else:
            print "Rock blunts Scissors "+player2.name+" WINS!"
    elif (p1 == "Rock"):
        if (p2 == "Paper"):
            print "Paper wraps Rock "+player2.name+" WINS!"
        else:
            print "Rock blunts Scissors "+player1.name+" WINS!"
    else:
        print "ERROR"
    
    print ""          
    print "Thanks for playing!"
                
if __name__ == "__main__":
    main()
    
















    


        
        
        
             


       


        
        
        