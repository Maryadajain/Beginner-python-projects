#1 import random
import random

#2 Create Subjects
subjects=[
        "Shanrukh Khan",
        "Virat Kohli",
        "Anushka Sharma",
        "A group of scientists",
        "A group of doctors",
        "A group of engineers", 
        "A group of students",
        "A group of teachers",
        "Airplane in the sky", 
        "A group of politicians", 
        "A group of musicians",
        "A group of writers",
        "A group of Monkeys",
        "A group of cats",
        "Auto rickshaw in the city",    
]

actions=[
    "discovers a new planet",
    "wins the Nobel Prize",
    "creates a new technology",
    "dances withjoy",
    "writes a bestselling book",
    "saves the world",
    "cancels a major event",
    "celebrates a major achievement",
    "launches a new product",
    "eats a delicious meal",

]

places_or_things=[
    "in the heart of the city",
    "in a remote village",
    "in a bustling market",
    "in a quiet library",
    "in a crowded stadium",
    "in a peaceful park",
    "in a high-tech laboratory",
    "on a beautiful beach",
    "in a historic museum",
    "in a futuristic city"
    "during IPL match",

]

#3 Start the headline generation
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    headline = f"  BREAKING NEWS: {subject} {action} {place_or_thing}."
    print("\n" + headline)
    user_input = input("\nDo you want to generate another headline? (yes/no)").strip().lower() #strip() removes leading and trailing spaces, lower() converts to lowercase
    if user_input != "yes":
        print("Thank you for using the Fake Headline Generator!")
        break
    else:
        continue