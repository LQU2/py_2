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
#we need to loop through the number of drawings we want to simulate and draw the winning numbers for each of those 
for drawing in range(num_drawings):
    white_drawing = set(random.sample(white_possibles, k=5)) #k=5, we want a sample of 5 of those. the random.sample is going to reutrn a list, but let's make it a set
    red_drawing = random.choice(red_possibles) #using random.choice to get one value from these possibilities

    winning_numbers = {
        "whites": white_drawing,
        "red": red_drawing,
    }

    for ticket in range(tickets_per_drawing)
        total_spent += 2
