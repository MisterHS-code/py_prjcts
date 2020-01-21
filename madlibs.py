print("I was ________ (verbing) at the ________ (noun that’s a place) the other day when I heard\n"\
    "________ (holiday song) come on the radio. I was feeling really ________ (adjective) and\nI’m pretty sure I looked"\
    " super ________ because ________ (your friend) walked in and \nalmost ________ (verbed). Seriously,"\
    " she ________ (verbed) for close to ________ \n(amount of time)!\n\nThis time every year I ________ (verb)"\
    " all the time because I get really exciting thinking \nabout holiday ________ (plural noun)! That’s why I"\
    " was sitting at the ________ (the place \nfrom up top): I was really hoping ________ (a relative) would come"\
    " by and give me at least \n________ (a number) pieces of holiday ________ (food item)!\n\nThat didn’t happen, but "\
    "suddenly ________ (a relative) ________ (verbed) by in a \nhuge________ (noun) on wheels dressed up as ________ "\
    "(a singer). I know ________ \n(adjective) things happen around the holidays, but this didn’t make any sense!"\
    " I picked up \nthe phone to call ________ (a person), but the phone turned into a big pile of ________ (a \nmessy food)"\
    " and dripped all the way down to my ________ (a body part)!\n\nThen my alarm clock went off for about ________ (amount of time)"\
    ". It was all a dream! I had \na ton of ________ (a holiday food) before I went to sleep. Maybe that’s what gave me the \ncrazy dream\n")

my_dict = {}

words = ["verb-ing", "place", "holiday song", "adjective", "adjective1", "your friend",  "verb in simple past", " verb in simple past1", 
"amount of time", "verb", "plural noun", "high place", "a relative", "a number", "food", "a relative1", "verb -ed", "noun", "noun1", "adjective2", 
"proper noun", "food1", "body part", "time", "food2"]

for prompt in words:
    my_dict[prompt] = input("\nWrite down a {}: ".format(prompt))

