import sys


def list_restaurant_ratings(filename):
    """Reads restaurant names and ratings from file, adds to dictionary,
        returns in alpha order

    """

    with open(filename) as text:

        rest_ratings = {}

        for line in text:
            restaurant, rating = line.rstrip().split(":")
            rest_ratings[restaurant] = rating

    restaurant = input("Please enter a restaurant name.\n>").title()
    rating = 0

    while rating not in [1, 2, 3, 4, 5]:
        try:
            rating = int(input("Please enter a rating for that restaurant from 1 to 5.\n>"))
            continue
        except ValueError:
            print("Not a valid entry!")

    rest_ratings[restaurant] = rating

    for restaurant, rating in sorted(rest_ratings.items()):
        print(f'{restaurant} is rated at {rating}.')


list_restaurant_ratings(sys.argv[1])
