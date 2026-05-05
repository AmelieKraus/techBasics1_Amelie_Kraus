import time


# Typing effect function
def type_scroll(text, speed=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()


print("Welcome to test game")
time.sleep(1)
name = input("What's your name? ")
time.sleep(1)
print("Hello", name)
time.sleep(2)

type_scroll(f"\n{name}, you stand in a dark and misty forrest before two paths... 🌳🌙")
time.sleep(1)

# Input 1
choice1 = input("Do you take the LEFT path or the RIGHT path? (left/right): ").lower()

# Logic 1
if choice1 == "right":
    type_scroll("\nYou continue your walk, but because of the darkness you cannot see the crack in the ground! You fall into a dark pit. 🕳️")
    time.sleep(1)

    # Input 2
    action = input("Do you SHOUT for help or CLIMB out? (shout/climb): ").lower()

    if action == "shout":
        type_scroll("Your voice echoes... but something hungry answers from the dark. 🐉. You can hear it approaching, but you cannot hide anywhere... ")
        time.sleep(1)
        type_scroll("GAME OVER.")
        exit()  # End game
    elif action == "climb":
        type_scroll("\nYou scramble up the jagged rocky wall, trying to find your way up.")
        type_scroll("You heave yourself over the edge and emerge... on a different path.")
        time.sleep(2)
        #to logic 2
        choice1 = "left"
    else:
        type_scroll(" You are frozen by fear while looking into the shadows. GAME OVER.")
        exit()

# Logic 2
if choice1 == "left":
    type_scroll("\nYou walk into a clearing in the forrest. Right in the centre is a pedestal with a magical scale on it.")
    time.sleep(1)

    # Input 3
    while True:
        print("\nOn one side of the scale lays a glowing orb, on the other lay plane stones. The scale is perfectly in balance...")
        val_input = input("You pick up more stones from the forrest ground. How many do you pick? (between 10 and 50): ")

        if val_input.isdigit():
            stones = int(val_input)
            # Conditional 2
            if 10 <= stones <= 50:
                print(f"The scale balances perfectly with {stones} stones...")
                break
            else:
                print("The scale tilts violently in one direction! That amount is not acceptable. Try again.")
        else:
            print("The scale doesn't recognize that! Please enter a number.")

    # Conditional 3 & 4
    type_scroll("\nA ghost appears out of the orb. 'Tell me,' it whispers, 'do you seek Wisdom or Wealth?'")
    choice2 = input("(wisdom/wealth): ").lower()

    if choice2 == "wisdom":
        #Conditional 5
        if stones > 40:
            type_scroll("✨ Your great approximation of the needed stones earns you the knowledge of the future. You win!")
        else:
            type_scroll("📜 You receive a small scroll of future events and knowledge. A modest success.")
    elif choice2 == "wealth":
        type_scroll("💰 The ghost vanishes, leaving you a bag of coins. You are richer, but still lost in the forrest.")
    else:
        type_scroll("The ghost dislikes your silence and vanishes with the orb. You find nothing.")

else:
    # If the user typed something other than left or right at the very start
    type_scroll("You hesitated for too long. The world fades away... 🌫️")
    print("GAME OVER.")

time.sleep(2)
type_scroll("\nThanks for playing! Goodbye.")