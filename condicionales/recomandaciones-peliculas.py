import random

print(
    """"
What is your favorite movie genre? (select 1, 2, 3, or 4)
1. Action
2. Comedy
3. Horror
4. Animation/Family 
"""
)
genre = int(input("Your choice: "))
age = int(input("Enter your age: "))

movies = {
    1: ["Avengers: Endgame", "Spider-Man: Homecoming", "John Wick"],
    2: ["The Lego Movie", "Despicable Me", "Home Alone"],
    3: ["It", "A Quiet Place", "The Conjuring"],
    4: ["Frozen", "Moana", "Toy Story"],
}

if genre in movies:
    if age <= 13:
        valid_options = movies[2] + movies[4]
        recomendation = random.choice(valid_options)
    else:
        recomendation = random.choice(movies[genre])
else:
    print("Enter a valid option.")

if recomendation is not None:
    print(f"We recommend you watch: {recomendation}")
