#Forest game 

def welcome():
    print("================================")
    print(" Welcome to the Adventure Game ")
    print("================================")


def forest():
    print("\nYou walk through a peaceful forest.")
    print("You discover a hidden treasure chest!")
    print("🎉 Congratulations! You Win!")


def dragon():
    print("\nA giant dragon appears!")

    choice = input("Do you want to fight or run? ").lower()

    if choice == "fight":
        print("You bravely fight the dragon.")
        print("🏆 You defeat the dragon and become a hero!")

    elif choice == "run":
        print("You escape safely.")
        print("Game Over.")

    else:
        print("The dragon is confused by your answer!")
        print("Game Over.")


def start_game():
    welcome()

    print("\nChoose your path:")
    print("1. Forest")
    print("2. Cave")

    option = input("Enter your choice (1 or 2): ")

    if option == "1":
        forest()

    elif option == "2":
        dragon()

    else:
        print("Invalid choice. Game Over.")


start_game()