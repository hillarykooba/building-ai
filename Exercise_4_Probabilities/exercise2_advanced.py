import random

def main():

    probs = [0.8, 0.9, 1.0]
    animals = ["dogs", "cats", "bats"]
    prob = random.random()
    favourite = ""
    if prob < probs[0]:
        favourite = animals[0]
    elif prob >= probs[0] and prob < probs[1]:
        favourite = animals[1]
    elif prob >= probs[1] and prob < probs[2]:
        favourite = animals[2]
    else:
        favourite = "bats"
        
    print("I love " + favourite) 

main()