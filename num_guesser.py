import random

running = True

def players_guess(x):
    global running
    try:
        guess = int(input("Guess the number:"))
        if guess == x:
            replay = input("Congratulations! Do you want to keep playing?(Yes/No)")
            if replay == "No":
                print("Thanks for playing!")
                running = False
        else:
            if guess > x:
                print("Too high! Try again.")
            if guess < x:
                print("Too low! Try again")
            players_guess(x)
    except:
        print("Please input a number") 


while running:
    act_number = random.randint(1, 25)
    print(act_number)
    players_guess(act_number)