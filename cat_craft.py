'''Import the cat class to implement the rules of the game so that the user can play the game in the shell.'''

from cat import Cat #imports the Cat class from cat file

def menu_option(cats):
     '''takes list of cats as paramenter and prints the cats, their status, health and fish count, 
     along with options for user to feed, hit, night, or quit the game'''
    
     index = 1
     for cat in cats: # loops through all the cats in the list
        print(f"\n{index}. {cat}") #prints the cats with their information
        index +=1
     print("\nOption:\n1. Feed\t2. Hit\t3. Night\t4. Quit") # prints the available options
     
def main():
    ''''this is the main program which calls functions from the Cat class and menu_option to implement
    the game and print exceptions, thank you message and cat sounds like 'Purr!' when fed and 'Hiss!' when hit.'''
    cats = [Cat("Lucy"), Cat("Leo"), Cat("Zoe")] # list of cats for input
    
    while True: # infinite loop
        menu_option(cats) #callus the menu option each time the code is run in the loop
        try: # try statement for exception
            
        ### Input
            choice = int(input("Choice: "))
            
        ###Processing
            if choice == 1: # if user chooses feed
                choose_cat = int(input("Which Cat?"))
                cats[choose_cat-1].feed() # subtracts 1 from user input to ge index of the cat and calls function from Cat class
                print("Purr!")
            
            elif choice == 2: # if user chooses hit
                choose_cat = int(input("Which Cat?"))
                cats[choose_cat-1].hit() # subtracts 1 from user input to ge index of the cat and calls function from Cat class
                print("Hiss!")
                
            elif choice == 4: # if user chooses quit
                print("Thanks for playing!")
                break # breaks the loop if user chooses quit
            
            elif choice == 3: # if user chooses night
                for cat in cats: #loops through the cats in the list
                    message = cat.night() # calls the function from Cat class
                    if message != None: # prints the message from that function only if output is not None
                        print(message)
            else: # error message for wrong input in numbers
                print("Error! wrong choice. Please Enter 1, 2, 3 or 4.")

        except (ValueError, TypeError): # covers valueerror and typeerror and raises exception 
            print("\nWrong Input\nTry Again!")
        except Exception as e: # any other exception including the ones from the Cat class raised by programmer
            print(f"Error: {e}")
   

# prevents unintended code execution when the file is imported       
if __name__ == "__main__":  #__name__ and __main__ are built-in python variables set this way by the interpretor
    main() # calls the main function