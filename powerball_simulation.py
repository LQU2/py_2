import random

white_possibles =  list (range(1, 70))
red_possibles =  list (range(1, 27))

tickets_per_drawing = 1
num_drawings = 1

total_spent = 0
earnings = 0

times_won = {
    "5+P": 0,
    "5": 0,
    "4+P": 0,
    "4": 0,
    "3+P": 0,
    "3": 0,
    "2+P": 0,
    "1+P": 0,
    "P": 0,
    "0": 0,
}


def calc_win_amt(my_numbers, winning_numbers):
    win_amt = 0
    #accessing the white numbers for my ticket
    white_matches = len(my_numbers["whites"].intersection(winning_numbers["whites"])) #for the set of my white numbers, i want to run an intersection with the white winning numbers. it'll return a set of the same values that are in both sets, but we want to see how many we matched. to get that number we wrap the entire thing into a length & get the length of the intersection
    #how many white numbers we matched from our ticket to the winning numbers
    power_match = my_numbers['red'] == winning_numbers['red'] #this conditional is going to return a true or false value. if they match, power_match will be true. if not, then power_match will be false

    if white_matches == 5: #then we matched all 5 of those white balls
        if power_match: #and we hit the powerball
            win_amt = 2_000_000_000
            times_won["5+P"] += 1 #also keeping track of how many times we hit the prizes
        else:
            win_amt = 1_000_000
            times_won["5"] += 1
    elif white_matches == 4:
        if power_match:
            win_amt = 50_000
            times_won["4+P"] += 1
        else: 
            win_amt = 100
            times_won["4"] += 1
    elif white_matches == 3:
        if power_match:
            win_amt = 100
            times_won["3+P"] += 1
        else:
            win_amt = 7
            times_won["3"] += 1
    elif white_matches == 2 and power_match: #we don't get anything for matching 2, we need 2 and the powerball to win
        win_amt = 7
        times_won["2+P"] += 1
    elif white_matches == 1 and power_match:
        win_amt = 4
        times_won["1+P"] += 1
    elif power_match:
        win_amt = 4
        times_won["P"] += 1
    else:
        times_won["0"] += 1

    return win_amt #putting parameters in place to make clear we'll solve the problem

#we need to loop through the number of drawings we want to simulate and draw the winning numbers for each of those 
for drawing in range(num_drawings):
    white_drawing = set(random.sample(white_possibles, k=5)) #k=5, we want a sample of 5 of those. the random.sample is going to reutrn a list, but let's make it a set
    red_drawing = random.choice(red_possibles) #using random.choice to get one value from these possibilities

    winning_numbers = {"whites": white_drawing, "red": red_drawing} # winning numers from a single drawing

    for ticket in range(tickets_per_drawing): #let's loop through the number of tickets we plan to buy for each drawing
        total_spent += 2
        my_whites = set(random.sample(white_possibles, k=5))
        my_red = random.choice(red_possibles)

        my_numbers = {"whites": my_whites, "red": my_red}

        # calc_win_amt