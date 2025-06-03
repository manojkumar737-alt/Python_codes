#guess the number
import random
Randum = random.randint(1, 50)

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I have selected a number between 1 and 50.")
    print("Try to guess it!")

    attempts = 0
    while attempts <= 5:
        if attempts == 5:
            print("You have reached the maximum number of attempts. Game over!")
            print(f"The number was: {Randum}")
            break
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < Randum:
                print(f"Total attempts: {attempts} , Guess number is Too low! Try again.")
            elif guess > Randum:
                print(f"Total attempts: {attempts} , Guess number isToo high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {Randum} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

#if __name__ == "__main__":
guess_the_number()