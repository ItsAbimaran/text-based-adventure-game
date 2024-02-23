from colorama import Fore,Style,init
import time
import pyttsx3

def colored_print(text, color=Fore.WHITE, style=Style.NORMAL):
    print(f"{style}{color}{text}{Style.RESET_ALL}")

def introduction():
    a=pyttsx3.init()
    a.say("Welcome to the Magical Kingdom Adventure.You find yourself in a mystical land full of wonders and dangers.")
    colored_print("Welcome to the Magical Kingdom Adventure!\nYour goal is to reach the enchanted castle and uncover its secrets.",Fore.CYAN)
    a.runAndWait()
    a.say("Let the adventure begin")
    a.runAndWait()
    colored_print("You find yourself in a mystical land full of wonders and dangers.",Fore.CYAN)
    time.sleep(1)
    colored_print("Your goal is to reach the enchanted castle and uncover its secrets.",Fore.CYAN)
    time.sleep(1)
    colored_print("Let the adventure begin!\n",Fore.CYAN)

def make_choice(options):
    print("Choose your path:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest():
    colored_print("\nYou enter the enchanted forest.",Fore.GREEN)
    time.sleep(2)
    colored_print("As you walk deeper, you hear mysterious whispers in the wind.",Fore.GREEN)
    time.sleep(2)
    colored_print("You encounter a fork in the path.",Fore.GREEN)
    
    options = [ Fore.YELLOW+ "Follow the path to the left.",Fore.YELLOW + "Take the path to the right."]
    choice = make_choice(options)
    
    if choice == 1:
        print("\nYou follow the path to the left.")
        time.sleep(2)
        colored_print("You discover a hidden grove with sparkling fireflies.",Fore.GREEN)
    else:
        print("\nYou take the path to the right.")
        time.sleep(2)
        colored_print("You stumble upon a pack of friendly forest creatures.",Fore.GREEN)

def mountain():
    colored_print("\nYou approach the towering mountains.",Fore.GREEN)
    time.sleep(2)
    colored_print("The air gets colder as you ascend.",Fore.GREEN)
    time.sleep(2)
    colored_print("You encounter a treacherous cliffside.",Fore.GREEN)

    options = [Fore.YELLOW +"Climb the cliff using your skills.",Fore.YELLOW + "Search for an alternative route."]
    choice = make_choice(options)

    if choice == 1:
        print("\nYou decide to climb the cliff.")
        time.sleep(2)
        colored_print("After a challenging climb, you reach the summit.",Fore.GREEN)
    else:
        print("\nYou search for an alternative route.")
        time.sleep(2)
        colored_print("You discover a hidden cave system within the mountains.",Fore.GREEN)

def castle():
    colored_print("\nYou finally arrive at the majestic castle.",Fore.GREEN)
    time.sleep(2)
    colored_print("The gates slowly creak open, inviting you inside.",Fore.GREEN)
    time.sleep(2)
    colored_print("You stand in the grand hall, surrounded by mystery.",Fore.GREEN)

    options = [Fore.YELLOW +"Explore the castle's corridors.",Fore.YELLOW +"Enter the throne room."]
    choice = make_choice(options)

    if choice == 1:
        print("\nYou decide to explore the castle's corridors.")
        time.sleep(2)
        colored_print("You uncover hidden chambers and ancient artifacts.",Fore.GREEN)
    else:
        print("\nYou boldly enter the throne room.")
        time.sleep(2)
        colored_print("You find the throne empty, but a magical presence lingers.",Fore.GREEN)

# Main game loop
def play_game():
    introduction()
    forest()
    mountain()
    castle()
    colored_print("your exited the Magical Kingdom Adventure without any obstacles",Fore.CYAN)
    a=pyttsx3.init()
    a.say("congratulation on completing the adventrous game.well done on navigating through challenges and triumphing in the the end.your exited the Magical Kingdom Adventure without any obstacles")
    a.runAndWait()

if __name__ == "__main__":
    play_game()
