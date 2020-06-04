import random

bars = [
    "Babylon's",
    "The tiger",
    "The lion",
    "Loves me",
    "Blind cow"
]

people = [
    "Babul",
    "Jhankar",
    "that person you forgot to include in the course",
    "Know the best",
    "Subir X Nokrek"
]


random_bar = random.choice(bars)
random_person = random.choice(people)

print (f"How about you to go to {random_bar} with {random_person}")