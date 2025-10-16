'''This code contains the functions that implement all the rules for the game with the implementation 
of information hiding and raises exceptions for wrong use of the cat and bad inputs by the user.'''

import random
class Cat:
    '''this class initializes the Cat and performs functions as per the game's rules like 
    changing it's health and fish count based on user inputs.'''
    
    def __init__(self,name):
        '''initializes the cat name, value of health and fish,and tells if it is tame or wild 
        and if it is dead or alive at the beginning of the game'''
        self.__name = name
        self.__is_tame = False
        self.__is_alive = True
        self.__health = 2.0
        self.__fish = 0
        
    def feed(self):
        '''raises exception if used when the cat is dead, otherwise adds 1 health and 1 fish 
        till the time health is not more than 4 and fish count is not more than 3. Kills the cat and
        raises exception when cat eats more than 3 fish and makes it tame randomly with 50% chances whenever fed'''
        
        if not self.__is_alive: # exception when user tries to feed a dead cat
            raise Exception("Can't feed a dead Cat")
       
        self.__fish +=1 # always add 1 fish
        if self.__health >= 0 and self.__health < 4:
            self.__health += 1 # adds the health only if the cat has health between 0 and 4
        if self.__fish > 3:
            self.__is_alive = False # cat dies when fish count exceeds 3
            self.__health = 0 # health becomes 0 when cat dies
            raise Exception (f"The cat {self.__name} ate too much.") # raises exception for overfeeding
        if random.random() < 0.5: # 50% chance of cat being tame in this function
            self.__is_tame = True
            
    def hit(self):
        '''raises exception when a dead cat is hit, ortherwise makes the cat wild and reduces health by 1.5 if the 
        health is more than 0, kills the cat when health becomes less than or equal to 0'''
        
        if not self.__is_alive:  # exception when user tries to hit a dead cat
            raise Exception("Can't hit a dead Cat")
        self.__is_tame = False # always makes the cat wild
        if self.__health > 0:
            self.__health -=1.5 # reduces health by 1.5 only if health is above 0
        if self.__health <= 0:
            self.__is_alive = False # kills the cat when health is less than or equal to 0
            self.__health = 0 # makes the health of dead cat 0 in case it is negative
            
    def night(self):
       '''proceeds only if the cat is alive, a tame cat with fish count more than 0 leaves a gift. at the end of the night
       every cat has one less fish and becomes wild if fish count drops to zero'''
       if self.__is_alive:  #continues only if the cat is alive       
                        
            if self.__is_tame and self.__fish >= 0:# The cat leaves a gift only if it's tame and has at least 1 fish
                
                if self.__fish > 0: # Reduce the number of fish by 1 if fish count is not 0
                    self.__fish -= 1
                if self.__fish == 0:  # If zero fish at the end of the night, the cat becomes wild
                    self.__is_tame = False
                return (f"{self.__name} left you a gift")
            else:
                if self.__fish > 0: # if the cat is not tame but has fish count more than 0
                    self.__fish -= 1 # reduces 1 cat
        
    
                
    def __str__(self):
        ''' returns the status of the cat with record of it's health and fish count'''
        if self.__is_alive == False:
            status1 = "Dead"
        else:
            status1 = "Alive"
        if self.__is_tame == True:
            status2 = "Tame"
        else:
            status2 = "Wild"
        return (f"{status1} {status2} Cat {self.__name}: {self.__health} Health ,{self.__fish} Fish")
            
       