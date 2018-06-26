import sys
import random


def check_inputs():
    rating = 0
    while rating not in [1, 2, 3, 4, 5]:
        try:
            rating = int(input("Please enter a rating from 1 to 5.\n>"))
            continue
        except ValueError:
            print("Not a valid entry!")
    return rating


def list_restaurant_ratings(filename):
    """Reads restaurant names and ratings from file, adds to dictionary,
        returns in alpha order

    """

    with open(filename) as text:

        rest_ratings = {}

        for line in text:
            restaurant, rating = line.rstrip().split(":")
            rest_ratings[restaurant] = rating

    while True:
        user_action = input("Please enter 'U' to update a restaurant rating 'R' to see ratings, 'A' to add a new restauraunt, or 'Q' to quit. \n>").upper()

        if user_action == "R":
            for restaurant, rating in sorted(rest_ratings.items()):
                print(f'{restaurant} is rated at {rating}.')

        elif user_action == "U":

            user_choice = input("""Do you want to choose a restaurant or update a random restaurant?
Type 'C' for choose and 'R' for random.\n>""").upper()

            if user_choice == "R":
                rest_to_update = random.choice(list(rest_ratings.keys()))
     
            elif user_choice == "C":
                rest_to_update = input("Which restaurant rating would you like to update?\n>")

            print(f"The current rating for {rest_to_update} is {rest_ratings[rest_to_update]}")
            new_rating = check_inputs()
            rest_ratings[rest_to_update] = new_rating

        elif user_action == "A":
            restaurant = input("Please enter a restaurant name.\n>").title()
            rating = check_inputs()
            rest_ratings[restaurant] = rating

        elif user_action == "Q":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice!")


list_restaurant_ratings(sys.argv[1])
