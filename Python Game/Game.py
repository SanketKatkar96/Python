import random 

secret_number = random.randint (1, 100)
attempts = 0

print( "=== Number Gussing Game ===")
print("Now you selected a Number Between 1 to 100.")

while True:
    guess = int(input("Enter Your guees:"))
    attempts += 1 
    if guess < secret_number:
        print("Too Low! Try Again.")
    elif guess > secret_number:
            print("Too High! Try Again.")
    else:
        print("🎉 Congratulations!")
        print("You guessed the correct number .")
        print("Attempts:",attempts)
        break
