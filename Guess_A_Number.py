import random

print ("Welcome to Guess A Number Game :D")

#difficulty levels:

while True:

    difficulty = input ("Plz Select a Difficulty Level (Potato, Hm Hm, See you tomorrow) :D ").title()

    if difficulty == "Potato":
            
        answer = random.randint(1, 10)
        max_range = 10
        break

    elif difficulty == "Hm Hm":

        answer = random.randint(1, 100)
        max_range = 100
        break

    elif difficulty == "See You Tomorrow":

        answer = random.randint(1, 1000)
        max_range = 1000
        break

    else:
        print ("That doesn't sound right")

print(f"Plz Type in a Number between 1 and {max_range}")

guess_count = 0

#Guessing Loop

while True:

    try:
        guess = int(input())

    except ValueError:
        print (f"Ermm that doesn't sound right. Plz Type in a Number between 1 and {max_range}")
        continue

    guess_count += 1

    if guess == answer:
        print ("Correct!!! Good Job :D")
        Score = print (f"Congratulations :D You have guessed the number in {guess_count} tries")
        break

    elif guess < answer:
        print ("Awww Too Low :( Plz Try Again")

    elif guess > answer:
        print ("Awww Too High :( Plz Try Again")

    else:
        print (f"Plz Type in a Number between 1 and {max_range}")


   

