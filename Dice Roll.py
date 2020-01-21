import random

_continue = True
die_type = {
        "D4" : (1, 4),
        "D6" : (1, 6),
        "D8" : (1, 8),
        "D10" : (1,10),
        "D12" : (1, 12),
        "D20" : (1,20)

}

print("""Choose your die:
D4
D6
D8
D10
D12
D20
""")

die = input("Type your die type:")

while _continue:
    r = random.randint(die_type[die][0], die_type[die][1])
    print (r) 
    user_input = input("\nDo you want to reroll? (Yes/No)\n")
    try:
        if user_input == "Yes":
            _continue = True
        if user_input == "No":
            _continue = False
    except:
        print("Choose correctly next time")

print("Thanks for your preference\n") 